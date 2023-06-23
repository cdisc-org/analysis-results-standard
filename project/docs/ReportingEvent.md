# Class: ReportingEvent


_A set of analyses and outputs created to meet a specific reporting requirement, such as a CSR or interim analysis._





URI: [ars:ReportingEvent](https://www.cdisc.org/ars/1-0/ReportingEvent)



```mermaid
 classDiagram
    class ReportingEvent
      NamedObject <|-- ReportingEvent
      
      ReportingEvent : analyses
        
          ReportingEvent --|> Analysis : analyses
        
      ReportingEvent : analysisCategorizations
        
          ReportingEvent --|> AnalysisCategorization : analysisCategorizations
        
      ReportingEvent : analysisGroupings
        
          ReportingEvent --|> SubjectGroupingFactor : analysisGroupings
        
      ReportingEvent : analysisSets
        
          ReportingEvent --|> AnalysisSet : analysisSets
        
      ReportingEvent : dataGroupings
        
          ReportingEvent --|> DataGroupingFactor : dataGroupings
        
      ReportingEvent : dataSubsets
        
          ReportingEvent --|> DataSubset : dataSubsets
        
      ReportingEvent : globalDisplaySections
        
          ReportingEvent --|> GlobalDisplaySection : globalDisplaySections
        
      ReportingEvent : id
        
      ReportingEvent : listOfPlannedAnalyses
        
          ReportingEvent --|> NestedList : listOfPlannedAnalyses
        
      ReportingEvent : listOfPlannedOutputs
        
          ReportingEvent --|> NestedList : listOfPlannedOutputs
        
      ReportingEvent : methods
        
          ReportingEvent --|> AnalysisMethod : methods
        
      ReportingEvent : name
        
      ReportingEvent : outputs
        
          ReportingEvent --|> Output : outputs
        
      ReportingEvent : referenceDocuments
        
          ReportingEvent --|> ReferenceDocument : referenceDocuments
        
      ReportingEvent : terminologyExtensions
        
          ReportingEvent --|> TerminologyExtension : terminologyExtensions
        
      ReportingEvent : version
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **ReportingEvent**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) | An ordinal indicating the version of the identified instance of the class | direct |
| [listOfPlannedAnalyses](listOfPlannedAnalyses.md) | 1..1 <br/> [NestedList](NestedList.md) | A structured list of the analyses defined for the reporting event | direct |
| [listOfPlannedOutputs](listOfPlannedOutputs.md) | 0..1 <br/> [NestedList](NestedList.md) | An optional structured list of the outputs defined for the reporting event | direct |
| [analysisSets](analysisSets.md) | 0..* <br/> [AnalysisSet](AnalysisSet.md) | The analysis sets (subject populations) defined for the reporting event | direct |
| [analysisGroupings](analysisGroupings.md) | 0..* <br/> [SubjectGroupingFactor](SubjectGroupingFactor.md) | Characteristics used to subdivide the subject population (e | direct |
| [dataSubsets](dataSubsets.md) | 0..* <br/> [DataSubset](DataSubset.md) | Subsets of data identified by selection criteria for inclusion in analysis de... | direct |
| [dataGroupings](dataGroupings.md) | 0..* <br/> [DataGroupingFactor](DataGroupingFactor.md) | Characteristics used to subdivide data records in analysis datasets (e | direct |
| [globalDisplaySections](globalDisplaySections.md) | 0..* <br/> [GlobalDisplaySection](GlobalDisplaySection.md) | Display section specifications that may be applied to any display | direct |
| [analysisCategorizations](analysisCategorizations.md) | 0..* <br/> [AnalysisCategorization](AnalysisCategorization.md) | Sets of related implementer-defined categories that can be used to categorize... | direct |
| [analyses](analyses.md) | 0..* <br/> [Analysis](Analysis.md) | The analyses defined for the reporting event | direct |
| [methods](methods.md) | 0..* <br/> [AnalysisMethod](AnalysisMethod.md) | The defined methods used to analyze any analysis variable | direct |
| [outputs](outputs.md) | 0..* <br/> [Output](Output.md) | The outputs defined for the reporting event | direct |
| [referenceDocuments](referenceDocuments.md) | 0..* <br/> [ReferenceDocument](ReferenceDocument.md) | External documents containing information referenced for the reporting event | direct |
| [terminologyExtensions](terminologyExtensions.md) | 0..* <br/> [TerminologyExtension](TerminologyExtension.md) | Any sponsor-defined extensions to extensible terminology | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ReportingEvent |
| native | ars:ReportingEvent |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReportingEvent
description: A set of analyses and outputs created to meet a specific reporting requirement,
  such as a CSR or interim analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- version
- listOfPlannedAnalyses
- listOfPlannedOutputs
- analysisSets
- analysisGroupings
- dataSubsets
- dataGroupings
- globalDisplaySections
- analysisCategorizations
- analyses
- methods
- outputs
- referenceDocuments
- terminologyExtensions
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: ReportingEvent
description: A set of analyses and outputs created to meet a specific reporting requirement,
  such as a CSR or interim analysis.
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
    owner: ReportingEvent
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
    description: An ordinal indicating the version of the identified instance of the
      class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: version
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    - Analysis
    - Output
    - OutputDisplay
    range: integer
  listOfPlannedAnalyses:
    name: listOfPlannedAnalyses
    description: A structured list of the analyses defined for the reporting event.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: listOfPlannedAnalyses
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: NestedList
    required: true
  listOfPlannedOutputs:
    name: listOfPlannedOutputs
    description: An optional structured list of the outputs defined for the reporting
      event.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: listOfPlannedOutputs
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: NestedList
    required: false
  analysisSets:
    name: analysisSets
    description: The analysis sets (subject populations) defined for the reporting
      event.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: analysisSets
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: AnalysisSet
    inlined: true
    inlined_as_list: true
  analysisGroupings:
    name: analysisGroupings
    description: Characteristics used to subdivide the subject population (e.g., treatment,
      sex, age group).
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: analysisGroupings
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: SubjectGroupingFactor
    inlined: true
    inlined_as_list: true
  dataSubsets:
    name: dataSubsets
    description: Subsets of data identified by selection criteria for inclusion in
      analysis definitions.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: dataSubsets
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: DataSubset
    inlined: true
    inlined_as_list: true
  dataGroupings:
    name: dataGroupings
    description: Characteristics used to subdivide data records in analysis datasets
      (e.g., visit, system organ class).
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: dataGroupings
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: DataGroupingFactor
    inlined: true
    inlined_as_list: true
  globalDisplaySections:
    name: globalDisplaySections
    description: Display section specifications that may be applied to any display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: globalDisplaySections
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: GlobalDisplaySection
    inlined: true
    inlined_as_list: true
  analysisCategorizations:
    name: analysisCategorizations
    description: Sets of related implementer-defined categories that can be used to
      categorize analyses or outputs.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: analysisCategorizations
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: AnalysisCategorization
    inlined: true
    inlined_as_list: true
  analyses:
    name: analyses
    description: The analyses defined for the reporting event.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: analyses
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: Analysis
    inlined: true
    inlined_as_list: true
  methods:
    name: methods
    description: The defined methods used to analyze any analysis variable.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: methods
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: AnalysisMethod
    inlined: true
    inlined_as_list: true
  outputs:
    name: outputs
    description: The outputs defined for the reporting event.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: outputs
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: Output
    inlined: true
    inlined_as_list: true
  referenceDocuments:
    name: referenceDocuments
    description: External documents containing information referenced for the reporting
      event.
    comments:
    - May include specification or report documents (e.g. the SAP or CSR) and program
      files.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: referenceDocuments
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: ReferenceDocument
    inlined: true
    inlined_as_list: true
  terminologyExtensions:
    name: terminologyExtensions
    description: Any sponsor-defined extensions to extensible terminology.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: terminologyExtensions
    owner: ReportingEvent
    domain_of:
    - ReportingEvent
    range: TerminologyExtension
    inlined: true
    inlined_as_list: true
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: ReportingEvent
    domain_of:
    - NamedObject
    range: string
    required: true
tree_root: true

```
</details>