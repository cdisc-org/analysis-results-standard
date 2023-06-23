# Slot: documentRefs


_References to external documents containing additional information._



URI: [ars:documentRefs](https://www.cdisc.org/ars/1-0/documentRefs)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  no  |







## Properties

* Range: [DocumentReference](DocumentReference.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: documentRefs
description: References to external documents containing additional information.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: documentRefs
domain_of:
- Analysis
- AnalysisMethod
- Output
range: DocumentReference
inlined: true
inlined_as_list: true

```
</details>