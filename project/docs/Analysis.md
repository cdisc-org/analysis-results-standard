# Class: Analysis

_An analysis that is designed to meet a requirement of the reporting event. Each analysis is defined as a set of specifications, including:_
* _The analysis variable that is the subject of the analysis._
* _The analysis method (set of statistical operations) that is performed for the analysis variable._
* _The analysis set (subject population) for which the analysis is performed._
* _The subset of data records on which the analysis is performed (optional)._
* _One or more factors by which either subjects or data records are grouped for analysis (optional)._




URI: [ars:Analysis](https://www.cdisc.org/ars/1-0/Analysis)




```mermaid
 classDiagram
    class Analysis
      NamedObject <|-- Analysis

      Analysis : id
        Analysis : version
        Analysis : description
        Analysis : reason
        Analysis --|> ExtensibleTerminologyTerm : reason
        Analysis : purpose
        Analysis --|> ExtensibleTerminologyTerm : purpose
        Analysis : documentRefs
        Analysis --|> DocumentReference : documentRefs
        Analysis : categoryIds
        Analysis --|> AnalysisCategory : categoryIds
        Analysis : dataset
        Analysis : variable
        Analysis : analysisSetId
        Analysis --|> AnalysisSet : analysisSetId
        Analysis : dataSubsetId
        Analysis --|> DataSubset : dataSubsetId
        Analysis : orderedGroupings
        Analysis --|> OrderedGroupingFactor : orderedGroupings
        Analysis : methodId
        Analysis --|> AnalysisMethod : methodId
        Analysis : referencedAnalysisOperations
        Analysis --|> ReferencedAnalysisOperation : referencedAnalysisOperations
        Analysis : programmingCode
        Analysis --|> AnalysisOutputProgrammingCode : programmingCode
        Analysis : results
        Analysis --|> OperationResult : results
        Analysis : name
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **Analysis**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) | An ordinal indicating the version of the identified instance of the class | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | direct |
| [reason](reason.md) | 1..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The rationale for performing this analysis | direct |
| [purpose](purpose.md) | 1..1 <br/> [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The purpose of the analysis within the body of evidence (e | direct |
| [documentRefs](documentRefs.md) | 0..* <br/> [DocumentReference](DocumentReference.md) | References to external documents containing additional information | direct |
| [categoryIds](categoryIds.md) | 0..* <br/> [AnalysisCategory](AnalysisCategory.md) | References to any implementer-defined categories that apply to the analysis | direct |
| [dataset](dataset.md) | 0..1 <br/> [String](String.md) | The name of the analysis dataset | direct |
| [variable](variable.md) | 0..1 <br/> [String](String.md) | The name of the variable | direct |
| [analysisSetId](analysisSetId.md) | 0..1 <br/> [AnalysisSet](AnalysisSet.md) | The identifier of the referenced analysis set | direct |
| [dataSubsetId](dataSubsetId.md) | 0..1 <br/> [DataSubset](DataSubset.md) | The identifier of the referenced data subset | direct |
| [orderedGroupings](orderedGroupings.md) | 0..* <br/> [OrderedGroupingFactor](OrderedGroupingFactor.md) | An ordered list of grouping factors used in the analysis | direct |
| [methodId](methodId.md) | 1..1 <br/> [AnalysisMethod](AnalysisMethod.md) | A reference to the set of one or more statistical operations performed for th... | direct |
| [referencedAnalysisOperations](referencedAnalysisOperations.md) | 0..* <br/> [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | Indications of which analysis contains the results for each referenced operat... | direct |
| [programmingCode](programmingCode.md) | 0..1 <br/> [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform the ... | direct |
| [results](results.md) | 0..* <br/> [OperationResult](OperationResult.md) | The results of the analysis | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analyses](analyses.md) | range | [Analysis](Analysis.md) |
| [OrderedListItem](OrderedListItem.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | [analysisId](analysisId.md) | range | [Analysis](Analysis.md) |






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
  (optional).'
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- version
- description
- reason
- purpose
- documentRefs
- categoryIds
- dataset
- variable
- analysisSetId
- dataSubsetId
- orderedGroupings
- methodId
- referencedAnalysisOperations
- programmingCode
- results
slot_usage:
  categoryIds:
    name: categoryIds
    description: References to any implementer-defined categories that apply to the
      analysis.
    domain_of:
    - Analysis
    - Output
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
  (optional).'
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slot_usage:
  categoryIds:
    name: categoryIds
    description: References to any implementer-defined categories that apply to the
      analysis.
    domain_of:
    - Analysis
    - Output
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
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: Analysis
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
  version:
    name: version
    description: An ordinal indicating the version of the identified instance of the
      class.
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
  description:
    name: description
    description: A textual description of the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: Analysis
    domain_of:
    - SponsorTerm
    - AnalysisMethod
    - ReferencedOperationRelationship
    - CodeParameter
    - Analysis
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
    description: References to external documents containing additional information.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: documentRefs
    owner: Analysis
    domain_of:
    - AnalysisMethod
    - Analysis
    - Output
    range: DocumentReference
    inlined: true
    inlined_as_list: true
  categoryIds:
    name: categoryIds
    description: References to any implementer-defined categories that apply to the
      analysis.
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
  dataset:
    name: dataset
    description: The name of the analysis dataset.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: dataset
    owner: Analysis
    domain_of:
    - WhereClauseCondition
    - Analysis
    range: string
  variable:
    name: variable
    description: The name of the variable.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: variable
    owner: Analysis
    domain_of:
    - WhereClauseCondition
    - Analysis
    range: string
  analysisSetId:
    name: analysisSetId
    description: The identifier of the referenced analysis set.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: false
    alias: analysisSetId
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisSet
    inlined: false
  dataSubsetId:
    name: dataSubsetId
    description: The identifier of the referenced data subset.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: dataSubsetId
    owner: Analysis
    domain_of:
    - Analysis
    range: DataSubset
    inlined: false
  orderedGroupings:
    name: orderedGroupings
    description: An ordered list of grouping factors used in the analysis.
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
    description: Indications of which analysis contains the results for each referenced
      operation.
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
    description: The results of the analysis.
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
    description: The name for the instance of the class.
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