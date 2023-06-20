# Enum: AnalysisReasonEnum




_The rationale for performing this analysis. It indicates when the analysis was planned._



URI: [AnalysisReasonEnum](AnalysisReasonEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SPECIFIED IN PROTOCOL | NCIT:C117752 | The analysis is specified in a protocol |
| SPECIFIED IN SAP | NCIT:C117753 | The analysis is specified in a statistical analysis plan |
| DATA DRIVEN | NCIT:C117750 | The analysis was triggered by findings in the data |
| REQUESTED BY REGULATORY AGENCY | NCIT:C117751 | The analysis has been requested by a regulatory agency |




## Slots

| Name | Description |
| ---  | --- |
| [controlledTerm](controlledTerm.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: AnalysisReasonEnum
description: The rationale for performing this analysis. It indicates when the analysis
  was planned.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
code_set: NCIT:C117744
permissible_values:
  SPECIFIED IN PROTOCOL:
    text: SPECIFIED IN PROTOCOL
    description: The analysis is specified in a protocol.
    meaning: NCIT:C117752
  SPECIFIED IN SAP:
    text: SPECIFIED IN SAP
    description: The analysis is specified in a statistical analysis plan.
    meaning: NCIT:C117753
  DATA DRIVEN:
    text: DATA DRIVEN
    description: The analysis was triggered by findings in the data.
    meaning: NCIT:C117750
  REQUESTED BY REGULATORY AGENCY:
    text: REQUESTED BY REGULATORY AGENCY
    description: The analysis has been requested by a regulatory agency.
    meaning: NCIT:C117751

```
</details>
