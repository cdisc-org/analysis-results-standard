# Class: AnalysisSet

_A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set based upon the intent-to-treat principle. [ICH E9]_




URI: [ars:AnalysisSet](https://www.cdisc.org/ars/1-0/AnalysisSet)




```mermaid
 classDiagram
    class AnalysisSet
      WhereClause <|-- AnalysisSet

      AnalysisSet : id
        AnalysisSet : label
        AnalysisSet : level
        AnalysisSet : order
        AnalysisSet : condition
        AnalysisSet --|> WhereClauseCondition : condition
        AnalysisSet : compoundExpression
        AnalysisSet --|> CompoundSetExpression : compoundExpression
        
```




## Inheritance
* [WhereClause](WhereClause.md)
    * **AnalysisSet**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | direct |
| [level](level.md) | 0..1 <br/> [Integer](Integer.md) | The level of the entry within a hierarchical structure | [WhereClause](WhereClause.md) |
| [order](order.md) | 0..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | [WhereClause](WhereClause.md) |
| [condition](condition.md) | 0..1 <br/> [WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] | [WhereClause](WhereClause.md) |
| [compoundExpression](compoundExpression.md) | 0..1 <br/> [CompoundSetExpression](CompoundSetExpression.md) | A compound expression that combines or negates where clauses | [WhereClause](WhereClause.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analysisSets](analysisSets.md) | range | [AnalysisSet](AnalysisSet.md) |
| [CompoundSetExpression](CompoundSetExpression.md) | [whereClauses](whereClauses.md) | range | [AnalysisSet](AnalysisSet.md) |
| [Analysis](Analysis.md) | [analysisSetId](analysisSetId.md) | range | [AnalysisSet](AnalysisSet.md) |






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
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: AnalysisSet
    domain_of:
    - ReportingEvent
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    - AnalysisCategorization
    - AnalysisCategory
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
  label:
    name: label
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: AnalysisSet
    domain_of:
    - AnalysisCategorization
    - AnalysisCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - AnalysisMethod
    - PageRef
    - Operation
    range: string
  level:
    name: level
    description: The level of the entry within a hierarchical structure.
    comments:
    - 1 is the top level.
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
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: AnalysisSet
    domain_of:
    - OrderedListItem
    - WhereClause
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    range: integer
  condition:
    name: condition
    description: A simple selection criterion exressed as [dataset].[variable] [comparator]
      [value(s)]
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: condition
    owner: AnalysisSet
    domain_of:
    - WhereClause
    range: WhereClauseCondition
  compoundExpression:
    name: compoundExpression
    description: A compound expression that combines or negates where clauses.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: compoundExpression
    owner: AnalysisSet
    domain_of:
    - WhereClause
    range: CompoundSetExpression

```
</details>