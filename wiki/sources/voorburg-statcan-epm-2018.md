---
title: "Statistics Canada's Enterprise Portfolio Management (EPM) Program"
type: source
updated: 2026-11-27
---

# Statistics Canada's Enterprise Portfolio Management (EPM) Program: profiling and collecting data on large complex enterprises

Paper by the Enterprise Statistics Division, Statistics Canada, for the Voorburg Group on Services Statistics meeting, Rome, 24–28 September 2018. Eight pages; individual authors are not named.

- **Original:** `IND - Canada Enterprise Portfolio Managers.pdf`. The route by which the user obtained it is not recorded here.
- **Reading copy:** Markdown conversion under `raw/md/`, not published with this wiki.
- **Issuer and authority:** the national statistical office describing its own programme. It is a conference paper, not a manual or policy document.
- **Reference period:** 2018 ("today" in the text). The programme started in 2006. No figure is dated more precisely, so staffing and portfolio sizes are 2018 snapshots.
- **Units:** enterprise (groups of legal and operating entities), establishment, legal entity, and "collection entity". Complexity is defined for entities on the Business Register (BR).
- **Scope:** about 300 of the largest and most complex Canadian enterprises. The remaining complex enterprises are handled by profilers in the BR Division (§2).

## Evidence guide

| Section / page | What the source says |
|---|---|
| Abstract, §1 (pp. 2) | Complex businesses are about 1% of businesses and contribute more than 52% of "total economic activity" (measure not defined). The programme works with 300 businesses. Four primary roles: build relationships; maintain legal, operating and accounting structures on the BR at provincial and national level; manage data collection; ensure reported data are complete, unduplicated and coherent. |
| §2 (p. 3) | The BR is the survey frame and also holds industry and geography codes and size measures. Updates draw on Canada Revenue Agency (CRA) administrative data, survey feedback and profiling. "Simple" entities have one operating entity, one industry and one region (over 99% of about 5 million businesses). "Complex" means more than one operating entity (about 1%). |
| §3 (pp. 3–4) | Staffing: 10 Enterprise Portfolio Managers (EPMs), 5 analysts and 4 coherence specialists, with about 30 enterprises per EPM. Selection ranks BR entities by number of industries, number of regions and relative importance (revenue and employment) in those industries and regions (Godbout and Youn, 2009). Rankings are updated every two years; final coverage also reflects feedback from subject-matter divisions and the national accounts about enterprises that cause measurement problems. |
| §3.1 (p. 4) | Relationship management: one named EPM per enterprise handles profiling, collection and other help. The paper calls the resulting trust "relationship capital" and reports EPMs negotiating access to company-held data through APIs. |
| §3.2 (pp. 4–5) | Organizational profiling is the start of the cycle. EPMs spend about 60% of their time on profiles. Method: in-depth telephone or on-site interviews with senior company staff. Full reviews at least every 3 years, or sooner on signals from media, internet research or subject-matter staff. Profiling questions are mandatory under the Statistics Act. Starting evidence: CRA legal-entity list plus respondent, administrative and survey information. The EPM links legal entities to operating entities, confirms for each unit its address, industry and employees, and confirms how the business accounts for operating profit so each production unit gets the right accounting type. Collection entities are derived from the profiled structure. |
| §3.3 (p. 5) | Collection management: survey inventories (coverage, contacts, reporting history) for each enterprise; customised arrangements such as combining questionnaires and a spreadsheet tool that collects several entities on one form, delivered by secure transfer. The standard central collection service manages surveys independently and does not link them across surveys, so one respondent can receive calls from several collectors. Reported response rate for EPM enterprises: 95%. |
| §3.4 (p. 6) | Coherence analysis by specialists, mostly on enterprise- and establishment-level microdata. Compares the sum of establishment data with enterprise-level control totals from tax sources; compares with company websites, news and government sources; compares monthly sums with annual benchmarks and provincial/territorial sums with national figures. A company-specific report precedes each EPM visit. The Integrated Business Statistics Program (IBSP, from 2014) centralises annual survey and administrative data (a "DataMart"), so coherence checks can come earlier. |
| §4 (pp. 6–7) | Training and tools: a 2-week course from the BR Division with a test; online manuals and job aids; a "Profiling task list and deliverables" document; a "Research Analyst Handbook"; industry-specific profiling guides (oil and gas, head-office activities, property ownership and management). Data science staff have API access to Factiva to produce structured research reports. |
| §5 (p. 7) | Conclusion: claimed benefits are a key contact for enterprises, direct feedback for survey programmes, up-to-date structures, better coherence and quality, and lower burden. |
| References (p. 8) | Da Pont (2014); Godbout and Youn (2009); Enterprise Statistics Division (2014, internal "Orange Book"); Vinette (2009). None is in `raw/`. |

## Limitations and how to read it

- **Self-description.** The paper reports benefits (better quality, lower burden, timely feedback) but gives no measure beyond a 95% response rate for EPM enterprises, no comparison with the period before the programme or with non-EPM enterprises, and no costs. Treat the benefits as the office's own assessment, not as demonstrated effects.
- **Does not describe how enterprises are delineated.** It says EPMs identify ownership between legal and operating entities to give an "integrated structure that corresponds with how the business is organized in Canada", and test accounting capability, but gives no decision rule. See the [UN Guidelines](un-guidelines-on-sbr.md), Annex F2, for that detail.
- **No failure modes.** Difficulties, turnover, workload, refusals, legal limits or things that did not work are not discussed. Only the 60% of EPM time spent on profiles is given; the split of the rest is not.
- **Undefined terms.** "Economic activity", "relationship capital" and "coherence" are not defined quantitatively; the "complex" label here (more than one operating entity) is a BR flag, not the EPM selection score.
- **Scope of the portfolio.** 300 enterprises is a 2018 figure. Selection formula details are in Godbout and Youn (2009), which was not ingested.
- **Related but separate sources.** The same office appears in [UN Guidelines Annex F2](un-guidelines-on-sbr.md) (profiling of a complex business). The two accounts are complementary, not identical; see [Canada](../countries/canada.md).

## Related pages

[Canada](../countries/canada.md) (EPM section), [LCU coordination](../concepts/lcu-coordination.md), [case selection](../concepts/case-selection.md), [profile change and quality](../concepts/profile-change-and-quality.md), [observation and reporting](../units/observation-and-reporting.md), [profiling workflow](../concepts/profiling-workflow.md), [profiling approaches](../analyses/profiling-approaches.md).
