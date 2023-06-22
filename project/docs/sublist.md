# Slot: sublist


_A sub-list of items (analyses or outputs) that may be further organized within sub-lists._



URI: [ars:sublist](https://www.cdisc.org/ars/1-0/sublist)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |  no  |







## Properties

* Range: [NestedList](NestedList.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: sublist
description: A sub-list of items (analyses or outputs) that may be further organized
  within sub-lists.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: false
alias: sublist
domain_of:
- OrderedListItem
range: NestedList
inlined: true

```
</details>