# Slot: compoundExpression


_A compound expression that combines or negates where clauses._



URI: [ars:compoundExpression](https://www.cdisc.org/ars/1-0/compoundExpression)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  yes  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  yes  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  yes  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |







## Properties

* Range: [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: compoundExpression
description: A compound expression that combines or negates where clauses.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: compoundExpression
domain_of:
- WhereClause
range: WhereClauseCompoundExpression

```
</details>