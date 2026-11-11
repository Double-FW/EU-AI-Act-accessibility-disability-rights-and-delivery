# A human-centred guide to the EU AI Act

**Document HG · Version 0.1.0 · 11 November 2026**  
[Home](../README.md) · [Scope](scope-and-surface-coverage.md) · [Runbook](governance-runbook.md) · [Sources](../sources/source-register.md)

## HG01 — Begin with the people and the purpose

The EU AI Act sets conditions for trustworthy AI, protecting health, safety and fundamental rights while supporting innovation. It concerns people affected by AI as well as people directly using it. A job applicant can be affected by a ranking system they never see. An employee needs an accessible oversight dashboard. A customer needs to understand an AI assistant's limits and recover from mistakes.

The useful starting questions are: What is the person trying to achieve? What does AI change? Who benefits, who may be excluded, and who can correct a harmful result? Record the intended benefit in ordinary language before discussing a model or vendor.

This guide explains the legal framework. Examples and delivery suggestions are recommended practice unless a legal anchor states the applicable duty. The [source register](../sources/source-register.md) identifies primary law; [status](../sources/legal-and-standards-status.md) records the dated position.

## HG02 — Understand what is being regulated

The Act defines an AI system as a machine-based system with varying levels of autonomy that may show adaptiveness after deployment and infers from inputs how to generate outputs such as predictions, content, recommendations or decisions that can influence physical or virtual environments. The full legal definition and official guidance determine difficult cases. A conventional rule-based form is not automatically AI because it is software.

An AI model is not the same thing as the service built around it. Distinguish the model, configured application, website/app/interface, connected tools, human process and resulting decision. A model may be supplied through an API and affect people through a separate app or background process.

Coverage extends to relevant providers, deployers, importers, distributors, product manufacturers and representatives. It includes specified EU market/service connections and third-country operators whose outputs are used in the EU. It is not limited to consumer websites. [L01: Articles 2–3.]

**Action:** use the [scope record](../templates/system-and-scope-record.md). Include every relevant surface and entity rather than describe a whole organisation as simply compliant or non-compliant.

## HG03 — Work out your role

| Role | Plain-English meaning | Example |
| --- | --- | --- |
| Provider | Develops or has AI developed and places it on the market or puts it into service under its own name/trademark. | A business builds its own recruitment tool, including relevant own-use circumstances. |
| Deployer | Uses AI under its authority, except excluded personal non-professional activity. | An employer uses a supplier's screening tool. |
| Importer/distributor | Brings relevant third-country AI to the EU market or makes it available in the supply chain. | A reseller supplies an AI product in the EU. |
| Product manufacturer | Integrates AI with its product under the relevant conditions. | A manufacturer markets a medical device containing AI. |
| Authorised representative | Acts under the required written mandate for a non-EU provider. | A qualifying representative supports the provider's specified EU responsibilities. |
| Affected person | Experiences AI's effects, whether or not they operate the system. | A person whose benefit eligibility is evaluated. |

One organisation can hold several roles. Article 25 can move high-risk provider responsibilities downstream after rebranding, substantial modification or a change of intended purpose. Buying a component does not automatically transfer the finished system's responsibilities to its supplier. [L01: Articles 3, 16, 22–26.]

## HG04 — Assess prohibited practices first

Article 5 prohibits specified practices. The precise conditions and exceptions matter; do not label every uncomfortable use prohibited without applying the test.

| Practice family | What to investigate |
| --- | --- |
| Harmful manipulation/deception | Whether techniques materially distort informed decisions and cause or are reasonably likely to cause significant harm. |
| Exploiting vulnerability | Exploitation due to age, disability or social/economic situation, with the required distortion and harm. |
| Social scoring | Specified scoring leading to unrelated, unjustified or disproportionate detrimental treatment. |
| Criminal-risk prediction | Specified predictions based solely on profiling or personality traits, with the statutory distinction for supported human assessment. |
| Facial-image scraping | Untargeted collection to create or expand facial-recognition databases. |
| Emotion inference at work/education | The covered emotion-recognition use and any genuine medical or safety exception. |
| Sensitive biometric categorisation | Inference of the specified protected characteristics from biometrics, with statutory qualifications. |
| Real-time remote biometric identification | Public-space law-enforcement use, including narrowly defined exceptions and safeguards. |
| Non-consensual intimate material and CSAM | The new prohibited generation/manipulation practices, definitions, consent conditions and limited qualifications applying from 2 December 2026. |

Disability does not imply vulnerability in every situation. Offering a user-chosen text mode is different from exploiting a cognitive vulnerability to induce a harmful purchase. Employee consent or a product's label does not by itself make a prohibited use lawful. [L01: Article 5; L02.]

**Action:** if a prohibition is identified, stop the affected use and follow WF11. A risk-acceptance signature cannot waive a prohibition.

## HG05 — Identify high-risk systems using the actual legal routes

There are two principal routes under Article 6. The product route concerns AI that is a product or safety component covered by Annex I legislation and the relevant third-party conformity-assessment condition. The use-case route concerns Annex III. Apply the amended safety-component distinctions and special sector rules in the [scope guide](scope-and-surface-coverage.md).

| Annex III area | Illustrative concern for people |
| --- | --- |
| Permitted biometrics | Incorrect identification, categorisation or emotion inference. |
| Critical infrastructure | Failure of relevant safety functions. |
| Education/vocational training | Access, admission, evaluation, placement or specified test monitoring. |
| Employment and self-employment | Recruitment, selection, management and specified worker evaluation. |
| Essential public/private services | Specified benefits, creditworthiness, life/health insurance and emergency uses. |
| Law enforcement | Specified evidence, risk, profiling and other listed activities. |
| Migration, asylum and borders | Specified assessment, examination and identification activities. |
| Justice and democratic processes | Specified judicial assistance and influence on elections/referendums. |

These headings are not the complete tests. Read the exact point and exceptions in Annex III. AI that merely formats a document and AI that ranks applicants can have different classifications even within the same organisation.

Article 6(3) allows a qualified derogation for certain Annex III systems that do not pose significant risk and meet the stated procedural/preparatory conditions. Document the reasoning. An Annex III system performing profiling of people remains high-risk. A human final decision is not a general exemption. [L01: Article 6, Annexes I/III.]

## HG06 — Know what high-risk providers and deployers must do

Providers' obligations include risk management, relevant data governance, technical documentation, logging capability, information for deployers, human oversight, accuracy/robustness/cybersecurity, quality management, accessibility, corrective action and the relevant conformity/registration steps. [L01: Articles 8–21, 43–49, 72–73.]

Deployers need appropriate use according to instructions, competent and authorised oversight, relevant input-data controls where they control inputs, monitoring, logs under their control, relevant worker/affected-person information, public-authority registration and specified incident cooperation. [L01: Article 26.]

Conformity assessment is not always third-party certification. Many Annex III uses follow an internal-control route. A supplier's CE marking, VPAT or accessibility statement does not prove that the buyer's integrated deployment is suitable or that all duties have been met.

**Action:** use the [obligations map](obligations-and-evidence.md) to create a requirement register for the actual role. Retain separate decisions for legal applicability and actual performance.

## HG07 — Make transparency useful to people

Article 50 contains different obligations that can overlap:

| Activity | Required actor/action, where applicable |
| --- | --- |
| Direct interaction | Providers design systems so people are informed they are interacting with AI, unless the qualified obviousness or other exception applies. |
| Synthetic audio/image/video/text | Providers make outputs machine-readably marked and detectable, with stated technical and editing qualifications. |
| Permitted emotion recognition/biometric categorisation | Deployers inform exposed people. A notice does not authorise a prohibited practice. |
| Deepfake image/audio/video | Deployers disclose generation/manipulation; evidently creative/fictional work has a tailored disclosure approach. |
| Public-interest text | Deployers disclose relevant AI-generated/manipulated text, with the human-review/editorial-control and editorial-responsibility exception and other conditions. |

Applicable human information must be clear, distinguishable, accessible and provided by first interaction or exposure. Machine marking and a readable notice serve different purposes. Not every AI-assisted sentence requires the same visible label. [L01: Article 50.]

Recommended communication should explain the service's purpose and limits, what it can actually do, how to check important information, and how to get help. Avoid promises of a human adviser when no such service exists. Evaluate whether people understand the notice rather than merely see it.

## HG08 — Understand model-level responsibilities

General-purpose AI models have a separate regime. Relevant providers must maintain technical/downstream information, a copyright policy and a public training-content summary. Systemic-risk models attract additional evaluation, mitigation, incident and cybersecurity obligations. Qualified open-source exceptions do not remove every duty. [L01: Articles 51–56.]

A downstream application can have its own responsibilities even when the underlying model provider supplies documentation. A model that generates text is not a guarantee that its answers are accurate, understandable or accessible when rendered. Procurement should request information relevant to the intended use, supported populations and known failure modes.

## HG09 — Put disability inclusion into the whole service

Article 16(l) expressly requires high-risk providers to ensure accessibility in accordance with WAD and EAA requirements. Article 13 requires relevant, accessible and comprehensible instructions to deployers. Article 50(5) addresses accessible transparency information. Recital 80 connects accessibility by design to dignity, privacy, universal design and the UN disability convention. [L01; L04.]

Four questions need distinct evidence:

1. Can people operate and understand the interface?
2. Is the output correct and usable for the task?
3. Is the decision/process fair to the people affected?
4. Can people stop, correct, challenge or obtain appropriate help?

An accessible interface can conceal discriminatory scoring. An accurate response can be lost in an inaccessible app. A summary can remove a legal qualification. The [accessibility guide](accessibility-delivery.md) explains how to assess these separately across all surfaces.

AI can also improve access through communication, alternative formats, task support and user-chosen adaptations. Evaluate the benefit with people. Do not require a diagnosis or intrusive profiling as the price of using a clearer explanation or another input method.

## HG10 — Handle data and impact assessments carefully

High-risk data governance concerns suitability, representativeness, relevant statistical characteristics, assumptions, gaps and harmful bias. Disability is diverse and intersecting; one aggregate group can conceal different outcomes. The Act does not prescribe a universal disability sampling quota or require identical numerical outcomes for every group. [L01: Article 10.]

Article 4a permits exceptional special-category processing for strictly necessary bias detection/correction under cumulative safeguards. It is not a general data-sharing or model-training permission. GDPR and other applicable privacy rules remain relevant. Record why less intrusive data cannot meet the purpose, restrictions on reuse/access, the no-third-party-access condition under this route, retention/deletion and processing records. [L01: Article 4a; L08.]

A fundamental rights impact assessment under Article 27 is required for specified deployers and uses, not all AI or every private employer. It addresses processes, frequency, affected groups, harms, oversight and response/complaint arrangements. Relevant DPIA sections can be cross-referenced; a DPIA does not automatically answer all fundamental-rights questions. [L01: Article 27.]

## HG11 — Preserve human control and routes to remedy

High-risk oversight should enable competent people to understand limitations, recognise automation bias, interpret output and, as appropriate, disregard, override, reverse or stop the system safely. A person rubber-stamping an unexplained score does not establish effective oversight. Make the tools and instructions accessible to disabled operators too. [L01: Articles 14, 26.]

Article 85 provides a complaint route to market surveillance. Article 86 provides a conditional right to clear and meaningful explanations for specified adverse Annex III decisions, subject to its exclusions and other legal rights. National equality, data and sector remedies remain separate. [L01: Articles 85–87.]

Recommended service design should make correction and challenge understandable and practicable. Test a mistaken result and an inaccessible support route, then check whether someone with real authority can resolve the problem.

## HG12 — Plan around dates without postponing existing access duties

| Date | Main relevant milestone |
| --- | --- |
| 2 February 2025 | Initial literacy and original prohibited-practice provisions began applying. |
| 2 August 2025 | Relevant general-purpose model and governance provisions began applying. |
| 27 July 2026 | Enacted AI Omnibus amendment entered into force. |
| 2 August 2026 | General application, including Article 50, subject to specific exceptions. |
| 2 December 2026 | New intimate-material/CSAM provisions and relevant pre-existing generator Article 50(2) transition. |
| 2 August 2027 | Deadline for models marketed before 2 August 2025 under Article 111(3). |
| 2 December 2027 | Relevant Chapter III Sections 1–3 for Article 6(2)/Annex III high-risk systems. |
| 2 August 2028 | Relevant Chapter III Sections 1–3 for Article 6(1)/Annex I systems, with sectoral qualifications. |
| Specified 2030 dates | Particular legacy and public-authority transitions under Article 111. |

This table is a summary, not a blanket extension for every duty. Record the actual paragraph, marketing/service date, design change and role. The law may apply differently to pre-existing systems. Independent EAA, WAD, equality and sector obligations continue on their own dates. [L01: Articles 111, 113; L02.]

## HG13 — Build capability and keep learning

Amended Article 4 requires providers/deployers to take measures supporting staff and relevant operators' AI literacy, considering knowledge, context and affected groups. It does not require guaranteeing a particular individual's attainment. Use accessible, role-relevant learning, practical exercises and feedback. [L01: Article 4.]

Article 95 supports voluntary practices including inclusive design and disability accessibility outside high-risk requirements. Innovation support and sandboxes can help learning, with conditions; participation is not a compliance certificate. Relevant real-world testing has safeguards distinct from ordinary product research. [L01: Articles 57–63, 95.]

Organisations need evidence that their controls work over time. Monitor changes, investigate complaints, maintain clear ownership and correct actual barriers. The [runbook](governance-runbook.md) turns these principles into policies and workflows.
