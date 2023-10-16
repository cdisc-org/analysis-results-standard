# Analysis Results Standard (ARS)

DRAFT Logical model to support both the prospective specification of analyses and the fully contextualized representation of the results of the analyses.


URI: https://www.cdisc.org/ars/1-0
Name: ars_ldm



## Schema Diagram
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


## Classes
_Classes provide templates for organizing data. Data objects instantiate classes in the schema. Each class has a set of slots (aka fields, attributes) that are applicable to it. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#classes) for more information._

| Class | Description |
| --- | --- |
| [NamedObject](NamedObject.md) | An object with a name |
| [ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |
| [NestedList](NestedList.md) | A list of items (analyses or outputs) that may be organized within sub-lists |
| [OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |
| [ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |
| [TerminologyExtension](TerminologyExtension.md) | An extensible set of controlled terminology that has been extended with at le... |
| [SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |
| [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The term used for an attribute whose terminology is extensible |
| [AnalysisOutputCategorization](AnalysisOutputCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |
| [AnalysisOutputCategory](AnalysisOutputCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |
| [WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |
| [WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] |
| [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | A compound expression consisting of either two or more where clauses combined... |
| [AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |
| [CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more identified analysis se... |
| [DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |
| [CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more where clauses combined... |
| [GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |
| [Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |
| [CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more identified group combi... |
| [SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |
| [AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |
| [DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |
| [DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |
| [AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |
| [DocumentReference](DocumentReference.md) | A reference to an external document |
| [PageRef](PageRef.md) | A reference to a specific part of a document as indicated by a list of one or... |
| [PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |
| [PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |
| [PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |
| [Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |
| [OperationRole](OperationRole.md) | The role that the referenced operation's result plays in the calculation of t... |
| [SponsorOperationRole](SponsorOperationRole.md) | The sponsor-defined role that the referenced operation's result plays in the ... |
| [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Programming statements and/or a reference to a used as a template for creatio... |
| [CodeParameter](CodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |
| [AnalysisReason](AnalysisReason.md) | The rationale for performing this analysis |
| [SponsorAnalysisReason](SponsorAnalysisReason.md) | The sponsor-defined rationale for performing this analysis |
| [AnalysisPurpose](AnalysisPurpose.md) | The purpose of the analysis within the body of evidence (e |
| [SponsorAnalysisPurpose](SponsorAnalysisPurpose.md) | The sponsor-defined purpose of the analysis within the body of evidence (e |
| [OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | An indication of the analysis that contains results of a referenced operation |
| [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform a sp... |
| [AnalysisOutputCodeParameter](AnalysisOutputCodeParameter.md) | A parameter whose value is used in programming code for a specific analysis o... |
| [OperationResult](OperationResult.md) | The result of an analysis method operation performed on a subdivision of subj... |
| [ResultGroup](ResultGroup.md) | For the specified grouping factor, an indication of the specific group of sub... |
| [GlobalDisplaySection](GlobalDisplaySection.md) | A global definition for part of a tabular display containing one or more piec... |
| [DisplaySubSection](DisplaySubSection.md) | An occurrence of a display section containing text |
| [Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |
| [OutputFile](OutputFile.md) | A file containing analysis output displays |
| [OutputFileType](OutputFileType.md) | The file format of the file containing output from analyses |
| [SponsorOutputFileType](SponsorOutputFileType.md) | The sponsor-defined file format of the file containing output from analyses |
| [OrderedDisplay](OrderedDisplay.md) | A display ordered with respect to other displays in an analysis output |
| [OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |
| [DisplaySection](DisplaySection.md) | A part of a tabular display containing one or more pieces of informational te... |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | A single subsection ordered with respect to other subsections in the same sec... |
| [OrderedSubSection](OrderedSubSection.md) | A subsection ordered with respect to other subsections of the same type |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | A reference to a subsection defined either globally or in another display sec... |


## Slots
_Slots (aka attributes, fields, columns, properties) can be associated with classes to specify what fields instances of that class can have. Slots operate the same way as “fields” in traditional object languages and the same ways as “columns” in spreadsheets and relational databases. See LinkML documentation [here](https://linkml.io/linkml/schemas/models.html#slots) and [here](https://linkml.io/linkml/schemas/slots.html) for more information._
 
| Slot | Description |
| --- | --- |
| [name](name.md) | The name for the instance of the class |
| [id](id.md) | The assigned identifying value for the instance of the class |
| [version](version.md) | An ordinal indicating the version of the identified instance of the class |
| [listOfPlannedAnalyses](listOfPlannedAnalyses.md) | A structured list of the analyses defined for the reporting event |
| [listOfPlannedOutputs](listOfPlannedOutputs.md) | An optional structured list of the outputs defined for the reporting event |
| [referenceDocuments](referenceDocuments.md) | External documents containing information referenced for the reporting event |
| [terminologyExtensions](terminologyExtensions.md) | Any sponsor-defined extensions to extensible terminology |
| [analysisOutputCategorizations](analysisOutputCategorizations.md) | Sets of related implementer-defined categories that can be used to categorize... |
| [analysisSets](analysisSets.md) | The analysis sets (subject populations) defined for the reporting event |
| [analysisGroupings](analysisGroupings.md) | Characteristics used to subdivide the subject population (e |
| [dataSubsets](dataSubsets.md) | Subsets of data identified by selection criteria for inclusion in analysis de... |
| [dataGroupings](dataGroupings.md) | Characteristics used to subdivide data records in analysis datasets (e |
| [methods](methods.md) | The defined methods used to analyze any analysis variable |
| [analyses](analyses.md) | The analyses defined for the reporting event |
| [globalDisplaySections](globalDisplaySections.md) | Display section specifications that may be applied to any display |
| [outputs](outputs.md) | The outputs defined for the reporting event |
| [listItems](listItems.md) | Items in the list |
| [level](level.md) | The level of the entry within a hierarchical structure |
| [order](order.md) | The ordinal of the instance with respect to other instances |
| [sublist](sublist.md) | A sub-list of items (analyses or outputs) that may be further organized withi... |
| [analysisId](analysisId.md) | The identifier of the referenced analysis |
| [outputId](outputId.md) | The identifier of the referenced output |
| [location](location.md) | A path (relative or absolute) indicating the location of the file |
| [enumeration](enumeration.md) | The name of the extensible enumeration |
| [sponsorTerms](sponsorTerms.md) | The sponsor-defined terms added to the extensible terminology |
| [submissionValue](submissionValue.md) | The specific value expected for submissions |
| [description](description.md) | A textual description of the instance of the class |
| [controlledTerm](controlledTerm.md) | One of the permissible values from the referenced enumeration |
| [sponsorTermId](sponsorTermId.md) | The identifier of the referenced sponsor term |
| [label](label.md) | A short informative description that may be used for display |
| [categories](categories.md) | Implementer-defined categories of analyses/outputs, each of which may include... |
| [subCategorizations](subCategorizations.md) | Sets of related implementer-defined sub-categories that can be used to catego... |
| [condition](condition.md) | A simple selection criterion exressed as [dataset] |
| [compoundExpression](compoundExpression.md) | A compound expression that combines or negates where clauses |
| [dataset](dataset.md) | The name of the analysis dataset |
| [variable](variable.md) | The name of the variable |
| [comparator](comparator.md) | Comparison operator indicating how the variable is compared to the value(s) |
| [value](value.md) | The prespecified value or values |
| [logicalOperator](logicalOperator.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... |
| [whereClauses](whereClauses.md) | A list of one or more where clauses (selection criteria) to be combined or ne... |
| [groupingVariable](groupingVariable.md) | For groupings based on a single variable, a reference to the dataset variable... |
| [dataDriven](dataDriven.md) | Indicates whether the groups defined by the grouping are prespecified (false)... |
| [groups](groups.md) | The pre-specified groups within the grouping |
| [documentRefs](documentRefs.md) | References to external documents containing additional information |
| [operations](operations.md) | The calculations performed for the method |
| [codeTemplate](codeTemplate.md) | Template programming statements used to perform the statistical operations fo... |
| [referenceDocumentId](referenceDocumentId.md) | The identifier of the referenced document |
| [pageRefs](pageRefs.md) | A list of references to specific parts of a document, which may be referenced... |
| [refType](refType.md) | The type of reference for page references |
| [pageNames](pageNames.md) | One or more named document references which each correspond with a page |
| [pageNumbers](pageNumbers.md) | One or more page numbers |
| [firstPage](firstPage.md) | The page number of the first page in a range of pages |
| [lastPage](lastPage.md) | The page number of the last page in a range of pages |
| [referencedOperationRelationships](referencedOperationRelationships.md) | Relationships to other operations indicating how the result of the referenced... |
| [resultPattern](resultPattern.md) | The default pattern or format to apply to the result for display |
| [referencedOperationRole](referencedOperationRole.md) | The role that the referenced operation's result plays in the calculation of t... |
| [operationId](operationId.md) | The identifier of the referenced operation |
| [context](context.md) | The name and version of the computer language used for the actual programming... |
| [code](code.md) | Programming statements used to perform the specific analysis |
| [documentRef](documentRef.md) | A reference to the document containing programming code |
| [parameters](parameters.md) | Replacement parameters that are referenced in the programming code or program... |
| [valueSource](valueSource.md) | A reference to the prespecified source of the value for the parameter |
| [reason](reason.md) | The rationale for performing this analysis |
| [purpose](purpose.md) | The purpose of the analysis within the body of evidence (e |
| [categoryIds](categoryIds.md) | References to any implementer-defined categories that apply to the analysis o... |
| [analysisSetId](analysisSetId.md) | The identifier of the referenced analysis set |
| [dataSubsetId](dataSubsetId.md) | The identifier of the referenced data subset |
| [orderedGroupings](orderedGroupings.md) | An ordered list of grouping factors used in the analysis |
| [methodId](methodId.md) | A reference to the set of one or more statistical operations performed for th... |
| [referencedAnalysisOperations](referencedAnalysisOperations.md) | Indications of which analysis contains the results for each referenced operat... |
| [programmingCode](programmingCode.md) | Programming statements used to perform the specific analysis or create the sp... |
| [results](results.md) | The results of the analysis |
| [groupingId](groupingId.md) | The identifier of the referenced subject or data grouping factor |
| [resultsByGroup](resultsByGroup.md) | Indicates whether a result is expected for each group in the grouping |
| [referencedOperationRelationshipId](referencedOperationRelationshipId.md) | The identifier of the defined referenced operation relationship |
| [resultGroups](resultGroups.md) | The group values associated with the result |
| [rawValue](rawValue.md) | The raw result value (e |
| [formattedValue](formattedValue.md) | The result value formatted for display according to the resultPattern |
| [groupId](groupId.md) | The identifier of a referenced predefined group within a grouping |
| [groupValue](groupValue.md) | The data value used as a group within a data-driven grouping |
| [sectionType](sectionType.md) | The type of display section that contains one or more pieces of informational... |
| [subSections](subSections.md) | A list of defined pieces of information text that may be displayed in display... |
| [text](text.md) | The text to be displayed in the display section |
| [fileSpecifications](fileSpecifications.md) | Specifications of output files |
| [displays](displays.md) | An ordered list of the displays included in the output |
| [fileType](fileType.md) | The format of the output file |
| [style](style.md) | Reference to the specification of the style used for the output |
| [display](display.md) | A display contained in the output |
| [displayTitle](displayTitle.md) | Display description which uniquely identifies the display in the report |
| [displaySections](displaySections.md) | The parts of the display containing one or more pieces of informational text ... |
| [orderedSubSections](orderedSubSections.md) | An ordered list of the informational text to display in the display section |
| [subSection](subSection.md) | A defined piece of information text to display in a display section |
| [subSectionId](subSectionId.md) | The identifier of the referenced subsection |


## Enumerations
_Enumerations are common features in modeling frameworks. These can be thought of as a “drop-down” of permissible values for a field/slot. See [LinkML documentation](https://linkml.io/linkml/schemas/enums.html) for more information._

| Enumeration | Description |
| --- | --- |
| [OutputFileTypeEnum](OutputFileTypeEnum.md) | The file format of the file containing output from analyses |
| [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) | Boolean operators denoting a logical operation (e |
| [ConditionComparatorEnum](ConditionComparatorEnum.md) | Comparison operators indicating how the value of a variable is compared to a ... |
| [DisplaySectionTypeEnum](DisplaySectionTypeEnum.md) | Types of display section that contain one or more pieces of informational tex... |
| [OperationRoleEnum](OperationRoleEnum.md) | The role that the referenced operation's result plays in the calculation of t... |
| [AnalysisReasonEnum](AnalysisReasonEnum.md) | The rationale for performing this analysis |
| [AnalysisPurposeEnum](AnalysisPurposeEnum.md) | The purpose of the analysis within the body of evidence (e |
| [ExtensibleTerminologyEnum](ExtensibleTerminologyEnum.md) | Extensible ARS enumerations |
| [PageRefTypeEnum](PageRefTypeEnum.md) | Type of reference for page references |


## Types
_Types in LinkML are scalar data values such as strings, integers, floats, and so on. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#types) for more information._

| Type | Description |
| --- | --- |
| [String](String.md) | A character string |
| [Integer](Integer.md) | An integer |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [Datetime](Datetime.md) | The combination of a date and time |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |
| [Curie](Curie.md) | a compact URI |
| [Uri](Uri.md) | a complete URI |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |


## Subsets
_Elements of a schema can be partitioned into named subsets. These have no semantic meaning, but they can be useful for tagging parts of a schema for different purposes. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#subsets) for more information._

| Subset | Description |
| --- | --- |
