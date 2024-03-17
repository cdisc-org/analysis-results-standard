# Class: ReferencedGroup

_A `Group` referenced by identifier (`subClauseId`) as the sub-clause of a compound expression._




URI: [ars:ReferencedGroup](https://www.cdisc.org/ars/1-0/ReferencedGroup)




```mermaid
 classDiagram
    class ReferencedGroup
      ReferencedWhereClause <|-- ReferencedGroup        
      ReferencedGroup : subClauseId
        ReferencedGroup --|> Group : subClauseId
        ReferencedGroup : level
        ReferencedGroup : order
        
```




## Inheritance
* [ReferencedWhereClause](ReferencedWhereClause.md) [ [LevelOrder](LevelOrder.md)]
    * **ReferencedGroup**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subClauseId](subClauseId.md) | 1..1 <br/> [Group](Group.md) | The identifier of the analysis set, data subset or group referenced in the co... | [ReferencedWhereClause](ReferencedWhereClause.md) |
| [level](level.md) | 1..1 <br/> [Integer](Integer.md) | The level of the entry within a hierarchical structure | [LevelOrder](LevelOrder.md) |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [LevelOrder](LevelOrder.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ReferencedGroup |
| native | ars:ReferencedGroup |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferencedGroup
description: A `Group` referenced by identifier (`subClauseId`) as the sub-clause
  of a compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ReferencedWhereClause
slot_usage:
  subClauseId:
    name: subClauseId
    domain_of:
    - ReferencedWhereClause
    range: Group

```
</details>

### Induced

<details>
```yaml
name: ReferencedGroup
description: A `Group` referenced by identifier (`subClauseId`) as the sub-clause
  of a compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ReferencedWhereClause
slot_usage:
  subClauseId:
    name: subClauseId
    domain_of:
    - ReferencedWhereClause
    range: Group
attributes:
  subClauseId:
    name: subClauseId
    description: The identifier of the analysis set, data subset or group referenced
      in the compound expression.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subClauseId
    owner: ReferencedGroup
    domain_of:
    - ReferencedWhereClause
    range: Group
    required: true
    inlined: false
    inlined_as_list: false
  level:
    name: level
    description: The level of the entry within a hierarchical structure.
    comments:
    - 1 is the top level.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: level
    owner: ReferencedGroup
    domain_of:
    - LevelOrder
    range: integer
    required: true
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: ReferencedGroup
    domain_of:
    - LevelOrder
    - Operation
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    range: integer
    required: true

```
</details>