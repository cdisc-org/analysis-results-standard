# Slot: parameters


_Replacement parameters that are referenced in the programming code or programming code template and  are used to generate or execute the programming code._

__



URI: [ars:parameters](https://www.cdisc.org/ars/1-0/parameters)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform a sp... |  yes  |
[AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Programming statements and/or a reference to a used as a template for creatio... |  yes  |







## Properties

* Range: [CodeParameter](CodeParameter.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: parameters
description: 'Replacement parameters that are referenced in the programming code or
  programming code template and  are used to generate or execute the programming code.

  '
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: parameters
domain_of:
- AnalysisOutputProgrammingCode
range: CodeParameter
inlined: true
inlined_as_list: true

```
</details>