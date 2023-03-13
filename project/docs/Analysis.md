
# Class: Analysis




URI: [https://www.cdisc.org/ars/1-0/Analysis](https://www.cdisc.org/ars/1-0/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedAnalysisOperation],[OrderedGroupingFactor],[OperationResult],[DataSubset],[AnalysisSet],[AnalysisMethod],[AnalysisCategory],[OperationResult]<results%200..*-++[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F;variable:string%20%3F],[ReferencedAnalysisOperation]<referencedAnalysisOperations%200..*-++[Analysis],[AnalysisMethod]<methodId%200..1-%20[Analysis],[DataSubset]<dataSubsetId%200..1-%20[Analysis],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSetId%200..1-%20[Analysis],[AnalysisCategory]<categoryIds%200..*-%20[Analysis],[ReferencedAnalysisOperation]-%20analysisId%201..1>[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysisId%200..1>[Analysis],[ReferencedAnalysisOperation]-%20analysisId(i)%200..1>[Analysis],[ReferencedOperationRelationship]-%20analysisId%200..1>[Analysis],[ReportingEvent],[ReferencedOperationRelationship],[OrderedListItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferencedAnalysisOperation],[OrderedGroupingFactor],[OperationResult],[DataSubset],[AnalysisSet],[AnalysisMethod],[AnalysisCategory],[OperationResult]<results%200..*-++[Analysis&#124;id:string;version:integer%20%3F;dataset:string%20%3F;variable:string%20%3F],[ReferencedAnalysisOperation]<referencedAnalysisOperations%200..*-++[Analysis],[AnalysisMethod]<methodId%200..1-%20[Analysis],[DataSubset]<dataSubsetId%200..1-%20[Analysis],[OrderedGroupingFactor]<orderedGroupings%200..*-++[Analysis],[AnalysisSet]<analysisSetId%200..1-%20[Analysis],[AnalysisCategory]<categoryIds%200..*-%20[Analysis],[ReferencedAnalysisOperation]-%20analysisId%201..1>[Analysis],[ReportingEvent]++-%20analyses%200..*>[Analysis],[OrderedListItem]-%20analysisId%200..1>[Analysis],[ReferencedAnalysisOperation]-%20analysisId(i)%200..1>[Analysis],[ReferencedOperationRelationship]-%20analysisId%200..1>[Analysis],[ReportingEvent],[ReferencedOperationRelationship],[OrderedListItem])

## Referenced by Class

 *  **[ReferencedAnalysisOperation](ReferencedAnalysisOperation.md)** *[ReferencedAnalysisOperation➞analysisId](ReferencedAnalysisOperation_analysisId.md)*  <sub>1..1</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysisId](analysisId.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [categoryIds](categoryIds.md)  <sub>0..\*</sub>
     * Range: [AnalysisCategory](AnalysisCategory.md)
 * [analysisSetId](analysisSetId.md)  <sub>0..1</sub>
     * Range: [AnalysisSet](AnalysisSet.md)
 * [orderedGroupings](orderedGroupings.md)  <sub>0..\*</sub>
     * Range: [OrderedGroupingFactor](OrderedGroupingFactor.md)
 * [dataSubsetId](dataSubsetId.md)  <sub>0..1</sub>
     * Range: [DataSubset](DataSubset.md)
 * [dataset](dataset.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [variable](variable.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [methodId](methodId.md)  <sub>0..1</sub>
     * Range: [AnalysisMethod](AnalysisMethod.md)
 * [referencedAnalysisOperations](referencedAnalysisOperations.md)  <sub>0..\*</sub>
     * Range: [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md)
 * [results](results.md)  <sub>0..\*</sub>
     * Range: [OperationResult](OperationResult.md)
