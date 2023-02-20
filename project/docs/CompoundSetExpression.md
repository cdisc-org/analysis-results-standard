
# Class: CompoundSetExpression




URI: [https://www.cdisc.org/ars/1-0/CompoundSetExpression](https://www.cdisc.org/ars/1-0/CompoundSetExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisSet]<whereClauses%200..*-%20[CompoundSetExpression&#124;logicalOperator(i):AndOr],[AnalysisSet]++-%20compoundExpression%200..1>[CompoundSetExpression],[CompoundExpression]^-[CompoundSetExpression],[CompoundExpression],[AnalysisSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnalysisSet]<whereClauses%200..*-%20[CompoundSetExpression&#124;logicalOperator(i):AndOr],[AnalysisSet]++-%20compoundExpression%200..1>[CompoundSetExpression],[CompoundExpression]^-[CompoundSetExpression],[CompoundExpression],[AnalysisSet])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **[AnalysisSet](AnalysisSet.md)** *[AnalysisSet➞compoundExpression](AnalysisSet_compoundExpression.md)*  <sub>0..1</sub>  **[CompoundSetExpression](CompoundSetExpression.md)**

## Attributes


### Own

 * [CompoundSetExpression➞whereClauses](CompoundSetExpression_whereClauses.md)  <sub>0..\*</sub>
     * Range: [AnalysisSet](AnalysisSet.md)

### Inherited from CompoundExpression:

 * [logicalOperator](logicalOperator.md)  <sub>1..1</sub>
     * Range: [AndOr](AndOr.md)
