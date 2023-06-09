# Slot: resultsByGroup


_Indicates whether a result is expected for each group in the grouping._



URI: [ars:resultsByGroup](https://www.cdisc.org/ars/1-0/resultsByGroup)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: resultsByGroup
description: Indicates whether a result is expected for each group in the grouping.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: resultsByGroup
domain_of:
- OrderedGroupingFactor
range: boolean
required: true

```
</details>