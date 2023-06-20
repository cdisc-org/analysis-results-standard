# Class: CompoundSubsetExpression



URI: [ars:CompoundSubsetExpression](https://www.cdisc.org/ars/1-0/CompoundSubsetExpression)



```mermaid
 classDiagram
    class CompoundSubsetExpression
      WhereClauseCompoundExpression <|-- CompoundSubsetExpression
      
      CompoundSubsetExpression : logicalOperator
        
          CompoundSubsetExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        
      CompoundSubsetExpression : whereClauses
        
          CompoundSubsetExpression --|> WhereClause : whereClauses
        
      
```





## Inheritance
* [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md)
    * **CompoundSubsetExpression**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) |  | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |
| [whereClauses](whereClauses.md) | 0..* <br/> [WhereClause](WhereClause.md) |  | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataSubset](DataSubset.md) | [compoundExpression](compoundExpression.md) | range | [CompoundSubsetExpression](CompoundSubsetExpression.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:CompoundSubsetExpression |
| native | ars:CompoundSubsetExpression |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompoundSubsetExpression
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: CompoundSubsetExpression
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClauseCompoundExpression
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    inlined: true
    inlined_as_list: true
attributes:
  logicalOperator:
    name: logicalOperator
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: logicalOperator
    owner: CompoundSubsetExpression
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
    owner: CompoundSubsetExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: WhereClause
    inlined: true
    inlined_as_list: true

```
</details>