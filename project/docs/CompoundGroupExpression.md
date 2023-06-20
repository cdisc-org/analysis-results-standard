# Class: CompoundGroupExpression



URI: [ars:CompoundGroupExpression](https://www.cdisc.org/ars/1-0/CompoundGroupExpression)



```mermaid
 classDiagram
    class CompoundGroupExpression
      WhereClauseCompoundExpression <|-- CompoundGroupExpression
      
      CompoundGroupExpression : logicalOperator
        
          CompoundGroupExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        
      CompoundGroupExpression : whereClauses
        
          CompoundGroupExpression --|> Group : whereClauses
        
      
```





## Inheritance
* [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md)
    * **CompoundGroupExpression**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) |  | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |
| [whereClauses](whereClauses.md) | 0..* <br/> [Group](Group.md) |  | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [compoundExpression](compoundExpression.md) | range | [CompoundGroupExpression](CompoundGroupExpression.md) |
| [AnalysisGroup](AnalysisGroup.md) | [compoundExpression](compoundExpression.md) | range | [CompoundGroupExpression](CompoundGroupExpression.md) |
| [DataGroup](DataGroup.md) | [compoundExpression](compoundExpression.md) | range | [CompoundGroupExpression](CompoundGroupExpression.md) |






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
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    range: Group
    inlined: false

```
</details>

### Induced

<details>
```yaml
name: CompoundGroupExpression
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    range: Group
    inlined: false
attributes:
  logicalOperator:
    name: logicalOperator
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
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: whereClauses
    owner: CompoundGroupExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: Group
    inlined: false

```
</details>