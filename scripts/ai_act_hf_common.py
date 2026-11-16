"""Fixed source/destination and committed-source integrity for the EU AI Act accessibility and delivery dataset."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import urllib.request

SOURCE = 'Double-FW/EU-AI-Act-accessibility-disability-rights-and-delivery'
TARGET = 'GarethFW/EU_AI_Act_accessibility_disability_rights_and_delivery'
ROOT = Path(__file__).resolve().parents[1]
MANAGED = ('README.md', 'LICENSE', 'documents.jsonl', 'knowledge_chunks.jsonl',
           'provenance.json', 'record_schema.json', 'validation_report.json')
REQUIRED_CONTEXT = {'AGENTS.md', 'sources/source-register.md', 'sources/legal-and-standards-status.md', 'docs/scope-and-surface-coverage.md', 'ADOPTION.md', 'docs/double-fw-delivery-map.md', 'templates/assessment-and-test-record.md'}
EXCLUDED_SOURCES = {'examples/worked-scenarios.md','CHANGELOG.md'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])

def destination(value):
    if value != TARGET:
        raise ValueError('Destination must be ' + TARGET + '.')
    return value

def load_config(root=ROOT):
    # Configuration and documents come from the same committed snapshot.
    attrs = git(root, 'ls-tree', 'HEAD', '--', 'huggingface/export-config.json').decode()
    if not attrs.startswith('100644 blob '):
        raise ValueError('Export configuration must be a committed regular file.')
    cfg = json.loads(git(root, 'show', 'HEAD:huggingface/export-config.json'))
    if cfg['source_repository'] != SOURCE:
        raise ValueError('Source must be the approved public EU AI Act accessibility and delivery repository.')
    destination(cfg['destination_dataset'])
    paths = cfg['files']
    if not isinstance(paths, list) or not paths or not all(isinstance(p,str) for p in paths) or len(set(paths)) != len(paths):
        raise ValueError('Approved paths must be a nonempty unique string list.')
    if set(paths) & EXCLUDED_SOURCES:
        raise ValueError('Illustrative scenarios and maintenance history are excluded from training views.')
    for path in paths:
        p = PurePosixPath(path)
        if p.is_absolute() or '..' in p.parts or any(x.startswith('.') for x in p.parts) or p.suffix != '.md':
            raise ValueError('Only approved Markdown source paths may be exported.')
    if set(cfg['required_files']) != set(paths + ['LICENSE']):
        raise ValueError('All approved documents and LICENSE must be required.')
    for field in ('document_only_files','context_files'):
        values = cfg[field]
        if not isinstance(values,list) or not all(isinstance(x,str) for x in values) or len(set(values)) != len(values) or not set(values) <= set(paths):
            raise ValueError(field + ' must contain unique approved paths.')
    if not REQUIRED_CONTEXT <= set(cfg['context_files']):
        raise ValueError('Governance, adoption, scope, source/status, delivery-map and result-vocabulary contexts are required.')
    return cfg

def public_source():
    request = urllib.request.Request('https://api.github.com/repos/' + SOURCE,
        headers={'User-Agent':'Double-FW-eu-ai-act-dataset-export'})
    with urllib.request.urlopen(request,timeout=30) as response:
        info=json.load(response)
    if info.get('full_name') != SOURCE or info.get('private') is not False or info.get('visibility') != 'public':
        raise ValueError('Publishing requires the approved public EU AI Act accessibility and delivery source repository.')

def read_sources(root,cfg):
    tree={}
    for item in git(root,'ls-tree','-rz','--full-tree','HEAD').split(b'\0'):
        if not item:continue
        attrs,raw_path=item.split(b'\t',1)
        mode,kind,sha=attrs.decode().split();tree[raw_path.decode()] = (mode,kind,sha)
    sources,manifest={},[]
    for path in cfg['files']+['LICENSE']:
        if path not in tree:raise ValueError('Required source is missing: '+path)
        mode,kind,sha=tree[path]
        if mode!='100644' or kind!='blob':raise ValueError('Source must be a committed regular file: '+path)
        data=git(root,'cat-file','blob',sha)
        if hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()!=sha:raise ValueError('Git blob integrity failed.')
        sources[path]=data.decode('utf-8')
        if any(marker in sources[path] for marker in ('chatgpt.com/library', 'account_id=', 'file_id=libfile_')):
            raise ValueError('A source contains private access metadata. Remove private links/identifiers before public export: '+path)
        manifest.append({'path':path,'git_blob_sha':sha,'sha256':digest(data),'size_bytes':len(data)})
    if digest(sources['LICENSE'].encode())!=cfg['approved_license_sha256']:
        raise ValueError('Licence changed. Review its terms, metadata and approved checksum before publishing.')
    return sources,manifest
