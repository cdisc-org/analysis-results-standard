# Slot: reason


_The rationale for performing this analysis. It indicates when the analysis was planned._



URI: [ars:reason](https://www.cdisc.org/ars/1-0reason)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: reason
description: The rationale for performing this analysis. It indicates when the analysis
  was planned.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: reason
domain_of:
- Analysis
range: string
required: true
inlined: false
any_of:
- range: AnalysisReason
- range: SponsorTerm

```
</details>