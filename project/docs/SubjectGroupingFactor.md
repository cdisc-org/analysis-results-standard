
# Class: SubjectGroupingFactor


A factor used to subdivide the subject population for comparative analysis (e.g., treatment, sex, race, age).

URI: [https://www.cdisc.org/ars/1-0/SubjectGroupingFactor](https://www.cdisc.org/ars/1-0/SubjectGroupingFactor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisGroup]<groups%200..*-++[SubjectGroupingFactor&#124;id(i):string;label(i):string%20%3F;groupingVariable(i):string%20%3F;dataDriven(i):boolean],[ReportingEvent]++-%20analysisGroupings%200..*>[SubjectGroupingFactor],[GroupingFactor]^-[SubjectGroupingFactor],[ReportingEvent],[GroupingFactor],[AnalysisGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisGroup]<groups%200..*-++[SubjectGroupingFactor&#124;id(i):string;label(i):string%20%3F;groupingVariable(i):string%20%3F;dataDriven(i):boolean],[ReportingEvent]++-%20analysisGroupings%200..*>[SubjectGroupingFactor],[GroupingFactor]^-[SubjectGroupingFactor],[ReportingEvent],[GroupingFactor],[AnalysisGroup])

## Parents

 *  is_a: [GroupingFactor](GroupingFactor.md) - A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.

## Referenced by Class

 *  **None** *[analysisGroupings](analysisGroupings.md)*  <sub>0..\*</sub>  **[SubjectGroupingFactor](SubjectGroupingFactor.md)**

## Attributes


### Own

 * [SubjectGroupingFactor➞groups](SubjectGroupingFactor_groups.md)  <sub>0..\*</sub>
     * Range: [AnalysisGroup](AnalysisGroup.md)

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
