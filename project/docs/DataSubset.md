
# Class: DataSubset


A subset of data identified by selection criteria for inclusion in the analysis.

URI: [https://www.cdisc.org/ars/1-0/DataSubset](https://www.cdisc.org/ars/1-0/DataSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression]<compoundExpression%200..1-++[DataSubset&#124;id:string;label:string%20%3F;level(i):integer%20%3F;order(i):integer%20%3F],[Analysis]-%20dataSubsetId%200..1>[DataSubset],[ReportingEvent]++-%20dataSubsets%200..*>[DataSubset],[WhereClause]^-[DataSubset],[ReportingEvent],[Condition],[CompoundSubsetExpression],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[WhereClause],[CompoundSubsetExpression]<compoundExpression%200..1-++[DataSubset&#124;id:string;label:string%20%3F;level(i):integer%20%3F;order(i):integer%20%3F],[Analysis]-%20dataSubsetId%200..1>[DataSubset],[ReportingEvent]++-%20dataSubsets%200..*>[DataSubset],[WhereClause]^-[DataSubset],[ReportingEvent],[Condition],[CompoundSubsetExpression],[Analysis])

## Parents

 *  is_a: [WhereClause](WhereClause.md)

## Referenced by Class

 *  **None** *[dataSubsetId](dataSubsetId.md)*  <sub>0..1</sub>  **[DataSubset](DataSubset.md)**
 *  **None** *[dataSubsets](dataSubsets.md)*  <sub>0..\*</sub>  **[DataSubset](DataSubset.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [DataSubset➞compoundExpression](DataSubset_compoundExpression.md)  <sub>0..1</sub>
     * Range: [CompoundSubsetExpression](CompoundSubsetExpression.md)

### Inherited from WhereClause:

 * [level](level.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [order](order.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [condition](condition.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
