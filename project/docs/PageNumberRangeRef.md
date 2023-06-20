# Class: PageNumberRangeRef


_A range of pages in the reference document, indicated by the first and last page number in the range._





URI: [ars:PageNumberRangeRef](https://www.cdisc.org/ars/1-0/PageNumberRangeRef)



```mermaid
 classDiagram
    class PageNumberRangeRef
      PageRef <|-- PageNumberRangeRef
      
      PageNumberRangeRef : firstPage
        
      PageNumberRangeRef : label
        
      PageNumberRangeRef : lastPage
        
      PageNumberRangeRef : pageNames
        
      PageNumberRangeRef : pageNumbers
        
      PageNumberRangeRef : refType
        
          PageNumberRangeRef --|> PageRefTypeEnum : refType
        
      
```





## Inheritance
* [PageRef](PageRef.md)
    * **PageNumberRangeRef**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [refType](refType.md) | 1..1 <br/> [PageRefTypeEnum](PageRefTypeEnum.md) |  | [PageRef](PageRef.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | Alternative label to provide a more specific and description to a page link | [PageRef](PageRef.md) |
| [pageNames](pageNames.md) | 0..* <br/> [String](String.md) | One or more named document references which each correspond with a page | [PageRef](PageRef.md) |
| [pageNumbers](pageNumbers.md) | 0..* <br/> [Integer](Integer.md) | One or more page numbers | [PageRef](PageRef.md) |
| [firstPage](firstPage.md) | 1..1 <br/> [Integer](Integer.md) | The page number of the first page in a range of pages | [PageRef](PageRef.md) |
| [lastPage](lastPage.md) | 1..1 <br/> [Integer](Integer.md) | The page number of the last page in a range of pages | [PageRef](PageRef.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:PageNumberRangeRef |
| native | ars:PageNumberRangeRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PageNumberRangeRef
description: A range of pages in the reference document, indicated by the first and
  last page number in the range.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: PhysicalRef
  pageNumbers:
    name: pageNumbers
    domain_of:
    - PageRef
    value_presence: ABSENT
  pageNames:
    name: pageNames
    domain_of:
    - PageRef
    value_presence: ABSENT
  firstPage:
    name: firstPage
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
  lastPage:
    name: lastPage
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
defining_slots:
- firstPage
- lastPage

```
</details>

### Induced

<details>
```yaml
name: PageNumberRangeRef
description: A range of pages in the reference document, indicated by the first and
  last page number in the range.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: PhysicalRef
  pageNumbers:
    name: pageNumbers
    domain_of:
    - PageRef
    value_presence: ABSENT
  pageNames:
    name: pageNames
    domain_of:
    - PageRef
    value_presence: ABSENT
  firstPage:
    name: firstPage
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
  lastPage:
    name: lastPage
    domain_of:
    - PageRef
    required: true
    value_presence: PRESENT
attributes:
  refType:
    name: refType
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: refType
    owner: PageNumberRangeRef
    domain_of:
    - PageRef
    range: PageRefTypeEnum
    required: true
    equals_string: PhysicalRef
  label:
    name: label
    description: Alternative label to provide a more specific and description to a
      page link.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: PageNumberRangeRef
    domain_of:
    - AnalysisCategorization
    - AnalysisCategory
    - AnalysisMethod
    - Operation
    - AnalysisSet
    - GroupingFactor
    - Group
    - DataSubset
    - PageRef
    range: string
  pageNames:
    name: pageNames
    description: One or more named document references which each correspond with
      a page.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageNames
    owner: PageNumberRangeRef
    domain_of:
    - PageRef
    range: string
    value_presence: ABSENT
  pageNumbers:
    name: pageNumbers
    description: One or more page numbers.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageNumbers
    owner: PageNumberRangeRef
    domain_of:
    - PageRef
    range: integer
    value_presence: ABSENT
  firstPage:
    name: firstPage
    description: The page number of the first page in a range of pages.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: firstPage
    owner: PageNumberRangeRef
    domain_of:
    - PageRef
    range: integer
    required: true
    value_presence: PRESENT
  lastPage:
    name: lastPage
    description: The page number of the last page in a range of pages.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: lastPage
    owner: PageNumberRangeRef
    domain_of:
    - PageRef
    range: integer
    required: true
    value_presence: PRESENT
defining_slots:
- firstPage
- lastPage

```
</details>