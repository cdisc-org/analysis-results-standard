# Analysis Results Standard (ARS)

Logical model to support both the prospective specification of analyses and the fully contextualized representation of the results of the analyses.


URI: https://www.cdisc.org/ars/1-0
Name: ars_ldm



## Schema Diagram
```mermaid 
erDiagram
ReportingEvent {
    string id  
    integer version  
    string name  
    string description  
    string label  
}
Output {
    string id  
    integer version  
    string name  
    string description  
    string label  
}
AnalysisOutputProgrammingCode {
    string context  
    string code  
}
AnalysisOutputCodeParameter {
    stringList value  
    string name  
    string description  
    string label  
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
    string description  
    string label  
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
    string description  
    string label  
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
    string description  
    string label  
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
    string dataset  
    string variable  
    string name  
    string description  
    string label  
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
    string name  
    string description  
    string label  
    integer level  
    integer order  
}
CompoundGroupExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
}
SubClause {
    integer level  
    integer order  
    string subClauseId  
}
WhereClauseCompoundExpression {
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
    string groupingDataset  
    string groupingVariable  
    boolean dataDriven  
    string name  
    string description  
    string label  
}
Operation {
    string id  
    integer order  
    string resultPattern  
    string name  
    string description  
    string label  
}
ReferencedOperationRelationship {
    string id  
    string description  
}
ReferencedAnalysisOperation {

}
AnalysisMethod {
    string id  
    string name  
    string description  
    string label  
}
AnalysisProgrammingCodeTemplate {
    string context  
    string code  
}
TemplateCodeParameter {
    string valueSource  
    stringList value  
    string name  
    string description  
    string label  
}
OrderedGroupingFactor {
    integer order  
    boolean resultsByGroup  
}
DataSubset {
    string id  
    string name  
    string description  
    string label  
    integer level  
    integer order  
}
CompoundSubsetExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
}
AnalysisSet {
    string id  
    string name  
    string description  
    string label  
    integer level  
    integer order  
}
CompoundSetExpression {
    ExpressionLogicalOperatorEnum logicalOperator  
}
TerminologyExtension {
    string id  
    ExtensibleTerminologyEnum enumeration  
}
ListOfContents {
    string name  
    string description  
    string label  
}
NestedList {

}
OrderedListItem {
    integer level  
    integer order  
    string name  
    string description  
    string label  
}

ReportingEvent ||--|| ListOfContents : "mainListOfContents"
ReportingEvent ||--}o ListOfContents : "otherListsOfContents"
ReportingEvent ||--}o ReferenceDocument : "referenceDocuments"
ReportingEvent ||--}o TerminologyExtension : "terminologyExtensions"
ReportingEvent ||--}o AnalysisOutputCategorization : "analysisOutputCategorizations"
ReportingEvent ||--}o AnalysisSet : "analysisSets"
ReportingEvent ||--}o DataSubset : "dataSubsets"
ReportingEvent ||--}o GroupingFactor : "analysisGroupings"
ReportingEvent ||--}o AnalysisMethod : "methods"
ReportingEvent ||--}o Analysis : "analyses"
ReportingEvent ||--}o GlobalDisplaySection : "globalDisplaySections"
ReportingEvent ||--}o Output : "outputs"
Output ||--}o OutputFile : "fileSpecifications"
Output ||--}| OrderedDisplay : "displays"
Output ||--}o AnalysisOutputCategory : "categoryIds"
Output ||--}o DocumentReference : "documentRefs"
Output ||--|o AnalysisOutputProgrammingCode : "programmingCode"
AnalysisOutputProgrammingCode ||--|o DocumentReference : "documentRef"
AnalysisOutputProgrammingCode ||--}o AnalysisOutputCodeParameter : "parameters"
DocumentReference ||--|| ReferenceDocument : "referenceDocumentId"
DocumentReference ||--}o PageRef : "pageRefs"
AnalysisOutputCategory ||--}o AnalysisOutputCategorization : "subCategorizations"
AnalysisOutputCategorization ||--}| AnalysisOutputCategory : "categories"
OrderedDisplay ||--|| OutputDisplay : "display"
OutputDisplay ||--}o DisplaySection : "displaySections"
DisplaySection ||--}o OrderedDisplaySubSection : "orderedSubSections"
OrderedDisplaySubSection ||--|o DisplaySubSection : "subSection"
OrderedDisplaySubSection ||--|o DisplaySubSection : "subSectionId"
OutputFile ||--|o ExtensibleTerminologyTerm : "fileType"
ExtensibleTerminologyTerm ||--|o SponsorTerm : "sponsorTermId"
GlobalDisplaySection ||--}o DisplaySubSection : "subSections"
Analysis ||--|| ExtensibleTerminologyTerm : "reason"
Analysis ||--|| ExtensibleTerminologyTerm : "purpose"
Analysis ||--}o DocumentReference : "documentRefs"
Analysis ||--}o AnalysisOutputCategory : "categoryIds"
Analysis ||--|o AnalysisSet : "analysisSetId"
Analysis ||--|o DataSubset : "dataSubsetId"
Analysis ||--}o OrderedGroupingFactor : "orderedGroupings"
Analysis ||--|| AnalysisMethod : "methodId"
Analysis ||--}o ReferencedAnalysisOperation : "referencedAnalysisOperations"
Analysis ||--|o AnalysisOutputProgrammingCode : "programmingCode"
Analysis ||--}o OperationResult : "results"
OperationResult ||--|| Operation : "operationId"
OperationResult ||--}o ResultGroup : "resultGroups"
ResultGroup ||--|| GroupingFactor : "groupingId"
ResultGroup ||--|o Group : "groupId"
Group ||--|o WhereClauseCondition : "condition"
Group ||--|o CompoundGroupExpression : "compoundExpression"
CompoundGroupExpression ||--}o SubClause : "whereClauses"
SubClause ||--|o WhereClauseCondition : "condition"
SubClause ||--|o WhereClauseCompoundExpression : "compoundExpression"
WhereClauseCompoundExpression ||--}o SubClause : "whereClauses"
GroupingFactor ||--}o Group : "groups"
Operation ||--}o ReferencedOperationRelationship : "referencedOperationRelationships"
ReferencedOperationRelationship ||--|| ExtensibleTerminologyTerm : "referencedOperationRole"
ReferencedOperationRelationship ||--|| Operation : "operationId"
ReferencedOperationRelationship ||--|o Analysis : "analysisId"
ReferencedAnalysisOperation ||--|| ReferencedOperationRelationship : "referencedOperationRelationshipId"
ReferencedAnalysisOperation ||--|| Analysis : "analysisId"
AnalysisMethod ||--}o DocumentReference : "documentRefs"
AnalysisMethod ||--}| Operation : "operations"
AnalysisMethod ||--|o AnalysisProgrammingCodeTemplate : "codeTemplate"
AnalysisProgrammingCodeTemplate ||--|o DocumentReference : "documentRef"
AnalysisProgrammingCodeTemplate ||--}o TemplateCodeParameter : "parameters"
OrderedGroupingFactor ||--|| GroupingFactor : "groupingId"
DataSubset ||--|o WhereClauseCondition : "condition"
DataSubset ||--|o CompoundSubsetExpression : "compoundExpression"
CompoundSubsetExpression ||--}o SubClause : "whereClauses"
AnalysisSet ||--|o WhereClauseCondition : "condition"
AnalysisSet ||--|o CompoundSetExpression : "compoundExpression"
CompoundSetExpression ||--}o SubClause : "whereClauses"
TerminologyExtension ||--}| SponsorTerm : "sponsorTerms"
ListOfContents ||--|| NestedList : "contentsList"
NestedList ||--}o OrderedListItem : "listItems"
OrderedListItem ||--|o Analysis : "analysisId"
OrderedListItem ||--|o Output : "outputId"
OrderedListItem ||--|o NestedList : "sublist"

``` 


## Classes
_Classes provide templates for organizing data. Data objects instantiate classes in the schema. Each class has a set of slots (aka fields, attributes) that are applicable to it. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#classes) for more information._

| Class | Description |
| --- | --- |
| [NamedObject](NamedObject.md) | An object with a name |
| [ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |
| [ListOfContents](ListOfContents.md) | A structured list of analyses and outputs included in the reporting event |
| [NestedList](NestedList.md) | A list of items (analyses or outputs) that may be organized within sub-lists |
| [LevelOrder](LevelOrder.md) | An abstract class containing attributes used to position class instances with... |
| [OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |
| [ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |
| [TerminologyExtension](TerminologyExtension.md) | An extensible set of controlled terminology that has been extended with at le... |
| [SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |
| [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The term used for an attribute whose terminology is extensible |
| [AnalysisOutputCategorization](AnalysisOutputCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |
| [AnalysisOutputCategory](AnalysisOutputCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |
| [WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |
| [WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] |
| [ReferencedWhereClause](ReferencedWhereClause.md) | An abstract class indicating an identified where clause (i |
| [SubClause](SubClause.md) | An abstract class containing all attributes that may be specified for a sub-c... |
| [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | An abstract class representing a compound expression consisting of either two... |
| [AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |
| [ReferencedAnalysisSet](ReferencedAnalysisSet.md) | An `AnalysisSet` referenced by identifier (`subClauseId`) as the sub-clause o... |
| [CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |
| [DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |
| [ReferencedDataSubset](ReferencedDataSubset.md) | A `DataSubset` referenced by identifier (`subClauseId`) as the sub-clause of ... |
| [CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |
| [GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |
| [Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |
| [ReferencedGroup](ReferencedGroup.md) | A `Group` referenced by identifier (`subClauseId`) as the sub-clause of a com... |
| [CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more sub-clauses combined w... |
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
| [description](description.md) | A textual description of the instance of the class |
| [label](label.md) | A short informative description that may be used for display |
| [id](id.md) | The assigned identifying value for the instance of the class |
| [version](version.md) | An ordinal indicating the version of the identified instance of the class |
| [mainListOfContents](mainListOfContents.md) | The main list of the analyses and outputs defined for the reporting event |
| [otherListsOfContents](otherListsOfContents.md) | Other lists of the analyses and outputs defined for the reporting event |
| [contentsList](contentsList.md) | A structured list of the analyses and outputs defined for the reporting event |
| [referenceDocuments](referenceDocuments.md) | External documents containing information referenced for the reporting event |
| [terminologyExtensions](terminologyExtensions.md) | Any sponsor-defined extensions to extensible terminology |
| [analysisOutputCategorizations](analysisOutputCategorizations.md) | Sets of related implementer-defined categories that can be used to categorize... |
| [analysisSets](analysisSets.md) | The analysis sets (subject populations) defined for the reporting event |
| [dataSubsets](dataSubsets.md) | Subsets of data identified by selection criteria for inclusion in analysis de... |
| [analysisGroupings](analysisGroupings.md) | Characteristics used to subdivide the subject population (e |
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
| [controlledTerm](controlledTerm.md) | One of the permissible values from the referenced enumeration |
| [sponsorTermId](sponsorTermId.md) | The identifier of the referenced sponsor term |
| [categories](categories.md) | Implementer-defined categories of analyses/outputs, each of which may include... |
| [subCategorizations](subCategorizations.md) | Sets of related implementer-defined sub-categories that can be used to catego... |
| [condition](condition.md) | A simple selection criterion exressed as [dataset] |
| [compoundExpression](compoundExpression.md) | A compound expression that combines or negates where clauses |
| [dataset](dataset.md) | The name of the analysis dataset |
| [variable](variable.md) | The name of the variable |
| [comparator](comparator.md) | Comparison operator indicating how the variable is compared to the value(s) |
| [value](value.md) | The prespecified value or values |
| [subClauseId](subClauseId.md) | The identifier of the analysis set, data subset or group referenced in the co... |
| [logicalOperator](logicalOperator.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... |
| [whereClauses](whereClauses.md) | A list of one or more where clauses (selection criteria) to be combined or ne... |
| [groupingDataset](groupingDataset.md) | For groupings based on a single variable, a reference to the dataset containi... |
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
