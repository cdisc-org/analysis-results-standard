
# Class: ResultGroup




URI: [https://www.cdisc.org/ars/1-0/ResultGroup](https://www.cdisc.org/ars/1-0/ResultGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Group]<groupId%200..1-%20[ResultGroup&#124;groupValue:string%20%3F],[GroupingFactor]<groupingId%200..1-%20[ResultGroup],[OperationResult]++-%20resultGroups%200..*>[ResultGroup],[OperationResult],[GroupingFactor],[Group])](https://yuml.me/diagram/nofunky;dir:TB/class/[Group]<groupId%200..1-%20[ResultGroup&#124;groupValue:string%20%3F],[GroupingFactor]<groupingId%200..1-%20[ResultGroup],[OperationResult]++-%20resultGroups%200..*>[ResultGroup],[OperationResult],[GroupingFactor],[Group])

## Referenced by Class

 *  **None** *[resultGroups](resultGroups.md)*  <sub>0..\*</sub>  **[ResultGroup](ResultGroup.md)**

## Attributes


### Own

 * [groupingId](groupingId.md)  <sub>0..1</sub>
     * Range: [GroupingFactor](GroupingFactor.md)
 * [groupId](groupId.md)  <sub>0..1</sub>
     * Range: [Group](Group.md)
 * [groupValue](groupValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
