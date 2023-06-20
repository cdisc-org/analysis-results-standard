# Class: OrderedListItem


_An item (analysis, output or sub-list) ordered relative to other items within a list or sub-list._





URI: [ars:OrderedListItem](https://www.cdisc.org/ars/1-0/OrderedListItem)



```mermaid
 classDiagram
    class OrderedListItem
      NamedObject <|-- OrderedListItem
      
      OrderedListItem : analysisId
        
          OrderedListItem --|> Analysis : analysisId
        
      OrderedListItem : level
        
      OrderedListItem : name
        
      OrderedListItem : order
        
      OrderedListItem : outputId
        
          OrderedListItem --|> Output : outputId
        
      OrderedListItem : sublist
        
          OrderedListItem --|> NestedList : sublist
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **OrderedListItem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [level](level.md) | 1..1 <br/> [Integer](Integer.md) |  | direct |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) |  | direct |
| [sublist](sublist.md) | 0..1 <br/> [NestedList](NestedList.md) |  | direct |
| [analysisId](analysisId.md) | 0..1 <br/> [Analysis](Analysis.md) |  | direct |
| [outputId](outputId.md) | 0..1 <br/> [Output](Output.md) |  | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | [NamedObject](NamedObject.md) |





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
- sublist
- analysisId
- outputId
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
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
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
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    required: true
attributes:
  level:
    name: level
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
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    range: integer
    required: true
  sublist:
    name: sublist
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: sublist
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    range: NestedList
    inlined: true
  analysisId:
    name: analysisId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: analysisId
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    - ReferencedAnalysisOperation
    - ReferencedOperationRelationship
    range: Analysis
    inlined: false
  outputId:
    name: outputId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: outputId
    owner: OrderedListItem
    domain_of:
    - OrderedListItem
    range: Output
    inlined: false
  name:
    name: name
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