# Slot: listItems

URI: [ars:listItems](https://www.cdisc.org/ars/1-0listItems)



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