# Class: PageNumberListRef


_One or more individual pages in the reference document, referenced by page number._





URI: [ars:PageNumberListRef](https://www.cdisc.org/ars/1-0PageNumberListRef)



```mermaid
 classDiagram
    class PageNumberListRef
      PageRef <|-- PageNumberListRef
      
      PageNumberListRef : label
        
      PageNumberListRef : pages
        
          PageNumberListRef --|> PageNumberList : pages
        
      PageNumberListRef : refType
        
          PageNumberListRef --|> PageRefType : refType
        
      
```





## Inheritance
* [PageRef](PageRef.md)
    * **PageNumberListRef**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [refType](refType.md) | 1..1 <br/> [PageRefType](PageRefType.md) |  | [PageRef](PageRef.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) |  | [PageRef](PageRef.md) |
| [pages](pages.md) | 0..1 <br/> [PageNumberList](PageNumberList.md) |  | [PageRef](PageRef.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:PageNumberListRef |
| native | ars:PageNumberListRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PageNumberListRef
description: One or more individual pages in the reference document, referenced by
  page number.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: PhysicalRef
  pages:
    name: pages
    domain_of:
    - PageRef
    range: PageNumberList

```
</details>

### Induced

<details>
```yaml
name: PageNumberListRef
description: One or more individual pages in the reference document, referenced by
  page number.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: PageRef
slot_usage:
  refType:
    name: refType
    domain_of:
    - PageRef
    equals_string: PhysicalRef
  pages:
    name: pages
    domain_of:
    - PageRef
    range: PageNumberList
attributes:
  refType:
    name: refType
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: refType
    owner: PageNumberListRef
    domain_of:
    - PageRef
    range: PageRefType
    required: true
    equals_string: PhysicalRef
  label:
    name: label
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: PageNumberListRef
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
  pages:
    name: pages
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: pages
    owner: PageNumberListRef
    domain_of:
    - PageRef
    range: PageNumberList

```
</details>