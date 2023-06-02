# Slot: order

URI: [ars:order](https://www.cdisc.org/ars/1-0order)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  yes  |
[OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |  yes  |
[OrderedDisplay](OrderedDisplay.md) |  |  yes  |
[DisplaySubSection](DisplaySubSection.md) |  |  yes  |
[WhereClause](WhereClause.md) |  |  no  |
[AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |  no  |
[Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |  no  |
[AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |  no  |
[DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |  no  |
[DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: order
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: order
domain_of:
- OrderedListItem
- OrderedGroupingFactor
- OrderedDisplay
- DisplaySubSection
- WhereClause
range: integer

```
</details>