
# Class: AnalysisSet


A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set based upon the intent-to-treat principle. [ICH E9]

URI: [https://www.cdisc.org/ars/1-0/AnalysisSet](https://www.cdisc.org/ars/1-0/AnalysisSet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[Condition],[CompoundSetExpression],[CompoundSetExpression]<compoundExpression%200..1-++[AnalysisSet&#124;label:string%20%3F;order:integer;id(i):string],[CompoundSetExpression]-%20whereClauses%200..*>[AnalysisSet],[Analysis]-%20analysisSet%200..1>[AnalysisSet],[ReportingEvent]++-%20analysisSets%200..*>[AnalysisSet],[WhereClause]^-[AnalysisSet],[ReportingEvent],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[Condition],[CompoundSetExpression],[CompoundSetExpression]<compoundExpression%200..1-++[AnalysisSet&#124;label:string%20%3F;order:integer;id(i):string],[CompoundSetExpression]-%20whereClauses%200..*>[AnalysisSet],[Analysis]-%20analysisSet%200..1>[AnalysisSet],[ReportingEvent]++-%20analysisSets%200..*>[AnalysisSet],[WhereClause]^-[AnalysisSet],[ReportingEvent],[Analysis])

## Parents

 *  is_a: [WhereClause](WhereClause.md)

## Referenced by Class

 *  **[CompoundSetExpression](CompoundSetExpression.md)** *[CompoundSetExpression➞whereClauses](CompoundSetExpression_whereClauses.md)*  <sub>0..\*</sub>  **[AnalysisSet](AnalysisSet.md)**
 *  **None** *[analysisSet](analysisSet.md)*  <sub>0..1</sub>  **[AnalysisSet](AnalysisSet.md)**
 *  **None** *[analysisSets](analysisSets.md)*  <sub>0..\*</sub>  **[AnalysisSet](AnalysisSet.md)**

## Attributes


### Own

 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [order](order.md)  <sub>1..1</sub>
     * Range: [Integer](types/Integer.md)
 * [AnalysisSet➞compoundExpression](AnalysisSet_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundSetExpression](CompoundSetExpression.md)

### Inherited from WhereClause:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
