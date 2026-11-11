# Delivering the EU AI Act from an accessibility perspective

**Document AC · Version 0.1.0 · 11 November 2026**  
[Home](../README.md) · [Runbook](governance-runbook.md) · [Double-FW methods](double-fw-delivery-map.md) · [Assessment template](../templates/assessment-and-test-record.md)

## AC01 — Define the accessibility outcome

People should be able to discover, perceive, operate, understand and benefit from the service, exercise meaningful control and obtain a remedy. Include customers, employees, operators and people affected by background decisions. Consider sensory, physical, speech, cognitive, learning, attention, fluctuating and intersecting needs without predicting an individual's capability from a diagnosis.

The direct legal anchors include **Article 16(l)** for applicable high-risk providers, **Article 13** for accessible/comprehensible deployer instructions and **Article 50(5)** for applicable transparency information. Articles 9–10, 14–15, 26–27 and rights provisions add relevant risk, data, oversight and deployment responsibilities. EAA, WAD, equality and sector obligations are separately applicable. [L01, L05–L14.]

This document provides recommended delivery methods. It does not turn every suggestion into an AI Act requirement or restrict accessibility to high-risk AI. Identify each legal/adopted-policy requirement and its actual applicability.

## AC02 — Maintain five separate assurance findings

| Finding | What to establish | Evidence methods |
| --- | --- | --- |
| Interface access | People can identify and use controls, content and state across relevant modalities. | Applicable WCAG/EN/platform assessment, manual keyboard/AT and complete-journey testing. |
| Output quality | The answer, transformed format or access feature preserves meaning and is usable for its purpose. | Source/expert review, repeated generation, comprehension and media evaluation. |
| Fair treatment | Data and decision practices do not create unlawful disadvantage; accommodations address relevant barriers. | Validity/proxy/data review, appropriate group/context analysis, case review and equality assessment. |
| Human control | Users and operators can exercise the relevant choice, intervention and recovery. | Stop/override/confirmation exercises and review of actual authority. |
| Remedy | People can question a result, provide corrections, obtain required explanations and access help. | End-to-end support/challenge tests and resolved-case evidence. |

Keep the results distinct even when a shared observation supports several. High satisfaction cannot cancel technical failure; a technical pass cannot establish fairness.

## AC03 — Discover barriers with people

Begin with real tasks, expected benefits, contexts and harm. Include people who abandon, are excluded from or cannot enter the current service, not only successful existing users. Follow D08's participation and data ethics guidance. Offer accessible recruitment, consent, communication, breaks, compensation/access support and ways to influence the questions and interpretation.

Use functional needs and optional preferences rather than demanding medical detail. EAA Annex I functional performance criteria can support coverage questions: without/with limited vision, colour perception, hearing, speech, manipulation, reach/strength, cognition, seizure risk and privacy. They are not a diagnostic segmentation system, nor permission to infer or track disability.

Record participant coverage, contexts, gaps and limitations. Neither one participant nor a synthetic persona represents a community. Simulated users can help explore a hypothesis; they are not evidence of lived experience or a replacement for affected people.

## AC04 — Establish the baseline and evidence plan

Use WF01–WF03 to determine the exact applicable legislation and standards. Recommended web delivery targets include WCAG 2.2 A/AA and applicable current EN clauses, while the legally cited edition and transition remain separately recorded. AAA items and stronger design goals stay labelled as such.

EN 301 549 covers more than web content: consider software, hardware, closed functionality, communications, documents, media and support. Apply clauses according to functions and actual versions. The [standards-status file](../sources/legal-and-standards-status.md) distinguishes publication from legal citation.

The plan should identify:

- Complete customer and operator journeys, languages, states and dependencies.
- Model, prompt, retrieval source, renderer, SDK, app, OS/browser, AT and device versions.
- Applicable legal/technical clauses and additional adopted delivery outcomes.
- Deterministic fixtures, real-model trials, negative/recovery cases and meaningful sample rationale.
- Required specialists, participant coverage, methods, expected results and protected evidence storage.
- Release criteria, defect severity, correction/retest ownership and change triggers.

Use D03's test governance, canonical outcomes, procedures and mapping sources. Retrieve exact test IDs from the owning file before adoption; no universal percentage of accessibility is assumed automatable.

## AC05 — Plan accessible UX and branding systems

Use D01's [design/brand process](https://github.com/Double-FW/Accessibility_Programme_Runbooks/blob/main/framework/design-and-brand-systems.md). Inventory the existing systems before creating new assets. Verify supplied/shared components in the real integration.

| Asset level | Required planning record for the adopted programme |
| --- | --- |
| Each foundation/practice | Outcome, guidance, applicable requirement, manual/AT method, meaningful automation and residual human work, owner/version and dependencies. Explicitly cover typography, colour, labelling/names, alternative text and content/reading order. |
| Each component/pattern | Design requirements for all states, technical techniques, delivery/evaluation methodology, versioned reference implementation, tests and user-oriented task scripts. |
| Each complete journey | Consuming components, host/integration dependencies, real input/output, errors, authentication, help, consequential steps and recovery. |

Classify automation as Direct, Partial or Manual-primary, with rationale. A property-presence test cannot establish meaningful alternative text or understandable wording. Do not create a trivial automated check just to fill a column.

For branding, preserve recognisability and purpose while evaluating inclusive communication:

| Brand ambition | Evaluate in AI-enabled service delivery |
| --- | --- |
| Help everyone identify the organisation/product/service | Clear identity, sender, source and accountable service across modalities. |
| Build trust with everyone | Accurate capabilities, honest uncertainty, reliable behaviour and usable remedy. |
| Set everybody's expectations | Understandable AI role, limits, actions, timing and consequences. |
| Create value for everyone | Access to the benefit and meaningful choice rather than a burdensome workaround. |
| Reinforce values in everyone's minds | Consistency between public commitments and operational treatment. |
| Resonate with every customer | Respectful language and relevant communication evaluated with diverse people. |

These are programme ambitions, not statutory criteria or proof that finite research establishes a universal response. Use D14 for brand reasoning and D09 for cognitive usability.

## AC06 — Choose methods appropriate to the surface

| Surface | Delivery actions | Assessment and limits |
| --- | --- | --- |
| Website/web app/WebView | Stable semantics, keyboard/focus, reading order, rendering, notices, streaming and host integration. | DOM/browser automation plus manual keyboard, AT, visual and complete-process review. axe-core addresses rendered web content, not every outcome. |
| Native mobile/desktop | Native accessibility APIs, names/roles/states, focus/navigation, scaling, contrast/preferences and device permissions. | Platform tools and real-device manual AT/input tests. A web scan or emulator does not establish native app accessibility. |
| API/headless/background AI | Structured consumable output, documentation, error/status information, relevant downstream access support and human decision process. | Contract/schema/output checks and integration/decision review. API tests do not prove downstream UI access or fairness. |
| Voice/telephone/wearable | Alternate input/output where required, speech/hearing differences, pace, repetition, transcript, privacy and recovery. | Speech/communication expertise, representative contexts, comprehension and alternate-mode journey tests. |
| Kiosk/closed-functionality/hardware | Physical reach/strength, tactile/sensory controls, audio privacy, timing, connection to AT and safe interaction. | Applicable EN/EAA/sector specialist assessment with real devices; a website keyboard script is insufficient. |
| Safety/medical/robotic product | Accessible instructions, alarms, operator control and safe stop within the safety design. | Qualified usability, safety/clinical/sector methods; no unsafe improvised failure test. |
| Media and synthetic content | Correct access assets, source fidelity, transparent content where applicable, metadata and end-to-end delivery. | Editorial/specialist and disabled-audience review through actual packaged routes/players. File syntax is not meaning. |
| Agent/action system | Clear scope, minimum permissions, accessible authorisation, confirmation as appropriate, history, cancellation and recovery. | Bounded safe test environment, tool/action traces and human intervention; simulate consequential actions before authorised real tests. |

AI Act robustness and WCAG robustness have related but different meanings. Reliable semantics/accessibility APIs support assistive technologies and some agents. Article 15 addresses accuracy, resilience and cybersecurity. No general requirement to expose an MCP server or unrestricted agent access is asserted.

## AC07 — Test the AI-specific service behaviours

These are **local recommended assessment scenarios**, not a full conformance library or approved W3C ACT rules. They all start **Not tested**. Add the applicable actual WCAG/EN clauses and canonical test IDs through D03. Human disclosure obligations come from law; WCAG supplies relevant presentation/operation requirements, not the requirement to identify AI itself.

Methods: **A** meaningful automated check; **M** manual/expert/AT; **U** participant research; **S** specialist data/model, language, media or safety review. Combined methods are complementary, not interchangeable.

| Local ID / applicability | Setup and actions | Expected observable outcome | Methods / guidance |
| --- | --- | --- | --- |
| AI-A01 — Applicable AI notices | Enter from each shipped route; read/operate the notice visually, with keyboard/AT and through relevant voice output. Repeat at first interaction/exposure. | Required AI information is clear, distinguishable, timely and accessible; no visual-only or audio-only dependency. Exception decision, if any, is separately evidenced. | A+M+U; Article 50, D07/D03. |
| AI-A02 — Discovery and complete entry | Locate/open AI help from the actual host, sign in, inspect permissions and begin the task. | Purpose, control names and navigation are understandable; no inaccessible precondition blocks use. | A+M+U; D07/D03. |
| AI-A03 — Streaming and history | Produce delayed/streamed answers; read earlier turns while new output arrives; stop and resume. | Reading position and focus remain usable; meaningful status is available without token-by-token interruption; partial output is identifiable. | A+M; D07 testing brief. |
| AI-A04 — Generated content | Generate headings, lists, links, tables, images and downloadable output with varied lengths/languages. Inspect actual rendered and exported content. | Relevant structure, labels and alternatives survive rendering/export; meaning, language and sources can be understood. | A+M+S; D03/D07. |
| AI-A05 — Comprehension and uncertainty | Ask an important question, request simpler steps, inspect sources and challenge an uncertain answer. | Simplification preserves qualifications/consequences; uncertainty and source limits are clear; users can check and recover. | M+U+S; D09/D07. |
| AI-A06 — Failure and resumption | Exercise lost connection, unknown delivery state, expiry, repeated input and return after interruption. | Draft/state follows the declared privacy policy; errors and next steps are accessible; consequential actions are not duplicated; resumption is coherent. | A+M+U; D07/D09. |
| AI-A07 — Alternative input/output | Complete the same relevant task with keyboard, speech/switch or other supported mode, and without voice where applicable. | Necessary functionality is reachable through the applicable alternatives; changing mode does not lose the task or impose unnecessary disclosure. | M+U; D03/D08. |
| AI-A08 — Native app access | On real supported devices/OS versions, use VoiceOver/TalkBack or relevant desktop AT; enlarge text, use device preferences, traverse key states and permissions. | Controls/state/content and focus/navigation remain usable; content does not clip or disappear; native and web portions connect coherently. | M+A where meaningful; D03 plus platform-specific expertise. |
| AI-A09 — Oversight and stop | Present a known erroneous output in a safe test case; ask the assigned operator to inspect, disregard/override and stop where appropriate. | Operator understands limits and has actual authority; accessible tools permit timely intervention and a safe recorded outcome. | M+S; Articles 14/26, D01/D10. |
| AI-A10 — Decision/accommodation | Evaluate a realistic application/assessment including an agreed accommodation and potentially disadvantaging proxy. Review validity/data and resulting human process. | The measure is relevant to purpose; accommodation is effective; suspected unlawful disadvantage is investigated and not hidden by an interface pass. | S+M+U; D08/D10/D11. |
| AI-A11 — Explanation and challenge | Start with an adverse decision; find and complete the relevant explanation, correction and challenge route using chosen communication/AT. | Person can understand the AI's role and relevant decision factors as required, correct information and reach the appropriate reviewer without an inaccessible loop. | M+U+S; Articles 85/86 and other law; D09/D10. |
| AI-A12 — Physical/closed product | Apply the approved specialist method to actual controls, reach, audio privacy, timing, error and safe-stop states. | Applicable physical/sensory/control requirements are demonstrated in the assessed configuration and safety constraints. | S+M+U; applicable EN/sector source; D04. |
| AI-A13 — Media access | Review generated captions/AD/signing against reference content; package/transmit/play through representative routes and seek/resume/advert transitions. | Meaning, language, timing and required information are preserved; correct assets reach and remain selectable/usable by the audience. | S+M+U; D06/D12/D13/D18. |
| AI-A14 — Marking and transformations | Where Article 50(2) applies, inspect marking/detectability and the human notice as separate outputs; transform/export through supported publishing paths. | Required marking remains effective within applicable technical conditions; accessible transformations preserve relevant provenance and disclosure. | A+S+M; Article 50 and publishing specifications. |
| AI-A15 — Agent actions and privacy | In a safe environment, give an ambiguous consequential instruction, introduce untrusted retrieved text, revoke permission and cancel/recover. Inspect tool and data traces. | Agent respects authorised scope; untrusted content does not grant permission; required confirmation is accessible; revocation/cancellation and recovery work; sensitive data is not unnecessarily exposed. | A+M+S; D01/D08/D10. |
| AI-A16 — Preference support | Choose text/pace/display/comprehension preferences; move between relevant channels, return, reverse and delete where supported. | Declared persistence/reversal works; access remains available without diagnostic inference; privacy information matches actual data flow. | A+M+U; D08/D09. |
| AI-A17 — Speech and language variation | Use relevant speech differences, accents/languages and noise conditions with authorised representative data; compare errors and recovery. | Failures are visible/correctable, alternative communication works and performance limitations are documented without equating speech difference with ability. | S+M+U; D08/D10 and specialist speech evaluation. |
| AI-A18 — Supplier/model change | Compare a recorded baseline with the changed model/SDK/configuration across affected critical and recovery journeys. | Material changes are detected, owned, corrected or routed for decision; previous evidence is not silently reused. | A+M+S/U as required; WF12, D03/D07. |

For every case retain objective, applicability, exact environment, fixture/source data, steps, expected/actual observations, method version, evaluator competence, evidence, result, limitations, defect, owner and retest. Split compound cases where assertions fail independently. Do not claim one scenario proves every related criterion.

## AC08 — Evaluate generated output and fairness proportionately

Use controlled content to verify deterministic renderer behaviour, then representative real-model prompts and outputs. Repeat trials according to purpose, variability and harm; report the rationale and observed distribution. A fixed seed or temperature does not guarantee reproduction across provider changes. A finite sample cannot establish that every future answer will be accessible.

For fairness, investigate the validity of what is measured, data/proxy assumptions, relevant performance differences, accommodations, feedback loops and actual adverse cases. Include relevant groups and intersections without publishing identifiable small cells. State uncertainty and missing populations. Equal approval rates do not alone establish lawful decision-making, and unequal rates require contextual investigation rather than automatic diagnosis.

Automated text metrics, model-as-judge scores and synthetic personas can support triage, with limitations. Expert review and actual participants establish different evidence. Do not use an LLM's self-assessment as its own release approval.

## AC09 — Release, monitor and correct

Before release, check the complete integrated customer/operator process, known material barriers, instructions, support, stop/override, applicable notices/marking and formal obligations. Keep lawful internal departures distinct from statutory nonconformity. Use WF08 for the actual decision.

Monitor both failures and outcomes: independent completion, correctness, understanding, task effort/fatigue, preference support, accommodation, human intervention, complaints and successful remedies. Use meaningful data minimisation and coverage limits. One overall score obscures the different assurance findings.

Reassess after model, prompt, retrieval, renderer, app, component, content, action permission, population, supplier or legal changes. Follow reverse dependencies from foundations/components to journeys, correct the real cause and verify the delivered result. A closed ticket or regenerated document is not evidence of restored access.
