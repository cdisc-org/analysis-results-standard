# Slot: sponsorTermId


_The identifier of the referenced sponsor term._



URI: [ars:sponsorTermId](https://www.cdisc.org/ars/1-0/sponsorTermId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The term used for an attribute whose terminology is extensible |  no  |
[AnalysisReason](AnalysisReason.md) | The rationale for performing this analysis |  yes  |
[SponsorAnalysisReason](SponsorAnalysisReason.md) | The sponsor-defined rationale for performing this analysis |  yes  |
[AnalysisPurpose](AnalysisPurpose.md) | The purpose of the analysis within the body of evidence (e |  yes  |
[SponsorAnalysisPurpose](SponsorAnalysisPurpose.md) | The sponsor-defined purpose of the analysis within the body of evidence (e |  yes  |
[OperationRole](OperationRole.md) | The role that the referenced operation's result plays in the calculation of t... |  yes  |
[SponsorOperationRole](SponsorOperationRole.md) | The sponsor-defined role that the referenced operation's result plays in the ... |  yes  |
[OutputFileType](OutputFileType.md) | The file format of the file containing output from analyses |  yes  |
[SponsorOutputFileType](SponsorOutputFileType.md) | The sponsor-defined file format of the file containing output from analyses |  yes  |







## Properties

* Range: [SponsorTerm](SponsorTerm.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: sponsorTermId
description: The identifier of the referenced sponsor term.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: sponsorTermId
domain_of:
- ExtensibleTerminologyTerm
range: SponsorTerm
inlined: false

```
</details>