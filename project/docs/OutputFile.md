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
        
      OutputFile : name
        
      OutputFile : style
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **OutputFile**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [fileType](fileType.md) | 0..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |  | direct |
| [location](location.md) | 0..1 <br/> [Uri](Uri.md) |  | direct |
| [style](style.md) | 0..1 <br/> [String](String.md) |  | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |





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
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: location
    owner: OutputFile
    domain_of:
    - OutputFile
    - ReferenceDocument
    range: uri
  style:
    name: style
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

```
</details>