# Class: AnalysisGroup


_A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A, subjects whose gender is male)._





URI: [ars:AnalysisGroup](https://www.cdisc.org/ars/1-0/AnalysisGroup)



```mermaid
 classDiagram
    class AnalysisGroup
      Group <|-- AnalysisGroup
      
      AnalysisGroup : compoundExpression
        
          AnalysisGroup --|> CompoundGroupExpression : compoundExpression
        
      AnalysisGroup : condition
        
          AnalysisGroup --|> WhereClauseCondition : condition
        
      AnalysisGroup : id
        
      AnalysisGroup : label
        
      AnalysisGroup : level
        
      AnalysisGroup : order
        
      
```





## Inheritance
* [WhereClause](WhereClause.md)
    * [Group](Group.md)
        * **AnalysisGroup**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | [Group](Group.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [Group](Group.md) |
| [level](level.md) | 0..1 <br/> [Integer](Integer.md) | The level of the entry within a hierarchical structure | [WhereClause](WhereClause.md) |
| [order](order.md) | 0..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [WhereClause](WhereClause.md) |
| [condition](condition.md) | 0..1 <br/> [WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] | [WhereClause](WhereClause.md) |
| [compoundExpression](compoundExpression.md) | 0..1 <br/> [CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression that combines or negates where clauses | [WhereClause](WhereClause.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SubjectGroupingFactor](SubjectGroupingFactor.md) | [groups](groups.md) | range | [AnalysisGroup](AnalysisGroup.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisGroup |
| native | ars:AnalysisGroup |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisGroup
description: A subdivision of the subject population based on a defined factor (e.g.,
  subjects whose treatment is Drug A, subjects whose gender is male).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: Group

```
</details>

### Induced

<details>
```yaml
name: AnalysisGroup
description: A subdivision of the subject population based on a defined factor (e.g.,
  subjects whose treatment is Drug A, subjects whose gender is male).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: Group
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: AnalysisGroup
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
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: AnalysisGroup
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
    description: The level of the entry within a hierarchical structure.
    comments:
    - 1 is the top level.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: level
    owner: AnalysisGroup
    domain_of:
    - OrderedListItem
    - WhereClause
    range: integer
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: AnalysisGroup
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    - WhereClause
    range: integer
  condition:
    name: condition
    description: A simple selection criterion exressed as [dataset].[variable] [comparator]
      [value(s)]
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: condition
    owner: AnalysisGroup
    domain_of:
    - WhereClause
    range: WhereClauseCondition
  compoundExpression:
    name: compoundExpression
    description: A compound expression that combines or negates where clauses.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: compoundExpression
    owner: AnalysisGroup
    domain_of:
    - WhereClause
    range: CompoundGroupExpression

```
</details>