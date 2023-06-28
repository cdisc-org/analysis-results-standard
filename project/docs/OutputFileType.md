# Class: OutputFileType


_The file format of the file containing output from analyses._





URI: [ars:OutputFileType](https://www.cdisc.org/ars/1-0/OutputFileType)


```mermaid
erDiagram
OutputFileType {
    OutputFileTypeEnum controlledTerm  
}
SponsorTerm {
    string id  
    string submissionValue  
    string description  
}

OutputFileType ||--|o SponsorTerm : "sponsorTermId"

```




## Inheritance
* [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)
    * **OutputFileType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [controlledTerm](controlledTerm.md) | 1..1 <br/> [OutputFileTypeEnum](OutputFileTypeEnum.md) | One of the permissible values from the referenced enumeration | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [sponsorTermId](sponsorTermId.md) | 0..1 <br/> [SponsorTerm](SponsorTerm.md) | NOT USED | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:OutputFileType |
| native | ars:OutputFileType |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OutputFileType
description: The file format of the file containing output from analyses.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: OutputFileTypeEnum
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
name: OutputFileType
description: The file format of the file containing output from analyses.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    domain_of:
    - ExtensibleTerminologyTerm
    range: OutputFileTypeEnum
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
    owner: OutputFileType
    domain_of:
    - ExtensibleTerminologyTerm
    range: OutputFileTypeEnum
    required: true
    value_presence: PRESENT
  sponsorTermId:
    name: sponsorTermId
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sponsorTermId
    owner: OutputFileType
    domain_of:
    - ExtensibleTerminologyTerm
    range: SponsorTerm
    inlined: false
    value_presence: ABSENT

```
</details>