
# Class: ReferencedOperationRelationship




URI: [https://www.cdisc.org/ars/1-0/ReferencedOperationRelationship](https://www.cdisc.org/ars/1-0/ReferencedOperationRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Analysis]<analysisId%200..1-%20[ReferencedOperationRelationship&#124;id:string;referencedOperationRole:OperationRole;description:string%20%3F],[Operation]<operationId%201..1-%20[ReferencedOperationRelationship],[ReferencedAnalysisOperation]-%20referencedOperationId%200..1>[ReferencedOperationRelationship],[Operation]++-%20referencedOperationRelationships%200..*>[ReferencedOperationRelationship],[ReferencedAnalysisOperation],[Operation],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Analysis]<analysisId%200..1-%20[ReferencedOperationRelationship&#124;id:string;referencedOperationRole:OperationRole;description:string%20%3F],[Operation]<operationId%201..1-%20[ReferencedOperationRelationship],[ReferencedAnalysisOperation]-%20referencedOperationId%200..1>[ReferencedOperationRelationship],[Operation]++-%20referencedOperationRelationships%200..*>[ReferencedOperationRelationship],[ReferencedAnalysisOperation],[Operation],[Analysis])

## Referenced by Class

 *  **None** *[referencedOperationId](referencedOperationId.md)*  <sub>0..1</sub>  **[ReferencedOperationRelationship](ReferencedOperationRelationship.md)**
 *  **None** *[referencedOperationRelationships](referencedOperationRelationships.md)*  <sub>0..\*</sub>  **[ReferencedOperationRelationship](ReferencedOperationRelationship.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [referencedOperationRole](referencedOperationRole.md)  <sub>1..1</sub>
     * Range: [OperationRole](OperationRole.md)
 * [operationId](operationId.md)  <sub>1..1</sub>
     * Range: [Operation](Operation.md)
 * [analysisId](analysisId.md)  <sub>0..1</sub>
     * Range: [Analysis](Analysis.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
