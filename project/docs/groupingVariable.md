# Slot: groupingVariable


_For groupings based on a single variable, a reference to the dataset variable upon which grouping is based._



URI: [ars:groupingVariable](https://www.cdisc.org/ars/1-0/groupingVariable)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |  no  |
[DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: groupingVariable
description: For groupings based on a single variable, a reference to the dataset
  variable upon which grouping is based.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: groupingVariable
domain_of:
- GroupingFactor
range: string

```
</details>