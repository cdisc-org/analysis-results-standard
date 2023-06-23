# Slot: version


_An ordinal indicating the version of the identified instance of the class._



URI: [ars:version](https://www.cdisc.org/ars/1-0/version)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  no  |
[OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: version
description: An ordinal indicating the version of the identified instance of the class.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: version
domain_of:
- ReportingEvent
- Analysis
- Output
- OutputDisplay
range: integer

```
</details>