
# Class: CompoundExpression




URI: [https://www.cdisc.org/ars/1-0/CompoundExpression](https://www.cdisc.org/ars/1-0/CompoundExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression],[CompoundSetExpression],[CompoundGroupExpression],[WhereClause]<whereClauses%200..*-++[CompoundExpression&#124;logicalOperator:LogicalOperator],[WhereClause]++-%20compoundExpression%200..1>[CompoundExpression],[CompoundExpression]^-[CompoundSubsetExpression],[CompoundExpression]^-[CompoundSetExpression],[CompoundExpression]^-[CompoundGroupExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression],[CompoundSetExpression],[CompoundGroupExpression],[WhereClause]<whereClauses%200..*-++[CompoundExpression&#124;logicalOperator:LogicalOperator],[WhereClause]++-%20compoundExpression%200..1>[CompoundExpression],[CompoundExpression]^-[CompoundSubsetExpression],[CompoundExpression]^-[CompoundSetExpression],[CompoundExpression]^-[CompoundGroupExpression])

## Children

 * [CompoundGroupExpression](CompoundGroupExpression.md)
 * [CompoundSetExpression](CompoundSetExpression.md)
 * [CompoundSubsetExpression](CompoundSubsetExpression.md)

## Referenced by Class

 *  **None** *[compoundExpression](compoundExpression.md)*  <sub>0..1</sub>  **[CompoundExpression](CompoundExpression.md)**

## Attributes


### Own

 * [logicalOperator](logicalOperator.md)  <sub>1..1</sub>
     * Range: [LogicalOperator](LogicalOperator.md)
 * [whereClauses](whereClauses.md)  <sub>0..\*</sub>
     * Range: [WhereClause](WhereClause.md)
