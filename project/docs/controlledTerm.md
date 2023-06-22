# Slot: controlledTerm


_One of the permissible values from the referenced enumeration._



URI: [ars:controlledTerm](https://www.cdisc.org/ars/1-0/controlledTerm)



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

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: controlledTerm
description: One of the permissible values from the referenced enumeration.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: controlledTerm
domain_of:
- ExtensibleTerminologyTerm
range: string
any_of:
- range: AnalysisReasonEnum
- range: AnalysisPurposeEnum
- range: OperationRoleEnum
- range: OutputFileTypeEnum

```
</details>