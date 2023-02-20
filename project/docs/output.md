
# Class: Output




URI: [https://www.cdisc.org/ars/1-0/Output](https://www.cdisc.org/ars/1-0/Output)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OutputDisplay],[AnalysisCategory]<categoryRefs%200..*-%20[Output&#124;id:string;version:integer%20%3F],[OutputDisplay]<outputDisplays%200..*-++[Output],[File]<fileSpecifications%200..*-++[Output],[OrderedListItem]-%20outputRef%200..1>[Output],[ReportingEvent]++-%20outputs%200..*>[Output],[ReportingEvent],[OrderedListItem],[File],[AnalysisCategory])](https://yuml.me/diagram/nofunky;dir:TB/class/[OutputDisplay],[AnalysisCategory]<categoryRefs%200..*-%20[Output&#124;id:string;version:integer%20%3F],[OutputDisplay]<outputDisplays%200..*-++[Output],[File]<fileSpecifications%200..*-++[Output],[OrderedListItem]-%20outputRef%200..1>[Output],[ReportingEvent]++-%20outputs%200..*>[Output],[ReportingEvent],[OrderedListItem],[File],[AnalysisCategory])

## Referenced by Class

 *  **None** *[outputRef](outputRef.md)*  <sub>0..1</sub>  **[Output](Output.md)**
 *  **None** *[outputs](outputs.md)*  <sub>0..\*</sub>  **[Output](Output.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [fileSpecifications](fileSpecifications.md)  <sub>0..\*</sub>
     * Range: [File](File.md)
 * [outputDisplays](outputDisplays.md)  <sub>0..\*</sub>
     * Range: [OutputDisplay](OutputDisplay.md)
 * [Output➞categoryRefs](Output_categoryRefs.md)  <sub>0..\*</sub>
     * Range: [AnalysisCategory](AnalysisCategory.md)
