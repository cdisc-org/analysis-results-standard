# Class: CompoundGroupExpression

_A compound expression consisting of either two or more sub-clauses combined with the `AND` or `OR` logical operator, or a single sub-clause negated with the `NOT` logical operator. Each sub-clause is either a fully-defined `WhereClause` (containing either a `condition` or a `compoundExpression`) or a `ReferencedGroup` (containing a `subClauseId` indicating the `id` of the referenced `Group`)._




URI: [ars:CompoundGroupExpression](https://www.cdisc.org/ars/1-0/CompoundGroupExpression)




```mermaid
 classDiagram
    class CompoundGroupExpression
      WhereClauseCompoundExpression <|-- CompoundGroupExpression        
      CompoundGroupExpression : logicalOperator
        CompoundGroupExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        CompoundGroupExpression : whereClauses
        CompoundGroupExpression --|> SubClause : whereClauses
        
```




## Inheritance
* [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md)
    * **CompoundGroupExpression**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |
| [whereClauses](whereClauses.md) | 0..* <br/> [SubClause](SubClause.md) | A list of one or more where clauses (selection criteria) to be combined or ne... | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [compoundExpression](compoundExpression.md) | range | [CompoundGroupExpression](CompoundGroupExpression.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:CompoundGroupExpression |
| native | ars:CompoundGroupExpression |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompoundGroupExpression
description: A compound expression consisting of either two or more sub-clauses combined
  with the `AND` or `OR` logical operator, or a single sub-clause negated with the
  `NOT` logical operator. Each sub-clause is either a fully-defined `WhereClause`
  (containing either a `condition` or a `compoundExpression`) or a `ReferencedGroup`
  (containing a `subClauseId` indicating the `id` of the referenced `Group`).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    any_of:
    - range: ReferencedGroup
    - range: WhereClause

```
</details>

### Induced

<details>
```yaml
name: CompoundGroupExpression
description: A compound expression consisting of either two or more sub-clauses combined
  with the `AND` or `OR` logical operator, or a single sub-clause negated with the
  `NOT` logical operator. Each sub-clause is either a fully-defined `WhereClause`
  (containing either a `condition` or a `compoundExpression`) or a `ReferencedGroup`
  (containing a `subClauseId` indicating the `id` of the referenced `Group`).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    any_of:
    - range: ReferencedGroup
    - range: WhereClause
attributes:
  logicalOperator:
    name: logicalOperator
    description: The boolean operator that is used to combine (AND, OR) or negate
      (NOT) the where claus(s) in the compound expression.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: logicalOperator
    owner: CompoundGroupExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: ExpressionLogicalOperatorEnum
    required: true
  whereClauses:
    name: whereClauses
    description: A list of one or more where clauses (selection criteria) to be combined
      or negated.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: whereClauses
    owner: CompoundGroupExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: SubClause
    inlined: true
    inlined_as_list: true
    any_of:
    - range: ReferencedGroup
    - range: WhereClause

```
</details>