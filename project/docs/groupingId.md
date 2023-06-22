# Slot: groupingId


_The identifier of the referenced subject or data grouping factor._



URI: [ars:groupingId](https://www.cdisc.org/ars/1-0/groupingId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |  no  |
[ResultGroup](ResultGroup.md) | For the specified grouping factor, an indication of the specific group of sub... |  no  |







## Properties

* Range: [GroupingFactor](GroupingFactor.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: groupingId
description: The identifier of the referenced subject or data grouping factor.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: groupingId
domain_of:
- OrderedGroupingFactor
- ResultGroup
range: GroupingFactor
inlined: false

```
</details>