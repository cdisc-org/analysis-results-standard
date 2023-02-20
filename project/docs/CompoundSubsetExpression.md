
# Class: CompoundSubsetExpression




URI: [https://www.cdisc.org/ars/1-0/CompoundSubsetExpression](https://www.cdisc.org/ars/1-0/CompoundSubsetExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[DataSubset],[WhereClause]<whereClauses%200..*-++[CompoundSubsetExpression&#124;logicalOperator(i):AndOr],[DataSubset]++-%20compoundExpression%200..1>[CompoundSubsetExpression],[CompoundExpression]^-[CompoundSubsetExpression],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[DataSubset],[WhereClause]<whereClauses%200..*-++[CompoundSubsetExpression&#124;logicalOperator(i):AndOr],[DataSubset]++-%20compoundExpression%200..1>[CompoundSubsetExpression],[CompoundExpression]^-[CompoundSubsetExpression],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **[DataSubset](DataSubset.md)** *[DataSubset➞compoundExpression](DataSubset_compoundExpression.md)*  <sub>0..1</sub>  **[CompoundSubsetExpression](CompoundSubsetExpression.md)**

## Attributes


### Own

 * [CompoundSubsetExpression➞whereClauses](CompoundSubsetExpression_whereClauses.md)  <sub>0..\*</sub>
     * Range: [WhereClause](WhereClause.md)

### Inherited from CompoundExpression:

 * [logicalOperator](logicalOperator.md)  <sub>1..1</sub>
     * Range: [AndOr](AndOr.md)
