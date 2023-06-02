# Slot: analysisId

URI: [ars:analysisId](https://www.cdisc.org/ars/1-0analysisId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | An indication of the analysis that contains results of a referenced operation |  yes  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to an statistical operation whose results is used in the calculat... |  no  |







## Properties

* Range: [Analysis](Analysis.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: analysisId
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: false
alias: analysisId
domain_of:
- OrderedListItem
- ReferencedAnalysisOperation
- ReferencedOperationRelationship
range: Analysis
inlined: false

```
</details>