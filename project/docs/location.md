# Slot: location


_A path (relative or absolute) indicating the location of the file._



URI: [ars:location](https://www.cdisc.org/ars/1-0/location)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |  no  |
[OutputFile](OutputFile.md) | A file containing analysis output displays |  no  |







## Properties

* Range: [Uri](Uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: location
description: A path (relative or absolute) indicating the location of the file.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: location
domain_of:
- ReferenceDocument
- OutputFile
range: uri

```
</details>