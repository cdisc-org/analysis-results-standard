# Class: PageNameRef

_One or more pages in the reference document, referenced by named destination._




URI: [ars:PageNameRef](https://www.cdisc.org/ars/1-0/PageNameRef)




```mermaid
 classDiagram
    class PageNameRef
      PageRef <|-- PageNameRef

      PageNameRef : refType
        PageNameRef --|> PageRefTypeEnum : refType
        PageNameRef : label
        PageNameRef : pageNames
        PageNameRef : pageNumbers
        PageNameRef : firstPage
        PageNameRef : lastPage
        
```




## Inheritance
* [PageRef](PageRef.md)
    * **PageNameRef**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [refType](refType.md) | 1..1 <br/> [PageRefTypeEnum](PageRefTypeEnum.md) | The type of reference for page references | [PageRef](PageRef.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | Alternative label to provide a more specific and description to a page link | [PageRef](PageRef.md) |
| [pageNames](pageNames.md) | 1..* <br/> [String](String.md) | One or more named document references which each correspond with a page | [PageRef](PageRef.md) |
| [pageNumbers](pageNumbers.md) | 0..* <br/> [Integer](Integer.md) | NOT USED | [PageRef](PageRef.md) |
| [firstPage](firstPage.md) | 0..1 <br/> [Integer](Integer.md) | NOT USED | [PageRef](PageRef.md) |
| [lastPage](lastPage.md) | 0..1 <br/> [Integer](Integer.md) | NOT USED | [PageRef](PageRef.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:PageNameRef |
| native | ars:PageNameRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PageNameRef
description: One or more pages in the reference document, referenced by named destination.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: NamedDestination
  pageNumbers:
    name: pageNumbers
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
  pageNames:
    name: pageNames
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
  firstPage:
    name: firstPage
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
  lastPage:
    name: lastPage
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
defining_slots:
- pageNames

```
</details>

### Induced

<details>
```yaml
name: PageNameRef
description: One or more pages in the reference document, referenced by named destination.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: NamedDestination
  pageNumbers:
    name: pageNumbers
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
  pageNames:
    name: pageNames
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
  firstPage:
    name: firstPage
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
  lastPage:
    name: lastPage
    description: NOT USED
    domain_of:
    - PageRef
    value_presence: ABSENT
attributes:
  refType:
    name: refType
    description: The type of reference for page references.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: refType
    owner: PageNameRef
    domain_of:
    - PageRef
    range: PageRefTypeEnum
    required: true
    equals_string: NamedDestination
  label:
    name: label
    description: Alternative label to provide a more specific and description to a
      page link.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: PageNameRef
    domain_of:
    - AnalysisCategorization
    - AnalysisCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - AnalysisMethod
    - PageRef
    - Operation
    range: string
  pageNames:
    name: pageNames
    description: One or more named document references which each correspond with
      a page.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageNames
    owner: PageNameRef
    domain_of:
    - PageRef
    range: string
    required: true
    value_presence: PRESENT
  pageNumbers:
    name: pageNumbers
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageNumbers
    owner: PageNameRef
    domain_of:
    - PageRef
    range: integer
    value_presence: ABSENT
  firstPage:
    name: firstPage
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: firstPage
    owner: PageNameRef
    domain_of:
    - PageRef
    range: integer
    value_presence: ABSENT
  lastPage:
    name: lastPage
    description: NOT USED
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: lastPage
    owner: PageNameRef
    domain_of:
    - PageRef
    range: integer
    value_presence: ABSENT
defining_slots:
- pageNames

```
</details>