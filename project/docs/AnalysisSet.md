# Class: AnalysisSet


_A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set based upon the intent-to-treat principle. [ICH E9]_





URI: [ars:AnalysisSet](https://www.cdisc.org/ars/1-0AnalysisSet)



```mermaid
 classDiagram
    class AnalysisSet
      WhereClause <|-- AnalysisSet
      
      AnalysisSet : compoundExpression
        
          AnalysisSet --|> CompoundSetExpression : compoundExpression
        
      AnalysisSet : condition
        
          AnalysisSet --|> WhereClauseCondition : condition
        
      AnalysisSet : id
        
      AnalysisSet : label
        
      AnalysisSet : level
        
      AnalysisSet : order
        
      
```





## Inheritance
* [WhereClause](WhereClause.md)
    * **AnalysisSet**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) |  | direct |
| [level](level.md) | 0..1 <br/> [Integer](Integer.md) |  | [WhereClause](WhereClause.md) |
| [order](order.md) | 0..1 <br/> [Integer](Integer.md) |  | [WhereClause](WhereClause.md) |
| [condition](condition.md) | 0..1 <br/> [WhereClauseCondition](WhereClauseCondition.md) |  | [WhereClause](WhereClause.md) |
| [compoundExpression](compoundExpression.md) | 0..1 <br/> [CompoundSetExpression](CompoundSetExpression.md) |  | [WhereClause](WhereClause.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analysisSets](analysisSets.md) | range | [AnalysisSet](AnalysisSet.md) |
| [Analysis](Analysis.md) | [analysisSetId](analysisSetId.md) | range | [AnalysisSet](AnalysisSet.md) |
| [CompoundSetExpression](CompoundSetExpression.md) | [whereClauses](whereClauses.md) | range | [AnalysisSet](AnalysisSet.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisSet |
| native | ars:AnalysisSet |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisSet
description: 'A set of subjects whose data are to be included in the main analyses.
  This should be defined in the statistical section of the protocol. NOTE: There are
  a number of potential analysis sets, including, for example, the set based upon
  the intent-to-treat principle. [ICH E9]'
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
    range: CompoundSetExpression

```
</details>

### Induced

<details>
```yaml
name: AnalysisSet
description: 'A set of subjects whose data are to be included in the main analyses.
  This should be defined in the statistical section of the protocol. NOTE: There are
  a number of potential analysis sets, including, for example, the set based upon
  the intent-to-treat principle. [ICH E9]'
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: WhereClause
slot_usage:
  compoundExpression:
    name: compoundExpression
    domain_of:
    - WhereClause
    range: CompoundSetExpression
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: AnalysisSet
    domain_of:
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
    - SponsorTerm
    range: string
    required: true
  label:
    name: label
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: AnalysisSet
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
    owner: AnalysisSet
    domain_of:
    - OrderedListItem
    - WhereClause
    range: integer
  order:
    name: order
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: AnalysisSet
    domain_of:
    - OrderedListItem
    - OrderedGroupingFactor
    - OrderedDisplay
    - DisplaySubSection
    - WhereClause
    range: integer
  condition:
    name: condition
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: condition
    owner: AnalysisSet
    domain_of:
    - WhereClause
    range: WhereClauseCondition
  compoundExpression:
    name: compoundExpression
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: compoundExpression
    owner: AnalysisSet
    domain_of:
    - WhereClause
    range: CompoundSetExpression

```
</details>