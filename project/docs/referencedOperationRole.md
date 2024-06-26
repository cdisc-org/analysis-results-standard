# Slot: referencedOperationRole


_The role that the referenced operation's result plays in the calculation of the result of the parent operation._



URI: [ars:referencedOperationRole](https://www.cdisc.org/ars/1-0/referencedOperationRole)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |  no  |







## Properties

* Range: [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: referencedOperationRole
description: The role that the referenced operation's result plays in the calculation
  of the result of the parent operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: referencedOperationRole
domain_of:
- ReferencedOperationRelationship
range: ExtensibleTerminologyTerm
required: true
any_of:
- range: OperationRole
- range: SponsorOperationRole

```
</details>