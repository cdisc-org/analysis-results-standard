# Class: Output



URI: [ars:Output](https://www.cdisc.org/ars/1-0Output)



```mermaid
 classDiagram
    class Output
      Output : categoryIds
        
          Output --|> AnalysisCategory : categoryIds
        
      Output : displays
        
          Output --|> OrderedDisplay : displays
        
      Output : fileSpecifications
        
          Output --|> File : fileSpecifications
        
      Output : id
        
      Output : version
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [fileSpecifications](fileSpecifications.md) | 0..* <br/> [File](File.md) |  | direct |
| [displays](displays.md) | 0..* <br/> [OrderedDisplay](OrderedDisplay.md) |  | direct |
| [categoryIds](categoryIds.md) | 0..* <br/> [AnalysisCategory](AnalysisCategory.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [outputs](outputs.md) | range | [Output](Output.md) |
| [OrderedListItem](OrderedListItem.md) | [outputId](outputId.md) | range | [Output](Output.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:Output |
| native | ars:Output |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Output
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- version
- fileSpecifications
- displays
- categoryIds
slot_usage:
  categoryIds:
    name: categoryIds
    domain_of:
    - Analysis
    - Output
    required: false
    inlined: false

```
</details>

### Induced

<details>
```yaml
name: Output
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slot_usage:
  categoryIds:
    name: categoryIds
    domain_of:
    - Analysis
    - Output
    required: false
    inlined: false
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: Output
    domain_of:
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
    - SponsorTerm
    range: string
    required: true
  version:
    name: version
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: version
    owner: Output
    domain_of:
    - Analysis
    - Output
    - OutputDisplay
    range: integer
  fileSpecifications:
    name: fileSpecifications
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: fileSpecifications
    owner: Output
    domain_of:
    - Output
    range: File
    inlined: true
    inlined_as_list: true
  displays:
    name: displays
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    list_elements_ordered: true
    alias: displays
    owner: Output
    domain_of:
    - Output
    range: OrderedDisplay
    inlined: true
    inlined_as_list: true
  categoryIds:
    name: categoryIds
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: categoryIds
    owner: Output
    domain_of:
    - Analysis
    - Output
    range: AnalysisCategory
    required: false
    inlined: false

```
</details>