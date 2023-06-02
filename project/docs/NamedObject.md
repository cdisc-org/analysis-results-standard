# Class: NamedObject


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ars:NamedObject](https://www.cdisc.org/ars/1-0NamedObject)



```mermaid
 classDiagram
    class NamedObject
      NamedObject <|-- ReportingEvent
      NamedObject <|-- OrderedListItem
      NamedObject <|-- Analysis
      NamedObject <|-- AnalysisMethod
      NamedObject <|-- Operation
      NamedObject <|-- CodeParameter
      NamedObject <|-- File
      NamedObject <|-- OutputDisplay
      NamedObject <|-- ReferenceDocument
      
      NamedObject : name
        
      
```





## Inheritance
* **NamedObject**
    * [ReportingEvent](ReportingEvent.md)
    * [OrderedListItem](OrderedListItem.md)
    * [Analysis](Analysis.md)
    * [AnalysisMethod](AnalysisMethod.md)
    * [Operation](Operation.md)
    * [CodeParameter](CodeParameter.md)
    * [File](File.md)
    * [OutputDisplay](OutputDisplay.md)
    * [ReferenceDocument](ReferenceDocument.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:NamedObject |
| native | ars:NamedObject |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedObject
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
slots:
- name

```
</details>

### Induced

<details>
```yaml
name: NamedObject
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
attributes:
  name:
    name: name
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: NamedObject
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>