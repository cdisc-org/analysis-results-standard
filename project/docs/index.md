# Analysis Results Standard (ARS)

DRAFT Logical model to support both the prospective specification of analyses and the fully contextualized representation of the results of the analyses.


URI: https://www.cdisc.org/ars/1-0
Name: ars_ldm



## Classes

| Class | Description |
| --- | --- |
| [Analysis](Analysis.md) | An analysis that is designed to meet a requirement of the reporting event |
| [AnalysisCategorization](AnalysisCategorization.md) | A set of related implementer-defined categories that can be used to categoriz... |
| [AnalysisCategory](AnalysisCategory.md) | An implementer-defined category of analyses/outputs, which may include one or... |
| [AnalysisGroup](AnalysisGroup.md) | A subdivision of the subject population based on a defined factor (e |
| [AnalysisMethod](AnalysisMethod.md) | A set of one or more statistical operations |
| [AnalysisOutputCodeParameter](AnalysisOutputCodeParameter.md) | A parameter whose value is used in programming code for a specific analysis o... |
| [AnalysisOutputProgrammingCode](AnalysisOutputProgrammingCode.md) | Programming statements and/or a reference to the program used to perform a sp... |
| [AnalysisProgrammingCodeTemplate](AnalysisProgrammingCodeTemplate.md) | Programming statements and/or a reference to a used as a template for creatio... |
| [AnalysisPurpose](AnalysisPurpose.md) | The purpose of the analysis within the body of evidence (e |
| [AnalysisReason](AnalysisReason.md) | The rationale for performing this analysis |
| [AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |
| [CodeParameter](CodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [CompoundGroupExpression](CompoundGroupExpression.md) | A compound expression consisting of either two or more identified group combi... |
| [CompoundSetExpression](CompoundSetExpression.md) | A compound expression consisting of either two or more identified analysis se... |
| [CompoundSubsetExpression](CompoundSubsetExpression.md) | A compound expression consisting of either two or more where clauses combined... |
| [DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |
| [DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |
| [DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |
| [DisplaySection](DisplaySection.md) | A part of a tabular display containing one or more pieces of informational te... |
| [DisplaySubSection](DisplaySubSection.md) | An occurrence of a display section containing text |
| [DocumentReference](DocumentReference.md) | A reference to an external document |
| [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) | The term used for an attribute whose terminology is extensible |
| [GlobalDisplaySection](GlobalDisplaySection.md) | A global definition for part of a tabular display containing one or more piec... |
| [Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |
| [GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |
| [NamedObject](NamedObject.md) | An object with a name |
| [NestedList](NestedList.md) | A list of items (analyses or outputs) that may be organized within sub-lists |
| [Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |
| [OperationResult](OperationResult.md) | The result of an analysis method operation performed on a subdivision of subj... |
| [OperationRole](OperationRole.md) | The role that the referenced operation's result plays in the calculation of t... |
| [OrderedDisplay](OrderedDisplay.md) | A display ordered with respect to other displays in an analysis output |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) | A single subsection ordered with respect to other subsections in the same sec... |
| [OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |
| [OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |
| [OrderedSubSection](OrderedSubSection.md) | A subsection ordered with respect to other subsections of the same type |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | A reference to a subsection defined either globally or in another display sec... |
| [Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |
| [OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |
| [OutputFile](OutputFile.md) | A file containing analysis output displays |
| [OutputFileType](OutputFileType.md) | The file format of the file containing output from analyses |
| [PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |
| [PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |
| [PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |
| [PageRef](PageRef.md) | A reference to a specific part of a document as indicated by a list of one or... |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | An indication of the analysis that contains results of a referenced operation |
| [ReferenceDocument](ReferenceDocument.md) | An external document containing supporting documentation or programming code |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to a statistical operation whose results are used in the calculat... |
| [ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |
| [ResultGroup](ResultGroup.md) | For the specified grouping factor, an indication of the specific group of sub... |
| [SponsorAnalysisPurpose](SponsorAnalysisPurpose.md) | The sponsor-defined purpose of the analysis within the body of evidence (e |
| [SponsorAnalysisReason](SponsorAnalysisReason.md) | The sponsor-defined rationale for performing this analysis |
| [SponsorOperationRole](SponsorOperationRole.md) | The sponsor-defined role that the referenced operation's result plays in the ... |
| [SponsorOutputFileType](SponsorOutputFileType.md) | The sponsor-defined file format of the file containing output from analyses |
| [SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |
| [SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |
| [TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [TerminologyExtension](TerminologyExtension.md) | An extensible set of controlled terminology that has been extended with at le... |
| [WhereClause](WhereClause.md) | Selection criteria defined as either a simple condition ([variable] [comparat... |
| [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) | A compound expression consisting of either two or more where clauses combined... |
| [WhereClauseCondition](WhereClauseCondition.md) | A simple selection criterion exressed as [dataset] |


## Slots

| Slot | Description |
| --- | --- |
| [analyses](analyses.md) | The analyses defined for the reporting event |
| [analysisCategorizations](analysisCategorizations.md) | Sets of related implementer-defined categories that can be used to categorize... |
| [analysisGroupings](analysisGroupings.md) | Characteristics used to subdivide the subject population (e |
| [analysisId](analysisId.md) | The identifier of the referenced analysis |
| [analysisSetId](analysisSetId.md) | The identifier of the referenced analysis set |
| [analysisSets](analysisSets.md) | The analysis sets (subject populations) defined for the reporting event |
| [categories](categories.md) | Implementer-defined categories of analyses/outputs, each of which may include... |
| [categoryIds](categoryIds.md) | References to any implementer-defined categories that apply to the analysis o... |
| [code](code.md) | Programming statements used to perform the specific analysis |
| [codeTemplate](codeTemplate.md) | Template programming statements used to perform the statistical operations fo... |
| [comparator](comparator.md) | Comparison operator indicating how the variable is compared to the value(s) |
| [compoundExpression](compoundExpression.md) | A compound expression that combines or negates where clauses |
| [condition](condition.md) | A simple selection criterion exressed as [dataset] |
| [context](context.md) | The name and version of the computer language used for the actual programming... |
| [controlledTerm](controlledTerm.md) | One of the permissible values from the referenced enumeration |
| [dataDriven](dataDriven.md) | Indicates whether the groups defined by the grouping are prespecified (false)... |
| [dataGroupings](dataGroupings.md) | Characteristics used to subdivide data records in analysis datasets (e |
| [dataset](dataset.md) | The name of the analysis dataset |
| [dataSubsetId](dataSubsetId.md) | The identifier of the referenced data subset |
| [dataSubsets](dataSubsets.md) | Subsets of data identified by selection criteria for inclusion in analysis de... |
| [description](description.md) | A textual description of the instance of the class |
| [display](display.md) | A display contained in the output |
| [displays](displays.md) | An ordered list of the displays included in the output |
| [displaySections](displaySections.md) | The parts of the display containing one or more pieces of informational text ... |
| [displayTitle](displayTitle.md) | Display description which uniquely identifies the display in the report |
| [documentRef](documentRef.md) | A reference to the document containing programming code |
| [documentRefs](documentRefs.md) | References to external documents containing additional information |
| [enumeration](enumeration.md) | The name of the extensible enumeration |
| [fileSpecifications](fileSpecifications.md) | Specifications of output files |
| [fileType](fileType.md) | The format of the output file |
| [firstPage](firstPage.md) | The page number of the first page in a range of pages |
| [formattedValue](formattedValue.md) | The result value formatted for display according to the resultPattern |
| [globalDisplaySections](globalDisplaySections.md) | Display section specifications that may be applied to any display |
| [groupId](groupId.md) | The identifier of a referenced predefined group within a grouping |
| [groupingId](groupingId.md) | The identifier of the referenced subject or data grouping factor |
| [groupingVariable](groupingVariable.md) | For groupings based on a single variable, a reference to the dataset variable... |
| [groups](groups.md) | The pre-specified groups within the grouping |
| [groupValue](groupValue.md) | The data value used as a group within a data-driven grouping |
| [id](id.md) | The assigned identifying value for the instance of the class |
| [label](label.md) | A short informative description that may be used for display |
| [lastPage](lastPage.md) | The page number of the last page in a range of pages |
| [level](level.md) | The level of the entry within a hierarchical structure |
| [listItems](listItems.md) | Items in the list |
| [listOfPlannedAnalyses](listOfPlannedAnalyses.md) | A structured list of the analyses defined for the reporting event |
| [listOfPlannedOutputs](listOfPlannedOutputs.md) | An optional structured list of the outputs defined for the reporting event |
| [location](location.md) | A path (relative or absolute) indicating the location of the file |
| [logicalOperator](logicalOperator.md) | The boolean operator that is used to combine (AND, OR) or negate (NOT) the wh... |
| [methodId](methodId.md) | A reference to the set of one or more statistical operations performed for th... |
| [methods](methods.md) | The defined methods used to analyze any analysis variable |
| [name](name.md) | The name for the instance of the class |
| [operationId](operationId.md) | The identifier of the referenced operation |
| [operations](operations.md) | The calculations performed for the method |
| [order](order.md) | The ordinal of the instance with respect to other instances |
| [orderedGroupings](orderedGroupings.md) | An ordered list of grouping factors used in the analysis |
| [orderedSubSections](orderedSubSections.md) | An ordered list of the informational text to display in the display section |
| [outputId](outputId.md) | The identifier of the referenced output |
| [outputs](outputs.md) | The outputs defined for the reporting event |
| [pageNames](pageNames.md) | One or more named document references which each correspond with a page |
| [pageNumbers](pageNumbers.md) | One or more page numbers |
| [pageRefs](pageRefs.md) | A list of references to specific parts of a document, which may be referenced... |
| [parameters](parameters.md) | Replacement parameters that are referenced in the programming code or program... |
| [programmingCode](programmingCode.md) | Programming statements used to perform the specific analysis or create the sp... |
| [purpose](purpose.md) | The purpose of the analysis within the body of evidence (e |
| [rawValue](rawValue.md) | The raw result value (e |
| [reason](reason.md) | The rationale for performing this analysis |
| [referencedAnalysisOperations](referencedAnalysisOperations.md) | Indications of which analysis contains the results for each referenced operat... |
| [referenceDocumentId](referenceDocumentId.md) | The identifier of the referenced document |
| [referenceDocuments](referenceDocuments.md) | External documents containing information referenced for the reporting event |
| [referencedOperationRelationshipId](referencedOperationRelationshipId.md) | The identifier of the defined referenced operation relationship |
| [referencedOperationRelationships](referencedOperationRelationships.md) | Relationships to other operations indicating how the result of the referenced... |
| [referencedOperationRole](referencedOperationRole.md) | The role that the referenced operation's result plays in the calculation of t... |
| [refType](refType.md) | The type of reference for page references |
| [resultGroups](resultGroups.md) | The group values associated with the result |
| [resultPattern](resultPattern.md) | The default pattern or format to apply to the result for display |
| [results](results.md) | The results of the analysis |
| [resultsByGroup](resultsByGroup.md) | Indicates whether a result is expected for each group in the grouping |
| [sectionType](sectionType.md) | The type of display section that contains one or more pieces of informational... |
| [sponsorTermId](sponsorTermId.md) | The identifier of the referenced sponsor term |
| [sponsorTerms](sponsorTerms.md) | The sponsor-defined terms added to the extensible terminology |
| [style](style.md) | Reference to the specification of the style used for the output |
| [subCategorizations](subCategorizations.md) | Sets of related implementer-defined sub-categories that can be used to catego... |
| [sublist](sublist.md) | A sub-list of items (analyses or outputs) that may be further organized withi... |
| [submissionValue](submissionValue.md) | The specific value expected for submissions |
| [subSection](subSection.md) | A defined piece of information text to display in a display section |
| [subSectionId](subSectionId.md) | The identifier of the referenced subsection |
| [subSections](subSections.md) | A list of defined pieces of information text that may be displayed in display... |
| [terminologyExtensions](terminologyExtensions.md) | Any sponsor-defined extensions to extensible terminology |
| [text](text.md) | The text to be displayed in the display section |
| [value](value.md) | The prespecified value or values |
| [valueSource](valueSource.md) | A reference to the prespecified source of the value for the parameter |
| [variable](variable.md) | The name of the variable |
| [version](version.md) | An ordinal indicating the version of the identified instance of the class |
| [whereClauses](whereClauses.md) | A list of one or more where clauses (selection criteria) to be combined or ne... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AnalysisPurposeEnum](AnalysisPurposeEnum.md) | The purpose of the analysis within the body of evidence (e |
| [AnalysisReasonEnum](AnalysisReasonEnum.md) | The rationale for performing this analysis |
| [ConditionComparatorEnum](ConditionComparatorEnum.md) | Comparison operators indicating how the value of a variable is compared to a ... |
| [DisplaySectionTypeEnum](DisplaySectionTypeEnum.md) | Types of display section that contain one or more pieces of informational tex... |
| [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) | Boolean operators denoting a logical operation (e |
| [ExtensibleTerminologyEnum](ExtensibleTerminologyEnum.md) | Extensible ARS enumerations |
| [OperationRoleEnum](OperationRoleEnum.md) | The role that the referenced operation's result plays in the calculation of t... |
| [OutputFileTypeEnum](OutputFileTypeEnum.md) | The file format of the file containing output from analyses |
| [PageRefTypeEnum](PageRefTypeEnum.md) | Type of reference for page references |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
