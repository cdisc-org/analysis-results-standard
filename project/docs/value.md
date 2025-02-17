# Slot: value


_The prespecified value or values._



URI: [ars:value](https://www.cdisc.org/ars/1-0/value)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] |  yes  |
[TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |  yes  |
[AnalysisOutputCodeParameter](AnalysisOutputCodeParameter.md) | A parameter whose value is used in programming code for a specific analysis o... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: value
description: The prespecified value or values.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: value
domain_of:
- WhereClauseCondition
- TemplateCodeParameter
- AnalysisOutputCodeParameter
range: string

```
</details>