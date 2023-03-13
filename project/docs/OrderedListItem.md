
# Class: OrderedListItem




URI: [https://www.cdisc.org/ars/1-0/OrderedListItem](https://www.cdisc.org/ars/1-0/OrderedListItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Output],[Output]<outputId%200..1-%20[OrderedListItem&#124;order:integer;name(i):string],[Analysis]<analysisId%200..1-%20[OrderedListItem],[NestedList]<sublist%200..1-++[OrderedListItem],[NestedList]++-%20listItems%200..*>[OrderedListItem],[NamedObject]^-[OrderedListItem],[NestedList],[NamedObject],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Output],[Output]<outputId%200..1-%20[OrderedListItem&#124;order:integer;name(i):string],[Analysis]<analysisId%200..1-%20[OrderedListItem],[NestedList]<sublist%200..1-++[OrderedListItem],[NestedList]++-%20listItems%200..*>[OrderedListItem],[NamedObject]^-[OrderedListItem],[NestedList],[NamedObject],[Analysis])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[listItems](listItems.md)*  <sub>0..\*</sub>  **[OrderedListItem](OrderedListItem.md)**

## Attributes


### Own

 * [order](order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [sublist](sublist.md)  <sub>0..1</sub>
     * Range: [NestedList](NestedList.md)
 * [analysisId](analysisId.md)  <sub>0..1</sub>
     * Range: [Analysis](Analysis.md)
 * [outputId](outputId.md)  <sub>0..1</sub>
     * Range: [Output](Output.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
