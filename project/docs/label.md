# Slot: label


_A short informative description that may be used for display._



URI: [ars:label](https://www.cdisc.org/ars/1-0/label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[NamedObject](NamedObject.md) | An object with a name |  no  |
[AnalysisOutputCategorization](AnalysisOutputCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |  no  |
[AnalysisOutputCategory](AnalysisOutputCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |  no  |
[PageRef](PageRef.md) | A reference to a specific part of a document as indicated by a list of one or... |  yes  |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |
[ListOfContents](ListOfContents.md) | A structured list of analyses and outputs included in the reporting event |  no  |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
[PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |  no  |
[PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |  no  |
[PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |  no  |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |
[CodeParameter](CodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |  no  |
[TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |  no  |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |
[AnalysisOutputCodeParameter](AnalysisOutputCodeParameter.md) | A parameter whose value is used in programming code for a specific analysis o... |  no  |
[Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |  no  |
[OutputFile](OutputFile.md) | A file containing analysis output displays |  no  |
[OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: label
description: A short informative description that may be used for display.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: label
domain_of:
- NamedObject
- AnalysisOutputCategorization
- AnalysisOutputCategory
- PageRef
range: string

```
</details>