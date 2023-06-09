# Slot: documentRefs

URI: [ars:documentRefs](https://www.cdisc.org/ars/1-0/documentRefs)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform a sp... |  no  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  no  |
[AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Programming statements and/or a reference to a used as a template for creatio... |  no  |







## Properties

* Range: [DocumentRef](DocumentRef.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: documentRefs
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: documentRefs
domain_of:
- Analysis
- AnalysisMethod
- AnalysisOutputProgrammingCode
- Output
range: DocumentRef
inlined: true
inlined_as_list: true

```
</details>