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
| [AnalysisPurpose](AnalysisPurpose.md) |  |
| [AnalysisReason](AnalysisReason.md) |  |
| [AnalysisSet](AnalysisSet.md) | A set of subjects whose data are to be included in the main analyses |
| [CodeParameter](CodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [CompoundGroupExpression](CompoundGroupExpression.md) |  |
| [CompoundSetExpression](CompoundSetExpression.md) |  |
| [CompoundSubsetExpression](CompoundSubsetExpression.md) |  |
| [DataGroup](DataGroup.md) | A subdivision of the analysis dataset records based on a defined factor |
| [DataGroupingFactor](DataGroupingFactor.md) | A factor used to subdivide data records in an analysis dataset for analysis |
| [DataSubset](DataSubset.md) | A subset of data identified by selection criteria for inclusion in the analys... |
| [DisplaySection](DisplaySection.md) | A part of a tabular display containing one or more pieces of informational te... |
| [DisplaySubSection](DisplaySubSection.md) | An occurrence of a display section containing text that is ordered with respe... |
| [DocumentReference](DocumentReference.md) |  |
| [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md) |  |
| [GlobalDisplaySection](GlobalDisplaySection.md) | A part of a tabular display containing one or more pieces of informational te... |
| [Group](Group.md) | A subdivision of the subject population or analysis dataset record set based ... |
| [GroupingFactor](GroupingFactor.md) | A factor used to subdivide either the subject population or data records in a... |
| [NamedObject](NamedObject.md) |  |
| [NestedList](NestedList.md) | A list of items (analyses or outputs) that may be organized within sub-lists |
| [Operation](Operation.md) | A statistical operation that produces a single analysis result value as part ... |
| [OperationResult](OperationResult.md) | The result of an analysis method operation performed on a subdivision of subj... |
| [OperationRole](OperationRole.md) |  |
| [OrderedDisplay](OrderedDisplay.md) | A display ordered with respect to other displays in an analysis output |
| [OrderedDisplaySubSection](OrderedDisplaySubSection.md) |  |
| [OrderedGroupingFactor](OrderedGroupingFactor.md) | A reference to a defined factor by which subjects or data records are grouped... |
| [OrderedListItem](OrderedListItem.md) | An item (analysis, output or sub-list) ordered relative to other items within... |
| [OrderedSubSection](OrderedSubSection.md) | A subsection ordered with respect to other subsections of the same type |
| [OrderedSubSectionRef](OrderedSubSectionRef.md) | A reference to a subsection defined either globally or in another display sec... |
| [Output](Output.md) | A report of results and their evaluation based on planned analyses performed ... |
| [OutputDisplay](OutputDisplay.md) | A tabular representation of the results of one or more analyses |
| [OutputFile](OutputFile.md) | A file containing analysis output displays |
| [OutputFileType](OutputFileType.md) |  |
| [PageNameRef](PageNameRef.md) | One or more pages in the reference document, referenced by named destination |
| [PageNumberListRef](PageNumberListRef.md) | One or more individual pages in the reference document, referenced by page nu... |
| [PageNumberRangeRef](PageNumberRangeRef.md) | A range of pages in the reference document, indicated by the first and last p... |
| [PageRef](PageRef.md) |  |
| [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md) | An indication of the analysis that contains results of a referenced operation |
| [ReferenceDocument](ReferenceDocument.md) |  |
| [ReferencedOperationRelationship](ReferencedOperationRelationship.md) | A reference to an statistical operation whose results is used in the calculat... |
| [ReportingEvent](ReportingEvent.md) | A set of analyses and outputs created to meet a specific reporting requiremen... |
| [ResultGroup](ResultGroup.md) | For the specified grouping factor, an indication of the specific group of sub... |
| [SponsorAnalysisPurpose](SponsorAnalysisPurpose.md) |  |
| [SponsorAnalysisReason](SponsorAnalysisReason.md) |  |
| [SponsorOperationRole](SponsorOperationRole.md) |  |
| [SponsorOutputFileType](SponsorOutputFileType.md) |  |
| [SponsorTerm](SponsorTerm.md) | A sponsor-defined term that is included in an extensible set of controlled te... |
| [SubjectGroupingFactor](SubjectGroupingFactor.md) | A factor used to subdivide the subject population for comparative analysis (e |
| [TemplateCodeParameter](TemplateCodeParameter.md) | A replacement parameter whose value is substituted in template programming co... |
| [TerminologyExtension](TerminologyExtension.md) | A sponsor-defined term that is included in an extensible set of controlled te... |
| [WhereClause](WhereClause.md) |  |
| [WhereClauseCompoundExpression](WhereClauseCompoundExpression.md) |  |
| [WhereClauseCondition](WhereClauseCondition.md) |  |


## Slots

| Slot | Description |
| --- | --- |
| [analyses](analyses.md) | The analyses defined for the reporting event |
| [analysisCategorizations](analysisCategorizations.md) |  |
| [analysisGroupings](analysisGroupings.md) | Characteristics used to subdivide the subject population (e |
| [analysisId](analysisId.md) |  |
| [analysisSetId](analysisSetId.md) |  |
| [analysisSets](analysisSets.md) | The analysis sets (subject populations) defined for the reporting event |
| [categories](categories.md) |  |
| [categoryIds](categoryIds.md) |  |
| [code](code.md) | Programming statements used to perform the specific analysis |
| [codeTemplate](codeTemplate.md) | Template programming statements and/or a reference to the template program us... |
| [comparator](comparator.md) |  |
| [compoundExpression](compoundExpression.md) |  |
| [condition](condition.md) |  |
| [context](context.md) | The name and version of the computer language used for the actual programming... |
| [controlledTerm](controlledTerm.md) |  |
| [dataDriven](dataDriven.md) | Indicates whether the groups defined by the grouping are prespecified (false)... |
| [dataGroupings](dataGroupings.md) | Characteristics used to subdivide data records in the analysis dataset (e |
| [dataset](dataset.md) |  |
| [dataSubsetId](dataSubsetId.md) |  |
| [dataSubsets](dataSubsets.md) |  |
| [description](description.md) |  |
| [display](display.md) |  |
| [displays](displays.md) |  |
| [displaySections](displaySections.md) |  |
| [displayTitle](displayTitle.md) |  |
| [documentRef](documentRef.md) |  |
| [documentRefs](documentRefs.md) |  |
| [enumeration](enumeration.md) | The name of the extensible enumeration |
| [fileSpecifications](fileSpecifications.md) |  |
| [fileType](fileType.md) |  |
| [firstPage](firstPage.md) | The page number of the first page in a range of pages |
| [formattedValue](formattedValue.md) |  |
| [globalDisplaySections](globalDisplaySections.md) |  |
| [groupId](groupId.md) |  |
| [groupingId](groupingId.md) |  |
| [groupingVariable](groupingVariable.md) | For groupings based on a single variable, a reference to the dataset variable... |
| [groups](groups.md) |  |
| [groupValue](groupValue.md) |  |
| [id](id.md) |  |
| [label](label.md) |  |
| [lastPage](lastPage.md) | The page number of the last page in a range of pages |
| [level](level.md) |  |
| [listItems](listItems.md) |  |
| [listOfPlannedAnalyses](listOfPlannedAnalyses.md) | A structured list of the analyses defined for the reporting event |
| [listOfPlannedOutputs](listOfPlannedOutputs.md) | An optional structured list of the outputs defined for the reporting event |
| [location](location.md) |  |
| [logicalOperator](logicalOperator.md) |  |
| [methodId](methodId.md) | A reference to the set of one or more statistical operations performed for th... |
| [methods](methods.md) | The defined methods used to analyze any analysis variable |
| [name](name.md) |  |
| [operationId](operationId.md) |  |
| [operations](operations.md) |  |
| [order](order.md) |  |
| [orderedGroupings](orderedGroupings.md) |  |
| [orderedSubSections](orderedSubSections.md) |  |
| [outputId](outputId.md) |  |
| [outputs](outputs.md) |  |
| [pageNames](pageNames.md) | One or more named document references which each correspond with a page |
| [pageNumbers](pageNumbers.md) | One or more page numbers |
| [pageRefs](pageRefs.md) |  |
| [parameters](parameters.md) | Replacement parameters that are referenced in the programming code or program... |
| [programmingCode](programmingCode.md) | Programming statements and/or a reference to the program used to perform the ... |
| [purpose](purpose.md) | The purpose of the analysis within the body of evidence (e |
| [rawValue](rawValue.md) |  |
| [reason](reason.md) | The rationale for performing this analysis |
| [referencedAnalysisOperations](referencedAnalysisOperations.md) |  |
| [referenceDocumentId](referenceDocumentId.md) |  |
| [referenceDocuments](referenceDocuments.md) |  |
| [referencedOperationId](referencedOperationId.md) |  |
| [referencedOperationRelationships](referencedOperationRelationships.md) |  |
| [referencedOperationRole](referencedOperationRole.md) |  |
| [refType](refType.md) |  |
| [resultGroups](resultGroups.md) |  |
| [resultPattern](resultPattern.md) |  |
| [results](results.md) |  |
| [resultsByGroup](resultsByGroup.md) | Indicates whether a result is expected for each group in the grouping |
| [sectionType](sectionType.md) |  |
| [sponsorTermId](sponsorTermId.md) |  |
| [sponsorTerms](sponsorTerms.md) | The sponsor-defined terms added to the extensible terminology |
| [style](style.md) |  |
| [subCategorizations](subCategorizations.md) |  |
| [sublist](sublist.md) |  |
| [submissionValue](submissionValue.md) | The specific value expected for submissions |
| [subSection](subSection.md) |  |
| [subSectionId](subSectionId.md) |  |
| [subSections](subSections.md) |  |
| [terminologyExtensions](terminologyExtensions.md) | Any sponsor-defined extensions to extensible terminology |
| [text](text.md) |  |
| [value](value.md) |  |
| [valueSource](valueSource.md) | A reference to the prespecified source of the value for the parameter |
| [variable](variable.md) |  |
| [version](version.md) |  |
| [whereClauses](whereClauses.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AnalysisPurposeEnum](AnalysisPurposeEnum.md) | The purpose of the analysis within the body of evidence (e |
| [AnalysisReasonEnum](AnalysisReasonEnum.md) | The rationale for performing this analysis |
| [ConditionComparatorEnum](ConditionComparatorEnum.md) |  |
| [DisplaySectionTypeEnum](DisplaySectionTypeEnum.md) |  |
| [ExpressionLogicalOperatorEnum](ExpressionLogicalOperatorEnum.md) |  |
| [ExtensibleTerminologyEnum](ExtensibleTerminologyEnum.md) | Extensible ARS enumerations |
| [OperationRoleEnum](OperationRoleEnum.md) |  |
| [OutputFileTypeEnum](OutputFileTypeEnum.md) |  |
| [PageRefTypeEnum](PageRefTypeEnum.md) | Type of page for page references |


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
