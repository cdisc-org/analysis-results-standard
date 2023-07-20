# Class: SponsorOperationRole

_The sponsor-defined role that the referenced operation's result plays in the calculation of the result of this operation._




URI: [ars:SponsorOperationRole](https://www.cdisc.org/ars/1-0/SponsorOperationRole)




```mermaid
 classDiagram
    class SponsorOperationRole
      ExtensibleTerminologyTerm <|-- SponsorOperationRole

      SponsorOperationRole : controlledTerm
        SponsorOperationRole : sponsorTermId
        SponsorOperationRole --|> SponsorTerm : sponsorTermId
        
```




## Inheritance
* [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)
    * **SponsorOperationRole**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [controlledTerm](controlledTerm.md) | 0..1 <br/> [String](String.md) | NOT USED | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |
| [sponsorTermId](sponsorTermId.md) | 1..1 <br/> [SponsorTerm](SponsorTerm.md) | A reference to a sponsor term in the TerminologyExtension with enumeration=Op... | [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:SponsorOperationRole |
| native | ars:SponsorOperationRole |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SponsorOperationRole
description: The sponsor-defined role that the referenced operation's result plays
  in the calculation of the result of this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    description: NOT USED
    domain_of:
    - ExtensibleTerminologyTerm
    value_presence: ABSENT
  sponsorTermId:
    name: sponsorTermId
    description: A reference to a sponsor term in the TerminologyExtension with enumeration=OperationRoleEnum
    domain_of:
    - ExtensibleTerminologyTerm
    required: true
    value_presence: PRESENT

```
</details>

### Induced

<details>
```yaml
name: SponsorOperationRole
description: The sponsor-defined role that the referenced operation's result plays
  in the calculation of the result of this operation.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: ExtensibleTerminologyTerm
slot_usage:
  controlledTerm:
    name: controlledTerm
    description: NOT USED
    domain_of:
    - ExtensibleTerminologyTerm
    value_presence: ABSENT
  sponsorTermId:
    name: sponsorTermId
    description: A reference to a sponsor term in the TerminologyExtension with enumeration=OperationRoleEnum
    domain_of:
    - ExtensibleTerminologyTerm
    required: true
    value_presence: PRESENT
attributes:
  controlledTerm:
    name: controlledTerm
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: controlledTerm
    owner: SponsorOperationRole
    domain_of:
    - ExtensibleTerminologyTerm
    range: string
    value_presence: ABSENT
  sponsorTermId:
    name: sponsorTermId
    description: A reference to a sponsor term in the TerminologyExtension with enumeration=OperationRoleEnum
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: sponsorTermId
    owner: SponsorOperationRole
    domain_of:
    - ExtensibleTerminologyTerm
    range: SponsorTerm
    required: true
    inlined: false
    value_presence: PRESENT

```
</details>