# Slot: condition


_A simple selection criterion exressed as [dataset].[variable] [comparator] [value(s)]_



URI: [ars:condition](https://www.cdisc.org/ars/1-0/condition)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |  no  |
[SubClause](SubClause.md) | An abstract class containing all attributes that may be specified for a sub-c... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |







## Properties

* Range: [WhereClauseCondition](WhereClauseCondition.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: condition
description: A simple selection criterion exressed as [dataset].[variable] [comparator]
  [value(s)]
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: condition
domain_of:
- WhereClause
range: WhereClauseCondition

```
</details>