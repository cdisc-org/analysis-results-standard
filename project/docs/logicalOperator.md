# Slot: logicalOperator

URI: [ars:logicalOperator](https://www.cdisc.org/ars/1-0/logicalOperator)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | A compound expression consisting of either two or more where clauses combined... |  no  |
[CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more identified analysis se... |  no  |
[CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more identified group combi... |  no  |
[CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more where clauses combined... |  no  |







## Properties

* Range: [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: logicalOperator
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: logicalOperator
domain_of:
- WhereClauseCompoundExpression
range: ExpressionLogicalOperatorEnum
required: true

```
</details>