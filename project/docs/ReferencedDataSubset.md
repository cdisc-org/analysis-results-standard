# Class: ReferencedDataSubset

_A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause of a compound expression._




URI: [ars:ReferencedDataSubset](https://www.cdisc.org/ars/1-0/ReferencedDataSubset)




```mermaid
 classDiagram
    class ReferencedDataSubset
      ReferencedWhereClause <|-- ReferencedDataSubset        
      ReferencedDataSubset : subClauseId
        ReferencedDataSubset --|> DataSubset : subClauseId
        ReferencedDataSubset : level
        ReferencedDataSubset : order
        
```




## Inheritance
* [ReferencedWhereClause](ReferencedWhereClause.md) [ [LevelOrder](LevelOrder.md)]
    * **ReferencedDataSubset**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subClauseId](subClauseId.md) | 1..1 <br/> [DataSubset](DataSubset.md) | The identifier of the analysis set, data subset or group referenced in the co... | [ReferencedWhereClause](ReferencedWhereClause.md) |
| [level](level.md) | 1..1 <br/> [Integer](Integer.md) | The level of the entry within a hierarchical structure | [LevelOrder](LevelOrder.md) |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [LevelOrder](LevelOrder.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ReferencedDataSubset |
| native | ars:ReferencedDataSubset |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferencedDataSubset
description: A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause
  of a compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ReferencedWhereClause
slot_usage:
  subClauseId:
    name: subClauseId
    domain_of:
    - ReferencedWhereClause
    range: DataSubset

```
</details>

### Induced

<details>
```yaml
name: ReferencedDataSubset
description: A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause
  of a compound expression.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ReferencedWhereClause
slot_usage:
  subClauseId:
    name: subClauseId
    domain_of:
    - ReferencedWhereClause
    range: DataSubset
attributes:
  subClauseId:
    name: subClauseId
    description: The identifier of the analysis set, data subset or group referenced
      in the compound expression.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subClauseId
    owner: ReferencedDataSubset
    domain_of:
    - ReferencedWhereClause
    range: DataSubset
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
    owner: ReferencedDataSubset
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
    owner: ReferencedDataSubset
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