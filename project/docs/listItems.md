# Slot: listItems


_Items in the list. Each item may include a reference to an analysis, a reference to an output, or a sub-list._



URI: [ars:listItems](https://www.cdisc.org/ars/1-0/listItems)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[NestedList](NestedList.md) | A list of items (analyses or outputs) that may be organized within sub-lists |  no  |







## Properties

* Range: [OrderedListItem](OrderedListItem.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: listItems
description: Items in the list. Each item may include a reference to an analysis,
  a reference to an output, or a sub-list.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: listItems
domain_of:
- NestedList
range: OrderedListItem
inlined: true
inlined_as_list: true

```
</details>