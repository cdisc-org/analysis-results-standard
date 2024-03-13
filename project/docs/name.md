# Slot: name


_The name for the instance of the class._



URI: [ars:name](https://www.cdisc.org/ars/1-0/name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[NamedObject](NamedObject.md) | An object with a name |  no  |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |
[ListOfContents](ListOfContents.md) | A structured list of analyses and outputs included in the reporting event |  no  |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |  no  |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |
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

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: name
description: The name for the instance of the class.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: name
domain_of:
- NamedObject
range: string
required: true

```
</details>