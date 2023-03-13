
# Class: AnalysisGroup


A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A, subjects whose gender is male).

URI: [https://www.cdisc.org/ars/1-0/AnalysisGroup](https://www.cdisc.org/ars/1-0/AnalysisGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Group],[Condition],[CompoundGroupExpression],[SubjectGroupingFactor]++-%20groups%200..*>[AnalysisGroup&#124;label(i):string%20%3F;order(i):integer;id(i):string],[Group]^-[AnalysisGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectGroupingFactor],[Group],[Condition],[CompoundGroupExpression],[SubjectGroupingFactor]++-%20groups%200..*>[AnalysisGroup&#124;label(i):string%20%3F;order(i):integer;id(i):string],[Group]^-[AnalysisGroup])

## Parents

 *  is_a: [Group](Group.md) - A subdivision of the subject population or analysis dataset record set based on a defined factor.

## Referenced by Class

 *  **[SubjectGroupingFactor](SubjectGroupingFactor.md)** *[SubjectGroupingFactor➞groups](SubjectGroupingFactor_groups.md)*  <sub>0..\*</sub>  **[AnalysisGroup](AnalysisGroup.md)**

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
