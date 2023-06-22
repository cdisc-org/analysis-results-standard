# Class: AnalysisReason


_The rationale for performing this analysis._





URI: [ars:AnalysisReason](https://www.cdisc.org/ars/1-0/AnalysisReason)



```mermaid
 classDiagram
    class AnalysisReason
      ExtensibleTerminologyTerm <|-- AnalysisReason
      
      AnalysisReason : controlledTerm
        
          AnalysisReason --|> AnalysisReasonEnum : controlledTerm
        
      AnalysisReason : sponsorTermId
        
          AnalysisReason --|> SponsorTerm : sponsorTermId
        
      
```





## Inheritance
* [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)
    * **AnalysisReason**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [controlledTerm](controlledTerm.md) | 1..1 <br/> [AnalysisReasonEnum](AnalysisReasonEnum.md) | One of the permissible values from the referenced enumeration | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [sponsorTermId](sponsorTermId.md) | 0..1 <br/> [SponsorTerm](SponsorTerm.md) | NOT USED | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisReason |
| native | ars:AnalysisReason |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisReason
description: The rationale for performing this analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisReasonEnum
    required: true
    value_presence: PRESENT
  sponsorTermId:
    name: sponsorTermId
    description: NOT USED
    domain_of:
    - ExtensibleTerminologyTerm
    value_presence: ABSENT

```
</details>

### Induced

<details>
```yaml
name: AnalysisReason
description: The rationale for performing this analysis.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisReasonEnum
    required: true
    value_presence: PRESENT
  sponsorTermId:
    name: sponsorTermId
    description: NOT USED
    domain_of:
    - ExtensibleTerminologyTerm
    value_presence: ABSENT
attributes:
  controlledTerm:
    name: controlledTerm
    description: One of the permissible values from the referenced enumeration.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: controlledTerm
    owner: AnalysisReason
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisReasonEnum
    required: true
    value_presence: PRESENT
  sponsorTermId:
    name: sponsorTermId
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sponsorTermId
    owner: AnalysisReason
    domain_of:
    - ExtensibleTerminologyTerm
    range: SponsorTerm
    inlined: false
    value_presence: ABSENT

```
</details>