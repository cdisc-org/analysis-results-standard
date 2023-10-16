```mermaid
erDiagram
ReportingEvent {
    string id  
    integer version  
    string name  
}
Output {
    string id  
    integer version  
    string name  
}
AnalysisOutputProgrammingCode {
    string context  
    string code  
}
AnalysisOutputCodeParameter {
    stringList value  
    string description  
    string name  
}
DocumentReference {

}
PageRef {
    PageRefTypeEnum refType  
    string label  
    stringList pageNames  
    integerList pageNumbers  
    integer firstPage  
    integer lastPage  
}
ReferenceDocument {
    string id  
    uri location  
    string name  
}
AnalysisOutputCategory {
    string id  
    string label  
}
AnalysisOutputCategorization {
    string id  
    string label  
}
OrderedDisplay {
    integer order  
}
OutputDisplay {
    string id  
    integer version  
    string displayTitle  
    string name  
}
DisplaySection {
    DisplaySectionTypeEnum sectionType  
}
OrderedDisplaySubSection {
    integer order  
}
DisplaySubSection {
    string id  
    string text  
}
OutputFile {
    uri location  
    string style  
    string name  
}
ExtensibleTerminologyTerm {
    string controlledTerm  
}
SponsorTerm {
    string id  
    string submissionValue  
    string description  
}
GlobalDisplaySection {
    DisplaySectionTypeEnum sectionType  
}
Analysis {
    string id  
    integer version  
    string description  
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
    ExpressionLogicalOperatorEnum logicalOperator  
}
WhereClauseCondition {
    string dataset  
    string variable  
    ConditionComparatorEnum comparator  
    stringList value  
}
GroupingFactor {
    string id  
    string label  
    string groupingVariable  
    boolean dataDriven  
}
Operation {
    string id  
    string label  
    string resultPattern  
    string name  
}
ReferencedOperationRelationship {
    string id  
    string description  
}
ReferencedAnalysisOperation {

}
AnalysisMethod {
    string id  
    string label  
    string description  
    string name  
}
AnalysisProgrammingCodeTemplate {
    string context  
    string code  
}
TemplateCodeParameter {
    string valueSource  
    stringList value  
    string description  
    string name  
}
OrderedGroupingFactor {
    integer order  
    boolean resultsByGroup  
}
DataSubset {
    string id  
    string label  
    integer level  
    integer order  
}
CompoundSubsetExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
}
WhereClause {
    integer level  
    integer order  
}
WhereClauseCompoundExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
}
AnalysisSet {
    string id  
    string label  
    integer level  
    integer order  
}
CompoundSetExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
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
TerminologyExtension {
    string id  
    ExtensibleTerminologyEnum enumeration  
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
ReportingEvent ||IdentifyingType.IDENTIFYING}o ReferenceDocument : "referenceDocuments"
ReportingEvent ||IdentifyingType.IDENTIFYING}o TerminologyExtension : "terminologyExtensions"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisOutputCategorization : "analysisOutputCategorizations"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisSet : "analysisSets"
ReportingEvent ||IdentifyingType.IDENTIFYING}o SubjectGroupingFactor : "analysisGroupings"
ReportingEvent ||IdentifyingType.IDENTIFYING}o DataSubset : "dataSubsets"
ReportingEvent ||IdentifyingType.IDENTIFYING}o DataGroupingFactor : "dataGroupings"
ReportingEvent ||IdentifyingType.IDENTIFYING}o AnalysisMethod : "methods"
ReportingEvent ||IdentifyingType.IDENTIFYING}o Analysis : "analyses"
ReportingEvent ||IdentifyingType.IDENTIFYING}o GlobalDisplaySection : "globalDisplaySections"
ReportingEvent ||IdentifyingType.IDENTIFYING}o Output : "outputs"
Output ||IdentifyingType.IDENTIFYING}o OutputFile : "fileSpecifications"
Output ||IdentifyingType.IDENTIFYING}o OrderedDisplay : "displays"
Output ||IdentifyingType.IDENTIFYING}o AnalysisOutputCategory : "categoryIds"
Output ||IdentifyingType.IDENTIFYING}o DocumentReference : "documentRefs"
Output ||IdentifyingType.IDENTIFYING|o AnalysisOutputProgrammingCode : "programmingCode"
AnalysisOutputProgrammingCode ||IdentifyingType.IDENTIFYING|o DocumentReference : "documentRef"
AnalysisOutputProgrammingCode ||IdentifyingType.IDENTIFYING}o AnalysisOutputCodeParameter : "parameters"
DocumentReference ||IdentifyingType.IDENTIFYING|| ReferenceDocument : "referenceDocumentId"
DocumentReference ||IdentifyingType.IDENTIFYING}o PageRef : "pageRefs"
AnalysisOutputCategory ||IdentifyingType.IDENTIFYING}o AnalysisOutputCategorization : "subCategorizations"
AnalysisOutputCategorization ||IdentifyingType.IDENTIFYING}| AnalysisOutputCategory : "categories"
OrderedDisplay ||IdentifyingType.IDENTIFYING|o OutputDisplay : "display"
OutputDisplay ||IdentifyingType.IDENTIFYING}o DisplaySection : "displaySections"
DisplaySection ||IdentifyingType.IDENTIFYING}o OrderedDisplaySubSection : "orderedSubSections"
OrderedDisplaySubSection ||IdentifyingType.IDENTIFYING|o DisplaySubSection : "subSection"
OrderedDisplaySubSection ||IdentifyingType.IDENTIFYING|o DisplaySubSection : "subSectionId"
OutputFile ||IdentifyingType.IDENTIFYING|o ExtensibleTerminologyTerm : "fileType"
ExtensibleTerminologyTerm ||IdentifyingType.IDENTIFYING|o SponsorTerm : "sponsorTermId"
GlobalDisplaySection ||IdentifyingType.IDENTIFYING}o DisplaySubSection : "subSections"
Analysis ||IdentifyingType.IDENTIFYING|| ExtensibleTerminologyTerm : "reason"
Analysis ||IdentifyingType.IDENTIFYING|| ExtensibleTerminologyTerm : "purpose"
Analysis ||IdentifyingType.IDENTIFYING}o DocumentReference : "documentRefs"
Analysis ||IdentifyingType.IDENTIFYING}o AnalysisOutputCategory : "categoryIds"
Analysis ||IdentifyingType.IDENTIFYING|o AnalysisSet : "analysisSetId"
Analysis ||IdentifyingType.IDENTIFYING|o DataSubset : "dataSubsetId"
Analysis ||IdentifyingType.IDENTIFYING}o OrderedGroupingFactor : "orderedGroupings"
Analysis ||IdentifyingType.IDENTIFYING|| AnalysisMethod : "methodId"
Analysis ||IdentifyingType.IDENTIFYING}o ReferencedAnalysisOperation : "referencedAnalysisOperations"
Analysis ||IdentifyingType.IDENTIFYING|o AnalysisOutputProgrammingCode : "programmingCode"
Analysis ||IdentifyingType.IDENTIFYING}o OperationResult : "results"
OperationResult ||IdentifyingType.IDENTIFYING|| Operation : "operationId"
OperationResult ||IdentifyingType.IDENTIFYING}o ResultGroup : "resultGroups"
ResultGroup ||IdentifyingType.IDENTIFYING|o GroupingFactor : "groupingId"
ResultGroup ||IdentifyingType.IDENTIFYING|o Group : "groupId"
Group ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
Group ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
CompoundGroupExpression ||IdentifyingType.IDENTIFYING}o Group : "whereClauses"
GroupingFactor ||IdentifyingType.IDENTIFYING}o Group : "groups"
Operation ||IdentifyingType.IDENTIFYING}o ReferencedOperationRelationship : "referencedOperationRelationships"
ReferencedOperationRelationship ||IdentifyingType.IDENTIFYING|| ExtensibleTerminologyTerm : "referencedOperationRole"
ReferencedOperationRelationship ||IdentifyingType.IDENTIFYING|| Operation : "operationId"
ReferencedOperationRelationship ||IdentifyingType.IDENTIFYING|o Analysis : "analysisId"
ReferencedAnalysisOperation ||IdentifyingType.IDENTIFYING|| ReferencedOperationRelationship : "referencedOperationRelationshipId"
ReferencedAnalysisOperation ||IdentifyingType.IDENTIFYING|| Analysis : "analysisId"
AnalysisMethod ||IdentifyingType.IDENTIFYING}o DocumentReference : "documentRefs"
AnalysisMethod ||IdentifyingType.IDENTIFYING}| Operation : "operations"
AnalysisMethod ||IdentifyingType.IDENTIFYING|o AnalysisProgrammingCodeTemplate : "codeTemplate"
AnalysisProgrammingCodeTemplate ||IdentifyingType.IDENTIFYING|o DocumentReference : "documentRef"
AnalysisProgrammingCodeTemplate ||IdentifyingType.IDENTIFYING}o TemplateCodeParameter : "parameters"
OrderedGroupingFactor ||IdentifyingType.IDENTIFYING|o GroupingFactor : "groupingId"
DataSubset ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
DataSubset ||IdentifyingType.IDENTIFYING|o CompoundSubsetExpression : "compoundExpression"
CompoundSubsetExpression ||IdentifyingType.IDENTIFYING}o WhereClause : "whereClauses"
WhereClause ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
WhereClause ||IdentifyingType.IDENTIFYING|o WhereClauseCompoundExpression : "compoundExpression"
WhereClauseCompoundExpression ||IdentifyingType.IDENTIFYING}o WhereClause : "whereClauses"
AnalysisSet ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
AnalysisSet ||IdentifyingType.IDENTIFYING|o CompoundSetExpression : "compoundExpression"
CompoundSetExpression ||IdentifyingType.IDENTIFYING}o AnalysisSet : "whereClauses"
DataGroupingFactor ||IdentifyingType.IDENTIFYING}o DataGroup : "groups"
DataGroup ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
DataGroup ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
SubjectGroupingFactor ||IdentifyingType.IDENTIFYING}o AnalysisGroup : "groups"
AnalysisGroup ||IdentifyingType.IDENTIFYING|o WhereClauseCondition : "condition"
AnalysisGroup ||IdentifyingType.IDENTIFYING|o CompoundGroupExpression : "compoundExpression"
TerminologyExtension ||IdentifyingType.IDENTIFYING}| SponsorTerm : "sponsorTerms"
NestedList ||IdentifyingType.IDENTIFYING}o OrderedListItem : "listItems"
OrderedListItem ||IdentifyingType.IDENTIFYING|o Analysis : "analysisId"
OrderedListItem ||IdentifyingType.IDENTIFYING|o Output : "outputId"
OrderedListItem ||IdentifyingType.IDENTIFYING|o NestedList : "sublist"

```

