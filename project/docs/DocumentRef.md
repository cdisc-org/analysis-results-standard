# Class: DocumentRef



URI: [ars:DocumentRef](https://www.cdisc.org/ars/1-0/DocumentRef)



```mermaid
 classDiagram
    class DocumentRef
      DocumentRef : pageRefs
        
          DocumentRef --|> PageRef : pageRefs
        
      DocumentRef : referenceDocumentId
        
          DocumentRef --|> ReferenceDocument : referenceDocumentId
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [referenceDocumentId](referenceDocumentId.md) | 1..1 <br/> [ReferenceDocument](ReferenceDocument.md) |  | direct |
| [pageRefs](pageRefs.md) | 0..* <br/> [PageRef](PageRef.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Analysis](Analysis.md) | [documentRefs](documentRefs.md) | range | [DocumentRef](DocumentRef.md) |
| [AnalysisMethod](AnalysisMethod.md) | [documentRefs](documentRefs.md) | range | [DocumentRef](DocumentRef.md) |
| [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | [documentRefs](documentRefs.md) | range | [DocumentRef](DocumentRef.md) |
| [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | [documentRefs](documentRefs.md) | range | [DocumentRef](DocumentRef.md) |
| [Output](Output.md) | [documentRefs](documentRefs.md) | range | [DocumentRef](DocumentRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:DocumentRef |
| native | ars:DocumentRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DocumentRef
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- referenceDocumentId
- pageRefs

```
</details>

### Induced

<details>
```yaml
name: DocumentRef
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  referenceDocumentId:
    name: referenceDocumentId
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: referenceDocumentId
    owner: DocumentRef
    domain_of:
    - DocumentRef
    range: ReferenceDocument
    required: true
    inlined: false
  pageRefs:
    name: pageRefs
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageRefs
    owner: DocumentRef
    domain_of:
    - DocumentRef
    range: PageRef

```
</details>