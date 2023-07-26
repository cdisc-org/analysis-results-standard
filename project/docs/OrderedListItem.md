# Class: OrderedListItem

_An item (analysis, output or sub-list) ordered relative to other items within a list or sub-list._




URI: [ars:OrderedListItem](https://www.cdisc.org/ars/1-0/OrderedListItem)




```mermaid
 classDiagram
    class OrderedListItem
      NamedObject <|-- OrderedListItem

      OrderedListItem : level
        OrderedListItem : order
        OrderedListItem : analysisId
        OrderedListItem --|> Analysis : analysisId
        OrderedListItem : outputId
        OrderedListItem --|> Output : outputId
        OrderedListItem : sublist
        OrderedListItem --|> NestedList : sublist
        OrderedListItem : name
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **OrderedListItem**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [level](level.md) | 1..1 <br/> [Integer](Integer.md) | The level of the entry within a hierarchical structure | direct |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | direct |
| [analysisId](analysisId.md) | 0..1 <br/> [Analysis](Analysis.md) | The identifier of the referenced analysis | direct |
| [outputId](outputId.md) | 0..1 <br/> [Output](Output.md) | The identifier of the referenced output | direct |
| [sublist](sublist.md) | 0..1 <br/> [NestedList](NestedList.md) | A sub-list of items (analyses or outputs) that may be further organized withi... | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NestedList](NestedList.md) | [listItems](listItems.md) | range | [OrderedListItem](OrderedListItem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OrderedListItem |
| native | ars:OrderedListItem |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrderedListItem
description: An item (analysis, output or sub-list) ordered relative to other items
  within a list or sub-list.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- level
- order
- analysisId
- outputId
- sublist
slot_usage:
  level:
    name: level
    domain_of:
    - OrderedListItem
    - WhereClause
    required: true
  order:
    name: order
    domain_of:
    - OrderedListItem
    - WhereClause
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    required: true

```
</details>

### Induced

<details>
```yaml
name: OrderedListItem
description: An item (analysis, output or sub-list) ordered relative to other items
  within a list or sub-list.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slot_usage:
  level:
    name: level
    domain_of:
    - OrderedListItem
    - WhereClause
    required: true
  order:
    name: order
    domain_of:
    - OrderedListItem
    - WhereClause
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    required: true
attributes:
  level:
    name: level
    description: The level of the entry within a hierarchical structure.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: level
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    - WhereClause
    range: integer
    required: true
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    - WhereClause
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    range: integer
    required: true
  analysisId:
    name: analysisId
    description: The identifier of the referenced analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: analysisId
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    - ReferencedOperationRelationship
    - ReferencedAnalysisOperation
    range: Analysis
    inlined: false
  outputId:
    name: outputId
    description: The identifier of the referenced output.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: outputId
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    range: Output
    inlined: false
  sublist:
    name: sublist
    description: A sub-list of items (analyses or outputs) that may be further organized
      within sub-lists.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: sublist
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    range: NestedList
    inlined: true
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: OrderedListItem
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>