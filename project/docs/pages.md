# Slot: pages

URI: [ars:pages](https://www.cdisc.org/ars/1-0pages)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PageRef](PageRef.md) |  |  no  |
[PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |  yes  |
[PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |  yes  |
[PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: pages
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: pages
domain_of:
- PageRef
range: string
any_of:
- range: PageNumberList
- range: PageNameList
- range: PageRange

```
</details>