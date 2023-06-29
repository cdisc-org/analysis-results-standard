# Class: OrderedSubSectionRef


_A reference to a subsection defined either globally or in another display section, ordered with respect to other subsections of the same type._





URI: [ars:OrderedSubSectionRef](https://www.cdisc.org/ars/1-0/OrderedSubSectionRef)




```mermaid
 classDiagram
    class OrderedSubSectionRef
      OrderedDisplaySubSection <|-- OrderedSubSectionRef
      
      OrderedSubSectionRef : order
        
      OrderedSubSectionRef : subSection
        
          OrderedSubSectionRef --|> DisplaySubSection : subSection
        
      OrderedSubSectionRef : subSectionId
        
          OrderedSubSectionRef --|> DisplaySubSection : subSectionId
        
      
```




## Inheritance
* [OrderedDisplaySubSection](OrderedDisplaySubSection.md)
    * **OrderedSubSectionRef**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |
| [subSection](subSection.md) | 0..1 <br/> [DisplaySubSection](DisplaySubSection.md) | NOT USED | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |
| [subSectionId](subSectionId.md) | 1..1 <br/> [DisplaySubSection](DisplaySubSection.md) | The identifier of the referenced subsection | [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OrderedSubSectionRef |
| native | ars:OrderedSubSectionRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrderedSubSectionRef
description: A reference to a subsection defined either globally or in another display
  section, ordered with respect to other subsections of the same type.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: OrderedDisplaySubSection
slot_usage:
  subSection:
    name: subSection
    description: NOT USED
    domain_of:
    - OrderedDisplaySubSection
    value_presence: ABSENT
  subSectionId:
    name: subSectionId
    domain_of:
    - OrderedDisplaySubSection
    required: true
    value_presence: PRESENT
defining_slots:
- subSectionId

```
</details>

### Induced

<details>
```yaml
name: OrderedSubSectionRef
description: A reference to a subsection defined either globally or in another display
  section, ordered with respect to other subsections of the same type.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: OrderedDisplaySubSection
slot_usage:
  subSection:
    name: subSection
    description: NOT USED
    domain_of:
    - OrderedDisplaySubSection
    value_presence: ABSENT
  subSectionId:
    name: subSectionId
    domain_of:
    - OrderedDisplaySubSection
    required: true
    value_presence: PRESENT
attributes:
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: OrderedSubSectionRef
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    range: integer
    required: true
  subSection:
    name: subSection
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subSection
    owner: OrderedSubSectionRef
    domain_of:
    - OrderedDisplaySubSection
    range: DisplaySubSection
    inlined: true
    value_presence: ABSENT
  subSectionId:
    name: subSectionId
    description: The identifier of the referenced subsection.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: subSectionId
    owner: OrderedSubSectionRef
    domain_of:
    - OrderedDisplaySubSection
    range: DisplaySubSection
    required: true
    inlined: false
    value_presence: PRESENT
defining_slots:
- subSectionId

```
</details>