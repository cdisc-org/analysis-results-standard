
# Class: DisplaySection




URI: [https://www.cdisc.org/ars/1-0/DisplaySection](https://www.cdisc.org/ars/1-0/DisplaySection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DisplaySubSection],[DisplaySubSection]<subSections%200..*-++[DisplaySection&#124;sectionType:SectionType%20%3F],[Display]++-%20displaySections%200..*>[DisplaySection],[ReportingEvent]++-%20globalDisplaySections%200..*>[DisplaySection],[ReportingEvent],[Display])](https://yuml.me/diagram/nofunky;dir:TB/class/[DisplaySubSection],[DisplaySubSection]<subSections%200..*-++[DisplaySection&#124;sectionType:SectionType%20%3F],[Display]++-%20displaySections%200..*>[DisplaySection],[ReportingEvent]++-%20globalDisplaySections%200..*>[DisplaySection],[ReportingEvent],[Display])

## Referenced by Class

 *  **None** *[displaySections](displaySections.md)*  <sub>0..\*</sub>  **[DisplaySection](DisplaySection.md)**
 *  **None** *[globalDisplaySections](globalDisplaySections.md)*  <sub>0..\*</sub>  **[DisplaySection](DisplaySection.md)**

## Attributes


### Own

 * [sectionType](sectionType.md)  <sub>0..1</sub>
     * Range: [SectionType](SectionType.md)
 * [subSections](subSections.md)  <sub>0..\*</sub>
     * Range: [DisplaySubSection](DisplaySubSection.md)
