# Class: WhereClauseCompoundExpression

_A compound expression consisting of either two or more where clauses combined with the `AND` or `OR` logical operator, or a single where clause negated with the `NOT` logical operator._


* __NOTE__: this is an abstract class and should not be instantiated directly

URI: [ars:WhereClauseCompoundExpression](https://www.cdisc.org/ars/1-0/WhereClauseCompoundExpression)




```mermaid
 classDiagram
    class WhereClauseCompoundExpression
      WhereClauseCompoundExpression <|-- CompoundSetExpression
      WhereClauseCompoundExpression <|-- CompoundSubsetExpression
      WhereClauseCompoundExpression <|-- CompoundGroupExpression
      WhereClauseCompoundExpression : logicalOperator        
        WhereClauseCompoundExpression --|> ExpressionLogicalOperatorEnum : logicalOperator
        WhereClauseCompoundExpression : whereClauses        
        WhereClauseCompoundExpression --|> SubClause : whereClauses
        
```




## Inheritance
* **WhereClauseCompoundExpression**
    * [CompoundSetExpression](CompoundSetExpression.md)
    * [CompoundSubsetExpression](CompoundSubsetExpression.md)
    * [CompoundGroupExpression](CompoundGroupExpression.md)



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [logicalOperator](logicalOperator.md) | 1..1 <br/> [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... | direct |
| [whereClauses](whereClauses.md) | 0..* <br/> [SubClause](SubClause.md) | A list of one or more where clauses (selection criteria) to be combined or ne... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WhereClause](WhereClause.md) | [compoundExpression](compoundExpression.md) | range | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |
| [SubClause](SubClause.md) | [compoundExpression](compoundExpression.md) | range | [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |






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
abstract: true
slots:
- logicalOperator
- whereClauses
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    any_of:
    - range: WhereClause
    - range: ReferencedWhereClause

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
abstract: true
slot_usage:
  whereClauses:
    name: whereClauses
    domain_of:
    - WhereClauseCompoundExpression
    any_of:
    - range: WhereClause
    - range: ReferencedWhereClause
attributes:
  logicalOperator:
    name: logicalOperator
    description: The boolean operator that is used to combine (AND, OR) or negate
      (NOT) the where claus(s) in the compound expression.
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
    description: A list of one or more where clauses (selection criteria) to be combined
      or negated.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: whereClauses
    owner: WhereClauseCompoundExpression
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