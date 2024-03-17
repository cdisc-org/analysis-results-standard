# Slot: analysisGroupings


_Characteristics used to subdivide the subject population (e.g., treatment, sex, age group) or data records in analysis datasets (e.g., visit, system organ class)._



URI: [ars:analysisGroupings](https://www.cdisc.org/ars/1-0/analysisGroupings)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |







## Properties

* Range: [GroupingFactor](GroupingFactor.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: analysisGroupings
description: Characteristics used to subdivide the subject population (e.g., treatment,
  sex, age group) or data records in analysis datasets (e.g., visit, system organ
  class).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: analysisGroupings
domain_of:
- ReportingEvent
range: GroupingFactor
inlined: true
inlined_as_list: true

```
</details>