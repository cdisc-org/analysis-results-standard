# Class: DisplaySection



URI: [ars:DisplaySection](https://www.cdisc.org/ars/1-0DisplaySection)



```mermaid
 classDiagram
    class DisplaySection
      DisplaySection : sectionType
        
          DisplaySection --|> DisplaySectionType : sectionType
        
      DisplaySection : subSections
        
          DisplaySection --|> DisplaySubSection : subSections
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sectionType](sectionType.md) | 0..1 <br/> [DisplaySectionType](DisplaySectionType.md) |  | direct |
| [subSections](subSections.md) | 0..* <br/> [DisplaySubSection](DisplaySubSection.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [globalDisplaySections](globalDisplaySections.md) | range | [DisplaySection](DisplaySection.md) |
| [OutputDisplay](OutputDisplay.md) | [displaySections](displaySections.md) | range | [DisplaySection](DisplaySection.md) |






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
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- sectionType
- subSections

```
</details>

### Induced

<details>
```yaml
name: DisplaySection
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
    range: DisplaySectionType
  subSections:
    name: subSections
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: subSections
    owner: DisplaySection
    domain_of:
    - DisplaySection
    range: DisplaySubSection
    inlined: true
    inlined_as_list: true

```
</details>