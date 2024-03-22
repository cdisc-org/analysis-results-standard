# Slot: level


_The level of the entry within a hierarchical structure._



URI: [ars:level](https://www.cdisc.org/ars/1-0/level)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[LevelOrder](LevelOrder.md) | An abstract class containing attributes used to position class instances with... |  no  |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |  no  |
[ReferencedWhereClause](ReferencedWhereClause.md) | An abstract class indicating an identified where clause (i |  no  |
[SubClause](SubClause.md) | An abstract class containing all attributes that may be specified for a sub-c... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[ReferencedAnalysisSet](ReferencedAnalysisSet.md) | An `AnalysisSet` referenced by identifier (`subClauseId`) as the sub-clause o... |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[ReferencedDataSubset](ReferencedDataSubset.md) | A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause of ... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[ReferencedGroup](ReferencedGroup.md) | A `Group` referenced by identifier (`subClauseId`) as the sub-clause of a com... |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





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
- LevelOrder
range: integer
required: true

```
</details>