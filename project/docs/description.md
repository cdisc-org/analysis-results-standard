# Slot: description


_A textual description of the instance of the class._



URI: [ars:description](https://www.cdisc.org/ars/1-0/description)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |  no  |
[CodeParameter](CodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |  no  |
[SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |  no  |
[AnalysisOutputCodeParameter](AnalysisOutputCodeParameter.md) | A parameter whose value is used in programming code for a specific analysis o... |  no  |
[TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: description
description: A textual description of the instance of the class.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: description
domain_of:
- Analysis
- AnalysisMethod
- ReferencedOperationRelationship
- CodeParameter
- SponsorTerm
range: string

```
</details>