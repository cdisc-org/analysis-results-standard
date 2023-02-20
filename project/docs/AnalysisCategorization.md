
# Class: AnalysisCategorization


An implementer-defined categorization of analyses/outputs.

URI: [https://www.cdisc.org/ars/1-0/AnalysisCategorization](https://www.cdisc.org/ars/1-0/AnalysisCategorization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisCategory],[AnalysisCategory]<categories%201..*-++[AnalysisCategorization&#124;id:string;label:string%20%3F],[ReportingEvent]++-%20analysisCategorizations%200..*>[AnalysisCategorization],[AnalysisCategory]++-%20subCategorizations%200..*>[AnalysisCategorization],[ReportingEvent])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisCategory],[AnalysisCategory]<categories%201..*-++[AnalysisCategorization&#124;id:string;label:string%20%3F],[ReportingEvent]++-%20analysisCategorizations%200..*>[AnalysisCategorization],[AnalysisCategory]++-%20subCategorizations%200..*>[AnalysisCategorization],[ReportingEvent])

## Referenced by Class

 *  **None** *[analysisCategorizations](analysisCategorizations.md)*  <sub>0..\*</sub>  **[AnalysisCategorization](AnalysisCategorization.md)**
 *  **None** *[subCategorizations](subCategorizations.md)*  <sub>0..\*</sub>  **[AnalysisCategorization](AnalysisCategorization.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [categories](categories.md)  <sub>1..\*</sub>
     * Range: [AnalysisCategory](AnalysisCategory.md)
