
# Class: NestedList




URI: [https://www.cdisc.org/ars/1-0/NestedList](https://www.cdisc.org/ars/1-0/NestedList)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedListItem],[OrderedListItem]<listItems%200..*-++[NestedList],[ReportingEvent]++-%20listOfPlannedAnalyses%201..1>[NestedList],[ReportingEvent]++-%20listOfPlannedOutputs%200..1>[NestedList],[OrderedListItem]++-%20sublist%200..1>[NestedList],[ReportingEvent])](https://yuml.me/diagram/nofunky;dir:TB/class/[OrderedListItem],[OrderedListItem]<listItems%200..*-++[NestedList],[ReportingEvent]++-%20listOfPlannedAnalyses%201..1>[NestedList],[ReportingEvent]++-%20listOfPlannedOutputs%200..1>[NestedList],[OrderedListItem]++-%20sublist%200..1>[NestedList],[ReportingEvent])

## Referenced by Class

 *  **None** *[listOfPlannedAnalyses](listOfPlannedAnalyses.md)*  <sub>1..1</sub>  **[NestedList](NestedList.md)**
 *  **None** *[listOfPlannedOutputs](listOfPlannedOutputs.md)*  <sub>0..1</sub>  **[NestedList](NestedList.md)**
 *  **None** *[sublist](sublist.md)*  <sub>0..1</sub>  **[NestedList](NestedList.md)**

## Attributes


### Own

 * [listItems](listItems.md)  <sub>0..\*</sub>
     * Range: [OrderedListItem](OrderedListItem.md)
