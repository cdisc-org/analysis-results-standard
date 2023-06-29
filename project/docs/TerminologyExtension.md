# Class: TerminologyExtension


_An extensible set of controlled terminology that has been extended with at least one sponsor-defined term._





URI: [ars:TerminologyExtension](https://www.cdisc.org/ars/1-0/TerminologyExtension)




```mermaid
 classDiagram
    class TerminologyExtension
      TerminologyExtension : enumeration
        
          TerminologyExtension --|> ExtensibleTerminologyEnum : enumeration
        
      TerminologyExtension : id
        
      TerminologyExtension : sponsorTerms
        
          TerminologyExtension --|> SponsorTerm : sponsorTerms
        
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [enumeration](enumeration.md) | 0..1 <br/> [ExtensibleTerminologyEnum](ExtensibleTerminologyEnum.md) | The name of the extensible enumeration | direct |
| [sponsorTerms](sponsorTerms.md) | 1..* <br/> [SponsorTerm](SponsorTerm.md) | The sponsor-defined terms added to the extensible terminology | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [terminologyExtensions](terminologyExtensions.md) | range | [TerminologyExtension](TerminologyExtension.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:TerminologyExtension |
| native | ars:TerminologyExtension |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TerminologyExtension
description: An extensible set of controlled terminology that has been extended with
  at least one sponsor-defined term.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- enumeration
- sponsorTerms

```
</details>

### Induced

<details>
```yaml
name: TerminologyExtension
description: An extensible set of controlled terminology that has been extended with
  at least one sponsor-defined term.
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
    owner: TerminologyExtension
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
  enumeration:
    name: enumeration
    description: The name of the extensible enumeration.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: enumeration
    owner: TerminologyExtension
    domain_of:
    - TerminologyExtension
    range: ExtensibleTerminologyEnum
  sponsorTerms:
    name: sponsorTerms
    description: The sponsor-defined terms added to the extensible terminology.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: sponsorTerms
    owner: TerminologyExtension
    domain_of:
    - TerminologyExtension
    range: SponsorTerm
    required: true
    inlined: true
    inlined_as_list: true

```
</details>