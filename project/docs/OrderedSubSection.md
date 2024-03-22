# Class: OrderedSubSection

_A subsection ordered with respect to other subsections of the same type._




URI: [ars:OrderedSubSection](https://www.cdisc.org/ars/1-0/OrderedSubSection)




```mermaid
 classDiagram
    class OrderedSubSection
      OrderedDisplaySubSection <|-- OrderedSubSection        
      OrderedSubSection : order
        OrderedSubSection : subSection
        OrderedSubSection --|> DisplaySubSection : subSection
        OrderedSubSection : subSectionId
        OrderedSubSection --|> DisplaySubSection : subSectionId
        
```




## Inheritance
* [OrderedDisplaySubSection](OrderedDisplaySubSection.md)
    * **OrderedSubSection**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |
| [subSection](subSection.md) | 1..1 <br/> [DisplaySubSection](DisplaySubSection.md) | A defined piece of information text to display in a display section | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |
| [subSectionId](subSectionId.md) | 0..1 <br/> [DisplaySubSection](DisplaySubSection.md) | NOT USED | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OrderedSubSection |
| native | ars:OrderedSubSection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrderedSubSection
description: A subsection ordered with respect to other subsections of the same type.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: OrderedDisplaySubSection
slot_usage:
  subSection:
    name: subSection
    domain_of:
    - OrderedDisplaySubSection
    required: true
    value_presence: PRESENT
  subSectionId:
    name: subSectionId
    description: NOT USED
    domain_of:
    - OrderedDisplaySubSection
    value_presence: ABSENT
defining_slots:
- subSection

```
</details>

### Induced

<details>
```yaml
name: OrderedSubSection
description: A subsection ordered with respect to other subsections of the same type.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: OrderedDisplaySubSection
slot_usage:
  subSection:
    name: subSection
    domain_of:
    - OrderedDisplaySubSection
    required: true
    value_presence: PRESENT
  subSectionId:
    name: subSectionId
    description: NOT USED
    domain_of:
    - OrderedDisplaySubSection
    value_presence: ABSENT
attributes:
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: OrderedSubSection
    domain_of:
    - LevelOrder
    - Operation
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    range: integer
    required: true
  subSection:
    name: subSection
    description: A defined piece of information text to display in a display section.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subSection
    owner: OrderedSubSection
    domain_of:
    - OrderedDisplaySubSection
    range: DisplaySubSection
    required: true
    inlined: true
    value_presence: PRESENT
  subSectionId:
    name: subSectionId
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subSectionId
    owner: OrderedSubSection
    domain_of:
    - OrderedDisplaySubSection
    range: DisplaySubSection
    inlined: false
    value_presence: ABSENT
defining_slots:
- subSection

```
</details>