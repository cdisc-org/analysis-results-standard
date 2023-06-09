# Class: AnalysisOutputProgrammingCode


_Programming statements and/or a reference to the program used to perform a specific analysis or create a specific output._





URI: [ars:AnalysisOutputProgrammingCode](https://www.cdisc.org/ars/1-0/AnalysisOutputProgrammingCode)



```mermaid
 classDiagram
    class AnalysisOutputProgrammingCode
      AnalysisOutputProgrammingCode <|-- AnalysisProgrammingCodeTemplate
      
      AnalysisOutputProgrammingCode : code
        
      AnalysisOutputProgrammingCode : context
        
      AnalysisOutputProgrammingCode : documentRefs
        
          AnalysisOutputProgrammingCode --|> DocumentRef : documentRefs
        
      AnalysisOutputProgrammingCode : parameters
        
          AnalysisOutputProgrammingCode --|> CodeParameter : parameters
        
      
```





## Inheritance
* **AnalysisOutputProgrammingCode**
    * [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [context](context.md) | 1..1 <br/> [String](String.md) | The name and version of the computer language used for the actual programming... | direct |
| [code](code.md) | 0..1 <br/> [String](String.md) | Programming statements used to perform the specific analysis | direct |
| [documentRefs](documentRefs.md) | 0..* <br/> [DocumentRef](DocumentRef.md) |  | direct |
| [parameters](parameters.md) | 0..* <br/> [CodeParameter](CodeParameter.md) | Parameter values used to generate or execute the programming code | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Analysis](Analysis.md) | [programmingCode](programmingCode.md) | range | [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) |
| [Output](Output.md) | [programmingCode](programmingCode.md) | range | [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisOutputProgrammingCode |
| native | ars:AnalysisOutputProgrammingCode |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisOutputProgrammingCode
description: Programming statements and/or a reference to the program used to perform
  a specific analysis or create a specific output.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- context
- code
- documentRefs
- parameters
slot_usage:
  parameters:
    name: parameters
    description: Parameter values used to generate or execute the programming code.
    domain_of:
    - AnalysisOutputProgrammingCode
    range: CodeParameter

```
</details>

### Induced

<details>
```yaml
name: AnalysisOutputProgrammingCode
description: Programming statements and/or a reference to the program used to perform
  a specific analysis or create a specific output.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slot_usage:
  parameters:
    name: parameters
    description: Parameter values used to generate or execute the programming code.
    domain_of:
    - AnalysisOutputProgrammingCode
    range: CodeParameter
attributes:
  context:
    name: context
    description: The name and version of the computer language used for the actual
      programming statements provided.
    examples:
    - value: SAS Version 9.2
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: context
    owner: AnalysisOutputProgrammingCode
    domain_of:
    - AnalysisOutputProgrammingCode
    range: string
    required: true
  code:
    name: code
    description: Programming statements used to perform the specific analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: code
    owner: AnalysisOutputProgrammingCode
    domain_of:
    - AnalysisOutputProgrammingCode
    range: string
  documentRefs:
    name: documentRefs
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: documentRefs
    owner: AnalysisOutputProgrammingCode
    domain_of:
    - Analysis
    - AnalysisMethod
    - AnalysisOutputProgrammingCode
    - Output
    range: DocumentRef
    inlined: true
    inlined_as_list: true
  parameters:
    name: parameters
    description: Parameter values used to generate or execute the programming code.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: parameters
    owner: AnalysisOutputProgrammingCode
    domain_of:
    - AnalysisOutputProgrammingCode
    range: CodeParameter
    inlined: true
    inlined_as_list: true

```
</details>