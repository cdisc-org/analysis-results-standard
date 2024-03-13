# Class: AnalysisOutputCategorization

_A set of related implementer-defined categories that can be used to categorize analyses or outputs._




URI: [ars:AnalysisOutputCategorization](https://www.cdisc.org/ars/1-0/AnalysisOutputCategorization)




```mermaid
 classDiagram
    class AnalysisOutputCategorization
      AnalysisOutputCategorization : categories
        AnalysisOutputCategorization --|> AnalysisOutputCategory : categories
        AnalysisOutputCategorization : id
        AnalysisOutputCategorization : label
        
```


<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | direct |
| [categories](categories.md) | 1..* <br/> [AnalysisOutputCategory](AnalysisOutputCategory.md) | Implementer-defined categories of analyses/outputs, each of which may include... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReportingEvent](ReportingEvent.md) | [analysisOutputCategorizations](analysisOutputCategorizations.md) | range | [AnalysisOutputCategorization](AnalysisOutputCategorization.md) |
| [AnalysisOutputCategory](AnalysisOutputCategory.md) | [subCategorizations](subCategorizations.md) | range | [AnalysisOutputCategorization](AnalysisOutputCategorization.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:AnalysisOutputCategorization |
| native | ars:AnalysisOutputCategorization |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisOutputCategorization
description: A set of related implementer-defined categories that can be used to categorize
  analyses or outputs.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
slots:
- id
- label
- categories

```
</details>

### Induced

<details>
```yaml
name: AnalysisOutputCategorization
description: A set of related implementer-defined categories that can be used to categorize
  analyses or outputs.
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
    owner: AnalysisOutputCategorization
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
    owner: AnalysisOutputCategorization
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
  categories:
    name: categories
    description: Implementer-defined categories of analyses/outputs, each of which
      may include one or more sub-categorization.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: categories
    owner: AnalysisOutputCategorization
    domain_of:
    - AnalysisOutputCategorization
    range: AnalysisOutputCategory
    required: true
    inlined: true
    inlined_as_list: true

```
</details>