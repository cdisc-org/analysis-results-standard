# Slot: dataDriven


_Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true)._



URI: [ars:dataDriven](https://www.cdisc.org/ars/1-0/dataDriven)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: dataDriven
description: Indicates whether the groups defined by the grouping are prespecified
  (false) or obtained from distinct data values of the groupingVariable (true).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: dataDriven
domain_of:
- GroupingFactor
range: boolean
required: true

```
</details>