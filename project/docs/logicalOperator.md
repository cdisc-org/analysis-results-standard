# Slot: logicalOperator


_The boolean operator that is used to combine (AND, OR) or negate (NOT) the where claus(s) in the compound expression._



URI: [ars:logicalOperator](https://www.cdisc.org/ars/1-0/logicalOperator)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | A compound expression consisting of either two or more where clauses combined... |  no  |
[CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more identified analysis se... |  no  |
[CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more where clauses combined... |  no  |
[CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more identified group combi... |  no  |







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
description: The boolean operator that is used to combine (AND, OR) or negate (NOT)
  the where claus(s) in the compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: logicalOperator
domain_of:
- WhereClauseCompoundExpression
range: ExpressionLogicalOperatorEnum
required: true

```
</details>