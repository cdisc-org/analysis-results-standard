# Class: ExtensibleTerminologyTerm


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ars:ExtensibleTerminologyTerm](https://www.cdisc.org/ars/1-0/ExtensibleTerminologyTerm)



```mermaid
 classDiagram
    class ExtensibleTerminologyTerm
      ExtensibleTerminologyTerm <|-- AnalysisReason
      ExtensibleTerminologyTerm <|-- SponsorAnalysisReason
      ExtensibleTerminologyTerm <|-- AnalysisPurpose
      ExtensibleTerminologyTerm <|-- SponsorAnalysisPurpose
      ExtensibleTerminologyTerm <|-- OperationRole
      ExtensibleTerminologyTerm <|-- SponsorOperationRole
      ExtensibleTerminologyTerm <|-- OutputFileType
      ExtensibleTerminologyTerm <|-- SponsorOutputFileType
      
      ExtensibleTerminologyTerm : controlledTerm
        
      ExtensibleTerminologyTerm : sponsorTermId
        
          ExtensibleTerminologyTerm --|> SponsorTerm : sponsorTermId
        
      
```





## Inheritance
* **ExtensibleTerminologyTerm**
    * [AnalysisReason](AnalysisReason.md)
    * [SponsorAnalysisReason](SponsorAnalysisReason.md)
    * [AnalysisPurpose](AnalysisPurpose.md)
    * [SponsorAnalysisPurpose](SponsorAnalysisPurpose.md)
    * [OperationRole](OperationRole.md)
    * [SponsorOperationRole](SponsorOperationRole.md)
    * [OutputFileType](OutputFileType.md)
    * [SponsorOutputFileType](SponsorOutputFileType.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [controlledTerm](controlledTerm.md) | 0..1 <br/> [String](String.md) |  | direct |
| [sponsorTermId](sponsorTermId.md) | 0..1 <br/> [SponsorTerm](SponsorTerm.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Analysis](Analysis.md) | [reason](reason.md) | range | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [Analysis](Analysis.md) | [purpose](purpose.md) | range | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | [referencedOperationRole](referencedOperationRole.md) | range | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [OutputFile](OutputFile.md) | [fileType](fileType.md) | range | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:ExtensibleTerminologyTerm |
| native | ars:ExtensibleTerminologyTerm |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtensibleTerminologyTerm
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
slots:
- controlledTerm
- sponsorTermId

```
</details>

### Induced

<details>
```yaml
name: ExtensibleTerminologyTerm
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
abstract: true
attributes:
  controlledTerm:
    name: controlledTerm
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: controlledTerm
    owner: ExtensibleTerminologyTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: string
    any_of:
    - range: AnalysisReasonEnum
    - range: AnalysisPurposeEnum
    - range: OperationRoleEnum
    - range: OutputFileTypeEnum
  sponsorTermId:
    name: sponsorTermId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sponsorTermId
    owner: ExtensibleTerminologyTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: SponsorTerm
    inlined: false

```
</details>