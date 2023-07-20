# Slot: analysisId


_The identifier of the referenced analysis._



URI: [ars:analysisId](https://www.cdisc.org/ars/1-0/analysisId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |  no  |
[ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | An indication of the analysis that contains results of a referenced operation |  yes  |







## Properties

* Range: [Analysis](Analysis.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: analysisId
description: The identifier of the referenced analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: false
alias: analysisId
domain_of:
- OrderedListItem
- ReferencedOperationRelationship
- ReferencedAnalysisOperation
range: Analysis
inlined: false

```
</details>