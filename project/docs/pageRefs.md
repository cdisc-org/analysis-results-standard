# Slot: pageRefs

URI: [ars:pageRefs](https://www.cdisc.org/ars/1-0/pageRefs)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DocumentReference](DocumentReference.md) |  |  no  |







## Properties

* Range: [PageRef](PageRef.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: pageRefs
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: pageRefs
domain_of:
- DocumentReference
range: PageRef
inlined: true
inlined_as_list: true
any_of:
- range: PageNumberListRef
- range: PageNumberRangeRef
- range: PageNameRef

```
</details>