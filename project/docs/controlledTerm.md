# Slot: controlledTerm

URI: [ars:controlledTerm](https://www.cdisc.org/ars/1-0/controlledTerm)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |  |  no  |
[AnalysisReason](AnalysisReason.md) |  |  yes  |
[SponsorAnalysisReason](SponsorAnalysisReason.md) |  |  yes  |
[AnalysisPurpose](AnalysisPurpose.md) |  |  yes  |
[SponsorAnalysisPurpose](SponsorAnalysisPurpose.md) |  |  yes  |
[OperationRole](OperationRole.md) |  |  yes  |
[SponsorOperationRole](SponsorOperationRole.md) |  |  yes  |
[OutputFileType](OutputFileType.md) |  |  yes  |
[SponsorOutputFileType](SponsorOutputFileType.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: controlledTerm
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