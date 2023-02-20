
# Class: OperationResult




URI: [https://www.cdisc.org/ars/1-0/OperationResult](https://www.cdisc.org/ars/1-0/OperationResult)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisGroup]<groupRefs%200..*-%20[OperationResult&#124;rawValue:string%20%3F;formattedValue:string%20%3F],[Operation]++-%20results%200..*>[OperationResult],[Operation],[AnalysisGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisGroup]<groupRefs%200..*-%20[OperationResult&#124;rawValue:string%20%3F;formattedValue:string%20%3F],[Operation]++-%20results%200..*>[OperationResult],[Operation],[AnalysisGroup])

## Referenced by Class

 *  **None** *[results](results.md)*  <sub>0..\*</sub>  **[OperationResult](OperationResult.md)**

## Attributes


### Own

 * [groupRefs](groupRefs.md)  <sub>0..\*</sub>
     * Range: [AnalysisGroup](AnalysisGroup.md)
 * [rawValue](rawValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [formattedValue](formattedValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
