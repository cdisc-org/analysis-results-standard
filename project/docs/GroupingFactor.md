# Class: GroupingFactor

_A factor used to subdivide either the subject population or data records in an analysis dataset for analysis._




URI: [ars:GroupingFactor](https://www.cdisc.org/ars/1-0/GroupingFactor)




```mermaid
 classDiagram
    class GroupingFactor
      NamedObject <|-- GroupingFactor        
      GroupingFactor : id
        GroupingFactor : groupingDataset
        GroupingFactor : groupingVariable
        GroupingFactor : dataDriven
        GroupingFactor : groups
        GroupingFactor --|> Group : groups
        GroupingFactor : name
        GroupingFactor : description
        GroupingFactor : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **GroupingFactor**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [groupingDataset](groupingDataset.md) | 0..1 <br/> [String](String.md) | For groupings based on a single variable, a reference to the dataset containi... | direct |
| [groupingVariable](groupingVariable.md) | 0..1 <br/> [String](String.md) | For groupings based on a single variable, a reference to the dataset variable... | direct |
| [dataDriven](dataDriven.md) | 1..1 <br/> [Boolean](Boolean.md) | Indicates whether the groups defined by the grouping are prespecified (false)... | direct |
| [groups](groups.md) | 0..* <br/> [Group](Group.md) | The pre-specified groups within the grouping | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analysisGroupings](analysisGroupings.md) | range | [GroupingFactor](GroupingFactor.md) |
| [OrderedGroupingFactor](OrderedGroupingFactor.md) | [groupingId](groupingId.md) | range | [GroupingFactor](GroupingFactor.md) |
| [ResultGroup](ResultGroup.md) | [groupingId](groupingId.md) | range | [GroupingFactor](GroupingFactor.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:GroupingFactor |
| native | ars:GroupingFactor |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupingFactor
description: A factor used to subdivide either the subject population or data records
  in an analysis dataset for analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- groupingDataset
- groupingVariable
- dataDriven
- groups

```
</details>

### Induced

<details>
```yaml
name: GroupingFactor
description: A factor used to subdivide either the subject population or data records
  in an analysis dataset for analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: GroupingFactor
    domain_of:
    - ReportingEvent
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - AnalysisMethod
    - Operation
    - ReferencedOperationRelationship
    - Analysis
    - DisplaySubSection
    - Output
    - OutputDisplay
    range: string
    required: true
  groupingDataset:
    name: groupingDataset
    description: For groupings based on a single variable, a reference to the dataset
      containing the variable upon which grouping is based.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: groupingDataset
    owner: GroupingFactor
    domain_of:
    - GroupingFactor
    range: string
  groupingVariable:
    name: groupingVariable
    description: For groupings based on a single variable, a reference to the dataset
      variable upon which grouping is based.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: groupingVariable
    owner: GroupingFactor
    domain_of:
    - GroupingFactor
    range: string
  dataDriven:
    name: dataDriven
    description: Indicates whether the groups defined by the grouping are prespecified
      (false) or obtained from distinct data values of the groupingVariable (true).
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: dataDriven
    owner: GroupingFactor
    domain_of:
    - GroupingFactor
    range: boolean
    required: true
  groups:
    name: groups
    description: The pre-specified groups within the grouping.
    examples:
    - value: '''Male'' and ''Female'' might be groups within a sex grouping.'
    - value: '''Treatment A'', ''Treatment B'', ''Placebo'' might be groups within
        a treatment grouping.'
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: groups
    owner: GroupingFactor
    domain_of:
    - GroupingFactor
    range: Group
    inlined: true
    inlined_as_list: true
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: GroupingFactor
    domain_of:
    - NamedObject
    range: string
    required: true
  description:
    name: description
    description: A textual description of the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: GroupingFactor
    domain_of:
    - NamedObject
    - SponsorTerm
    - ReferencedOperationRelationship
    range: string
  label:
    name: label
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: GroupingFactor
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - PageRef
    range: string

```
</details>