# Class: PageNameRef


_One or more pages in the reference document, referenced by named destination._





URI: [ars:PageNameRef](https://www.cdisc.org/ars/1-0/PageNameRef)



```mermaid
 classDiagram
    class PageNameRef
      PageRef <|-- PageNameRef
      
      PageNameRef : label
        
      PageNameRef : pages
        
          PageNameRef --|> PageNameList : pages
        
      PageNameRef : refType
        
          PageNameRef --|> PageRefType : refType
        
      
```





## Inheritance
* [PageRef](PageRef.md)
    * **PageNameRef**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [refType](refType.md) | 1..1 <br/> [PageRefType](PageRefType.md) |  | [PageRef](PageRef.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | Alternative label to provide a more specific and description to a page link | [PageRef](PageRef.md) |
| [pages](pages.md) | 0..1 <br/> [PageNameList](PageNameList.md) |  | [PageRef](PageRef.md) |









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
  pages:
    name: pages
    domain_of:
    - PageRef
    range: PageNameList

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
  pages:
    name: pages
    domain_of:
    - PageRef
    range: PageNameList
attributes:
  refType:
    name: refType
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: refType
    owner: PageNameRef
    domain_of:
    - PageRef
    range: PageRefType
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
    owner: PageNameRef
    domain_of:
    - PageRef
    range: PageNameList

```
</details>