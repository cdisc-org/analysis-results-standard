
# Class: DataGroup


A subdivision of the analysis dataset records based on a defined factor.

URI: [https://www.cdisc.org/ars/1-0/DataGroup](https://www.cdisc.org/ars/1-0/DataGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[DataGroupingFactor],[DataGroupingFactor]++-%20groups%200..*>[DataGroup&#124;id(i):string;label(i):string%20%3F;level(i):integer%20%3F;order(i):integer%20%3F],[Group]^-[DataGroup],[Condition],[CompoundGroupExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[DataGroupingFactor],[DataGroupingFactor]++-%20groups%200..*>[DataGroup&#124;id(i):string;label(i):string%20%3F;level(i):integer%20%3F;order(i):integer%20%3F],[Group]^-[DataGroup],[Condition],[CompoundGroupExpression])

## Parents

 *  is_a: [Group](Group.md) - A subdivision of the subject population or analysis dataset record set based on a defined factor.

## Referenced by Class

 *  **[DataGroupingFactor](DataGroupingFactor.md)** *[DataGroupingFactor➞groups](DataGroupingFactor_groups.md)*  <sub>0..\*</sub>  **[DataGroup](DataGroup.md)**

## Attributes


### Inherited from Group:

 * [level](level.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [order](order.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [Group➞compoundExpression](Group_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundGroupExpression](CompoundGroupExpression.md)
