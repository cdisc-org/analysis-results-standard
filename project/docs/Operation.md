
# Class: Operation




URI: [https://www.cdisc.org/ars/1-0/Operation](https://www.cdisc.org/ars/1-0/Operation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedOperationRelationship],[ReferencedOperationRelationship]<referencedOperationRelationships%200..*-++[Operation&#124;id:string;label:string%20%3F;resultPattern:string%20%3F;name(i):string],[OperationResult]-%20operationId%201..1>[Operation],[ReferencedOperationRelationship]-%20operationId%201..1>[Operation],[AnalysisMethod]++-%20operations%201..*>[Operation],[NamedObject]^-[Operation],[OperationResult],[NamedObject],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedOperationRelationship],[ReferencedOperationRelationship]<referencedOperationRelationships%200..*-++[Operation&#124;id:string;label:string%20%3F;resultPattern:string%20%3F;name(i):string],[OperationResult]-%20operationId%201..1>[Operation],[ReferencedOperationRelationship]-%20operationId%201..1>[Operation],[AnalysisMethod]++-%20operations%201..*>[Operation],[NamedObject]^-[Operation],[OperationResult],[NamedObject],[AnalysisMethod])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[operationId](operationId.md)*  <sub>1..1</sub>  **[Operation](Operation.md)**
 *  **None** *[operations](operations.md)*  <sub>1..\*</sub>  **[Operation](Operation.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [referencedOperationRelationships](referencedOperationRelationships.md)  <sub>0..\*</sub>
     * Range: [ReferencedOperationRelationship](ReferencedOperationRelationship.md)
 * [resultPattern](resultPattern.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
