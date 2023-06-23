# Slot: referenceDocuments


_External documents containing information referenced for the reporting event._



URI: [ars:referenceDocuments](https://www.cdisc.org/ars/1-0/referenceDocuments)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |  no  |







## Properties

* Range: [ReferenceDocument](ReferenceDocument.md)

* Multivalued: True





## Comments

* May include specification or report documents (e.g. the SAP or CSR) and program files.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: referenceDocuments
description: External documents containing information referenced for the reporting
  event.
comments:
- May include specification or report documents (e.g. the SAP or CSR) and program
  files.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: referenceDocuments
domain_of:
- ReportingEvent
range: ReferenceDocument
inlined: true
inlined_as_list: true

```
</details>