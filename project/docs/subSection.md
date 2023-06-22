# Slot: subSection

URI: [ars:subSection](https://www.cdisc.org/ars/1-0/subSection)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedDisplaySubSection](OrderedDisplaySubSection.md) | A single subsection ordered with respect to other subsections in the same sec... |  no  |
[OrderedSubSection](OrderedSubSection.md) | A subsection ordered with respect to other subsections of the same type |  yes  |
[OrderedSubSectionRef](OrderedSubSectionRef.md) | A reference to a subsection defined either globally or in another display sec... |  yes  |







## Properties

* Range: [DisplaySubSection](DisplaySubSection.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: subSection
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: subSection
domain_of:
- OrderedDisplaySubSection
range: DisplaySubSection
inlined: true

```
</details>