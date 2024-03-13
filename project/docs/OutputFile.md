# Class: OutputFile

_A file containing analysis output displays._




URI: [ars:OutputFile](https://www.cdisc.org/ars/1-0/OutputFile)




```mermaid
 classDiagram
    class OutputFile
      NamedObject <|-- OutputFile

      OutputFile : fileType
        OutputFile --|> ExtensibleTerminologyTerm : fileType
        OutputFile : location
        OutputFile : style
        OutputFile : name
        OutputFile : description
        OutputFile : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **OutputFile**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [fileType](fileType.md) | 0..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The format of the output file | direct |
| [location](location.md) | 0..1 <br/> [Uri](Uri.md) | A path (relative or absolute) indicating the location of the file | direct |
| [style](style.md) | 0..1 <br/> [String](String.md) | Reference to the specification of the style used for the output | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Output](Output.md) | [fileSpecifications](fileSpecifications.md) | range | [OutputFile](OutputFile.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OutputFile |
| native | ars:OutputFile |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OutputFile
description: A file containing analysis output displays.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- fileType
- location
- style

```
</details>

### Induced

<details>
```yaml
name: OutputFile
description: A file containing analysis output displays.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
attributes:
  fileType:
    name: fileType
    description: The format of the output file.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: fileType
    owner: OutputFile
    domain_of:
    - OutputFile
    range: ExtensibleTerminologyTerm
    any_of:
    - range: OutputFileType
    - range: SponsorOutputFileType
  location:
    name: location
    description: A path (relative or absolute) indicating the location of the file.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: location
    owner: OutputFile
    domain_of:
    - ReferenceDocument
    - OutputFile
    range: uri
  style:
    name: style
    description: Reference to the specification of the style used for the output.
    comments:
    - This is a placeholder attribute. Style specifications are not yet included in
      the model.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: style
    owner: OutputFile
    domain_of:
    - OutputFile
    range: string
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: OutputFile
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
    owner: OutputFile
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
    owner: OutputFile
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - PageRef
    range: string

```
</details>