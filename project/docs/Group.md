
# Class: Group


A subdivision of the subject population or analysis dataset record set based on a defined factor.

URI: [https://www.cdisc.org/ars/1-0/Group](https://www.cdisc.org/ars/1-0/Group)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundGroupExpression]<compoundExpression%200..1-++[Group&#124;label:string%20%3F;order:integer;id(i):string],[CompoundGroupExpression]-%20whereClauses%200..*>[Group],[ResultGroup]-%20groupId%200..1>[Group],[GroupingFactor]++-%20groups%200..*>[Group],[Group]^-[DataGroup],[Group]^-[AnalysisGroup],[WhereClause]^-[Group],[ResultGroup],[GroupingFactor],[DataGroup],[Condition],[CompoundGroupExpression],[AnalysisGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundGroupExpression]<compoundExpression%200..1-++[Group&#124;label:string%20%3F;order:integer;id(i):string],[CompoundGroupExpression]-%20whereClauses%200..*>[Group],[ResultGroup]-%20groupId%200..1>[Group],[GroupingFactor]++-%20groups%200..*>[Group],[Group]^-[DataGroup],[Group]^-[AnalysisGroup],[WhereClause]^-[Group],[ResultGroup],[GroupingFactor],[DataGroup],[Condition],[CompoundGroupExpression],[AnalysisGroup])

## Parents

 *  is_a: [WhereClause](WhereClause.md)

## Children

 * [AnalysisGroup](AnalysisGroup.md) - A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A, subjects whose gender is male).
 * [DataGroup](DataGroup.md) - A subdivision of the analysis dataset records based on a defined factor.

## Referenced by Class

 *  **[CompoundGroupExpression](CompoundGroupExpression.md)** *[CompoundGroupExpression➞whereClauses](CompoundGroupExpression_whereClauses.md)*  <sub>0..\*</sub>  **[Group](Group.md)**
 *  **None** *[groupId](groupId.md)*  <sub>0..1</sub>  **[Group](Group.md)**
 *  **None** *[groups](groups.md)*  <sub>0..\*</sub>  **[Group](Group.md)**

## Attributes


### Own

 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [order](order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [Group➞compoundExpression](Group_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundGroupExpression](CompoundGroupExpression.md)

### Inherited from WhereClause:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
