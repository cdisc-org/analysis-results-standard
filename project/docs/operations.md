# Slot: operations


_The calculations performed for the method. Each operation generates a statistical result._



URI: [ars:operations](https://www.cdisc.org/ars/1-0/operations)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |  no  |







## Properties

* Range: [Operation](Operation.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: operations
description: The calculations performed for the method. Each operation generates a
  statistical result.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: operations
domain_of:
- AnalysisMethod
range: Operation
required: true
inlined: true
inlined_as_list: true

```
</details>