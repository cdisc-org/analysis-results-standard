# Class: Analysis


_An analysis that is designed to meet a requirement of the reporting event. Each analysis is defined as a set of specifications, including:_

_* The analysis variable that is the subject of the analysis._

_* The analysis method (set of statistical operations) that is performed for the analysis variable._

_* The analysis set (subject population) for which the analysis is performed._

_* The subset of data records on which the analysis is performed (optional)._

_* One or more factors by which either subjects or data records are grouped for analysis (optional)._

__





URI: [ars:Analysis](https://www.cdisc.org/ars/1-0/Analysis)



```mermaid
 classDiagram
    class Analysis
      NamedObject <|-- Analysis
      
      Analysis : analysisSetId
        
          Analysis --|> AnalysisSet : analysisSetId
        
      Analysis : categoryIds
        
          Analysis --|> AnalysisCategory : categoryIds
        
      Analysis : dataset
        
      Analysis : dataSubsetId
        
          Analysis --|> DataSubset : dataSubsetId
        
      Analysis : description
        
      Analysis : documentRefs
        
          Analysis --|> DocumentReference : documentRefs
        
      Analysis : id
        
      Analysis : methodId
        
          Analysis --|> AnalysisMethod : methodId
        
      Analysis : name
        
      Analysis : orderedGroupings
        
          Analysis --|> OrderedGroupingFactor : orderedGroupings
        
      Analysis : programmingCode
        
          Analysis --|> AnalysisOutputProgrammingCode : programmingCode
        
      Analysis : purpose
        
          Analysis --|> ExtensibleTerminologyTerm : purpose
        
      Analysis : reason
        
          Analysis --|> ExtensibleTerminologyTerm : reason
        
      Analysis : referencedAnalysisOperations
        
          Analysis --|> ReferencedAnalysisOperation : referencedAnalysisOperations
        
      Analysis : results
        
          Analysis --|> OperationResult : results
        
      Analysis : variable
        
      Analysis : version
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **Analysis**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [categoryIds](categoryIds.md) | 0..* <br/> [AnalysisCategory](AnalysisCategory.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [reason](reason.md) | 1..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The rationale for performing this analysis | direct |
| [purpose](purpose.md) | 1..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The purpose of the analysis within the body of evidence (e | direct |
| [documentRefs](documentRefs.md) | 0..* <br/> [DocumentReference](DocumentReference.md) |  | direct |
| [analysisSetId](analysisSetId.md) | 0..1 <br/> [AnalysisSet](AnalysisSet.md) |  | direct |
| [orderedGroupings](orderedGroupings.md) | 0..* <br/> [OrderedGroupingFactor](OrderedGroupingFactor.md) |  | direct |
| [dataSubsetId](dataSubsetId.md) | 0..1 <br/> [DataSubset](DataSubset.md) |  | direct |
| [dataset](dataset.md) | 0..1 <br/> [String](String.md) |  | direct |
| [variable](variable.md) | 0..1 <br/> [String](String.md) |  | direct |
| [methodId](methodId.md) | 1..1 <br/> [AnalysisMethod](AnalysisMethod.md) | A reference to the set of one or more statistical operations performed for th... | direct |
| [referencedAnalysisOperations](referencedAnalysisOperations.md) | 0..* <br/> [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) |  | direct |
| [programmingCode](programmingCode.md) | 0..1 <br/> [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform the ... | direct |
| [results](results.md) | 0..* <br/> [OperationResult](OperationResult.md) |  | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | [NamedObject](NamedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analyses](analyses.md) | range | [Analysis](Analysis.md) |
| [OrderedListItem](OrderedListItem.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:Analysis |
| native | ars:Analysis |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Analysis
description: 'An analysis that is designed to meet a requirement of the reporting
  event. Each analysis is defined as a set of specifications, including:

  * The analysis variable that is the subject of the analysis.

  * The analysis method (set of statistical operations) that is performed for the
  analysis variable.

  * The analysis set (subject population) for which the analysis is performed.

  * The subset of data records on which the analysis is performed (optional).

  * One or more factors by which either subjects or data records are grouped for analysis
  (optional).

  '
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- version
- categoryIds
- description
- reason
- purpose
- documentRefs
- analysisSetId
- orderedGroupings
- dataSubsetId
- dataset
- variable
- methodId
- referencedAnalysisOperations
- programmingCode
- results
slot_usage:
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific analysis.
    domain_of:
    - Analysis
    - Output

```
</details>

### Induced

<details>
```yaml
name: Analysis
description: 'An analysis that is designed to meet a requirement of the reporting
  event. Each analysis is defined as a set of specifications, including:

  * The analysis variable that is the subject of the analysis.

  * The analysis method (set of statistical operations) that is performed for the
  analysis variable.

  * The analysis set (subject population) for which the analysis is performed.

  * The subset of data records on which the analysis is performed (optional).

  * One or more factors by which either subjects or data records are grouped for analysis
  (optional).

  '
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slot_usage:
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific analysis.
    domain_of:
    - Analysis
    - Output
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: Analysis
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
  version:
    name: version
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: version
    owner: Analysis
    domain_of:
    - ReportingEvent
    - Analysis
    - Output
    - OutputDisplay
    range: integer
  categoryIds:
    name: categoryIds
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: categoryIds
    owner: Analysis
    domain_of:
    - Analysis
    - Output
    range: AnalysisCategory
    required: false
    inlined: false
  description:
    name: description
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: Analysis
    domain_of:
    - Analysis
    - AnalysisMethod
    - ReferencedOperationRelationship
    - CodeParameter
    - SponsorTerm
    range: string
  reason:
    name: reason
    description: The rationale for performing this analysis. It indicates when the
      analysis was planned.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: reason
    owner: Analysis
    domain_of:
    - Analysis
    range: ExtensibleTerminologyTerm
    required: true
    any_of:
    - range: AnalysisReason
    - range: SponsorAnalysisReason
  purpose:
    name: purpose
    description: The purpose of the analysis within the body of evidence (e.g., section
      in the clinical study report).
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: purpose
    owner: Analysis
    domain_of:
    - Analysis
    range: ExtensibleTerminologyTerm
    required: true
    any_of:
    - range: AnalysisPurpose
    - range: SponsorAnalysisPurpose
  documentRefs:
    name: documentRefs
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: documentRefs
    owner: Analysis
    domain_of:
    - Analysis
    - AnalysisMethod
    - Output
    range: DocumentReference
    inlined: true
    inlined_as_list: true
  analysisSetId:
    name: analysisSetId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: analysisSetId
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisSet
    inlined: false
  orderedGroupings:
    name: orderedGroupings
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: orderedGroupings
    owner: Analysis
    domain_of:
    - Analysis
    range: OrderedGroupingFactor
    inlined: true
    inlined_as_list: true
  dataSubsetId:
    name: dataSubsetId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: dataSubsetId
    owner: Analysis
    domain_of:
    - Analysis
    range: DataSubset
    inlined: false
  dataset:
    name: dataset
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: dataset
    owner: Analysis
    domain_of:
    - Analysis
    - WhereClauseCondition
    range: string
  variable:
    name: variable
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: variable
    owner: Analysis
    domain_of:
    - Analysis
    - WhereClauseCondition
    range: string
  methodId:
    name: methodId
    description: A reference to the set of one or more statistical operations performed
      for the analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: methodId
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisMethod
    required: true
    inlined: false
  referencedAnalysisOperations:
    name: referencedAnalysisOperations
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: referencedAnalysisOperations
    owner: Analysis
    domain_of:
    - Analysis
    range: ReferencedAnalysisOperation
    inlined: true
    inlined_as_list: true
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific analysis.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: programmingCode
    owner: Analysis
    domain_of:
    - Analysis
    - Output
    range: AnalysisOutputProgrammingCode
  results:
    name: results
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: results
    owner: Analysis
    domain_of:
    - Analysis
    range: OperationResult
    inlined: true
    inlined_as_list: true
  name:
    name: name
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: Analysis
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>