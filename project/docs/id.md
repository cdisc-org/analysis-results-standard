# Slot: id


_The assigned identifying value for the instance of the class._



URI: [ars:id](https://www.cdisc.org/ars/1-0/id)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |
[ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |  no  |
[TerminologyExtension](TerminologyExtension.md) | An extensible set of controlled terminology that has been extended with at le... |  no  |
[SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |  no  |
[AnalysisCategorization](AnalysisCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |  no  |
[AnalysisCategory](AnalysisCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |  no  |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[DisplaySubSection](DisplaySubSection.md) | An occurrence of a display section containing text |  no  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  no  |
[OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |  no  |
[SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: id
description: The assigned identifying value for the instance of the class.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
identifier: true
alias: id
domain_of:
- ReportingEvent
- ReferenceDocument
- TerminologyExtension
- SponsorTerm
- AnalysisCategorization
- AnalysisCategory
- AnalysisSet
- DataSubset
- GroupingFactor
- Group
- AnalysisMethod
- Operation
- ReferencedOperationRelationship
- Analysis
- DisplaySubSection
- Output
- OutputDisplay
range: string
required: true

```
</details>