# Enum: PageRefType




_Type of page for page references._



URI: [PageRefType](PageRefType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PhysicalRef | None | References are to page numbers |
| NamedDestination | None | References are to named destinations in the referenced document |




## Slots

| Name | Description |
| ---  | --- |
| [refType](refType.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: PageRefType
description: Type of page for page references.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  PhysicalRef:
    text: PhysicalRef
    description: References are to page numbers.
  NamedDestination:
    text: NamedDestination
    description: References are to named destinations in the referenced document.

```
</details>
