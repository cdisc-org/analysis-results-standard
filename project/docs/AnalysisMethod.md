# Class: AnalysisMethod

_A set of one or more statistical operations._




URI: [ars:AnalysisMethod](https://www.cdisc.org/ars/1-0/AnalysisMethod)




```mermaid
 classDiagram
    class AnalysisMethod
      NamedObject <|-- AnalysisMethod        
      AnalysisMethod : id
        AnalysisMethod : documentRefs
        AnalysisMethod --|> DocumentReference : documentRefs
        AnalysisMethod : operations
        AnalysisMethod --|> Operation : operations
        AnalysisMethod : codeTemplate
        AnalysisMethod --|> AnalysisProgrammingCodeTemplate : codeTemplate
        AnalysisMethod : name
        AnalysisMethod : description
        AnalysisMethod : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **AnalysisMethod**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [documentRefs](documentRefs.md) | 0..* <br/> [DocumentReference](DocumentReference.md) | References to external documents containing additional information | direct |
| [operations](operations.md) | 1..* <br/> [Operation](Operation.md) | The calculations performed for the method | direct |
| [codeTemplate](codeTemplate.md) | 0..1 <br/> [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Template programming statements used to perform the statistical operations fo... | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [methods](methods.md) | range | [AnalysisMethod](AnalysisMethod.md) |
| [Analysis](Analysis.md) | [methodId](methodId.md) | range | [AnalysisMethod](AnalysisMethod.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisMethod |
| native | ars:AnalysisMethod |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisMethod
description: A set of one or more statistical operations.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- documentRefs
- operations
- codeTemplate

```
</details>

### Induced

<details>
```yaml
name: AnalysisMethod
description: A set of one or more statistical operations.
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
    owner: AnalysisMethod
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
  documentRefs:
    name: documentRefs
    description: References to external documents containing additional information.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: documentRefs
    owner: AnalysisMethod
    domain_of:
    - AnalysisMethod
    - Analysis
    - Output
    range: DocumentReference
    inlined: true
    inlined_as_list: true
  operations:
    name: operations
    description: The calculations performed for the method. Each operation generates
      a statistical result.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: operations
    owner: AnalysisMethod
    domain_of:
    - AnalysisMethod
    range: Operation
    required: true
    inlined: true
    inlined_as_list: true
  codeTemplate:
    name: codeTemplate
    description: Template programming statements used to perform the statistical operations
      for any analysis that uses this method.
    comments:
    - Template programming statements may be represented as code or as a reference
      to the program file.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: codeTemplate
    owner: AnalysisMethod
    domain_of:
    - AnalysisMethod
    range: AnalysisProgrammingCodeTemplate
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: AnalysisMethod
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
    owner: AnalysisMethod
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
    owner: AnalysisMethod
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - PageRef
    range: string

```
</details>