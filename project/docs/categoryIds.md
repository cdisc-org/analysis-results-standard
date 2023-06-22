# Slot: categoryIds


_References to any implementer-defined categories that apply to the analysis or output._



URI: [ars:categoryIds](https://www.cdisc.org/ars/1-0/categoryIds)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  yes  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  yes  |







## Properties

* Range: [AnalysisCategory](AnalysisCategory.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: categoryIds
description: References to any implementer-defined categories that apply to the analysis
  or output.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: categoryIds
domain_of:
- Analysis
- Output
range: AnalysisCategory
required: false
inlined: false

```
</details>