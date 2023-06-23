# Enum: ConditionComparatorEnum




_Comparison operators indicating how the value of a variable is compared to a (list of) prespecified value(s)._



URI: [ConditionComparatorEnum](ConditionComparatorEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EQ | None | Is equal to |
| NE | None | Is not equal to |
| GT | None | Is greater than |
| GE | None | Is greater than or equal to |
| LT | None | Is less than |
| LE | None | Is less than or equal to |
| IN | None | Is in |
| NOTIN | None | Is not in |




## Slots

| Name | Description |
| ---  | --- |
| [comparator](comparator.md) | Comparison operator indicating how the variable is compared to the value(s) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: ConditionComparatorEnum
description: Comparison operators indicating how the value of a variable is compared
  to a (list of) prespecified value(s).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  EQ:
    text: EQ
    description: Is equal to
  NE:
    text: NE
    description: Is not equal to
  GT:
    text: GT
    description: Is greater than
  GE:
    text: GE
    description: Is greater than or equal to
  LT:
    text: LT
    description: Is less than
  LE:
    text: LE
    description: Is less than or equal to
  IN:
    text: IN
    description: Is in
  NOTIN:
    text: NOTIN
    description: Is not in

```
</details>
