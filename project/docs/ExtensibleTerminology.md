# Enum: ExtensibleTerminology




_Extensible ARS enumerations._



URI: [ExtensibleTerminology](ExtensibleTerminology)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| AnalysisReason | NCIT:C117744 | The rationale for performing this analysis |
| AnalysisPurpose | NCIT:C117745 | The purpose of the analysis within the body of evidence (e |
| OperationRole | None |  |
| OutputFileType | None |  |




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
name: ExtensibleTerminology
description: Extensible ARS enumerations.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  AnalysisReason:
    text: AnalysisReason
    description: The rationale for performing this analysis. It indicates when the
      analysis was planned.
    meaning: NCIT:C117744
  AnalysisPurpose:
    text: AnalysisPurpose
    description: The purpose of the analysis within the body of evidence (e.g., section
      in the clinical study report).
    meaning: NCIT:C117745
  OperationRole:
    text: OperationRole
  OutputFileType:
    text: OutputFileType

```
</details>
