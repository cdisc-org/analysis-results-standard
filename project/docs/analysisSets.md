# Slot: analysisSets


_The analysis sets (subject populations) defined for the reporting event._



URI: [ars:analysisSets](https://www.cdisc.org/ars/1-0/analysisSets)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |







## Properties

* Range: [AnalysisSet](AnalysisSet.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: analysisSets
description: The analysis sets (subject populations) defined for the reporting event.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: analysisSets
domain_of:
- ReportingEvent
range: AnalysisSet
inlined: true
inlined_as_list: true

```
</details>