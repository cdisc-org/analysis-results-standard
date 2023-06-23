# Slot: resultPattern


_The default pattern or format to apply to the result for display._



URI: [ars:resultPattern](https://www.cdisc.org/ars/1-0/resultPattern)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |  no  |







## Properties

* Range: [String](String.md)





## Comments

* May be a textual representation of a generic result to be displayed in a table shell (e.g. XX.X) or a machine readable formatting instruction.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: resultPattern
description: The default pattern or format to apply to the result for display.
comments:
- May be a textual representation of a generic result to be displayed in a table shell
  (e.g. XX.X) or a machine readable formatting instruction.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: resultPattern
domain_of:
- Operation
range: string

```
</details>