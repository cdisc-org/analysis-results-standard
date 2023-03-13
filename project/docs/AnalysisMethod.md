
# Class: AnalysisMethod




URI: [https://www.cdisc.org/ars/1-0/AnalysisMethod](https://www.cdisc.org/ars/1-0/AnalysisMethod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Operation],[NamedObject],[Operation]<operations%201..*-++[AnalysisMethod&#124;id:string;label:string%20%3F;description:string%20%3F;name(i):string],[Analysis]-%20methodId%200..1>[AnalysisMethod],[ReportingEvent]++-%20methods%200..*>[AnalysisMethod],[NamedObject]^-[AnalysisMethod],[ReportingEvent],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Operation],[NamedObject],[Operation]<operations%201..*-++[AnalysisMethod&#124;id:string;label:string%20%3F;description:string%20%3F;name(i):string],[Analysis]-%20methodId%200..1>[AnalysisMethod],[ReportingEvent]++-%20methods%200..*>[AnalysisMethod],[NamedObject]^-[AnalysisMethod],[ReportingEvent],[Analysis])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[methodId](methodId.md)*  <sub>0..1</sub>  **[AnalysisMethod](AnalysisMethod.md)**
 *  **None** *[methods](methods.md)*  <sub>0..\*</sub>  **[AnalysisMethod](AnalysisMethod.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [operations](operations.md)  <sub>1..\*</sub>
     * Range: [Operation](Operation.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
