
# Class: OrderedGroupingFactor




URI: [https://www.cdisc.org/ars/1-0/OrderedGroupingFactor](https://www.cdisc.org/ars/1-0/OrderedGroupingFactor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataGroupingFactor]<dataGrouping%200..1-++[OrderedGroupingFactor&#124;order:integer],[GroupingFactor]<groupingRef%200..1-%20[OrderedGroupingFactor],[Analysis]++-%20orderedGroupings%200..*>[OrderedGroupingFactor],[GroupingFactor],[DataGroupingFactor],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataGroupingFactor]<dataGrouping%200..1-++[OrderedGroupingFactor&#124;order:integer],[GroupingFactor]<groupingRef%200..1-%20[OrderedGroupingFactor],[Analysis]++-%20orderedGroupings%200..*>[OrderedGroupingFactor],[GroupingFactor],[DataGroupingFactor],[Analysis])

## Referenced by Class

 *  **None** *[orderedGroupings](orderedGroupings.md)*  <sub>0..\*</sub>  **[OrderedGroupingFactor](OrderedGroupingFactor.md)**

## Attributes


### Own

 * [order](order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [groupingRef](groupingRef.md)  <sub>0..1</sub>
     * Range: [GroupingFactor](GroupingFactor.md)
 * [dataGrouping](dataGrouping.md)  <sub>0..1</sub>
     * Range: [DataGroupingFactor](DataGroupingFactor.md)
