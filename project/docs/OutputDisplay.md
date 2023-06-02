# Class: OutputDisplay



URI: [ars:OutputDisplay](https://www.cdisc.org/ars/1-0OutputDisplay)



```mermaid
 classDiagram
    class OutputDisplay
      NamedObject <|-- OutputDisplay
      
      OutputDisplay : displaySections
        
          OutputDisplay --|> DisplaySection : displaySections
        
      OutputDisplay : displayTitle
        
      OutputDisplay : id
        
      OutputDisplay : name
        
      OutputDisplay : version
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **OutputDisplay**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [displayTitle](displayTitle.md) | 0..1 <br/> [String](String.md) |  | direct |
| [displaySections](displaySections.md) | 0..* <br/> [DisplaySection](DisplaySection.md) |  | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | [NamedObject](NamedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OrderedDisplay](OrderedDisplay.md) | [display](display.md) | range | [OutputDisplay](OutputDisplay.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OutputDisplay |
| native | ars:OutputDisplay |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OutputDisplay
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- version
- displayTitle
- displaySections

```
</details>

### Induced

<details>
```yaml
name: OutputDisplay
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: OutputDisplay
    domain_of:
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
    - SponsorTerm
    range: string
    required: true
  version:
    name: version
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: version
    owner: OutputDisplay
    domain_of:
    - Analysis
    - Output
    - OutputDisplay
    range: integer
  displayTitle:
    name: displayTitle
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: displayTitle
    owner: OutputDisplay
    domain_of:
    - OutputDisplay
    range: string
  displaySections:
    name: displaySections
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: displaySections
    owner: OutputDisplay
    domain_of:
    - OutputDisplay
    range: DisplaySection
    inlined: true
    inlined_as_list: true
  name:
    name: name
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: OutputDisplay
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>