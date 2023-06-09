# Slot: dataGroupings


_Characteristics used to subdivide data records in the analysis dataset (e.g., visit, system organ class)._



URI: [ars:dataGroupings](https://www.cdisc.org/ars/1-0/dataGroupings)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |







## Properties

* Range: [DataGroupingFactor](DataGroupingFactor.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: dataGroupings
description: Characteristics used to subdivide data records in the analysis dataset
  (e.g., visit, system organ class).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: dataGroupings
domain_of:
- ReportingEvent
range: DataGroupingFactor
inlined: true
inlined_as_list: true

```
</details>