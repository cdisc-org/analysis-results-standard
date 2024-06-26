# Class: ReferenceDocument

_An external document containing supporting documentation or programming code._




URI: [ars:ReferenceDocument](https://www.cdisc.org/ars/1-0/ReferenceDocument)




```mermaid
 classDiagram
    class ReferenceDocument
      NamedObject <|-- ReferenceDocument        
      ReferenceDocument : id
        ReferenceDocument : location
        ReferenceDocument : name
        ReferenceDocument : description
        ReferenceDocument : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **ReferenceDocument**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [location](location.md) | 0..1 <br/> [Uri](Uri.md) | A path (relative or absolute) indicating the location of the file | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [referenceDocuments](referenceDocuments.md) | range | [ReferenceDocument](ReferenceDocument.md) |
| [DocumentReference](DocumentReference.md) | [referenceDocumentId](referenceDocumentId.md) | range | [ReferenceDocument](ReferenceDocument.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ReferenceDocument |
| native | ars:ReferenceDocument |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferenceDocument
description: An external document containing supporting documentation or programming
  code.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- location

```
</details>

### Induced

<details>
```yaml
name: ReferenceDocument
description: An external document containing supporting documentation or programming
  code.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: ReferenceDocument
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
  location:
    name: location
    description: A path (relative or absolute) indicating the location of the file.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: location
    owner: ReferenceDocument
    domain_of:
    - ReferenceDocument
    - OutputFile
    range: uri
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: ReferenceDocument
    domain_of:
    - NamedObject
    range: string
    required: true
  description:
    name: description
    description: A textual description of the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: ReferenceDocument
    domain_of:
    - NamedObject
    - SponsorTerm
    - ReferencedOperationRelationship
    range: string
  label:
    name: label
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: ReferenceDocument
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - PageRef
    range: string

```
</details>