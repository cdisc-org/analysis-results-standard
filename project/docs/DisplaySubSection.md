# Class: DisplaySubSection


_An occurrence of a display section containing text that is ordered with respect to other occurrences of the same type of display section._





URI: [ars:DisplaySubSection](https://www.cdisc.org/ars/1-0/DisplaySubSection)



```mermaid
 classDiagram
    class DisplaySubSection
      DisplaySubSection : id
        
      DisplaySubSection : text
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [text](text.md) | 1..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSection](OrderedSubSection.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSection](OrderedSubSection.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [GlobalDisplaySection](GlobalDisplaySection.md) | [subSections](subSections.md) | range | [DisplaySubSection](DisplaySubSection.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:DisplaySubSection |
| native | ars:DisplaySubSection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisplaySubSection
description: An occurrence of a display section containing text that is ordered with
  respect to other occurrences of the same type of display section.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- text
slot_usage:
  text:
    name: text
    domain_of:
    - DisplaySubSection
    required: true

```
</details>

### Induced

<details>
```yaml
name: DisplaySubSection
description: An occurrence of a display section containing text that is ordered with
  respect to other occurrences of the same type of display section.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slot_usage:
  text:
    name: text
    domain_of:
    - DisplaySubSection
    required: true
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: DisplaySubSection
    domain_of:
    - ReportingEvent
    - AnalysisCategorization
    - AnalysisCategory
    - Analysis
    - AnalysisMethod
    - Operation
    - ReferencedOperationRelationship
    - Output
    - OutputDisplay
    - DisplaySubSection
    - AnalysisSet
    - GroupingFactor
    - Group
    - DataSubset
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    range: string
    required: true
  text:
    name: text
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: text
    owner: DisplaySubSection
    domain_of:
    - DisplaySubSection
    range: string
    required: true

```
</details>