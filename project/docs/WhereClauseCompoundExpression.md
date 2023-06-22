# Class: WhereClauseCompoundExpression


_A compound expression consisting of either two or more where clauses combined with the `AND` or `OR` logical operator, or a single where clause negated with the `NOT` logical operator._





URI: [ars:WhereClauseCompoundExpression](https://www.cdisc.org/ars/1-0/WhereClauseCompoundExpression)



```mermaid
 classDiagram
    class WhereClauseCompoundExpression
      WhereClauseCompoundExpression <|-- CompoundSetExpression
      WhereClauseCompoundExpression <|-- CompoundGroupExpression
      WhereClauseCompoundExpression <|-- CompoundSubsetExpression
      
      WhereClauseCompoundExpression : logicalOperator
        
          WhereClauseCompoundExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        
      WhereClauseCompoundExpression : whereClauses
        
          WhereClauseCompoundExpression --|> WhereClause : whereClauses
        
      
```





## Inheritance
* **WhereClauseCompoundExpression**
    * [CompoundSetExpression](CompoundSetExpression.md)
    * [CompoundGroupExpression](CompoundGroupExpression.md)
    * [CompoundSubsetExpression](CompoundSubsetExpression.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) |  | direct |
| [whereClauses](whereClauses.md) | 0..* <br/> [WhereClause](WhereClause.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WhereClause](WhereClause.md) | [compoundExpression](compoundExpression.md) | range | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:WhereClauseCompoundExpression |
| native | ars:WhereClauseCompoundExpression |


## Examples
### Example: WhereClauseCompoundExpression-01 AND

```yaml
# Compound expression: (    ADAE.TRTEMFL EQ 'Y'
#                       AND ADAE.AESDTH EQ 'Y')
logicalOperator: AND
whereClauses:
- level: 2
  order: 1
  condition:
    dataset: ADAE
    variable: TRTEMFL
    comparator: EQ
    value:
    - Y
- level: 2
  order: 2
  condition:
    dataset: ADAE
    variable: AESDTH
    comparator: EQ
    value:
    - Y
```
### Example: WhereClauseCompoundExpression-02 NOT with OR

```yaml
# Compound expression: NOT (ADXX.VAR1 IN ('value 1','value 2') OR ADXX.VAR2 GT 37)
logicalOperator: NOT
whereClauses:
- level: 2
  order: 1
  compoundExpression:
    logicalOperator: OR
    whereClauses:
    - level: 3
      order: 1
      condition:
        dataset: ADXX
        variable: VAR1
        comparator: IN
        value:
        - value 1
        - value 2
    - level: 3
      order: 2
      condition:
        dataset: ADXX
        variable: VAR2
        comparator: GT
        value:
        - 37
```




## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WhereClauseCompoundExpression
description: A compound expression consisting of either two or more where clauses
  combined with the `AND` or `OR` logical operator, or a single where clause negated
  with the `NOT` logical operator.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- logicalOperator
- whereClauses

```
</details>

### Induced

<details>
```yaml
name: WhereClauseCompoundExpression
description: A compound expression consisting of either two or more where clauses
  combined with the `AND` or `OR` logical operator, or a single where clause negated
  with the `NOT` logical operator.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  logicalOperator:
    name: logicalOperator
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: logicalOperator
    owner: WhereClauseCompoundExpression
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
    owner: WhereClauseCompoundExpression
    domain_of:
    - WhereClauseCompoundExpression
    range: WhereClause
    inlined: false

```
</details>