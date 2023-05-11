
# Class: OrderedGroupingFactor




URI: [https://www.cdisc.org/ars/1-0/OrderedGroupingFactor](https://www.cdisc.org/ars/1-0/OrderedGroupingFactor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataGroupingFactor]<dataGrouping%200..1-++[OrderedGroupingFactor&#124;order:integer;resultsByGroup:boolean],[GroupingFactor]<groupingId%200..1-%20[OrderedGroupingFactor],[Analysis]++-%20orderedGroupings%200..*>[OrderedGroupingFactor],[GroupingFactor],[DataGroupingFactor],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataGroupingFactor]<dataGrouping%200..1-++[OrderedGroupingFactor&#124;order:integer;resultsByGroup:boolean],[GroupingFactor]<groupingId%200..1-%20[OrderedGroupingFactor],[Analysis]++-%20orderedGroupings%200..*>[OrderedGroupingFactor],[GroupingFactor],[DataGroupingFactor],[Analysis])

## Referenced by Class

 *  **None** *[orderedGroupings](orderedGroupings.md)*  <sub>0..\*</sub>  **[OrderedGroupingFactor](OrderedGroupingFactor.md)**

## Attributes


### Own

 * [OrderedGroupingFactor➞order](OrderedGroupingFactor_order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [groupingId](groupingId.md)  <sub>0..1</sub>
     * Range: [GroupingFactor](GroupingFactor.md)
 * [dataGrouping](dataGrouping.md)  <sub>0..1</sub>
     * Range: [DataGroupingFactor](DataGroupingFactor.md)
 * [resultsByGroup](resultsByGroup.md)  <sub>1..1</sub>
     * Description: Indicates whether a result is expected for each group in the grouping.
     * Range: [Boolean](types/Boolean.md)
