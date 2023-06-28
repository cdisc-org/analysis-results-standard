# Class: ReferencedOperationRelationship


_A reference to a statistical operation whose results are used in the calculation of the result for this operation._





URI: [ars:ReferencedOperationRelationship](https://www.cdisc.org/ars/1-0/ReferencedOperationRelationship)


```mermaid
erDiagram
ReferencedOperationRelationship {
    string id  
    string description  
}
Analysis {
    string id  
    integer version  
    string description  
    string dataset  
    string variable  
    string name  
}
OperationResult {
    string rawValue  
    string formattedValue  
}
AnalysisOutputProgrammingCode {
    string context  
    string code  
}
ReferencedAnalysisOperation {

}
AnalysisMethod {
    string id  
    string label  
    string description  
    string name  
}
DataSubset {
    string id  
    string label  
    integer level  
    integer order  
}
OrderedGroupingFactor {
    integer order  
    boolean resultsByGroup  
}
AnalysisSet {
    string id  
    string label  
    integer level  
    integer order  
}
DocumentReference {

}
ExtensibleTerminologyTerm {
    string controlledTerm  
}
AnalysisCategory {
    string id  
    string label  
}
Operation {
    string id  
    string label  
    string resultPattern  
    string name  
}

ReferencedOperationRelationship ||--|| ExtensibleTerminologyTerm : "referencedOperationRole"
ReferencedOperationRelationship ||--|| Operation : "operationId"
ReferencedOperationRelationship ||--|o Analysis : "analysisId"
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
OperationResult ||--|| Operation : "operationId"
OperationResult ||--}o ResultGroup : "resultGroups"
AnalysisOutputProgrammingCode ||--|o DocumentReference : "documentRef"
AnalysisOutputProgrammingCode ||--}o AnalysisOutputCodeParameter : "parameters"
ReferencedAnalysisOperation ||--|| ReferencedOperationRelationship : "referencedOperationRelationshipId"
ReferencedAnalysisOperation ||--|| Analysis : "analysisId"
AnalysisMethod ||--}| Operation : "operations"
AnalysisMethod ||--}o DocumentReference : "documentRefs"
AnalysisMethod ||--|o AnalysisProgrammingCodeTemplate : "codeTemplate"
DataSubset ||--|o WhereClauseCondition : "condition"
DataSubset ||--|o CompoundSubsetExpression : "compoundExpression"
OrderedGroupingFactor ||--|o GroupingFactor : "groupingId"
AnalysisSet ||--|o WhereClauseCondition : "condition"
AnalysisSet ||--|o CompoundSetExpression : "compoundExpression"
DocumentReference ||--|| ReferenceDocument : "referenceDocumentId"
DocumentReference ||--}o PageRef : "pageRefs"
ExtensibleTerminologyTerm ||--|o SponsorTerm : "sponsorTermId"
AnalysisCategory ||--}o AnalysisCategorization : "subCategorizations"
Operation ||--}o ReferencedOperationRelationship : "referencedOperationRelationships"

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