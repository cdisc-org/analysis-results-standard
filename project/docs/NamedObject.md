# Class: NamedObject

_An object with a name._


* __NOTE__: this is an abstract class and should not be instantiated directly

URI: [ars:NamedObject](https://www.cdisc.org/ars/1-0/NamedObject)




```mermaid
 classDiagram
    class NamedObject
      NamedObject <|-- ReportingEvent
      NamedObject <|-- ListOfContents
      NamedObject <|-- OrderedListItem
      NamedObject <|-- ReferenceDocument
      NamedObject <|-- AnalysisSet
      NamedObject <|-- DataSubset
      NamedObject <|-- GroupingFactor
      NamedObject <|-- Group
      NamedObject <|-- AnalysisMethod
      NamedObject <|-- Operation
      NamedObject <|-- CodeParameter
      NamedObject <|-- Analysis
      NamedObject <|-- Output
      NamedObject <|-- OutputFile
      NamedObject <|-- OutputDisplay
      NamedObject : name        
        NamedObject : description        
        NamedObject : label        
        
```




## Inheritance
* **NamedObject**
    * [ReportingEvent](ReportingEvent.md)
    * [ListOfContents](ListOfContents.md)
    * [OrderedListItem](OrderedListItem.md) [ [LevelOrder](LevelOrder.md)]
    * [ReferenceDocument](ReferenceDocument.md)
    * [AnalysisSet](AnalysisSet.md) [ [WhereClause](WhereClause.md)]
    * [DataSubset](DataSubset.md) [ [WhereClause](WhereClause.md)]
    * [GroupingFactor](GroupingFactor.md)
    * [Group](Group.md) [ [WhereClause](WhereClause.md)]
    * [AnalysisMethod](AnalysisMethod.md)
    * [Operation](Operation.md)
    * [CodeParameter](CodeParameter.md)
    * [Analysis](Analysis.md)
    * [Output](Output.md)
    * [OutputFile](OutputFile.md)
    * [OutputDisplay](OutputDisplay.md)



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








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
description: An object with a name.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
slots:
- name
- description
- label

```
</details>

### Induced

<details>
```yaml
name: NamedObject
description: An object with a name.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
attributes:
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: NamedObject
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
    owner: NamedObject
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
    owner: NamedObject
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - PageRef
    range: string

```
</details>