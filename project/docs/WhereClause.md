
# Class: WhereClause




URI: [https://www.cdisc.org/ars/1-0/WhereClause](https://www.cdisc.org/ars/1-0/WhereClause)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CompoundExpression]<compoundExpression%200..1-++[WhereClause&#124;level:integer%20%3F;order:integer%20%3F],[Condition]<condition%200..1-++[WhereClause],[CompoundSubsetExpression]++-%20whereClauses%200..*>[WhereClause],[CompoundExpression]++-%20whereClauses%200..*>[WhereClause],[WhereClause]^-[Group],[WhereClause]^-[DataSubset],[WhereClause]^-[AnalysisSet],[Group],[DataSubset],[Condition],[CompoundSubsetExpression],[CompoundExpression],[AnalysisSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[CompoundExpression]<compoundExpression%200..1-++[WhereClause&#124;level:integer%20%3F;order:integer%20%3F],[Condition]<condition%200..1-++[WhereClause],[CompoundSubsetExpression]++-%20whereClauses%200..*>[WhereClause],[CompoundExpression]++-%20whereClauses%200..*>[WhereClause],[WhereClause]^-[Group],[WhereClause]^-[DataSubset],[WhereClause]^-[AnalysisSet],[Group],[DataSubset],[Condition],[CompoundSubsetExpression],[CompoundExpression],[AnalysisSet])

## Children

 * [AnalysisSet](AnalysisSet.md) - A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set based upon the intent-to-treat principle. [ICH E9]
 * [DataSubset](DataSubset.md) - A subset of data identified by selection criteria for inclusion in the analysis.
 * [Group](Group.md) - A subdivision of the subject population or analysis dataset record set based on a defined factor.

## Referenced by Class

 *  **[CompoundSubsetExpression](CompoundSubsetExpression.md)** *[CompoundSubsetExpression➞whereClauses](CompoundSubsetExpression_whereClauses.md)*  <sub>0..\*</sub>  **[WhereClause](WhereClause.md)**
 *  **None** *[whereClauses](whereClauses.md)*  <sub>0..\*</sub>  **[WhereClause](WhereClause.md)**

## Attributes


### Own

 * [level](level.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [order](order.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
 * [compoundExpression](compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundExpression](CompoundExpression.md)
