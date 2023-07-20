# Slot: documentRef


_A reference to the document containing programming code._



URI: [ars:documentRef](https://www.cdisc.org/ars/1-0/documentRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Programming statements and/or a reference to a used as a template for creatio... |  no  |
[AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform a sp... |  no  |







## Properties

* Range: [DocumentReference](DocumentReference.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: documentRef
description: A reference to the document containing programming code.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: false
alias: documentRef
domain_of:
- AnalysisProgrammingCodeTemplate
- AnalysisOutputProgrammingCode
range: DocumentReference
inlined: true
inlined_as_list: true

```
</details>