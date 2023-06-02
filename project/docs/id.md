# Slot: id

URI: [ars:id](https://www.cdisc.org/ars/1-0id)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisCategorization](AnalysisCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |  no  |
[AnalysisCategory](AnalysisCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |  no  |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to an statistical operation whose results is used in the calculat... |  no  |
[Output](Output.md) |  |  no  |
[OutputDisplay](OutputDisplay.md) |  |  no  |
[DisplaySubSection](DisplaySubSection.md) |  |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[ReferenceDocument](ReferenceDocument.md) |  |  no  |
[SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |  no  |
[SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |  no  |
[DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
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
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
identifier: true
alias: id
domain_of:
- AnalysisCategorization
- AnalysisCategory
- Analysis
- AnalysisMethod
- Operation
- ReferencedOperationRelationship
- Output
- OutputDisplay
- DisplaySubSection
- AnalysisSet
- GroupingFactor
- Group
- DataSubset
- ReferenceDocument
- SponsorTerm
range: string
required: true

```
</details>