# Slot: resultGroups


_The group values associated with the result._



URI: [ars:resultGroups](https://www.cdisc.org/ars/1-0/resultGroups)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OperationResult](OperationResult.md) | The result of an analysis method operation performed on a subdivision of subj... |  no  |







## Properties

* Range: [ResultGroup](ResultGroup.md)

* Multivalued: True





## Comments

* There should be a result group value for each grouping that is indicated as being associated with a separate result (resultsByGroup = True)

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: resultGroups
description: The group values associated with the result.
comments:
- There should be a result group value for each grouping that is indicated as being
  associated with a separate result (resultsByGroup = True)
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
multivalued: true
alias: resultGroups
domain_of:
- OperationResult
range: ResultGroup
inlined: true
inlined_as_list: true

```
</details>