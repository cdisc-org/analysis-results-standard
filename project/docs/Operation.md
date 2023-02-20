
# Class: Operation




URI: [https://www.cdisc.org/ars/1-0/Operation](https://www.cdisc.org/ars/1-0/Operation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedResultRelationship],[OperationResult],[OperationResult]<results%200..*-++[Operation&#124;id:string;label:string%20%3F;resultPattern:string%20%3F;name(i):string],[ReferencedResultRelationship]<referencedResultRelationships%200..*-++[Operation],[ReferencedResultRelationship]-%20operationRef%201..1>[Operation],[AnalysisMethod]++-%20operations%201..*>[Operation],[NamedObject]^-[Operation],[NamedObject],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedResultRelationship],[OperationResult],[OperationResult]<results%200..*-++[Operation&#124;id:string;label:string%20%3F;resultPattern:string%20%3F;name(i):string],[ReferencedResultRelationship]<referencedResultRelationships%200..*-++[Operation],[ReferencedResultRelationship]-%20operationRef%201..1>[Operation],[AnalysisMethod]++-%20operations%201..*>[Operation],[NamedObject]^-[Operation],[NamedObject],[AnalysisMethod])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[operationRef](operationRef.md)*  <sub>1..1</sub>  **[Operation](Operation.md)**
 *  **None** *[operations](operations.md)*  <sub>1..\*</sub>  **[Operation](Operation.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [referencedResultRelationships](referencedResultRelationships.md)  <sub>0..\*</sub>
     * Range: [ReferencedResultRelationship](ReferencedResultRelationship.md)
 * [resultPattern](resultPattern.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [results](results.md)  <sub>0..\*</sub>
     * Range: [OperationResult](OperationResult.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
