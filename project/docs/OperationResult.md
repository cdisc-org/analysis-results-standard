
# Class: OperationResult




URI: [https://www.cdisc.org/ars/1-0/OperationResult](https://www.cdisc.org/ars/1-0/OperationResult)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResultGroup],[ResultGroup]<resultGroups%200..*-++[OperationResult&#124;rawValue:string%20%3F;formattedValue:string%20%3F],[Operation]<operationId%201..1-%20[OperationResult],[Analysis]++-%20results%200..*>[OperationResult],[Operation],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResultGroup],[ResultGroup]<resultGroups%200..*-++[OperationResult&#124;rawValue:string%20%3F;formattedValue:string%20%3F],[Operation]<operationId%201..1-%20[OperationResult],[Analysis]++-%20results%200..*>[OperationResult],[Operation],[Analysis])

## Referenced by Class

 *  **None** *[results](results.md)*  <sub>0..\*</sub>  **[OperationResult](OperationResult.md)**

## Attributes


### Own

 * [operationId](operationId.md)  <sub>1..1</sub>
     * Range: [Operation](Operation.md)
 * [resultGroups](resultGroups.md)  <sub>0..\*</sub>
     * Range: [ResultGroup](ResultGroup.md)
 * [rawValue](rawValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [formattedValue](formattedValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
