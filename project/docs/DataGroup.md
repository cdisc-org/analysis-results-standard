
# Class: DataGroup


A subdivision of the analysis dataset records based on a defined factor.

URI: [https://www.cdisc.org/ars/1-0/DataGroup](https://www.cdisc.org/ars/1-0/DataGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[DataGroupingFactor],[DataGroupingFactor]++-%20groups%200..*>[DataGroup&#124;label(i):string%20%3F;order(i):integer;id(i):string],[Group]^-[DataGroup],[Condition],[CompoundGroupExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[DataGroupingFactor],[DataGroupingFactor]++-%20groups%200..*>[DataGroup&#124;label(i):string%20%3F;order(i):integer;id(i):string],[Group]^-[DataGroup],[Condition],[CompoundGroupExpression])

## Parents

 *  is_a: [Group](Group.md) - A subdivision of the subject population or analysis dataset record set based on a defined factor.

## Referenced by Class

 *  **[DataGroupingFactor](DataGroupingFactor.md)** *[DataGroupingFactor➞groups](DataGroupingFactor_groups.md)*  <sub>0..\*</sub>  **[DataGroup](DataGroup.md)**

## Attributes


### Inherited from Group:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [order](order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [Group➞compoundExpression](Group_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundGroupExpression](CompoundGroupExpression.md)
