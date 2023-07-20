# Slot: level


_The level of the entry within a hierarchical structure._



URI: [ars:level](https://www.cdisc.org/ars/1-0/level)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  yes  |
[WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |







## Properties

* Range: [Integer](Integer.md)





## Comments

* 1 is the top level.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: level
description: The level of the entry within a hierarchical structure.
comments:
- 1 is the top level.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: level
domain_of:
- OrderedListItem
- WhereClause
range: integer

```
</details>