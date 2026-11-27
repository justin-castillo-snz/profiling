---
title: "Statistics Canada, Integrated Business Statistics Program Overview (2015)"
type: source
updated: 2026-11-27
---

# Statistics Canada, *Integrated Business Statistics Program Overview* (2015)

> **Historical source.** Released June 2015 and written while the system was being built. Everything below describes Statistics Canada's plans and situation **as of 2015**. It is kept as historical context, not as a description of current practice. Later accounts: [Voorburg paper, 2018](voorburg-statcan-epm-2018.md).

- **Original:** `SP - StatsCan IBSP processing.pdf`. Reading copy not produced; the PDF was read directly (21 pages).
- **Issuer:** Statistics Canada, Catalogue no. 68-515-X, ISBN 978-0-660-02486-8. Authors not named. Released 2015-06-17 under the Open Licence; public, no microdata.
- **Scope:** the architecture of a programme that moves most economic surveys onto one platform. Profiling is a minor part (§§4, 8).
- **Units:** Statistics Canada's statistical enterprise, company, establishment and location (§4). These are not interchangeable with the NZ or Eurostat units.
- **Reference period:** 2015, mostly forward-looking ("will be"). By 2016 "the majority" of surveys were expected to be in the programme.

## Evidence guide

| Section / page | What the source says |
|---|---|
| §1 (p. 4) | IBSP grew from the 2010 Corporate Business Architecture initiative and replaces the Unified Enterprise Statistics (UES) programme of the late 1990s, which began with 7 pilot surveys and grew to about 60 annual surveys. The UES infrastructure was described as antiquated. |
| §2 (p. 5) | Six objectives: quality, lower response burden, modernised infrastructure, integration of most economic surveys, simpler processes, lower costs. Main features: the Business Register (BR) as the frame, electronic questionnaires, active collection management, a common editing strategy, metadata-driven processes. |
| §3 (pp. 6–8) | Metadata-driven design. Generic services for sampling (G-SAM), editing and imputation (BANFF), estimation (G-EST), confidentiality (G-CONFID) and dissemination (G-EXPORT); data services for the BR, a tax warehouse, a collection warehouse and a programme data mart. |
| §4 (pp. 9–10) | The BR is updated from administrative data, survey feedback and profiling (direct contact and internet research). 99% of BR businesses are "simple" (one operating entity, one industry, one region). "Complex" businesses are about 1% of the total but about 50% of revenue; their structure is updated mainly by profiling and survey feedback because administrative data often lack the level needed. Four derived units: **statistical enterprise** (often one legal unit, but for very complex businesses a family of legal units); **statistical company** (lowest level at which investment, operating profit, assets and liabilities can be measured); **statistical establishment** (usually a profit centre, where output value, input costs and labour can be measured); **statistical location** (lowest level, where employment and/or revenue are available). |
| §4 (pp. 9–10) | **Allocation factors** (revenue and employment) stored on the BR distribute enterprise- or company-level data to establishments and locations, giving provincial and territorial figures. Source 1 is tax payroll data by province, used when available by business number, covering all provinces where the entity operates and more current than profile data. Otherwise, BR profile variables are used (updated frequently for the most complex businesses). The revenue factor is used for most variables; the employment factor for salaries and wages. Subject-matter analysts validate the factors. A field retains commodity and activity flags maintained by subject-matter divisions to support sample selection. |
| §5 (p. 11) | Content model uses NAICS, NAPCS and a Chart of Accounts that bridges tax concepts and national accounts needs; revenue and expense variables are mapped to tax files. |
| §6 (pp. 12–13) | Tax data are the backbone of financial estimates. About 2,000 very complex enterprises are mostly surveyed directly. "Smart replacement" may substitute administrative data for survey data for some complex businesses, judged case by case on availability, accuracy and coherence, and operational and structural stability over the last 3 years, compared across the 3 most recent survey cycles. Active collection management uses rolling estimates and quality and impact indicators to target follow-up. |
| §7 (p. 14) | Under UES, coherence analysis happened after release. IBSP moves it into collection; a prototype viewer targets gaps between enterprise- and establishment-level data and duplication across surveys. |
| §8 (pp. 14–15) | Largest units are always sampled. The **Enterprise Portfolio Manager (EPM)** programme works with the largest and most complex businesses to keep frame profiles current, negotiate reporting arrangements, ensure coherent reporting across surveys and act as single contact. A parallel agriculture programme (LAOS) does the same for the largest farms and also collects their data. In 2015: EPM covered 330 enterprise groups (several thousand establishments), about 90% response; LAOS covered 370 enterprises. Custom reporting relied on spreadsheets incorporating essential variables, costing substantial manual effort and preventing early coherence analysis; a metadata-based customisable reporting tool was planned. |
| §9 (pp. 15–16) | Two-phase sampling (phase 1 collects commodity and activity information for phase 2 selection; example: only 40–60% of 30,000 units on one capital expenditure survey reported such spending). Weights calibrated to tax totals for "take-some" units; "take-all" units keep weight 1; "take-none" units are covered with tax data. Updates from phase 1 or supplements go to the BR through EPM or the BR profile programme. |
| §§10–11 (pp. 17–20) | Top-down analysis with selective editing on rolling estimates, shared by national accounts and subject-matter staff. Governance by eight committees (top: Program Management Team); change management and an integrated schedule. |

## Limitations

- **Dated and prospective.** Figures (99%/1%/50%, 330 groups, 2,000 very complex enterprises, 90% response) are 2015 values. The 2018 paper gives about 300 enterprises, 95% response and "more than 52%" of activity, with different wording; see [Canada](../countries/canada.md). Differences may reflect time, definition or scope; neither paper explains.
- **Not a profiling manual.** No delineation rules, interview method or review cycle; for those see [UN Guidelines Annex F2](un-guidelines-on-sbr.md) and the 2018 paper.
- **Internal references unavailable.** Cited internal documents were not in `raw/`.
- **"Revenue" and "activity" shares are not defined** beyond the BR context.

## Related pages

[Canada](../countries/canada.md), [Voorburg EPM paper](voorburg-statcan-epm-2018.md), [establishment, KAU and local unit](../units/activity-and-location.md), [observation and reporting](../units/observation-and-reporting.md), [LCU coordination](../concepts/lcu-coordination.md), [profile change and quality](../concepts/profile-change-and-quality.md), [glossary](../concepts/glossary.md).
