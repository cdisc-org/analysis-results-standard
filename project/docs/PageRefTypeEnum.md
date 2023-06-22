# Enum: PageRefTypeEnum




_Type of reference for page references._



URI: [PageRefTypeEnum](PageRefTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PhysicalRef | None | References are to page numbers |
| NamedDestination | None | References are to named destinations in the referenced document |




## Slots

| Name | Description |
| ---  | --- |
| [refType](refType.md) | The type of reference for page references |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: PageRefTypeEnum
description: Type of reference for page references.
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
