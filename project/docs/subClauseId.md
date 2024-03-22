# Slot: subClauseId


_The identifier of the analysis set, data subset or group referenced in the compound expression._



URI: [ars:subClauseId](https://www.cdisc.org/ars/1-0/subClauseId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferencedWhereClause](ReferencedWhereClause.md) | An abstract class indicating an identified where clause (i |  yes  |
[SubClause](SubClause.md) | An abstract class containing all attributes that may be specified for a sub-c... |  yes  |
[ReferencedAnalysisSet](ReferencedAnalysisSet.md) | An `AnalysisSet` referenced by identifier (`subClauseId`) as the sub-clause o... |  yes  |
[ReferencedDataSubset](ReferencedDataSubset.md) | A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause of ... |  yes  |
[ReferencedGroup](ReferencedGroup.md) | A `Group` referenced by identifier (`subClauseId`) as the sub-clause of a com... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: subClauseId
description: The identifier of the analysis set, data subset or group referenced in
  the compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: subClauseId
domain_of:
- ReferencedWhereClause
range: string
inlined: false
inlined_as_list: false
any_of:
- range: AnalysisSet
- range: DataSubset
- range: Group

```
</details>