# Class: AnalysisProgrammingCodeTemplate


_Programming statements and/or a reference to a used as a template for creation of a program to perform method operations for a specific analysis._





URI: [ars:AnalysisProgrammingCodeTemplate](https://www.cdisc.org/ars/1-0/AnalysisProgrammingCodeTemplate)




```mermaid
 classDiagram
    class AnalysisProgrammingCodeTemplate
      AnalysisProgrammingCodeTemplate : code
        
      AnalysisProgrammingCodeTemplate : context
        
      AnalysisProgrammingCodeTemplate : documentRef
        
          AnalysisProgrammingCodeTemplate --|> DocumentReference : documentRef
        
      AnalysisProgrammingCodeTemplate : parameters
        
          AnalysisProgrammingCodeTemplate --|> TemplateCodeParameter : parameters
        
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [context](context.md) | 1..1 <br/> [String](String.md) | The name and version of the computer language used for the actual programming... | direct |
| [code](code.md) | 0..1 <br/> [String](String.md) | Programming statements used to perform the specific analysis | direct |
| [documentRef](documentRef.md) | 0..1 <br/> [DocumentReference](DocumentReference.md) | A reference to the document containing programming code | direct |
| [parameters](parameters.md) | 0..* <br/> [TemplateCodeParameter](TemplateCodeParameter.md) | Parameters whose values will be used to generate or execute the programming c... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisMethod](AnalysisMethod.md) | [codeTemplate](codeTemplate.md) | range | [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisProgrammingCodeTemplate |
| native | ars:AnalysisProgrammingCodeTemplate |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisProgrammingCodeTemplate
description: Programming statements and/or a reference to a used as a template for
  creation of a program to perform method operations for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- context
- code
- documentRef
- parameters
slot_usage:
  parameters:
    name: parameters
    description: Parameters whose values will be used to generate or execute the programming
      code for a specific analysis.
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: TemplateCodeParameter

```
</details>

### Induced

<details>
```yaml
name: AnalysisProgrammingCodeTemplate
description: Programming statements and/or a reference to a used as a template for
  creation of a program to perform method operations for a specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slot_usage:
  parameters:
    name: parameters
    description: Parameters whose values will be used to generate or execute the programming
      code for a specific analysis.
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: TemplateCodeParameter
attributes:
  context:
    name: context
    description: The name and version of the computer language used for the actual
      programming statements provided.
    examples:
    - value: SAS Version 9.4
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: context
    owner: AnalysisProgrammingCodeTemplate
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: string
    required: true
  code:
    name: code
    description: Programming statements used to perform the specific analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: code
    owner: AnalysisProgrammingCodeTemplate
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: string
  documentRef:
    name: documentRef
    description: A reference to the document containing programming code.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: documentRef
    owner: AnalysisProgrammingCodeTemplate
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: DocumentReference
    inlined: true
    inlined_as_list: true
  parameters:
    name: parameters
    description: Parameters whose values will be used to generate or execute the programming
      code for a specific analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: parameters
    owner: AnalysisProgrammingCodeTemplate
    domain_of:
    - AnalysisOutputProgrammingCode
    - AnalysisProgrammingCodeTemplate
    range: TemplateCodeParameter
    inlined: true
    inlined_as_list: true

```
</details>