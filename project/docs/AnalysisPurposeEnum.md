# Enum: AnalysisPurposeEnum




_The purpose of the analysis within the body of evidence (e.g., section in the clinical study report)._



URI: [AnalysisPurposeEnum](AnalysisPurposeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PRIMARY OUTCOME MEASURE | NCIT:C98772 | The outcome measure(s) of greatest importance specified in the protocol, usua... |
| SECONDARY OUTCOME MEASURE | NCIT:C98781 | The outcome measure(s) that is part of a pre-specified analysis plan used to ... |
| EXPLORATORY OUTCOME MEASURE | NCIT:C98724 | The outcome measure(s) that is part of a pre-specified analysis plan used to ... |




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
name: AnalysisPurposeEnum
description: The purpose of the analysis within the body of evidence (e.g., section
  in the clinical study report).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
code_set: NCIT:C117745
permissible_values:
  PRIMARY OUTCOME MEASURE:
    text: PRIMARY OUTCOME MEASURE
    description: The outcome measure(s) of greatest importance specified in the protocol,
      usually the one(s) used in the power calculation, to evaluate the primary endpoint(s)
      associated with the primary study objective(s). (After Clinicaltrials.gov)
    meaning: NCIT:C98772
  SECONDARY OUTCOME MEASURE:
    text: SECONDARY OUTCOME MEASURE
    description: The outcome measure(s) that is part of a pre-specified analysis plan
      used to evaluate the secondary endpoint(s) associated with secondary study objective(s)
      and/or used to evaluate any measure(s) ancillary to the primary or secondary
      endpoint(s). (After Clinicaltrials.gov).
    meaning: NCIT:C98781
  EXPLORATORY OUTCOME MEASURE:
    text: EXPLORATORY OUTCOME MEASURE
    description: The outcome measure(s) that is part of a pre-specified analysis plan
      used to evaluate the exploratory endpoint(s) associated with exploratory study
      objective(s) and/or any other measures, excluding post-hoc measures, that are
      a focus of the study. (After clinicaltrials.gov)
    meaning: NCIT:C98724

```
</details>
