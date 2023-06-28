# Class: AnalysisPurpose


_The purpose of the analysis within the body of evidence (e.g., section in the clinical study report)._





URI: [ars:AnalysisPurpose](https://www.cdisc.org/ars/1-0/AnalysisPurpose)


```mermaid
erDiagram
AnalysisPurpose {
    AnalysisPurposeEnum controlledTerm  
}
SponsorTerm {
    string id  
    string submissionValue  
    string description  
}

AnalysisPurpose ||--|o SponsorTerm : "sponsorTermId"

```




## Inheritance
* [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)
    * **AnalysisPurpose**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [controlledTerm](controlledTerm.md) | 1..1 <br/> [AnalysisPurposeEnum](AnalysisPurposeEnum.md) | One of the permissible values from the referenced enumeration | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [sponsorTermId](sponsorTermId.md) | 0..1 <br/> [SponsorTerm](SponsorTerm.md) | NOT USED | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisPurpose |
| native | ars:AnalysisPurpose |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisPurpose
description: The purpose of the analysis within the body of evidence (e.g., section
  in the clinical study report).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisPurposeEnum
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
name: AnalysisPurpose
description: The purpose of the analysis within the body of evidence (e.g., section
  in the clinical study report).
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisPurposeEnum
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
    owner: AnalysisPurpose
    domain_of:
    - ExtensibleTerminologyTerm
    range: AnalysisPurposeEnum
    required: true
    value_presence: PRESENT
  sponsorTermId:
    name: sponsorTermId
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sponsorTermId
    owner: AnalysisPurpose
    domain_of:
    - ExtensibleTerminologyTerm
    range: SponsorTerm
    inlined: false
    value_presence: ABSENT

```
</details>