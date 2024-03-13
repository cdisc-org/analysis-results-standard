# Class: AnalysisOutputCategory

_An implementer-defined category of analyses/outputs, which may include one or more sub-categorization._




URI: [ars:AnalysisOutputCategory](https://www.cdisc.org/ars/1-0/AnalysisOutputCategory)




```mermaid
 classDiagram
    class AnalysisOutputCategory
      AnalysisOutputCategory : id
        AnalysisOutputCategory : label
        AnalysisOutputCategory : subCategorizations
        AnalysisOutputCategory --|> AnalysisOutputCategorization : subCategorizations
        
```


<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | direct |
| [subCategorizations](subCategorizations.md) | 0..* <br/> [AnalysisOutputCategorization](AnalysisOutputCategorization.md) | Sets of related implementer-defined sub-categories that can be used to catego... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisOutputCategorization](AnalysisOutputCategorization.md) | [categories](categories.md) | range | [AnalysisOutputCategory](AnalysisOutputCategory.md) |
| [Analysis](Analysis.md) | [categoryIds](categoryIds.md) | range | [AnalysisOutputCategory](AnalysisOutputCategory.md) |
| [Output](Output.md) | [categoryIds](categoryIds.md) | range | [AnalysisOutputCategory](AnalysisOutputCategory.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisOutputCategory |
| native | ars:AnalysisOutputCategory |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisOutputCategory
description: An implementer-defined category of analyses/outputs, which may include
  one or more sub-categorization.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- label
- subCategorizations

```
</details>

### Induced

<details>
```yaml
name: AnalysisOutputCategory
description: An implementer-defined category of analyses/outputs, which may include
  one or more sub-categorization.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: AnalysisOutputCategory
    domain_of:
    - ReportingEvent
    - ReferenceDocument
    - TerminologyExtension
    - SponsorTerm
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - AnalysisMethod
    - Operation
    - ReferencedOperationRelationship
    - Analysis
    - DisplaySubSection
    - Output
    - OutputDisplay
    range: string
    required: true
  label:
    name: label
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: AnalysisOutputCategory
    domain_of:
    - NamedObject
    - AnalysisOutputCategorization
    - AnalysisOutputCategory
    - AnalysisSet
    - DataSubset
    - GroupingFactor
    - Group
    - PageRef
    range: string
  subCategorizations:
    name: subCategorizations
    description: Sets of related implementer-defined sub-categories that can be used
      to categorize analyses or outputs.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: subCategorizations
    owner: AnalysisOutputCategory
    domain_of:
    - AnalysisOutputCategory
    range: AnalysisOutputCategorization
    inlined: true
    inlined_as_list: true

```
</details>