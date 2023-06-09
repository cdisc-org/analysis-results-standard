# Class: CodeParameter


_A replacement parameter whose value is substituted in template programming code to create statements required for a specific analysis._





URI: [ars:CodeParameter](https://www.cdisc.org/ars/1-0/CodeParameter)



```mermaid
 classDiagram
    class CodeParameter
      NamedObject <|-- CodeParameter
      

      CodeParameter <|-- TemplateCodeParameter
      
      
      CodeParameter : description
        
      CodeParameter : name
        
      CodeParameter : value
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **CodeParameter**
        * [TemplateCodeParameter](TemplateCodeParameter.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [value](value.md) | 1..1 <br/> [String](String.md) | The value of the parameter | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | [NamedObject](NamedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | [parameters](parameters.md) | range | [CodeParameter](CodeParameter.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:CodeParameter |
| native | ars:CodeParameter |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CodeParameter
description: A replacement parameter whose value is substituted in template programming
  code to create statements required for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- description
- value
slot_usage:
  value:
    name: value
    description: The value of the parameter.
    domain_of:
    - CodeParameter
    - WhereClauseCondition
    required: true

```
</details>

### Induced

<details>
```yaml
name: CodeParameter
description: A replacement parameter whose value is substituted in template programming
  code to create statements required for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slot_usage:
  value:
    name: value
    description: The value of the parameter.
    domain_of:
    - CodeParameter
    - WhereClauseCondition
    required: true
attributes:
  description:
    name: description
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: CodeParameter
    domain_of:
    - Analysis
    - AnalysisMethod
    - ReferencedOperationRelationship
    - CodeParameter
    - SponsorTerm
    range: string
  value:
    name: value
    description: The value of the parameter.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: value
    owner: CodeParameter
    domain_of:
    - CodeParameter
    - WhereClauseCondition
    range: string
    required: true
  name:
    name: name
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: CodeParameter
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>