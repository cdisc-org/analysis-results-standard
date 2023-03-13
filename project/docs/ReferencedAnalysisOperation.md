
# Class: ReferencedAnalysisOperation




URI: [https://www.cdisc.org/ars/1-0/ReferencedAnalysisOperation](https://www.cdisc.org/ars/1-0/ReferencedAnalysisOperation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedOperationRelationship],[Analysis]<analysisId%201..1-%20[ReferencedAnalysisOperation],[ReferencedOperationRelationship]<referencedOperationId%200..1-%20[ReferencedAnalysisOperation],[Analysis]++-%20referencedAnalysisOperations%200..*>[ReferencedAnalysisOperation],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedOperationRelationship],[Analysis]<analysisId%201..1-%20[ReferencedAnalysisOperation],[ReferencedOperationRelationship]<referencedOperationId%200..1-%20[ReferencedAnalysisOperation],[Analysis]++-%20referencedAnalysisOperations%200..*>[ReferencedAnalysisOperation],[Analysis])

## Referenced by Class

 *  **None** *[referencedAnalysisOperations](referencedAnalysisOperations.md)*  <sub>0..\*</sub>  **[ReferencedAnalysisOperation](ReferencedAnalysisOperation.md)**

## Attributes


### Own

 * [referencedOperationId](referencedOperationId.md)  <sub>0..1</sub>
     * Range: [ReferencedOperationRelationship](ReferencedOperationRelationship.md)
 * [ReferencedAnalysisOperation➞analysisId](ReferencedAnalysisOperation_analysisId.md)  <sub>1..1</sub>
     * Range: [Analysis](Analysis.md)
