# Class: Group


_A subdivision of the subject population or analysis dataset record set based on a defined factor._





URI: [ars:Group](https://www.cdisc.org/ars/1-0/Group)



```mermaid
 classDiagram
    class Group
      WhereClause <|-- Group
      

      Group <|-- AnalysisGroup
      Group <|-- DataGroup
      
      
      Group : compoundExpression
        
          Group --|> CompoundGroupExpression : compoundExpression
        
      Group : condition
        
          Group --|> WhereClauseCondition : condition
        
      Group : id
        
      Group : label
        
      Group : level
        
      Group : order
        
      
```





## Inheritance
* [WhereClause](WhereClause.md)
    * **Group**
        * [AnalysisGroup](AnalysisGroup.md)
        * [DataGroup](DataGroup.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) |  | direct |
| [level](level.md) | 0..1 <br/> [Integer](Integer.md) |  | [WhereClause](WhereClause.md) |
| [order](order.md) | 0..1 <br/> [Integer](Integer.md) |  | [WhereClause](WhereClause.md) |
| [condition](condition.md) | 0..1 <br/> [WhereClauseCondition](WhereClauseCondition.md) |  | [WhereClause](WhereClause.md) |
| [compoundExpression](compoundExpression.md) | 0..1 <br/> [CompoundGroupExpression](CompoundGroupExpression.md) |  | [WhereClause](WhereClause.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ResultGroup](ResultGroup.md) | [groupId](groupId.md) | range | [Group](Group.md) |
| [CompoundGroupExpression](CompoundGroupExpression.md) | [whereClauses](whereClauses.md) | range | [Group](Group.md) |
| [GroupingFactor](GroupingFactor.md) | [groups](groups.md) | range | [Group](Group.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:Group |
| native | ars:Group |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Group
description: A subdivision of the subject population or analysis dataset record set
  based on a defined factor.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClause
slots:
- id
- label
slot_usage:
  compoundExpression:
    name: compoundExpression
    domain_of:
    - WhereClause
    range: CompoundGroupExpression

```
</details>

### Induced

<details>
```yaml
name: Group
description: A subdivision of the subject population or analysis dataset record set
  based on a defined factor.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClause
slot_usage:
  compoundExpression:
    name: compoundExpression
    domain_of:
    - WhereClause
    range: CompoundGroupExpression
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: Group
    domain_of:
    - ReportingEvent
    - AnalysisCategorization
    - AnalysisCategory
    - Analysis
    - AnalysisMethod
    - Operation
    - ReferencedOperationRelationship
    - Output
    - OutputDisplay
    - DisplaySubSection
    - AnalysisSet
    - GroupingFactor
    - Group
    - DataSubset
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    range: string
    required: true
  label:
    name: label
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: Group
    domain_of:
    - AnalysisCategorization
    - AnalysisCategory
    - AnalysisMethod
    - Operation
    - AnalysisSet
    - GroupingFactor
    - Group
    - DataSubset
    - PageRef
    range: string
  level:
    name: level
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: level
    owner: Group
    domain_of:
    - OrderedListItem
    - WhereClause
    range: integer
  order:
    name: order
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: Group
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    range: integer
  condition:
    name: condition
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: condition
    owner: Group
    domain_of:
    - WhereClause
    range: WhereClauseCondition
  compoundExpression:
    name: compoundExpression
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: compoundExpression
    owner: Group
    domain_of:
    - WhereClause
    range: CompoundGroupExpression

```
</details>