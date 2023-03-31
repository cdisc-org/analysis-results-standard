
# Class: CompoundGroupExpression




URI: [https://www.cdisc.org/ars/1-0/CompoundGroupExpression](https://www.cdisc.org/ars/1-0/CompoundGroupExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[Group]<whereClauses%200..*-%20[CompoundGroupExpression&#124;logicalOperator(i):LogicalOperator],[Group]++-%20compoundExpression%200..1>[CompoundGroupExpression],[CompoundExpression]^-[CompoundGroupExpression],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Group],[Group]<whereClauses%200..*-%20[CompoundGroupExpression&#124;logicalOperator(i):LogicalOperator],[Group]++-%20compoundExpression%200..1>[CompoundGroupExpression],[CompoundExpression]^-[CompoundGroupExpression],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **[Group](Group.md)** *[Group➞compoundExpression](Group_compoundExpression.md)*  <sub>0..1</sub>  **[CompoundGroupExpression](CompoundGroupExpression.md)**

## Attributes


### Own

 * [CompoundGroupExpression➞whereClauses](CompoundGroupExpression_whereClauses.md)  <sub>0..\*</sub>
     * Range: [Group](Group.md)

### Inherited from CompoundExpression:

 * [logicalOperator](logicalOperator.md)  <sub>1..1</sub>
     * Range: [LogicalOperator](LogicalOperator.md)
