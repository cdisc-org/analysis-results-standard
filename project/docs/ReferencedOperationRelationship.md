# Class: ReferencedOperationRelationship


_A reference to a statistical operation whose results are used in the calculation of the result for this operation._





URI: [ars:ReferencedOperationRelationship](https://www.cdisc.org/ars/1-0/ReferencedOperationRelationship)




```mermaid
 classDiagram
    class ReferencedOperationRelationship
      ReferencedOperationRelationship : analysisId
        
          ReferencedOperationRelationship --|> Analysis : analysisId
        
      ReferencedOperationRelationship : description
        
      ReferencedOperationRelationship : id
        
      ReferencedOperationRelationship : operationId
        
          ReferencedOperationRelationship --|> Operation : operationId
        
      ReferencedOperationRelationship : referencedOperationRole
        
          ReferencedOperationRelationship --|> ExtensibleTerminologyTerm : referencedOperationRole
        
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [referencedOperationRole](referencedOperationRole.md) | 1..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The role that the referenced operation's result plays in the calculation of t... | direct |
| [operationId](operationId.md) | 1..1 <br/> [Operation](Operation.md) | The identifier of the referenced operation | direct |
| [analysisId](analysisId.md) | 0..1 <br/> [Analysis](Analysis.md) | The identifier of the referenced analysis | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | [referencedOperationRelationshipId](referencedOperationRelationshipId.md) | range | [ReferencedOperationRelationship](ReferencedOperationRelationship.md) |
| [Operation](Operation.md) | [referencedOperationRelationships](referencedOperationRelationships.md) | range | [ReferencedOperationRelationship](ReferencedOperationRelationship.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ReferencedOperationRelationship |
| native | ars:ReferencedOperationRelationship |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferencedOperationRelationship
description: A reference to a statistical operation whose results are used in the
  calculation of the result for this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- referencedOperationRole
- operationId
- analysisId
- description

```
</details>

### Induced

<details>
```yaml
name: ReferencedOperationRelationship
description: A reference to a statistical operation whose results are used in the
  calculation of the result for this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: ReferencedOperationRelationship
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
  referencedOperationRole:
    name: referencedOperationRole
    description: The role that the referenced operation's result plays in the calculation
      of the result of the parent operation.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: referencedOperationRole
    owner: ReferencedOperationRelationship
    domain_of:
    - ReferencedOperationRelationship
    range: ExtensibleTerminologyTerm
    required: true
    any_of:
    - range: OperationRole
    - range: SponsorOperationRole
  operationId:
    name: operationId
    description: The identifier of the referenced operation.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: operationId
    owner: ReferencedOperationRelationship
    domain_of:
    - OperationResult
    - ReferencedOperationRelationship
    range: Operation
    required: true
    inlined: false
  analysisId:
    name: analysisId
    description: The identifier of the referenced analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: analysisId
    owner: ReferencedOperationRelationship
    domain_of:
    - OrderedListItem
    - ReferencedAnalysisOperation
    - ReferencedOperationRelationship
    range: Analysis
    inlined: false
  description:
    name: description
    description: A textual description of the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: ReferencedOperationRelationship
    domain_of:
    - Analysis
    - AnalysisMethod
    - ReferencedOperationRelationship
    - CodeParameter
    - SponsorTerm
    range: string

```
</details>