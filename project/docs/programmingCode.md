# Slot: programmingCode


_Programming statements used to perform the specific analysis or create the specific output._



URI: [ars:programmingCode](https://www.cdisc.org/ars/1-0/programmingCode)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  yes  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  yes  |







## Properties

* Range: [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md)





## Comments

* Programming statements may be represented as code or as a reference to the program file.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: programmingCode
description: Programming statements used to perform the specific analysis or create
  the specific output.
comments:
- Programming statements may be represented as code or as a reference to the program
  file.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: programmingCode
domain_of:
- Analysis
- Output
range: AnalysisOutputProgrammingCode

```
</details>