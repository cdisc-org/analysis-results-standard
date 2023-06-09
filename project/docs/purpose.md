# Slot: purpose


_The purpose of the analysis within the body of evidence (e.g., section in the clinical study report)._



URI: [ars:purpose](https://www.cdisc.org/ars/1-0/purpose)



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
name: purpose
description: The purpose of the analysis within the body of evidence (e.g., section
  in the clinical study report).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: purpose
domain_of:
- Analysis
range: string
required: true
inlined: false
any_of:
- range: AnalysisPurpose
- range: SponsorTerm

```
</details>