# Slot: condition

URI: [ars:condition](https://www.cdisc.org/ars/1-0/condition)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClause](WhereClause.md) |  |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |







## Properties

* Range: [WhereClauseCondition](WhereClauseCondition.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: condition
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: condition
domain_of:
- WhereClause
range: WhereClauseCondition

```
</details>