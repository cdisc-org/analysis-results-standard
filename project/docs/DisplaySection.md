# Class: DisplaySection


_A part of a tabular display containing one or more pieces of informational text._





URI: [ars:DisplaySection](https://www.cdisc.org/ars/1-0/DisplaySection)



```mermaid
 classDiagram
    class DisplaySection
      DisplaySection : orderedSubSections
        
          DisplaySection --|> OrderedDisplaySubSection : orderedSubSections
        
      DisplaySection : sectionType
        
          DisplaySection --|> DisplaySectionTypeEnum : sectionType
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sectionType](sectionType.md) | 0..1 <br/> [DisplaySectionTypeEnum](DisplaySectionTypeEnum.md) |  | direct |
| [orderedSubSections](orderedSubSections.md) | 0..* <br/> [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OutputDisplay](OutputDisplay.md) | [displaySections](displaySections.md) | range | [DisplaySection](DisplaySection.md) |







## Examples

| Value |
| --- |
| Title |
| Footnote |
| Legend |
| Abbreviation |

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:DisplaySection |
| native | ars:DisplaySection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisplaySection
description: A part of a tabular display containing one or more pieces of informational
  text.
examples:
- value: Title
- value: Footnote
- value: Legend
- value: Abbreviation
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- sectionType
- orderedSubSections

```
</details>

### Induced

<details>
```yaml
name: DisplaySection
description: A part of a tabular display containing one or more pieces of informational
  text.
examples:
- value: Title
- value: Footnote
- value: Legend
- value: Abbreviation
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  sectionType:
    name: sectionType
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sectionType
    owner: DisplaySection
    domain_of:
    - DisplaySection
    - GlobalDisplaySection
    range: DisplaySectionTypeEnum
  orderedSubSections:
    name: orderedSubSections
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: orderedSubSections
    owner: DisplaySection
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