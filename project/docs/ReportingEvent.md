
# Class: ReportingEvent




URI: [https://www.cdisc.org/ars/1-0/ReportingEvent](https://www.cdisc.org/ars/1-0/ReportingEvent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Output]<outputs%200..*-++[ReportingEvent&#124;name(i):string],[Analysis]<analyses%200..*-++[ReportingEvent],[AnalysisCategorization]<analysisCategorizations%200..*-++[ReportingEvent],[DisplaySection]<globalDisplaySections%200..*-++[ReportingEvent],[DataSubset]<dataSubsets%200..*-++[ReportingEvent],[SubjectGroupingFactor]<analysisGroupings%200..*-++[ReportingEvent],[AnalysisSet]<analysisSets%200..*-++[ReportingEvent],[NestedList]<listOfPlannedOutputs%200..1-++[ReportingEvent],[NestedList]<listOfPlannedAnalyses%201..1-++[ReportingEvent],[NamedObject]^-[ReportingEvent],[Output],[NestedList],[NamedObject],[DisplaySection],[DataSubset],[AnalysisSet],[AnalysisCategorization],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Output]<outputs%200..*-++[ReportingEvent&#124;name(i):string],[Analysis]<analyses%200..*-++[ReportingEvent],[AnalysisCategorization]<analysisCategorizations%200..*-++[ReportingEvent],[DisplaySection]<globalDisplaySections%200..*-++[ReportingEvent],[DataSubset]<dataSubsets%200..*-++[ReportingEvent],[SubjectGroupingFactor]<analysisGroupings%200..*-++[ReportingEvent],[AnalysisSet]<analysisSets%200..*-++[ReportingEvent],[NestedList]<listOfPlannedOutputs%200..1-++[ReportingEvent],[NestedList]<listOfPlannedAnalyses%201..1-++[ReportingEvent],[NamedObject]^-[ReportingEvent],[Output],[NestedList],[NamedObject],[DisplaySection],[DataSubset],[AnalysisSet],[AnalysisCategorization],[Analysis])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Attributes


### Own

 * [listOfPlannedAnalyses](listOfPlannedAnalyses.md)  <sub>1..1</sub>
     * Range: [NestedList](NestedList.md)
 * [listOfPlannedOutputs](listOfPlannedOutputs.md)  <sub>0..1</sub>
     * Range: [NestedList](NestedList.md)
 * [analysisSets](analysisSets.md)  <sub>0..\*</sub>
     * Range: [AnalysisSet](AnalysisSet.md)
 * [analysisGroupings](analysisGroupings.md)  <sub>0..\*</sub>
     * Range: [SubjectGroupingFactor](SubjectGroupingFactor.md)
 * [dataSubsets](dataSubsets.md)  <sub>0..\*</sub>
     * Range: [DataSubset](DataSubset.md)
 * [globalDisplaySections](globalDisplaySections.md)  <sub>0..\*</sub>
     * Range: [DisplaySection](DisplaySection.md)
 * [analysisCategorizations](analysisCategorizations.md)  <sub>0..\*</sub>
     * Range: [AnalysisCategorization](AnalysisCategorization.md)
 * [analyses](analyses.md)  <sub>0..\*</sub>
     * Range: [Analysis](Analysis.md)
 * [outputs](outputs.md)  <sub>0..\*</sub>
     * Range: [Output](Output.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
