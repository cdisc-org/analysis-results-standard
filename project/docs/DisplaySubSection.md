# Class: DisplaySubSection

_An occurrence of a display section containing text._




URI: [ars:DisplaySubSection](https://www.cdisc.org/ars/1-0/DisplaySubSection)




```mermaid
 classDiagram
    class DisplaySubSection
      DisplaySubSection : id
        DisplaySubSection : text
        
```


<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [text](text.md) | 1..1 <br/> [String](String.md) | The text to be displayed in the display section | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GlobalDisplaySection](GlobalDisplaySection.md) | [subSections](subSections.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSection](OrderedSubSection.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSection](OrderedSubSection.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | [subSection](subSection.md) | range | [DisplaySubSection](DisplaySubSection.md) |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | [subSectionId](subSectionId.md) | range | [DisplaySubSection](DisplaySubSection.md) |






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
description: An occurrence of a display section containing text.
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
description: An occurrence of a display section containing text.
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
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: DisplaySubSection
    domain_of:
    - ReportingEvent
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - AnalysisMethod
    - Operation
    - ReferencedOperationRelationship
    - Analysis
    - DisplaySubSection
    - Output
    - OutputDisplay
    range: string
    required: true
  text:
    name: text
    description: The text to be displayed in the display section.
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