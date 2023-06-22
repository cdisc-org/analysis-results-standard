# Slot: pageNumbers


_One or more page numbers._



URI: [ars:pageNumbers](https://www.cdisc.org/ars/1-0/pageNumbers)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PageRef](PageRef.md) | A reference to a specific part of a document as indicated by a list of one or... |  no  |
[PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |  yes  |
[PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |  yes  |
[PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |  yes  |







## Properties

* Range: [Integer](Integer.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: pageNumbers
description: One or more page numbers.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: pageNumbers
domain_of:
- PageRef
range: integer

```
</details>