# Slot: whereClauses


_A list of one or more where clauses (selection criteria) to be combined or negated._



URI: [ars:whereClauses](https://www.cdisc.org/ars/1-0/whereClauses)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | An abstract class representing a compound expression consisting of either two... |  yes  |
[CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |  yes  |
[CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |  yes  |
[CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |  yes  |







## Properties

* Range: [SubClause](SubClause.md)

* Multivalued: True





## Comments

* Each where clause may be defined as either a simple condition ([variable] [comparator] [value(s)]) or a compound expression that may combine additional simple conditions or compound expressions.
* Two or more where clauses should be specified when the logical operator is AND or OR.
* Only one where clause should be specfied when the logical operator is NOT. This where clause will usually be a compound expression.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: whereClauses
description: A list of one or more where clauses (selection criteria) to be combined
  or negated.
comments:
- Each where clause may be defined as either a simple condition ([variable] [comparator]
  [value(s)]) or a compound expression that may combine additional simple conditions
  or compound expressions.
- Two or more where clauses should be specified when the logical operator is AND or
  OR.
- Only one where clause should be specfied when the logical operator is NOT. This
  where clause will usually be a compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: whereClauses
domain_of:
- WhereClauseCompoundExpression
range: SubClause
inlined: true
inlined_as_list: true
any_of:
- range: WhereClause
- range: ReferencedWhereClause

```
</details>