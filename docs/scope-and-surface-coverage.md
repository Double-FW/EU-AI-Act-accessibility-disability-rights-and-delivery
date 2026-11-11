# Scope, operator roles and surface coverage

**Document SC · Version 0.1.0 · 11 November 2026**  
[Home](../README.md) · [Human guide](human-centred-guide.md) · [Scope template](../templates/system-and-scope-record.md)

## SC01 — Make one decision per use, entity and version

The AI Act regulates systems, models, uses and operators, not a list of website types. Define the service purpose, intended use, affected people, supplier, entity, model/application version, relevant countries and marketing/service dates. Include foreseeable misuse and connected services in risk assessment. Classify distinct uses separately when necessary.

**Legal anchors:** L01 Articles 2–3, 5–7, 25, 111, 113 and Annexes I/III; L02. Sources are in the [register](../sources/source-register.md). This guide is a decision method; incomplete facts do not establish an exemption.

## SC02 — Apply the scope questions in order

| Step | Question | Retained result |
| --- | --- | --- |
| 1 | Does it meet the AI system definition, or is it a general-purpose model requiring separate analysis? | Definition analysis, function and evidence; uncertain cases retained. |
| 2 | Which entity does what: provider, deployer, importer, distributor, manufacturer or representative? | Role per system/model/use and relevant contracts. |
| 3 | What is the EU connection under Article 2? | Market/service/use/output and entity facts. |
| 4 | Does a precise exclusion, tailored sector rule or open-source condition apply? | Exact provision, evidence and limits. |
| 5 | Which applicable Article 5 practices need assessment? | Prohibition finding; specialist review for exceptions. |
| 6 | Does Article 6(1)/Annex I or Article 6(2)/Annex III classify the system high-risk? | Exact route and annex point. |
| 7 | If relying on Article 6(3), are all relevant conditions met and documented? | Reasoned derogation, profiling check and applicable documentation/registration. |
| 8 | Do Article 50 duties apply, and which paragraphs/exceptions? | Separate actor, content and notice/marking decisions. |
| 9 | Are GPAI or systemic-risk model duties relevant? | Model-level responsibility, source and downstream information. |
| 10 | What dates and legacy/change conditions apply to each duty? | Paragraph-specific applicability date, not a general system launch deadline. |
| 11 | What other legal regimes apply independently? | EAA/WAD/AVMSD/equality/privacy/procurement/sector records. |

Possible conclusions are In scope, Outside scope, Qualified/partial application or Undetermined. These are applicability findings, not test results. Assign the decision-maker, evidence, confidence, unanswered facts and review trigger.

## SC03 — Retain important exclusions and tailored rules

Article 2 includes specific national-security/military/defence, research, personal-use, international-cooperation and open-source provisions. Each has conditions. Pre-market research/development exclusion does not cover real-world testing in the same way. Publicly releasing code does not exempt high-risk systems or systems falling under Articles 5/50. GPAI model exceptions require their own analysis.

For Article 6(1) systems connected to **Annex I Section B**, Article 2(2) specifies a restricted set of AI Act provisions and sectoral integration. Do not apply the whole standard high-risk checklist by default. Establish the exact sector instrument and requirements integrated into it, including Articles 57–59 only in the circumstances stated. Aviation, transport and machinery need competent sector routing.

For **Annex I Section A**, Article 2(13) provides a mechanism for specified limitations where equivalent/higher sectoral protection exists. An organisation cannot invent an equivalence exemption: identify an actual applicable delegated measure and its scope before relying on it.

Article 6's amended safety-component rules exclude solely non-safety assistance, efficiency and convenience functions from that category, but a failure endangering health/safety can qualify. A third-party assessment concerned solely with non-health/safety risks does not automatically satisfy the product-route condition. Preserve the exact amended paragraphs.

## SC04 — Cover every relevant surface

The table identifies things to inventory and assess. It does not declare every example legally high-risk.

| Surface/system | Typical AI use | Scope and delivery focus |
| --- | --- | --- |
| Public website or embedded widget | Support, recommendations, eligibility assistant. | Host page, widget, consent/authentication, transparency, content, handoff and consequential functions. |
| Web application/SaaS | Recruitment, workflow, financial decision support. | Intended decision/use, tenant configuration, admin/operator tools and complete processes. |
| Native mobile app | Voice assistant, banking, camera interpretation. | iOS/Android accessibility APIs, device permissions, touch/AT, offline/error states and backend use. |
| Native desktop app | Document creation, staff assessment, creative AI. | Platform semantics, keyboard/AT, generated documents, updates and connected accounts. |
| API/headless or back-office system | Scoring, triage, extraction, recommendations. | Decision/data obligations despite no direct UI; downstream information, logs and accessible operator/customer touchpoints. |
| General-purpose model | Text, speech, image or multimodal foundation. | Model regime, release/licensing facts, systemic risk and downstream information. |
| Autonomous or assisted agent | Tool calls, purchases, scheduling, case processing. | Intended use and action authority; connected tools, prompts, data access, human control and rollback. |
| Voice, telephone, smart speaker or wearable | Spoken assistance, transcription, navigation. | Speech/hearing alternatives, comprehension, privacy, errors, device controls and emergency implications. |
| Kiosk, terminal or connected consumer device | Self-service, identification, payment. | Closed functionality, physical controls/reach, sensory alternatives and EAA product/service duties where applicable. |
| Medical/assistive product | Diagnosis, monitoring, physical support. | Medical intended purpose, classification, safety conditions, instructions and actual use by patients/operators. |
| Machinery, robotics and other safety products | Safety control, automation or user assistance. | Actual safety function; Annex I section and sectoral route; physical/safe-stop interface. |
| Infrastructure/transport/aviation | Specified safety, dispatch or control use. | Annex I versus Annex III route, sector integration and qualified specialist assurance. |
| Education/employment/public services | Admission, ranking, benefits, staff decisions. | Exact Annex III point, affected people, accommodations, notices, oversight and relevant FRIA. |
| Media/content production | Synthetic content, captions, description, translation. | Article 50 content duties, editorial responsibility, output quality, AVMSD/EAA and publishing route. |
| Internal administrative/oversight tool | Monitoring dashboards and report preparation. | Whether independently AI; accessible instructions and operator interfaces; support for the governed system. |

Record absent functions explicitly. A missing screen does not remove backend obligations; a system outside the AI definition may still have accessibility/equality duties.

## SC05 — Describe complete journeys and dependencies

Map discovery, information, enrolment, authentication, interaction, generated output, action/decision, confirmation, help, challenge and exit. Include the people operating the service. Identify which supplier and system owns each step.

For a model/API chain, record upstream model, middleware/retrieval, application, renderer, host/OS, action tools and human process. A barrier may arise in a different layer from the AI model. Preserve both cause and affected outcome. Use dependency links so a changed SDK or model opens the correct reassessment.

## SC06 — Revisit classification after change

Trigger WF12 after changes to purpose, people, country, model, tools, data, autonomy, product safety function or ownership. Consider whether an Article 25 role change, significant legacy design change or substantial modification/new conformity assessment is involved. These are different legal concepts; do not use one label for all.

Keep previous decisions and effective periods. An exception expires or is reopened when its assumptions no longer hold. A transition under Article 111 is not permission to ignore prohibited practices or independent laws.
