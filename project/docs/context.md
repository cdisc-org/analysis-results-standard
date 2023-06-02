# Slot: context


_The name and version of the computer language used for the actual programming statements provided._



URI: [ars:context](https://www.cdisc.org/ars/1-0context)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ProgrammingCodeTemplate](ProgrammingCodeTemplate.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| SAS Version 9.2 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: context
description: The name and version of the computer language used for the actual programming
  statements provided.
examples:
- value: SAS Version 9.2
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: context
domain_of:
- ProgrammingCodeTemplate
range: string
required: true

```
</details>