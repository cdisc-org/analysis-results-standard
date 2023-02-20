
# Class: Analysis




URI: [https://www.cdisc.org/ars/1-0/Analysis](https://www.cdisc.org/ars/1-0/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedGroupingFactor],[AnalysisSet],[AnalysisCategory],[AnalysisCategory]<categoryRefs%200..*-%20[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSet%200..1-%20[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysis%200..1>[Analysis],[ReportingEvent],[OrderedListItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedGroupingFactor],[AnalysisSet],[AnalysisCategory],[AnalysisCategory]<categoryRefs%200..*-%20[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSet%200..1-%20[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysis%200..1>[Analysis],[ReportingEvent],[OrderedListItem])

## Referenced by Class

 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysis](analysis.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [analysisSet](analysisSet.md)  <sub>0..1</sub>
     * Range: [AnalysisSet](AnalysisSet.md)
 * [orderedGroupings](orderedGroupings.md)  <sub>0..\*</sub>
     * Range: [OrderedGroupingFactor](OrderedGroupingFactor.md)
 * [dataset](dataset.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [categoryRefs](categoryRefs.md)  <sub>0..\*</sub>
     * Range: [AnalysisCategory](AnalysisCategory.md)
