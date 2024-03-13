# Class: Operation

_A statistical operation that produces a single analysis result value as part of an analysis method._




URI: [ars:Operation](https://www.cdisc.org/ars/1-0/Operation)




```mermaid
 classDiagram
    class Operation
      NamedObject <|-- Operation

      Operation : id
        Operation : order
        Operation : referencedOperationRelationships
        Operation --|> ReferencedOperationRelationship : referencedOperationRelationships
        Operation : resultPattern
        Operation : name
        Operation : description
        Operation : label
        
```




## Inheritance
* [NamedObject](NamedObject.md)
    * **Operation**



## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | The assigned identifying value for the instance of the class | direct |
| [order](order.md) | 1..1 <br/> [Integer](Integer.md) | The ordinal of the instance with respect to other instances | direct |
| [referencedOperationRelationships](referencedOperationRelationships.md) | 0..* <br/> [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | Relationships to other operations indicating how the result of the referenced... | direct |
| [resultPattern](resultPattern.md) | 0..1 <br/> [String](String.md) | The default pattern or format to apply to the result for display | direct |
| [name](name.md) | 1..1 <br/> [String](String.md) | The name for the instance of the class | [NamedObject](NamedObject.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A textual description of the instance of the class | [NamedObject](NamedObject.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | A short informative description that may be used for display | [NamedObject](NamedObject.md) |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalysisMethod](AnalysisMethod.md) | [operations](operations.md) | range | [Operation](Operation.md) |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | [operationId](operationId.md) | range | [Operation](Operation.md) |
| [OperationResult](OperationResult.md) | [operationId](operationId.md) | range | [Operation](Operation.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ars:Operation |
| native | ars:Operation |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Operation
description: A statistical operation that produces a single analysis result value
  as part of an analysis method.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
slots:
- id
- order
- referencedOperationRelationships
- resultPattern

```
</details>

### Induced

<details>
```yaml
name: Operation
description: A statistical operation that produces a single analysis result value
  as part of an analysis method.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
is_a: NamedObject
attributes:
  id:
    name: id
    description: The assigned identifying value for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    identifier: true
    alias: id
    owner: Operation
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
  order:
    name: order
    description: The ordinal of the instance with respect to other instances.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: order
    owner: Operation
    domain_of:
    - OrderedListItem
    - WhereClause
    - Operation
    - OrderedGroupingFactor
    - OrderedDisplay
    - OrderedDisplaySubSection
    range: integer
    required: true
  referencedOperationRelationships:
    name: referencedOperationRelationships
    description: Relationships to other operations indicating how the result of the
      referenced operation are used in the calculation of the result for this operation.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    multivalued: true
    alias: referencedOperationRelationships
    owner: Operation
    domain_of:
    - Operation
    range: ReferencedOperationRelationship
    inlined: true
    inlined_as_list: true
  resultPattern:
    name: resultPattern
    description: The default pattern or format to apply to the result for display.
    comments:
    - May be a textual representation of a generic result to be displayed in a table
      shell (e.g. XX.X) or a machine readable formatting instruction.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: resultPattern
    owner: Operation
    domain_of:
    - Operation
    range: string
  name:
    name: name
    description: The name for the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: name
    owner: Operation
    domain_of:
    - NamedObject
    range: string
    required: true
  description:
    name: description
    description: A textual description of the instance of the class.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: description
    owner: Operation
    domain_of:
    - NamedObject
    - SponsorTerm
    - ReferencedOperationRelationship
    range: string
  label:
    name: label
    description: A short informative description that may be used for display.
    from_schema: https://www.cdisc.org/ars/1-0
    rank: 1000
    alias: label
    owner: Operation
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

```
</details>