# Slot: templateCode


_Template programming statements and/or a reference to the template program used to perform the specific analysis._



URI: [ars:templateCode](https://www.cdisc.org/ars/1-0templateCode)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ProgrammingCodeTemplate](ProgrammingCodeTemplate.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: templateCode
description: Template programming statements and/or a reference to the template program
  used to perform the specific analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: templateCode
domain_of:
- ProgrammingCodeTemplate
range: string
any_of:
- range: string
- range: DocumentRef

```
</details>