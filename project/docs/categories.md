# Slot: categories


_Implementer-defined categories of analyses/outputs, each of which may include one or more sub-categorization._



URI: [ars:categories](https://www.cdisc.org/ars/1-0/categories)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnalysisOutputCategorization](AnalysisOutputCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |  no  |







## Properties

* Range: [AnalysisOutputCategory](AnalysisOutputCategory.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: categories
description: Implementer-defined categories of analyses/outputs, each of which may
  include one or more sub-categorization.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: categories
domain_of:
- AnalysisOutputCategorization
range: AnalysisOutputCategory
required: true
inlined: true
inlined_as_list: true

```
</details>