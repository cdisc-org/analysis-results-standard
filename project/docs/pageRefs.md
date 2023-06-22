# Slot: pageRefs


_A list of references to specific parts of a document, which may be referenced as a list of one or more page numbers, a range of page numbers, or a list of named destinations in the document (e.g. bookmarks)._



URI: [ars:pageRefs](https://www.cdisc.org/ars/1-0/pageRefs)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DocumentReference](DocumentReference.md) | A reference to an external document |  no  |







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
description: A list of references to specific parts of a document, which may be referenced
  as a list of one or more page numbers, a range of page numbers, or a list of named
  destinations in the document (e.g. bookmarks).
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