# Class: DocumentReference

_A reference to an external document._




URI: [ars:DocumentReference](https://www.cdisc.org/ars/1-0/DocumentReference)




```mermaid
 classDiagram
    class DocumentReference
      DocumentReference : pageRefs
        DocumentReference --|> PageRef : pageRefs
        DocumentReference : referenceDocumentId
        DocumentReference --|> ReferenceDocument : referenceDocumentId
        
```


<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [referenceDocumentId](referenceDocumentId.md) | 1..1 <br/> [ReferenceDocument](ReferenceDocument.md) | The identifier of the referenced document | direct |
| [pageRefs](pageRefs.md) | 0..* <br/> [PageRef](PageRef.md) | A list of references to specific parts of a document, which may be referenced... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisMethod](AnalysisMethod.md) | [documentRefs](documentRefs.md) | range | [DocumentReference](DocumentReference.md) |
| [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | [documentRef](documentRef.md) | range | [DocumentReference](DocumentReference.md) |
| [Analysis](Analysis.md) | [documentRefs](documentRefs.md) | range | [DocumentReference](DocumentReference.md) |
| [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | [documentRef](documentRef.md) | range | [DocumentReference](DocumentReference.md) |
| [Output](Output.md) | [documentRefs](documentRefs.md) | range | [DocumentReference](DocumentReference.md) |






## Comments

* One or more pageRefs may be specified to refer to specific part(s) of the document. Omit pageRefs to refer to the document as a whole.

## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:DocumentReference |
| native | ars:DocumentReference |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DocumentReference
description: A reference to an external document.
comments:
- One or more pageRefs may be specified to refer to specific part(s) of the document.
  Omit pageRefs to refer to the document as a whole.
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
name: DocumentReference
description: A reference to an external document.
comments:
- One or more pageRefs may be specified to refer to specific part(s) of the document.
  Omit pageRefs to refer to the document as a whole.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  referenceDocumentId:
    name: referenceDocumentId
    description: The identifier of the referenced document.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: referenceDocumentId
    owner: DocumentReference
    domain_of:
    - DocumentReference
    range: ReferenceDocument
    required: true
    inlined: false
  pageRefs:
    name: pageRefs
    description: A list of references to specific parts of a document, which may be
      referenced as a list of one or more page numbers, a range of page numbers, or
      a list of named destinations in the document (e.g. bookmarks).
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: pageRefs
    owner: DocumentReference
    domain_of:
    - DocumentReference
    range: PageRef
    inlined: true
    inlined_as_list: true
    any_of:
    - range: PageNumberListRef
    - range: PageNumberRangeRef
    - range: PageNameRef

```
</details>