# Class: TemplateCodeParameter

_A replacement parameter whose value is substituted in template programming code to create statements required for a specific analysis._




URI: [ars:TemplateCodeParameter](https://www.cdisc.org/ars/1-0/TemplateCodeParameter)




```mermaid
 classDiagram
    class TemplateCodeParameter
      CodeParameter <|-- TemplateCodeParameter

      TemplateCodeParameter : valueSource
        TemplateCodeParameter : value
        TemplateCodeParameter : name
        TemplateCodeParameter : description
        TemplateCodeParameter : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * [CodeParameter](CodeParameter.md)
        * **TemplateCodeParameter**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [valueSource](valueSource.md) | 0..1 <br/> [String](String.md) | A reference to the prespecified source of the value for the parameter | direct |
| [value](value.md) | 0..* <br/> [String](String.md) | The value to be used for the parameter when the method is used in an analysis | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | [parameters](parameters.md) | range | [TemplateCodeParameter](TemplateCodeParameter.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:TemplateCodeParameter |
| native | ars:TemplateCodeParameter |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TemplateCodeParameter
description: A replacement parameter whose value is substituted in template programming
  code to create statements required for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: CodeParameter
slots:
- valueSource
- value
slot_usage:
  value:
    name: value
    description: The value to be used for the parameter when the method is used in
      an analysis. Multiple values may be specified to indicate a choice.
    domain_of:
    - WhereClauseCondition
    - TemplateCodeParameter
    - AnalysisOutputCodeParameter
    required: false

```
</details>

### Induced

<details>
```yaml
name: TemplateCodeParameter
description: A replacement parameter whose value is substituted in template programming
  code to create statements required for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: CodeParameter
slot_usage:
  value:
    name: value
    description: The value to be used for the parameter when the method is used in
      an analysis. Multiple values may be specified to indicate a choice.
    domain_of:
    - WhereClauseCondition
    - TemplateCodeParameter
    - AnalysisOutputCodeParameter
    required: false
attributes:
  valueSource:
    name: valueSource
    description: A reference to the prespecified source of the value for the parameter.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: valueSource
    owner: TemplateCodeParameter
    domain_of:
    - TemplateCodeParameter
    range: string
  value:
    name: value
    description: The value to be used for the parameter when the method is used in
      an analysis. Multiple values may be specified to indicate a choice.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: value
    owner: TemplateCodeParameter
    domain_of:
    - WhereClauseCondition
    - TemplateCodeParameter
    - AnalysisOutputCodeParameter
    range: string
    required: false
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: TemplateCodeParameter
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
    owner: TemplateCodeParameter
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
    owner: TemplateCodeParameter
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