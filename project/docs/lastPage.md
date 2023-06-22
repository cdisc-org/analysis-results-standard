# Slot: lastPage


_The page number of the last page in a range of pages._



URI: [ars:lastPage](https://www.cdisc.org/ars/1-0/lastPage)



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





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: lastPage
description: The page number of the last page in a range of pages.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: lastPage
domain_of:
- PageRef
range: integer

```
</details>