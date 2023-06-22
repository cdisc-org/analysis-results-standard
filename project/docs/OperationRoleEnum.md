# Enum: OperationRoleEnum




_The role that the referenced operation's result plays in the calculation of the result of this operation._



URI: [OperationRoleEnum](OperationRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NUMERATOR | None | The dividend of a fraction |
| DENOMINATOR | None | The divisor of a fraction |




## Slots

| Name | Description |
| ---  | --- |
| [controlledTerm](controlledTerm.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: OperationRoleEnum
description: The role that the referenced operation's result plays in the calculation
  of the result of this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  NUMERATOR:
    text: NUMERATOR
    description: The dividend of a fraction.
  DENOMINATOR:
    text: DENOMINATOR
    description: The divisor of a fraction.

```
</details>
