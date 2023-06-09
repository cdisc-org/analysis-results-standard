# Class: Output


_A report of results and their evaluation based on planned analyses performed during the course of a trial._





URI: [ars:Output](https://www.cdisc.org/ars/1-0/Output)



```mermaid
 classDiagram
    class Output
      NamedObject <|-- Output
      
      Output : categoryIds
        
          Output --|> AnalysisCategory : categoryIds
        
      Output : displays
        
          Output --|> OrderedDisplay : displays
        
      Output : documentRefs
        
          Output --|> DocumentRef : documentRefs
        
      Output : fileSpecifications
        
          Output --|> OutputFile : fileSpecifications
        
      Output : id
        
      Output : name
        
      Output : programmingCode
        
          Output --|> AnalysisOutputProgrammingCode : programmingCode
        
      Output : version
        
      
```





## Inheritance
* [NamedObject](NamedObject.md)
    * **Output**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) |  | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [fileSpecifications](fileSpecifications.md) | 0..* <br/> [OutputFile](OutputFile.md) |  | direct |
| [displays](displays.md) | 0..* <br/> [OrderedDisplay](OrderedDisplay.md) |  | direct |
| [categoryIds](categoryIds.md) | 0..* <br/> [AnalysisCategory](AnalysisCategory.md) |  | direct |
| [documentRefs](documentRefs.md) | 0..* <br/> [DocumentRef](DocumentRef.md) |  | direct |
| [programmingCode](programmingCode.md) | 0..1 <br/> [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform the ... | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) |  | [NamedObject](NamedObject.md) |





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
description: A report of results and their evaluation based on planned analyses performed
  during the course of a trial.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- version
- fileSpecifications
- displays
- categoryIds
- documentRefs
- programmingCode
slot_usage:
  categoryIds:
    name: categoryIds
    domain_of:
    - Analysis
    - Output
    required: false
    inlined: false
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific output.
    domain_of:
    - Analysis
    - Output

```
</details>

### Induced

<details>
```yaml
name: Output
description: A report of results and their evaluation based on planned analyses performed
  during the course of a trial.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slot_usage:
  categoryIds:
    name: categoryIds
    domain_of:
    - Analysis
    - Output
    required: false
    inlined: false
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific output.
    domain_of:
    - Analysis
    - Output
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
    range: OutputFile
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
  documentRefs:
    name: documentRefs
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: documentRefs
    owner: Output
    domain_of:
    - Analysis
    - AnalysisMethod
    - AnalysisOutputProgrammingCode
    - Output
    range: DocumentRef
    inlined: true
    inlined_as_list: true
  programmingCode:
    name: programmingCode
    description: Programming statements and/or a reference to the program used to
      perform the specific output.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: programmingCode
    owner: Output
    domain_of:
    - Analysis
    - Output
    range: AnalysisOutputProgrammingCode
  name:
    name: name
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: Output
    domain_of:
    - NamedObject
    range: string
    required: true

```
</details>