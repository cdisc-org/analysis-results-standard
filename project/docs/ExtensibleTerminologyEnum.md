# Enum: ExtensibleTerminologyEnum




_Extensible ARS enumerations._



URI: [ExtensibleTerminologyEnum](ExtensibleTerminologyEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| AnalysisReasonEnum | NCIT:C117744 | The rationale for performing this analysis |
| AnalysisPurposeEnum | NCIT:C117745 | The purpose of the analysis within the body of evidence (e |
| OperationRoleEnum | None | The role that the referenced operation's result plays in the calculation of t... |
| OutputFileTypeEnum | None | The file format of the file containing output from analyses |




## Slots

| Name | Description |
| ---  | --- |
| [enumeration](enumeration.md) | The name of the extensible enumeration |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: ExtensibleTerminologyEnum
description: Extensible ARS enumerations.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  AnalysisReasonEnum:
    text: AnalysisReasonEnum
    description: The rationale for performing this analysis. It indicates when the
      analysis was planned.
    meaning: NCIT:C117744
  AnalysisPurposeEnum:
    text: AnalysisPurposeEnum
    description: The purpose of the analysis within the body of evidence (e.g., section
      in the clinical study report).
    meaning: NCIT:C117745
  OperationRoleEnum:
    text: OperationRoleEnum
    description: The role that the referenced operation's result plays in the calculation
      of the result of this operation.
  OutputFileTypeEnum:
    text: OutputFileTypeEnum
    description: The file format of the file containing output from analyses.

```
</details>
