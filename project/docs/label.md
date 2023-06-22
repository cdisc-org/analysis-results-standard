# Slot: label

URI: [ars:label](https://www.cdisc.org/ars/1-0/label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisCategorization](AnalysisCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |  no  |
[AnalysisCategory](AnalysisCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[PageRef](PageRef.md) | A reference to a specific part of a document as indicated by a list of one or... |  yes  |
[SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |  no  |
[DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |
[PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |  no  |
[PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |  no  |
[PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: label
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: label
domain_of:
- AnalysisCategorization
- AnalysisCategory
- AnalysisMethod
- Operation
- AnalysisSet
- GroupingFactor
- Group
- DataSubset
- PageRef
range: string

```
</details>