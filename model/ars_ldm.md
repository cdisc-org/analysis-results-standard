```mermaid
erDiagram
ReportingEvent {
    string name  
}
Output {
    string id  
    integer version  
}
AnalysisCategory {
    string id  
    string label  
}
AnalysisCategorization {
    string id  
    string label  
}
OutputDisplay {
    integer order  
}
Display {
    string id  
    integer version  
    string displayTitle  
    string name  
}
DisplaySection {
    SectionType sectionType  
}
DisplaySubSection {
    string id  
    integer order  
    string text  
}
File {
    FileType fileType  
    string location  
    string style  
    string name  
}
AnalysisMethod {
    string id  
    string label  
    string description  
    string name  
}
Operation {
    string id  
    string label  
    string resultPattern  
    string name  
}
ReferencedOperationRelationship {
    string id  
    OperationRole referencedOperationRole  
    string description  
}
Analysis {
    string id  
    integer version  
    string dataset  
    string variable  
    string name  
}
OperationResult {
    string rawValue  
    string formattedValue  
}
ResultGroup {
    string groupValue  
}
Group {
    string id  
    string label  
    integer level  
    integer order  
}
CompoundGroupExpression {
    LogicalOperator logicalOperator  
}
Condition {
    string dataset  
    string variable  
    Comparator comparator  
    stringList value  
}
GroupingFactor {
    string id  
    string label  
    string groupingVariable  
    boolean dataDriven  
}
ReferencedAnalysisOperation {

}
DataSubset {
    string id  
    string label  
    integer level  
    integer order  
}
CompoundSubsetExpression {
    LogicalOperator logicalOperator  
}
WhereClause {
    integer level  
    integer order  
}
CompoundExpression {
    LogicalOperator logicalOperator  
}
OrderedGroupingFactor {
    integer order  
    boolean resultsByGroup  
}
DataGroupingFactor {
    string id  
    string label  
    string groupingVariable  
    boolean dataDriven  
}
DataGroup {
    string id  
    string label  
    integer level  
    integer order  
}
AnalysisSet {
    string id  
    string label  
    integer level  
    integer order  
}
CompoundSetExpression {
    LogicalOperator logicalOperator  
}
SubjectGroupingFactor {
    string id  
    string label  
    string groupingVariable  
    boolean dataDriven  
}
AnalysisGroup {
    string id  
    string label  
    integer level  
    integer order  
}
NestedList {

}
OrderedListItem {
    integer level  
    integer order  
    string name  
}

ReportingEvent ||IdentifyingType.IDENTIFYING|| NestedList : "listOfPlannedAnalyses"
ReportingEvent ||IdentifyingType.IDENTIFYING|o NestedList : "listOfPlannedOutputs"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisSet : "analysisSets"
ReportingEvent ||IdentifyingType.IDENTIFYING}o SubjectGroupingFactor : "analysisGroupings"
ReportingEvent ||IdentifyingType.IDENTIFYING}o DataSubset : "dataSubsets"
ReportingEvent ||IdentifyingType.IDENTIFYING}o DataGroupingFactor : "dataGroupings"
ReportingEvent ||IdentifyingType.IDENTIFYING}o DisplaySection : "globalDisplaySections"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisCategorization : "analysisCategorizations"
ReportingEvent ||IdentifyingType.IDENTIFYING}o Analysis : "analyses"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisMethod : "methods"
ReportingEvent ||IdentifyingType.IDENTIFYING}o Output : "outputs"
Output ||IdentifyingType.IDENTIFYING}o File : "fileSpecifications"
Output ||IdentifyingType.IDENTIFYING}o OutputDisplay : "outputDisplays"
Output ||IdentifyingType.IDENTIFYING}o AnalysisCategory : "categoryIds"
AnalysisCategory ||IdentifyingType.IDENTIFYING}o AnalysisCategorization : "subCategorizations"
AnalysisCategorization ||IdentifyingType.IDENTIFYING}| AnalysisCategory : "categories"
OutputDisplay ||IdentifyingType.IDENTIFYING|o Display : "display"
Display ||IdentifyingType.IDENTIFYING}o DisplaySection : "displaySections"
DisplaySection ||IdentifyingType.IDENTIFYING}o DisplaySubSection : "subSections"
AnalysisMethod ||IdentifyingType.IDENTIFYING}| Operation : "operations"
Operation ||IdentifyingType.IDENTIFYING}o ReferencedOperationRelationship : "referencedOperationRelationships"
ReferencedOperationRelationship ||IdentifyingType.IDENTIFYING|| Operation : "operationId"
ReferencedOperationRelationship ||IdentifyingType.IDENTIFYING|o Analysis : "analysisId"
Analysis ||IdentifyingType.IDENTIFYING}o AnalysisCategory : "categoryIds"
Analysis ||IdentifyingType.IDENTIFYING|o AnalysisSet : "analysisSetId"
Analysis ||IdentifyingType.IDENTIFYING}o OrderedGroupingFactor : "orderedGroupings"
Analysis ||IdentifyingType.IDENTIFYING|o DataSubset : "dataSubsetId"
Analysis ||IdentifyingType.IDENTIFYING|| AnalysisMethod : "methodId"
Analysis ||IdentifyingType.IDENTIFYING}o ReferencedAnalysisOperation : "referencedAnalysisOperations"
Analysis ||IdentifyingType.IDENTIFYING}o OperationResult : "results"
OperationResult ||IdentifyingType.IDENTIFYING|| Operation : "operationId"
OperationResult ||IdentifyingType.IDENTIFYING}o ResultGroup : "resultGroups"
ResultGroup ||IdentifyingType.IDENTIFYING|o GroupingFactor : "groupingId"
ResultGroup ||IdentifyingType.IDENTIFYING|o Group : "groupId"
Group ||IdentifyingType.IDENTIFYING|o Condition : "condition"
Group ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
CompoundGroupExpression ||IdentifyingType.IDENTIFYING}o Group : "whereClauses"
GroupingFactor ||IdentifyingType.IDENTIFYING}o Group : "groups"
ReferencedAnalysisOperation ||IdentifyingType.IDENTIFYING|o ReferencedOperationRelationship : "referencedOperationId"
ReferencedAnalysisOperation ||IdentifyingType.IDENTIFYING|| Analysis : "analysisId"
DataSubset ||IdentifyingType.IDENTIFYING|o Condition : "condition"
DataSubset ||IdentifyingType.IDENTIFYING|o CompoundSubsetExpression : "compoundExpression"
CompoundSubsetExpression ||IdentifyingType.IDENTIFYING}o WhereClause : "whereClauses"
WhereClause ||IdentifyingType.IDENTIFYING|o Condition : "condition"
WhereClause ||IdentifyingType.IDENTIFYING|o CompoundExpression : "compoundExpression"
CompoundExpression ||IdentifyingType.IDENTIFYING}o WhereClause : "whereClauses"
OrderedGroupingFactor ||IdentifyingType.IDENTIFYING|o GroupingFactor : "groupingId"
OrderedGroupingFactor ||IdentifyingType.IDENTIFYING|o DataGroupingFactor : "dataGrouping"
DataGroupingFactor ||IdentifyingType.IDENTIFYING}o DataGroup : "groups"
DataGroup ||IdentifyingType.IDENTIFYING|o Condition : "condition"
DataGroup ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
AnalysisSet ||IdentifyingType.IDENTIFYING|o Condition : "condition"
AnalysisSet ||IdentifyingType.IDENTIFYING|o CompoundSetExpression : "compoundExpression"
CompoundSetExpression ||IdentifyingType.IDENTIFYING}o AnalysisSet : "whereClauses"
SubjectGroupingFactor ||IdentifyingType.IDENTIFYING}o AnalysisGroup : "groups"
AnalysisGroup ||IdentifyingType.IDENTIFYING|o Condition : "condition"
AnalysisGroup ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
NestedList ||IdentifyingType.IDENTIFYING}o OrderedListItem : "listItems"
OrderedListItem ||IdentifyingType.IDENTIFYING|o NestedList : "sublist"
OrderedListItem ||IdentifyingType.IDENTIFYING|o Analysis : "analysisId"
OrderedListItem ||IdentifyingType.IDENTIFYING|o Output : "outputId"

```

