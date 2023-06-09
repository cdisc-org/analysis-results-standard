# Slot: operationId

URI: [ars:operationId](https://www.cdisc.org/ars/1-0/operationId)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OperationResult](OperationResult.md) | The result of an analysis method operation performed on a subdivision of subj... |  no  |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to an statistical operation whose results is used in the calculat... |  no  |







## Properties

* Range: [Operation](Operation.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: operationId
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: operationId
domain_of:
- OperationResult
- ReferencedOperationRelationship
range: Operation
required: true
inlined: false

```
</details>