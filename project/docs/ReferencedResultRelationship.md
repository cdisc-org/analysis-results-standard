
# Class: ReferencedResultRelationship




URI: [https://www.cdisc.org/ars/1-0/ReferencedResultRelationship](https://www.cdisc.org/ars/1-0/ReferencedResultRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Operation]<operationRef%201..1-%20[ReferencedResultRelationship&#124;referencedResultRole:OperationRole],[Operation]++-%20referencedResultRelationships%200..*>[ReferencedResultRelationship],[Operation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Operation]<operationRef%201..1-%20[ReferencedResultRelationship&#124;referencedResultRole:OperationRole],[Operation]++-%20referencedResultRelationships%200..*>[ReferencedResultRelationship],[Operation])

## Referenced by Class

 *  **None** *[referencedResultRelationships](referencedResultRelationships.md)*  <sub>0..\*</sub>  **[ReferencedResultRelationship](ReferencedResultRelationship.md)**

## Attributes


### Own

 * [referencedResultRole](referencedResultRole.md)  <sub>1..1</sub>
     * Range: [OperationRole](OperationRole.md)
 * [operationRef](operationRef.md)  <sub>1..1</sub>
     * Range: [Operation](Operation.md)
