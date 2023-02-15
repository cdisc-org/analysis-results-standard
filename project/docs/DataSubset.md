
# Class: DataSubset


A subset of data identified by selection criteria for inclusion in the analysis.

URI: [https://www.cdisc.org/ars/1-0/DataSubset](https://www.cdisc.org/ars/1-0/DataSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression]<compoundExpression%200..1-++[DataSubset&#124;label:string%20%3F;id(i):string],[ReportingEvent]++-%20dataSubsets%200..*>[DataSubset],[WhereClause]^-[DataSubset],[ReportingEvent],[Condition],[CompoundSubsetExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression]<compoundExpression%200..1-++[DataSubset&#124;label:string%20%3F;id(i):string],[ReportingEvent]++-%20dataSubsets%200..*>[DataSubset],[WhereClause]^-[DataSubset],[ReportingEvent],[Condition],[CompoundSubsetExpression])

## Parents

 *  is_a: [WhereClause](WhereClause.md)

## Referenced by Class

 *  **None** *[dataSubsets](dataSubsets.md)*  <sub>0..\*</sub>  **[DataSubset](DataSubset.md)**

## Attributes


### Own

 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [DataSubset➞compoundExpression](DataSubset_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundSubsetExpression](CompoundSubsetExpression.md)

### Inherited from WhereClause:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
