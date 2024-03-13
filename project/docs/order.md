# Slot: order


_The ordinal of the instance with respect to other instances._



URI: [ars:order](https://www.cdisc.org/ars/1-0/order)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |  no  |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |
[OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |  no  |
[OrderedDisplay](OrderedDisplay.md) | A display ordered with respect to other displays in an analysis output |  no  |
[OrderedDisplaySubSection](OrderedDisplaySubSection.md) | A single subsection ordered with respect to other subsections in the same sec... |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |
[OrderedSubSection](OrderedSubSection.md) | A subsection ordered with respect to other subsections of the same type |  no  |
[OrderedSubSectionRef](OrderedSubSectionRef.md) | A reference to a subsection defined either globally or in another display sec... |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: order
description: The ordinal of the instance with respect to other instances.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: order
domain_of:
- OrderedListItem
- WhereClause
- Operation
- OrderedGroupingFactor
- OrderedDisplay
- OrderedDisplaySubSection
range: integer
required: true

```
</details>