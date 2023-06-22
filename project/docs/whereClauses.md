# Slot: whereClauses

URI: [ars:whereClauses](https://www.cdisc.org/ars/1-0/whereClauses)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | A compound expression consisting of either two or more where clauses combined... |  no  |
[CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more identified analysis se... |  yes  |
[CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more identified group combi... |  yes  |
[CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more where clauses combined... |  yes  |







## Properties

* Range: [WhereClause](WhereClause.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: whereClauses
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: whereClauses
domain_of:
- WhereClauseCompoundExpression
range: WhereClause
inlined: false

```
</details>