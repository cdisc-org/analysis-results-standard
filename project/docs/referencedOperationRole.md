# Slot: referencedOperationRole

URI: [ars:referencedOperationRole](https://www.cdisc.org/ars/1-0/referencedOperationRole)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to an statistical operation whose results is used in the calculat... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: referencedOperationRole
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: referencedOperationRole
domain_of:
- ReferencedOperationRelationship
range: string
required: true
inlined: false
any_of:
- range: OperationRole
- range: SponsorTerm

```
</details>