# Slot: orderedSubSections


_An ordered list of the informational text to display in the display section._



URI: [ars:orderedSubSections](https://www.cdisc.org/ars/1-0/orderedSubSections)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DisplaySection](DisplaySection.md) | A part of a tabular display containing one or more pieces of informational te... |  no  |







## Properties

* Range: [OrderedDisplaySubSection](OrderedDisplaySubSection.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: orderedSubSections
description: An ordered list of the informational text to display in the display section.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: orderedSubSections
domain_of:
- DisplaySection
range: OrderedDisplaySubSection
inlined: true
inlined_as_list: true
any_of:
- range: OrderedSubSection
- range: OrderedSubSectionRef

```
</details>