
# Class: Analysis




URI: [https://www.cdisc.org/ars/1-0/Analysis](https://www.cdisc.org/ars/1-0/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedGroupingFactor],[DataSubset],[AnalysisSet],[AnalysisMethod],[AnalysisCategory],[AnalysisMethod]<method%200..1-++[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F;variable:string%20%3F],[DataSubset]<dataSubsetRef%200..1-%20[Analysis],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSetRef%200..1-%20[Analysis],[AnalysisCategory]<categoryRefs%200..*-%20[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysisRef%200..1>[Analysis],[ReportingEvent],[OrderedListItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedGroupingFactor],[DataSubset],[AnalysisSet],[AnalysisMethod],[AnalysisCategory],[AnalysisMethod]<method%200..1-++[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F;variable:string%20%3F],[DataSubset]<dataSubsetRef%200..1-%20[Analysis],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSetRef%200..1-%20[Analysis],[AnalysisCategory]<categoryRefs%200..*-%20[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysisRef%200..1>[Analysis],[ReportingEvent],[OrderedListItem])

## Referenced by Class

 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysisRef](analysisRef.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [categoryRefs](categoryRefs.md)  <sub>0..\*</sub>
     * Range: [AnalysisCategory](AnalysisCategory.md)
 * [analysisSetRef](analysisSetRef.md)  <sub>0..1</sub>
     * Range: [AnalysisSet](AnalysisSet.md)
 * [orderedGroupings](orderedGroupings.md)  <sub>0..\*</sub>
     * Range: [OrderedGroupingFactor](OrderedGroupingFactor.md)
 * [dataSubsetRef](dataSubsetRef.md)  <sub>0..1</sub>
     * Range: [DataSubset](DataSubset.md)
 * [dataset](dataset.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [variable](variable.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [method](method.md)  <sub>0..1</sub>
     * Range: [AnalysisMethod](AnalysisMethod.md)
