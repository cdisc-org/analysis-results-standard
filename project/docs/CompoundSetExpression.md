# Class: CompoundSetExpression


_A compound expression consisting of either two or more identified analysis sets combined with the `AND` or `OR` logical operator, or a single identified analysis set negated with the `NOT` logical operator._





URI: [ars:CompoundSetExpression](https://www.cdisc.org/ars/1-0/CompoundSetExpression)




```mermaid
 classDiagram
    class CompoundSetExpression
      WhereClauseCompoundExpression <|-- CompoundSetExpression
      
      CompoundSetExpression : logicalOperator
        
          CompoundSetExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        
      CompoundSetExpression : whereClauses
        
          CompoundSetExpression --|> AnalysisSet : whereClauses
        
      
```




## Inheritance
* [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md)
    * **CompoundSetExpression**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |
| [whereClauses](whereClauses.md) | 0..* <br/> [AnalysisSet](AnalysisSet.md) | A list of one or more where clauses (selection criteria) to be combined or ne... | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisSet](AnalysisSet.md) | [compoundExpression](compoundExpression.md) | range | [CompoundSetExpression](CompoundSetExpression.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:CompoundSetExpression |
| native | ars:CompoundSetExpression |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompoundSetExpression
description: A compound expression consisting of either two or more identified analysis
  sets combined with the `AND` or `OR` logical operator, or a single identified analysis
  set negated with the `NOT` logical operator.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    range: AnalysisSet
    inlined: false

```
</details>

### Induced

<details>
```yaml
name: CompoundSetExpression
description: A compound expression consisting of either two or more identified analysis
  sets combined with the `AND` or `OR` logical operator, or a single identified analysis
  set negated with the `NOT` logical operator.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    range: AnalysisSet
    inlined: false
attributes:
  logicalOperator:
    name: logicalOperator
    description: The boolean operator that is used to combine (AND, OR) or negate
      (NOT) the where claus(s) in the compound expression.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: logicalOperator
    owner: CompoundSetExpression
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
    owner: CompoundSetExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: AnalysisSet
    inlined: false

```
</details>