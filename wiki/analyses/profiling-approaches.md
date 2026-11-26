---
title: Profiling approaches and where they have been used
type: analysis
updated: 2026-11-27
---

# Profiling approaches and where they have been used

A cumulative catalogue of the profiling approaches found in ingested sources, and of which offices use them. It has two parts: [General approaches](#general-approaches) (the list of distinct approaches) and [Country approaches](#country-approaches) (one entry per office whose approach is documented).

**Status: provisional.** The core sources are the [UN Guidelines](../sources/un-guidelines-on-sbr.md) (2024), the [Eurostat 2020 manual](../sources/european-business-profiling-2020.md) and the [Eurostat LCU Guidelines](../sources/eurostat-lcu-guidelines.md) (2026, preliminary). Allen's [2025 Wiesbaden presentation](../sources/wbg-statistical-units-2025.md) adds evidence about the choice of statistical units and comparability, but does not describe a new delineation method.

**Evidence labels.** The sources describe what each office did. Naming that practice as an "approach", and grouping offices under it, is **analyst interpretation**. Country accounts are dated snapshots, not current policy, and not a model for Stats NZ.

**How to maintain.** Procedure in [AGENTS.md](https://github.com/justin-castillo-snz/profiling/blob/main/AGENTS.md): identify the office's approach, compare it with the list below, add a general approach only if it is substantially different, and always add or update the country entry.

## General approaches

Each approach is distinguished by what the work **starts from**, the **decision rule** and the **output**.

### Top-down: from the group to autonomous enterprises

- **Starts from:** the enterprise group, ideally with the global group head or global decision centre.
- **Decision rule:** enterprises are formed first, by autonomy in the production process and resource allocation; legal units are then linked to them.
- **Output:** a statistical structure of enterprises within the group (nationally, within the resident or truncated group).
- **Documented:**
  - The UN says delineation should ideally be top-down, but it may not be feasible where only part of the group is resident and data exchange between offices is restricted. ([UN Guidelines](../sources/un-guidelines-on-sbr.md), §4.33; Box 6.11, where the top-down approach is credited with improving understanding of multinational structure; Annex F1.)
  - Eurostat's manual describes European profiling as top-down: the global enterprise is delineated within the global enterprise group, and partner offices then decide the national enterprises. ([Eurostat 2020](../sources/european-business-profiling-2020.md), §3.A and Chapters 1–4; see [European profiling](../concepts/european-profiling.md).)
- **Variants:**
  - *European collaborative:* a lead office proposes global enterprises and partner offices validate their national slices.
  - *National top-down:* a single office applies the same rule to the resident group.
  - *Business lines:* Spain uses business lines, where available, to propose enterprises.
- **Trial roster, not adoption:** by December 2017, 25 European countries had tested the European methodology for at least a year (UN Box 6.11, footnote 46). A separate Eurostat 2020 count is 26 NSIs collaborating on 241 groups in 2016–2018 (§5.C.2, p. 88), which does not name them.

### Bottom-up: from legal units to enterprises

- **Starts from:** the legal units belonging to the group (resident ones, in the national case).
- **Decision rule:** legal units are grouped to create enterprises.
- **Output:** enterprises built up from legal units.
- **Documented:**
  - The UN names it as the fallback when top-down is infeasible: delineation may "only" be possible from the resident legal units. ([UN Guidelines](../sources/un-guidelines-on-sbr.md), §4.33.)
  - Statistics Netherlands (CBS) describes it as its earlier method. It moved to top-down because, in its account, that gives a better statistical structure, although "in theory" the outcome should be identical. ([UN Guidelines](../sources/un-guidelines-on-sbr.md), Annex F5; no changeover year is given.)
- **Evidence is thin:** one office's historical method and one fallback caveat. The UN data-dictionary turnover entry lists profiling a group bottom-up as a purpose. Building up employment from legal units, as in the [Eurostat 2020 manual](../sources/european-business-profiling-2020.md), §4.E, is not in itself delineation.

### Group-perimeter mapping from public and consolidated sources

- **Starts from:** a ranked or known list of large groups (for example holding companies).
- **Decision rule:** investigators work from annual reports, financial statements and public material to identify which legal units belong to each group, with approvals for changes.
- **Output:** a validated list of group members and relationships; enterprise delineation is not the stated aim.
- **Documented:** Colombia ([UN Annex F3](../sources/un-guidelines-on-sbr.md)) and Indonesia ([UN Annex F4, C6](../sources/un-guidelines-on-sbr.md)).
- **Open question:** this may be the first stage of top-down or bottom-up work rather than a separate approach. The sources stop at the perimeter, so the two are kept apart for now.

### Operating-unit and reporting-unit mapping with the business

- **Starts from:** the register structure for an already-known complex business.
- **Decision rule:** research, then contact, to establish operating units (and, where relevant, workplaces) and what each can report.
- **Output:** locations, establishments and reporting units linked to the group, so surveys and employment data are collected and placed correctly.
- **Documented:**
  - Canada: legal and operating hierarchies, an accounts test for location versus establishment, and research before contact.
  - Switzerland: recurring workplace-employment delivery.
  - UK: a desk template with a call or visit.
  - ([UN Guidelines](../sources/un-guidelines-on-sbr.md), Annex F2, F7, F8; see [activity and location](../units/activity-and-location.md) and [observation and reporting](../units/observation-and-reporting.md).)

### Consistency-led investigation

- **Starts from:** a discrepancy between sources or periods (for example trade versus turnover, balance-of-payments flows, or survey versus tax data).
- **Decision rule:** explain the discrepancy by structure (group perimeter, branch, reporting unit) or by concept. A confirmed structural cause leads to a profile update; a conceptual or measurement cause does not.
- **Output:** corrected or explained data, and sometimes a revised profile.
- **Documented:** the LCU guidelines ([Eurostat LCU](../sources/eurostat-lcu-guidelines.md), Chapter 6 cases). §1.2 says working top-down from the group, later in the process, took longer and needed more data checked than starting at source. §5.4 describes treating the most inconsistent units first. This is a different use of "top-down" from the delineation approach above.
- **Open question:** whether this is a profiling approach or a use of profiles. LCUs are in scope, so it is listed here.

### Rule-based automatic profiling

- **Starts from:** administrative or register data on smaller or lower-priority groups.
- **Decision rule:** an algorithm derives the structure; analysts review selected cases such as significant changes.
- **Output:** a derived structure with limited manual review.
- **Documented:** [Eurostat 2020](../sources/european-business-profiling-2020.md), §6.B.1 and Table 1; [UN Guidelines](../sources/un-guidelines-on-sbr.md), Annex F5; [Eurostat LCU](../sources/eurostat-lcu-guidelines.md), §6.8. The 2020 manual names manual profiling for the largest groups and automatic profiling for the rest.
- **Limit:** the sources do not describe the algorithms in detail. Allen reports that automatically and intensively profiled enterprises raised [comparability issues](../concepts/profile-change-and-quality.md) in the EU, without identifying the affected algorithms or populations. [Wiesbaden 2025](../sources/wbg-statistical-units-2025.md), slides 10–11.

### What is not listed as a separate approach

- *Desk, light, intensive and follow-up* profiling are stages or intensities of work, not ways of delineating units. See [profiling workflow](../concepts/profiling-workflow.md) and [European profiling](../concepts/european-profiling.md).
- *Top-down* also means choosing a unit's [principal activity](../units/activity-and-location.md#activity-classification-after-delineation). This is a classification rule for an already-defined unit, not a way to form it. [UN Guidelines](../sources/un-guidelines-on-sbr.md), glossary and principal activity method; [Wiesbaden 2025](../sources/wbg-statistical-units-2025.md), slides 15–16.

## Country approaches

One row per office whose approach is documented. Offices that fit more than one approach are listed under each. "Variation" records any tweak to the general approach. Source dates differ and are shown.

| Country | Approach | Variation or tweak | Source and date |
|---|---|---|---|
| [Belgium](../countries/belgium.md) | Consistency-led | Agrees the group perimeter with Statistics Belgium before testing supply and use. Tested European profiling. | LCU §6.5 (2026, as of April 2024); UN Box 6.11 fn 46 (Dec 2017) |
| [Canada](../countries/canada.md) | Operating/reporting-unit mapping | Separate legal and operating hierarchies; research before contact; critical-establishment prioritisation | UN Annex F2 (2024) |
| [Colombia](../countries/colombia.md) | Group-perimeter mapping | Desk-led from public reports, targeted visits; truncated (resident) group | UN Annex F3 (2024) |
| [Denmark](../countries/denmark.md) | Consistency-led | Starts at the reporting legal unit; domains implement corrections. Tested European profiling. | LCU §6.1 (2026, as of April 2024); UN Box 6.11 fn 46 (Dec 2017) |
| [Finland](../countries/finland.md) | Consistency-led (decentralised) | Statistical domains do much of the work; thresholds and procedures not given. Tested European profiling. | LCU §§1.4, 2.1 (2026); UN Box 6.11 fn 46 (Dec 2017) |
| [France](../countries/france.md) | Top-down; rule-based automatic | European top-down as lead and partner; manual for the largest non-financial groups, algorithm for the rest. Separately, a legal unit with autonomous divisions was split into several enterprises. | Eurostat 2020 §6.B.1 (manuscript Feb 2020); UN Box 4.4 (2024) |
| [Indonesia](../countries/indonesia.md) | Group-perimeter mapping | Starts from a published revenue-ranked list; supervisors approve additions and relationships | UN Annex F4, C6 (2024) |
| [Ireland](../countries/ireland.md) | Consistency-led | One combined collection, edited before domains compile; ownership questions put to the group | LCU §6.2 (2026, as of April 2024) |
| [Italy](../countries/italy.md) | Consistency-led (event-driven) | News and discrepancies are leads that are verified. 2020: manual group profiling in the business-register team. Tested European profiling. | LCU §6.7 (2026); Eurostat 2020 §6.B.1; UN Box 6.11 fn 46 |
| [Netherlands](../countries/netherlands.md) | Top-down; rule-based automatic; consistency-led | Changed from bottom-up to top-down; an algorithm outside Top-X with review of significant changes; ConGO consistency checks. Tested European profiling. The 2025 slides mention establishment-based industry statistics, not a different way of delineating enterprises. | UN Annex F5 (2024); LCU §6.4; Eurostat 2020 §6.B.1; [Wiesbaden 2025](../sources/wbg-statistical-units-2025.md), slide 13 |
| [Poland](../countries/poland.md) | Consistency-led; rule-based automatic | The profiling team supplies manual and automatic results, stored by year for the LCU population. Tested European profiling. | LCU §§1.4, 6.8 (2026); Eurostat 2020 Table 1; UN Box 6.11 fn 46 |
| [Romania](../countries/romania.md) | Rule-based automatic | About 7,000 groups treated automatically, 6 manually a year, as reported in 2020 | Eurostat 2020 Table 1, p. 101 |
| [Spain](../countries/spain.md) | Top-down | Uses business lines where available; intensive validation with the group; ranking includes cross-source inconsistencies. Tested European profiling. | LCU §6.6 (2026); UN Box 6.11 fn 46 |
| [Sweden](../countries/sweden.md) | Consistency-led | Separates conceptual differences from avoidable errors; collection stays with the collection department. Tested European profiling. | LCU §6.3 (2026); UN Box 6.11 fn 46 |
| [Switzerland](../countries/switzerland.md) | Operating/reporting-unit mapping | Recurring delivery of workplace employment from large employers; tiered contact. 2020: manual for the top 400, algorithm planned. Tested European profiling. | UN Annex F7, Boxes 7.2, 7.6 (2024); Eurostat 2020 Table 1 |
| [United Kingdom](../countries/united-kingdom.md) | Operating/reporting-unit mapping | Desk template with telephone contact; visits for a few complex cases. 2020: manual for the top 2,500 groups, no automatic process in the table. Tested European profiling. The 2025 slides mention enterprise-based surveys without specifying a delineation procedure. | UN Annex F8 (2024); Eurostat 2020 §6.B.1; UN Box 6.11 fn 46; [Wiesbaden 2025](../sources/wbg-statistical-units-2025.md), slide 8 |

**Documented, but the approach is not identified.** These pages describe organisation, scope or capability without saying how enterprises or groups are formed: [South Africa](../countries/south-africa.md) (2025 Wiesbaden presentation: group-level profiling of resident groups with legal-unit classification and a turnover-plus-complexity selection rule, but no enterprise delineation rule; [presentation](../sources/wbg-stats-sa-profiling-presentation-2025.md), slides 5–12), [Australia](../countries/australia.md) (targeted maintenance, UN Box 7.2), [Germany](../countries/germany.md) (role split, LCU §2.3; tested European profiling), [Greece](../countries/greece.md) (staffing, LCU §2.3) and [Malaysia](../countries/malaysia.md) (enterprise module, UN Annex C5). Add them to the table when a source describes the approach.

**Other countries.** The UN roster of European testers also lists countries that have no page here (for example Austria and Norway). That roster only shows a trial, so they are not tabled until a source describes their practice.

## Open questions

- Should group-perimeter mapping be merged into top-down or bottom-up once more country accounts show what follows the perimeter?
- Is consistency-led investigation a profiling approach or a use of profiles? The LCU guidelines treat the two as connected but not identical.
- Do the approaches overlap in practice? The Netherlands, France and Poland appear under more than one because a single programme combines them.
- When a census collects by establishment and compiles by enterprise, is it using an existing link to enterprises or forming them from scratch? Allen's World Bank example names neither a decision rule nor a national implementation, so it is not evidence of adoption of the legal-unit bottom-up method. [Wiesbaden 2025](../sources/wbg-statistical-units-2025.md), slide 14.

Related: [Profiling practices compared](profiling-practices.md), [profiling workflow](../concepts/profiling-workflow.md), [group and enterprise](../units/group-and-enterprise.md).
