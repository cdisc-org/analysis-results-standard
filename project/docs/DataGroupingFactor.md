
# Class: DataGroupingFactor


A factor used to subdivide data records in an analysis dataset for analysis.

URI: [https://www.cdisc.org/ars/1-0/DataGroupingFactor](https://www.cdisc.org/ars/1-0/DataGroupingFactor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GroupingFactor],[DataGroup]<groups%200..*-++[DataGroupingFactor&#124;id(i):string;label(i):string%20%3F;groupingVariable(i):string%20%3F;dataDriven(i):boolean],[OrderedGroupingFactor]++-%20dataGrouping%200..1>[DataGroupingFactor],[GroupingFactor]^-[DataGroupingFactor],[OrderedGroupingFactor],[DataGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[GroupingFactor],[DataGroup]<groups%200..*-++[DataGroupingFactor&#124;id(i):string;label(i):string%20%3F;groupingVariable(i):string%20%3F;dataDriven(i):boolean],[OrderedGroupingFactor]++-%20dataGrouping%200..1>[DataGroupingFactor],[GroupingFactor]^-[DataGroupingFactor],[OrderedGroupingFactor],[DataGroup])

## Parents

 *  is_a: [GroupingFactor](GroupingFactor.md) - A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.

## Referenced by Class

 *  **None** *[dataGrouping](dataGrouping.md)*  <sub>0..1</sub>  **[DataGroupingFactor](DataGroupingFactor.md)**

## Attributes


### Own

 * [DataGroupingFactor➞groups](DataGroupingFactor_groups.md)  <sub>0..\*</sub>
     * Range: [DataGroup](DataGroup.md)

### Inherited from GroupingFactor:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [groupingVariable](groupingVariable.md)  <sub>0..1</sub>
     * Description: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
     * Range: [String](types/String.md)
 * [dataDriven](dataDriven.md)  <sub>1..1</sub>
     * Description: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
     * Range: [Boolean](types/Boolean.md)
