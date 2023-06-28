# Class: NestedList


_A list of items (analyses or outputs) that may be organized within sub-lists._





URI: [ars:NestedList](https://www.cdisc.org/ars/1-0/NestedList)


```mermaid
erDiagram
NestedList {

}
OrderedListItem {
    integer level  
    integer order  
    string name  
}
Output {
    string id  
    integer version  
    string name  
}
Analysis {
    string id  
    integer version  
    string description  
    string dataset  
    string variable  
    string name  
}

NestedList ||--}o OrderedListItem : "listItems"
OrderedListItem ||--|o NestedList : "sublist"
OrderedListItem ||--|o Analysis : "analysisId"
OrderedListItem ||--|o Output : "outputId"
Output ||--}o OutputFile : "fileSpecifications"
Output ||--}o OrderedDisplay : "displays"
Output ||--}o AnalysisCategory : "categoryIds"
Output ||--}o DocumentReference : "documentRefs"
Output ||--|o AnalysisOutputProgrammingCode : "programmingCode"
Analysis ||--}o AnalysisCategory : "categoryIds"
Analysis ||--|| ExtensibleTerminologyTerm : "reason"
Analysis ||--|| ExtensibleTerminologyTerm : "purpose"
Analysis ||--}o DocumentReference : "documentRefs"
Analysis ||--|o AnalysisSet : "analysisSetId"
Analysis ||--}o OrderedGroupingFactor : "orderedGroupings"
Analysis ||--|o DataSubset : "dataSubsetId"
Analysis ||--|| AnalysisMethod : "methodId"
Analysis ||--}o ReferencedAnalysisOperation : "referencedAnalysisOperations"
Analysis ||--|o AnalysisOutputProgrammingCode : "programmingCode"
Analysis ||--}o OperationResult : "results"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [listItems](listItems.md) | 0..* <br/> [OrderedListItem](OrderedListItem.md) | Items in the list | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [listOfPlannedAnalyses](listOfPlannedAnalyses.md) | range | [NestedList](NestedList.md) |
| [ReportingEvent](ReportingEvent.md) | [listOfPlannedOutputs](listOfPlannedOutputs.md) | range | [NestedList](NestedList.md) |
| [OrderedListItem](OrderedListItem.md) | [sublist](sublist.md) | range | [NestedList](NestedList.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:NestedList |
| native | ars:NestedList |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NestedList
description: A list of items (analyses or outputs) that may be organized within sub-lists.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- listItems

```
</details>

### Induced

<details>
```yaml
name: NestedList
description: A list of items (analyses or outputs) that may be organized within sub-lists.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  listItems:
    name: listItems
    description: Items in the list. Each item may include a reference to an analysis,
      a reference to an output, or a sub-list.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: listItems
    owner: NestedList
    domain_of:
    - NestedList
    range: OrderedListItem
    inlined: true
    inlined_as_list: true

```
</details>