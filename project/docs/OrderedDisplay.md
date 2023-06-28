# Class: OrderedDisplay


_A display ordered with respect to other displays in an analysis output._





URI: [ars:OrderedDisplay](https://www.cdisc.org/ars/1-0/OrderedDisplay)


```mermaid
erDiagram
OrderedDisplay {
    integer order  
}
OutputDisplay {
    string id  
    integer version  
    string displayTitle  
    string name  
}
DisplaySection {
    DisplaySectionTypeEnum sectionType  
}

OrderedDisplay ||--|o OutputDisplay : "display"
OutputDisplay ||--}o DisplaySection : "displaySections"
DisplaySection ||--}o OrderedDisplaySubSection : "orderedSubSections"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | direct |
| [display](display.md) | 0..1 <br/> [OutputDisplay](OutputDisplay.md) | A display contained in the output | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Output](Output.md) | [displays](displays.md) | range | [OrderedDisplay](OrderedDisplay.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OrderedDisplay |
| native | ars:OrderedDisplay |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrderedDisplay
description: A display ordered with respect to other displays in an analysis output.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- order
- display
slot_usage:
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
name: OrderedDisplay
description: A display ordered with respect to other displays in an analysis output.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slot_usage:
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
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: OrderedDisplay
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    range: integer
    required: true
  display:
    name: display
    description: A display contained in the output.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: display
    owner: OrderedDisplay
    domain_of:
    - OrderedDisplay
    range: OutputDisplay
    inlined: true

```
</details>