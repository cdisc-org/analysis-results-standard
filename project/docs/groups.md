# Slot: groups


_The pre-specified groups within the grouping._



URI: [ars:groups](https://www.cdisc.org/ars/1-0/groups)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |  no  |
[SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |  yes  |
[DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |  yes  |







## Properties

* Range: [Group](Group.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 'Male' and 'Female' might be groups within a sex grouping. |
| 'Treatment A', 'Treatment B', 'Placebo' might be groups within a treatment grouping. |

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: groups
description: The pre-specified groups within the grouping.
examples:
- value: '''Male'' and ''Female'' might be groups within a sex grouping.'
- value: '''Treatment A'', ''Treatment B'', ''Placebo'' might be groups within a treatment
    grouping.'
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
list_elements_ordered: true
alias: groups
domain_of:
- GroupingFactor
range: Group
inlined: true
inlined_as_list: true

```
</details>