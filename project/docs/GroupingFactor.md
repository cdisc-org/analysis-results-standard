
# Class: GroupingFactor


A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.

URI: [https://www.cdisc.org/ars/1-0/GroupingFactor](https://www.cdisc.org/ars/1-0/GroupingFactor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Group]<groups%200..*-++[GroupingFactor&#124;id:string;label:string%20%3F;groupingVariable:string%20%3F;dataDriven:boolean],[OrderedGroupingFactor]-%20groupingRef%200..1>[GroupingFactor],[GroupingFactor]^-[SubjectGroupingFactor],[GroupingFactor]^-[DataGroupingFactor],[OrderedGroupingFactor],[Group],[DataGroupingFactor])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Group]<groups%200..*-++[GroupingFactor&#124;id:string;label:string%20%3F;groupingVariable:string%20%3F;dataDriven:boolean],[OrderedGroupingFactor]-%20groupingRef%200..1>[GroupingFactor],[GroupingFactor]^-[SubjectGroupingFactor],[GroupingFactor]^-[DataGroupingFactor],[OrderedGroupingFactor],[Group],[DataGroupingFactor])

## Children

 * [DataGroupingFactor](DataGroupingFactor.md) - A factor used to subdivide data records in an analysis dataset for analysis.
 * [SubjectGroupingFactor](SubjectGroupingFactor.md) - A factor used to subdivide the subject population for comparative analysis (e.g., treatment, sex, race, age).

## Referenced by Class

 *  **None** *[groupingRef](groupingRef.md)*  <sub>0..1</sub>  **[GroupingFactor](GroupingFactor.md)**

## Attributes


### Own

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
 * [groups](groups.md)  <sub>0..\*</sub>
     * Range: [Group](Group.md)
