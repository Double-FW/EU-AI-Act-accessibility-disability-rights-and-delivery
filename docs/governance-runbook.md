# Runbook: policies, processes, workflows and decisions

**Document RB · Version 0.1.0 · 11 November 2026**  
[Home](../README.md) · [Obligations](obligations-and-evidence.md) · [Accessibility](accessibility-delivery.md) · [Reporting](reporting.md)

## RB01 — Adopt a proportionate operating model

This runbook is a recommended management method. Legal duties come from the [source register](../sources/source-register.md), with scope and dates in the [status file](../sources/legal-and-standards-status.md). An organisation can integrate the method with existing risk, privacy, safety, accessibility, quality and procurement systems rather than create parallel bureaucracy.

Start with a service/use, assign authority and resources, and keep traceability from duty to control to observation to decision. Maintain separate legal conclusions where the same evidence supports several laws. Apply urgent corrective action immediately when needed; do not wait for the next governance meeting.

## RB02 — Assign responsibilities

The functions below are proposed roles, not appointed people. Name an accountable human, responsible people, deputies and relevant competence for each adopted activity. Small organisations can combine roles; preserve meaningful challenge for consequential decisions.

| Activity | Accountable function | Responsible/contributing functions | AI support |
| --- | --- | --- | --- |
| Programme remit and resources | Executive sponsor | Programme owner, service owners, finance. | Options, priorities and evidence summaries. |
| Applicability and legal interpretation | Delegated legal/compliance decision-maker | Service facts owner and sector/privacy specialists. | Retrieve sources; draft reasoned scope records. |
| Procurement and supplier arrangements | Service/product owner | Procurement, legal, engineering, security, accessibility. | Compare evidence and identify missing commitments. |
| Risk, FRIA and DPIA work | Relevant assessment owner within delegation | Legal, privacy, security, equality, affected groups. | Organise hazards and cross-references. |
| Design and implementation | Delivery owner | UX, brand, content, engineering and operations. | Reviewable designs, content and candidate code. |
| Assessment evidence | Assurance/test owner | Model/data evaluators, QA, AT and research specialists. | Execute authorised bounded checks and organise results. |
| Release and material change | Authorised release/service owner | Relevant independent reviewers and operations. | Produce evidence-backed recommendation. |
| Monitoring, complaints and incidents | Operational service owner | Support, incident/security/privacy leads, supplier. | Approved monitoring, routing and chronology. |
| Reporting and public claims | Authorised reporting/publication owner | Evidence owners, legal, communications and accessibility. | Draft reports; check scope and source consistency. |

AI cannot become the accountable approver by generating a name or signature. Tool availability is not delegation. Adopt controls in the organisation's real systems; these documents do not enforce them.

## RB03 — Maintain a coherent policy set

Use the [policy starter](../templates/policy-starter.md). Keep organisation-wide principles concise, with service-specific controls in records and procedures.

| Policy area | Decision to adopt | Linked process |
| --- | --- | --- |
| Responsible AI | Permitted purposes, unacceptable practices, roles, ownership and escalation. | WF02–WF03, WF11. |
| Accessibility and accommodation | Applicable baseline, complete-journey access, user choice, individual support and remedy. | WF05–WF08, WF10. |
| Data and research | Lawful/minimum data, sensitive data, recipients, retention, participation and access. | WF05–WF07. |
| Procurement | Evidence before purchase, contractual cooperation, change notices and exit. | WF04. |
| Human oversight and agent actions | Competence, authority, intervention, permissions and recovery. | WF06–WF09. |
| Transparency and content | Article 50 paragraph/exception decisions, notices, marking and accessible publishing. | WF03, WF06–WF08. |
| AI literacy | Accessible role-specific support, practice, feedback and updates. | WF05, WF09. |
| Release and change | Evidence thresholds, lawful departures, conformity route and reassessment. | WF08, WF12. |
| Reporting and remedy | Complaint access, incident clocks, authority routing and truthful claims. | WF10–WF11, reporting guide. |
| Lifecycle and retirement | Monitoring, logs, record retention, supplier termination and safe migration. | WF09, WF12. |

A policy exception can authorise a departure from an adopted internal target only within delegated authority and applicable law. It cannot waive a statutory requirement. Separate policy acceptance from legal conformity.

## RB04 — Run the workflows

Each workflow produces a reviewable record. Missing critical facts hold the affected decision, while independent authorised work continues. All template fields are blank until completed with real information.

### WF01 — Verify sources and establish the context

**Trigger:** new programme/use, legal update or a source being relied on. **Owner:** source/compliance owner. **Inputs:** service facts, source register and applicable jurisdictions.

1. Identify the authentic law and current amendment/consolidation; record exact provisions, dates and language.
2. Verify standards publication, legal citation and covered requirements separately. Check national/sector rules and current authority instructions where relevant.
3. Record source type, version, retrieval date, interpretation and limitations. Identify superseded or unavailable sources.
4. Open owned gaps; route material changes to WF12.

**Output:** dated source/status record with affected claims. **Exit:** sufficient verified sources for the next specific decision. An inaccessible source blocks only the conclusions depending on it; a search snippet alone does not prove a whole provision.

### WF02 — Inventory and decide applicability

**Trigger:** proposed, existing, acquired or changed AI use. **Owner:** service owner, with legal/compliance decision authority. **Input:** [system/scope record](../templates/system-and-scope-record.md).

1. Describe the human purpose and affected people. Map model, application, surfaces, tools, entities, countries, dates and supplier chain.
2. Apply SC02: AI definition, roles, territorial link, exclusions/sector tailoring, prohibitions, high-risk route, Article 50 and GPAI.
3. Record exact annex points and conditions, including profiling, Annex I section, legacy facts and any Article 25 role change.
4. Separate other-law applicability. Record conclusion, evidence, unresolved facts, decision-maker and review trigger.

**Output:** reasoned applicability decision. **Exit:** authorised scope/classification for dependent work; urgent suspected prohibitions route to WF11 rather than routine acceptance.

### WF03 — Map obligations and plan the programme

**Trigger:** approved scope or changed duties. **Owner:** programme/service owner. **Inputs:** scope decision and [obligation map](obligations-and-evidence.md).

1. Create local requirements linked to exact law, contract or adopted policy. Keep authority types distinct.
2. Assign outcome, control, accountable/responsible functions, evidence method, applicability date and dependencies.
3. Identify budgets, expertise, procurement lead times and affected design/brand systems. Plan all surfaces, not only the public UI.
4. Define release/monitoring criteria and reporting audiences. Preserve unresolved interpretation as an owned decision.

**Output:** funded requirement/action register and programme plan. **Exit:** owners and feasible evidence routes exist. A document's publication is not evidence that the control operates.

### WF04 — Procure and establish supply-chain cooperation

**Trigger:** selection, renewal, integration or material supplier change. **Owner:** service/procurement owner. **Input:** [supplier/change record](../templates/supplier-and-change-record.md).

1. Describe intended use, roles and required capabilities. Ask for applicable conformity, model and accessibility evidence for actual versions.
2. Examine limitations, datasets/evaluation appropriate to the buyer's role, instructions, oversight, output marking and integration requirements.
3. Arrange required information, technical access and assistance under Article 25 where relevant. Agree incident cooperation, change notices, data terms, remedies and exit.
4. Test the configured integration and complete journeys; qualify unsupported supplier assertions.

**Output:** supplier evidence disposition and contract/action record. **Exit:** authorised procurement decision with gaps and ownership. Supplier approval does not approve every subsequent use.

### WF05 — Assess harms, data, participation and capability

**Trigger:** planned high-risk use, material change or any significant potential harm. **Owner:** risk/impact owner. **Input:** [risk/impact record](../templates/risk-and-impact-record.md).

1. Identify health, safety and fundamental-rights risks, affected people, misuse, exclusion, privacy and cumulative burden.
2. Assess relevant data assumptions, gaps, proxies and bias; establish processing conditions before collecting personal/sensitive data.
3. Decide FRIA and DPIA applicability separately. Map overlapping evidence without treating either as automatically sufficient for the other. Complete relevant notification steps through the reporting owner.
4. Plan accessible participation and literacy/oversight support. Distinguish research, usability evaluation and regulated real-world testing.
5. Choose controls, verification, residual issues, owners and review triggers.

**Output:** reasoned risk/impact assessments and action plan. **Exit:** required assessments completed for dependent use and controls ready for verification. No invented participants, demographic quotas or diagnostic inference.

### WF06 — Design and implement the complete service

**Trigger:** build, configuration, remediation or content release. **Owner:** delivery owner. **Inputs:** requirements, supplier constraints, risk controls and accessibility plan.

1. Specify normal, error, interruption, refusal, uncertainty, stop, human intervention and recovery states.
2. Plan accessible UX and branding systems: foundations, components, guidance, reference assets, manual/automatable checks and task scripts.
3. Implement the applicable notices, marking and decision communications. Preserve editorial meaning and user preferences across modalities.
4. Bound agent/data access, consequential actions and recovery. Define logging without excessive personal-data retention.
5. Hand over versioned code/configuration/content, instructions, dependencies, known limits and proposed test evidence.

**Output:** reviewable implementation and assessment-ready environment. **Exit:** controls can be exercised; implementation assertion alone is not a pass.

### WF07 — Assess, test and research

**Trigger:** candidate release/change, complaint or scheduled local assessment. **Owner:** assurance/test owner. **Input:** [assessment record](../templates/assessment-and-test-record.md).

1. Confirm exact versions, supported environments, applicable clauses, methods, expected results and privacy permissions.
2. Run relevant automated, manual, AT, specialist model/data and user methods. Include negative, recovery and operator states.
3. Use controlled fixtures and repeated real-model evaluation. Record variability, subgroup/context coverage and uncertainties.
4. Keep legal/technical assessment, output quality, user research, fairness and oversight findings separate. Preserve original tool statuses.
5. Link failures to issues, owners, correction and retest. Record unavailable or invalid evidence honestly.

**Output:** executed evidence and unresolved findings. **Exit:** adequate evidence for a scoped decision; no universal conformity inferred from one scan, one group or one run.

### WF08 — Decide readiness and complete formal steps

**Trigger:** initial deployment, market release or change requiring a new decision. **Owner:** authorised release/service owner. **Inputs:** assessment package, applicable legal route, supplier and operational readiness.

1. Check scope, current sources, mandatory requirements, unresolved risks and actual evidence.
2. Complete applicable conformity assessment, declaration, CE marking, registration and information duties. Check internal-control versus notified-body/sector route.
3. Confirm competent oversight, support, complaints, monitoring and incident readiness. Exercise intervention and fallback.
4. Record decision, exact scope, conditions, remaining nonconformity, lawful rationale and review date/trigger. A launch signature cannot erase a failed obligation.
5. Approve only the specific public claim supported by evidence, through its authorised owner.

**Output:** [decision record](../templates/decision-and-corrective-action.md), required formal artifacts and operational handover. **Exit:** authorised readiness decision and verified completion of applicable formal steps. A draft submission is not a receipt.

### WF09 — Operate, monitor and support literacy

**Trigger:** operation, supplier update or local review cycle. **Owner:** operational service owner. **Inputs:** monitoring plan, instructions, approved baselines and support data.

1. Monitor performance, accessible operation, drift, output variation, harmful patterns and interactions with other systems proportionately.
2. Review complaints and excluded/abandoned journeys as well as successful usage. Minimise data and protect small groups from identification.
3. Maintain instructions, required logs and role-specific literacy/oversight capability. Check controls still operate after changes.
4. Escalate material harm to WF11 and change to WF12; verify corrections and update reporting.

**Output:** monitoring findings and management report. **Exit:** next actions owned. Suggested monthly operational, quarterly governance and annual programme reviews are local planning defaults, not AI Act reporting intervals or automations created by this repository.

### WF10 — Handle requests, explanations, complaints and access barriers

**Trigger:** access request, disputed output, complaint or rights request. **Owner:** support/remedy owner, with legal/privacy functions as required.

1. Offer accessible contact and acknowledgement. Establish the affected service/version and requested communication mode without unnecessary diagnosis.
2. Separate an accessibility issue, Article 86 explanation request, data right, equality/accommodation request and statutory complaint. Preserve all applicable routes.
3. Investigate source data, output, service process and human decision; avoid inventing a model's hidden reasoning.
4. Provide the required/relevant response in an accessible form, correction and appropriate review by a competent person.
5. Record outcome, harm, systemic implications and feedback; escalate incidents promptly through WF11.

**Output:** protected case record and linked issue/correction. **Exit:** evidenced response/remedy or explained next review/enforcement route. Apply actual statutory response times from the relevant law; do not substitute a generic service target.

### WF11 — Respond to prohibited use, risks and incidents

**Trigger:** suspected prohibited practice, unsafe/exclusionary operation, serious incident or data/security event. **Owner:** incident/service owner with relevant statutory reporting authority.

1. Protect affected people and stop/suspend the affected use when required; maintain an accessible safe alternative where practicable.
2. Preserve evidence and chronology, including awareness, causal assessment, affected versions and actions. Avoid altering evidence needed for investigation.
3. Classify each applicable reporting route: Article 26 deployer duty, Article 73 provider serious incident, GPAI, privacy/security, product safety and national/sector rules.
4. Calculate recipient and clock using the exact provision. Send authorised initial reports when completeness would otherwise delay required notification.
5. Investigate, correct, retest and decide restart through WF08. Communicate with affected people accessibly where required or appropriate.

**Output:** incident record, real submission evidence, correction/retest and lessons. **Exit:** safe, authorised next state and fulfilled reporting duties. Do not wait for a routine committee to meet before an applicable clock runs.

### WF12 — Manage changes, sources and retirement

**Trigger:** model, prompt, retrieval, renderer, purpose, autonomy, tools, population, jurisdiction, law or supplier change; withdrawal/retirement.

1. Record the change, affected dependencies and previous evidence. Determine scope/role, classification, substantial modification and legacy-design implications separately.
2. Reopen only affected requirements while preserving necessary complete-journey coverage; update legal/standards status if sources change.
3. Assess, implement and retest through relevant workflows. Maintain rollback and support continuity.
4. For retirement, remove access safely, migrate users and data, communicate consequences accessibly and apply required retention/deletion.
5. Preserve effective periods, old decisions, corrections and final closure evidence.

**Owner:** change/service owner with relevant decision authorities. **Output:** controlled change or retirement record. **Exit:** approved new state, rollback or closed service with obligations addressed.

## RB05 — Records, statuses and reporting

Use the templates as field guides; live records can remain in established organisational systems. Link by stable IDs: system/use, obligation, risk, supplier, test execution, issue, decision, incident and report. Record versions/effective periods. Keep evidence locations protected and personal data outside public repositories.

Maintain separate statuses for legal applicability, implementation, test result, approval and report submission. An approved plan is not an executed control. A fixed issue requires a linked observation; a submitted report requires evidence of sending/receipt appropriate to its route. See [reporting](reporting.md).

## RB06 — Measure whether the process helps people

Alongside statutory evidence, review independent task completion, accuracy, understanding, effort/fatigue, preference support, accommodation outcomes, challenge success, support burden and trust. Report sample size and coverage; high satisfaction cannot erase a failed requirement. Examine trends and decisions with disabled people, including those unable to use the service.

Use D01–D18 in the [delivery map](double-fw-delivery-map.md). Their methods strengthen organisational capability; adoption and actual evaluation supply operational evidence.
