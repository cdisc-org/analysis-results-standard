# Slot: referencedOperationRelationships


_Relationships to other operations indicating how the result of the referenced operation are used in the calculation of the result for this operation._



URI: [ars:referencedOperationRelationships](https://www.cdisc.org/ars/1-0/referencedOperationRelationships)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |







## Properties

* Range: [ReferencedOperationRelationship](ReferencedOperationRelationship.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: referencedOperationRelationships
description: Relationships to other operations indicating how the result of the referenced
  operation are used in the calculation of the result for this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: referencedOperationRelationships
domain_of:
- Operation
range: ReferencedOperationRelationship
inlined: true
inlined_as_list: true

```
</details>