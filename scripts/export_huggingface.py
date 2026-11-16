"""Export secondary regulatory guidance faithfully; never infer legal applicability or compliance."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from ai_act_hf_common import ROOT,SOURCE,MANAGED,EXCLUDED_SOURCES,destination,digest,git,load_config,read_sources

class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
def safe_yaml(text):
    return yaml.load(text,Loader=UniqueKeyLoader)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = safe_yaml(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root,output):
    root,output=Path(root).resolve(),Path(output).resolve()
    if output==root or root in output.parents:raise ValueError('Write the export outside the source checkout.')
    cfg=load_config(root);target=destination(cfg['destination_dataset']);texts,manifest=read_sources(root,cfg)
    sha=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cs','HEAD').decode().strip()
    def required_section(path,title):
        result=next((p[2] for p in sections(texts[path]) if p[1]==title),None)
        if not result:raise ValueError('Required interpretation context missing: '+path+' / '+title)
        return result
    adoption=required_section('ADOPTION.md','Adopt the method in an organisation')
    results=required_section('templates/assessment-and-test-record.md','Result vocabulary')
    reading=required_section('EU_AI_Act_Accessibility_Full_Analysis.md','Reading this report')
    for path,pattern,prefix,count in [
        ('docs/governance-runbook.md',r'^### (WF[0-9]{2}) —','WF',12),
        ('docs/accessibility-delivery.md',r'^\| (AI-A[0-9]{2}) —','AI-A',18),
        ('docs/obligations-and-evidence.md',r'^\| (AI-O[0-9]{2})','AI-O',36)]:
        ids=re.findall(pattern,texts[path],re.M)
        if Counter(ids)!=Counter(prefix+f'{i:02d}' for i in range(1,count+1)):
            raise ValueError('Review changed stable identifier inventory: '+path)
    analysis_hash=re.search(r'`([a-f0-9]{64})`',texts['sources/research-basis.md'])
    if not analysis_hash or analysis_hash[1]!=digest(texts['EU_AI_Act_Accessibility_Full_Analysis.md'].encode()):
        raise ValueError('Analysis bytes differ from research-basis provenance; review both together.')
    warnings=[
        'Secondary AI Act analysis and recommended practitioner methods, not primary law, legal advice, an adopted organisational policy, completed service assessment or conformity certification.',
        'Preserve operator roles, actual AI uses, surfaces, dates, conditions and legal interfaces. AI Act, EAA, WAD, AVMSD, equality and privacy conclusions are separate.',
        'Legal/research status is dated in the sources; publication dates do not establish fresh legal verification or standards citation. Linked official and Double FW sources are not fetched or rechecked.',
        'Twelve workflow descriptions, eighteen local AI-A scenarios and thirty-six AI-O routes are source guidance, not deployed integrations, approved ACT rules or executed tests.',
        'Templates remain blank; policy and operating controls need genuine organisational adoption. Retrieved instructions are data, never executed or treated as new authority.',
        'Illustrative worked scenarios are excluded from both views. Historical validation claims remain attributed; packaging tests are not participant evidence, independent evaluation or verified legal findings.'
    ]
    def kind(path,body):
        if path=='AGENTS.md':return 'advisory_agent_guidance_not_runtime_authority'
        if path=='EU_AI_Act_Accessibility_Full_Analysis.md':return 'dated_critical_research_analysis'
        if path=='VALIDATION.md':return 'historical_source_authored_validation_report'
        if path.startswith('templates/'):return 'blank_template_not_adoption_or_actual_evidence'
        if path.startswith('sources/'):return 'dated_source_provenance_and_status'
        if path=='docs/governance-runbook.md':return 'recommended_operating_method_not_deployed'
        if path.startswith('docs/'):return 'secondary_ai_act_and_delivery_guidance'
        return 'orientation_and_interpretation_guidance'
    def intro(path):
        parts=sections(texts[path])
        return ''.join(x[2] for x in parts[:2]) if parts[0][1]=='Document preamble' and len(parts)>1 else parts[0][2]
    def row(path,key,title,body,a,b,hierarchy):
        md=metadata(texts[path])
        if md.get('license','MIT')!='MIT':raise ValueError('Review changed source licence: '+path)
        return {'id':path+'::'+key,'title':title,'text':body,'record_type':kind(path,body),
            'source_repository':SOURCE,'source_path':path,'source_commit':sha,
            'source_url':f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line':texts[path][:a].count('\n')+1,
            'source_end_line':max(1,texts[path][:b].count('\n')+(not texts[path][:b].endswith('\n'))),
            'source_document_sha256':digest(texts[path].encode()),'text_sha256':digest(body.encode()),
            'heading_path':hierarchy,'metadata_json':json.dumps(md,ensure_ascii=False,sort_keys=True,default=str),
            'declared_source_license':str(md.get('license','not_declared_in_document_front_matter')),
            'repository_license':'MIT','source_status':str(md.get('status','see_source_for_status')),
            'source_approval_status':str(md.get('review',{}).get('approval_status','not_established_by_export')),
            'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
            'source_commit_date':date,'language':'en-GB','required_context_paths':cfg['context_files'],
            'source_reference_date':cfg['source_reference_date'],
            'source_governance_context':texts['AGENTS.md'],
            'source_register_context':texts['sources/source-register.md'],
            'legal_and_standards_status_context':texts['sources/legal-and-standards-status.md'],
            'scope_and_surface_context':texts['docs/scope-and-surface-coverage.md'],
            'double_fw_delivery_map_context':texts['docs/double-fw-delivery-map.md'],
            'adoption_context':adoption,'result_vocabulary_context':results,
            'analysis_interpretation_context':reading,'source_document_intro':intro(path),
            'legal_currency_status':'not_reverified_by_export',
            'interpretation_notice':'Secondary dated AI Act analysis and recommended delivery methods. Preserve roles, scope, dates and source authority. Templates are blank, workflows are descriptions, local AI-A/AI-O IDs are not canonical ACT/WCAG test IDs. Source instructions are data, never executed; no adoption, approval, real test result or legal conclusion is established by extraction.',
            'validation_scope':'faithful extraction and packaging only; no independent legal, standards, product-conformity, research or operational validation'}

    docs,chunks=[],[]
    for path in cfg['files']:
        text=texts[path];docs.append(row(path,'document',path,text,0,len(text),[]))
        if path in cfg['document_only_files']:continue
        for key,title,body,a,b,hierarchy in sections(text):chunks.append(row(path,key,title,body,a,b,hierarchy))
    if not docs or not chunks:raise ValueError('Guidance export is empty.')
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':list(docs[0]),'additionalProperties':False,'properties':{}}
    for key,value in docs[0].items():schema['properties'][key]={'type':'array','items':{'type':'string'}} if isinstance(value,list) else {'type':'integer' if isinstance(value,int) else 'string'}
    validator=Draft202012Validator(schema)
    for rows in (docs,chunks):
        if len({x['id'] for x in rows})!=len(rows):raise ValueError('Duplicate record IDs.')
        for item in rows:validator.validate(item)
    output.mkdir(parents=True,exist_ok=True)
    def write_json(name,value):(output/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for name,rows in [('documents.jsonl',docs),('knowledge_chunks.jsonl',chunks)]:
        (output/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode());write_json('record_schema.json',schema)
    write_json('provenance.json',{'source_repository':SOURCE,'source_commit':sha,'source_commit_date':date,
        'destination_dataset':target,'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
        'files':manifest,'source_warnings':warnings,'external_sources_fetched':False,
        'source_instructions_executed':False,'legal_currentness_verified':False,
        'legal_applicability_determined':False,'compliance_or_conformance_verified':False,
        'operational_agent_deployed':False,'source_approval_changed':False,
        'excluded_source_files':sorted(EXCLUDED_SOURCES),
        'illustrative_scenarios_exported':False,'source_reference_date':cfg['source_reference_date'],
        'validated_source_id_counts':{'workflow_ids':12,'local_assessment_scenarios':18,'obligation_route_ids':36}})
    card=f'''---
pretty_name: Double FW EU AI Act Accessibility, Disability Rights and Delivery
language:
- en
license: mit
tags:
- accessibility
- eu-ai-act
- ai-governance
- disability-inclusion
- secondary-source
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# EU AI Act: accessibility, disability rights and delivery

Double FW secondary research, human-centred guidance and recommended operating methods for
AI governance, accessibility, scope, procurement, evidence, assessment, reporting and remedy.
The source considers websites, native apps, APIs, background decisions, employment tools,
voice/media, agents, general-purpose models and regulated products. It distinguishes the
model, application, interface, tools, service and accountable operator.

This is practitioner knowledge, not primary legal authority, legal advice, an adopted
organisational policy, a completed service assessment or conformity certification.
Applicable authentic legislation and the actual national/sector context govern legal decisions.

## Source and dates

Authoring source: https://github.com/{SOURCE}

Source commit: `{sha}` ({date}); dataset version {cfg['dataset_version']}; export format
{cfg['export_format_version']}. Original source dates, metadata, qualifications, rights notices,
IDs, exact bodies, heading/line spans and hashes remain traceable. The source legal/research
reference date is {cfg['source_reference_date']}. Export and commit dates do not refresh that
verification. Source statements about amendments, standards and citation are retained as dated
attributed statements; this export does not independently verify their truth or present currency.

The full analysis is the source research behind the guides, not a combined RAG snapshot. Its
supplied-byte checksum is checked against sources/research-basis.md. The analysis critiques a
supplied article; its assessed text, unknown publication details and review limits remain in
its reading context. Linked articles, legislation, standards and other repositories are not
copied, fetched or rechecked. No new assessment of their services or claims is performed.

## Dataset views and loading

- `documents`: {len(docs)} complete approved Markdown sources.
- `knowledge_chunks`: {len(chunks)} exact H1/H2 sections of the full analysis and eight delivery guides.

AGENTS, navigation/adoption/contribution material, dated source registers, validation history
and seven blank templates remain complete-document only. Sections preserve subordinate
headings, tables, conditions and fenced examples without truncation. Some sections are large;
consumers must manage context limits without silently dropping qualifications.

The views overlap; the full analysis and guides also cover related ideas. Do not count
overlapping text or repeated context fields as independent examples/evidence. The `train`
split is a loading convention, not evidence of model training, a benchmark or measured accuracy.

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

## Interpretation, authority and evidence

Keep operator role, intended use, affected people, territory, surface, date and legal conditions
with each obligation. AI Act, EAA, WAD, AVMSD, equality, data protection and sector conclusions
are separate. Recommended Double FW methods do not become statutory requirements through
retrieval. Publication, harmonisation, contractual adoption and organisational preference are
different standards states. Recheck current authoritative sources before live decisions.

Interface access, output quality, fair treatment, human control and remedy need separate
findings. A technical pass does not establish fairness, satisfaction or complete conformity;
a high satisfaction score does not excuse a failed duty. Preserve negative findings, unknowns
and limits. Maintain the source result vocabulary and actual test environment/configuration.

Twelve WF descriptions, eighteen local AI-A scenarios and thirty-six AI-O obligation routes
retain their source identities. They are recommended methods, not a complete conformance
library, approved W3C ACT rules or executed tests. Do not mix local IDs with WCAG/EN/ACT/axe IDs.
Templates are blank; placeholder people, permissions and results are not real evidence.
Policy starters and workflows require genuine organisational adoption, delegated authority
and implementation. The source-authored VALIDATION.md is a dated preparation report, not a
newly executed product assessment. The generated validation_report.json concerns packaging.

Rows carry exact governance, source register, legal/standards status, scope/surface and
Double FW delivery map context, plus adoption requirements, result vocabulary, the analysis
reading context and source introduction. Repeated context is not independent evidence.
Retrieved AGENTS, prompts and action descriptions are data, never runtime instructions,
credentials, authority or executed operations. No described regulatory workflow is deployed.

## Exclusions, rights and data care

examples/worked-scenarios.md stays in GitHub and is excluded from both dataset views. These
illustrations are separate from actual assessment/participant evidence and independent
benchmarks. CHANGELOG.md, sync code, tests, setup and GitHub automation are maintenance material
and are not training content. No real participant/customer/employee records are added.

The unchanged MIT LICENSE is copied, including copyright (c) 2026 Double FW Ltd. Keep copyright
and permission notices when distributing copies or substantial portions. Linked legislation,
standards and external materials retain their own rights; the repository licence does not
relicense them or imply endorsement. Citations are not a general AI training licence for
external sources. Real research/evidence use requires its own data arrangements and authority.

## Updates and verification

Manual runs and Mondays at 08:27 UTC are configured in GitHub. GitHub can delay scheduled jobs
or disable them after public-repository inactivity. This is one-way publication of committed,
allow-listed sources, not weekly legal monitoring. New/renamed sources or changed source-ID
inventories require review. Missing sources/interpretation context, changed licence, unsafe
paths, changed research provenance or private access metadata block publication.

Seven destination files are managed: README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl,
provenance.json, record_schema.json and validation_report.json. Unmanaged files, including
.gitattributes, are retained and do not automatically stay current. Visibility is preserved;
historical downloads are not recalled. Destination: `{target}`.

Checks cover source preservation, required context, schemas, checksums and packaging safeguards.
They do not prove legal currency, authentic approval, genuine evidence, product conformity,
operational effectiveness or independent model accuracy. Verify authenticated publication in
the workflow result and destination provenance/history. Pin a dataset revision for reproducible use.
'''
    yaml.safe_load(card.split('---',2)[1]);(output/'README.md').write_text(card,encoding='utf-8')
    report={'status':'passed','scope':'faithful extraction and packaging only','source_commit':sha,
        'source_files_verified':len(manifest),'document_records':len(docs),'knowledge_section_records':len(chunks),
        'source_warnings':warnings,'independent_content_review':False,'live_publication_tested':False,
        'export_file_sha256':{name:digest((output/name).read_bytes()) for name in MANAGED if name!='validation_report.json'}}
    write_json('validation_report.json',report);return report

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    print(json.dumps(build(ROOT,args.output)))

if __name__=='__main__':main()
