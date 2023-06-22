# Slot: orderedGroupings


_An ordered list of grouping factors used in the analysis._



URI: [ars:orderedGroupings](https://www.cdisc.org/ars/1-0/orderedGroupings)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |  no  |







## Properties

* Range: [OrderedGroupingFactor](OrderedGroupingFactor.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: orderedGroupings
description: An ordered list of grouping factors used in the analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: orderedGroupings
domain_of:
- Analysis
range: OrderedGroupingFactor
inlined: true
inlined_as_list: true

```
</details>