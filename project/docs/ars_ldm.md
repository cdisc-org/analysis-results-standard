
# ars_ldm


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [Analysis](Analysis.md)
 * [AnalysisCategorization](AnalysisCategorization.md) - An implementer-defined categorization of analyses/outputs.
 * [AnalysisCategory](AnalysisCategory.md) - An implementer-defined category of analyses/outputs.
 * [CompoundExpression](CompoundExpression.md)
     * [CompoundGroupExpression](CompoundGroupExpression.md)
     * [CompoundSetExpression](CompoundSetExpression.md)
     * [CompoundSubsetExpression](CompoundSubsetExpression.md)
 * [Condition](Condition.md)
 * [DisplaySection](DisplaySection.md)
 * [DisplaySubSection](DisplaySubSection.md)
 * [GroupingFactor](GroupingFactor.md) - A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.
     * [DataGroupingFactor](DataGroupingFactor.md) - A factor used to subdivide data records in an analysis dataset for analysis.
     * [SubjectGroupingFactor](SubjectGroupingFactor.md) - A factor used to subdivide the subject population for comparative analysis (e.g., treatment, sex, race, age).
 * [NamedObject](NamedObject.md)
     * [AnalysisMethod](AnalysisMethod.md)
     * [Display](Display.md)
     * [File](File.md)
     * [Operation](Operation.md)
     * [OrderedListItem](OrderedListItem.md)
     * [ReportingEvent](ReportingEvent.md)
 * [NestedList](NestedList.md)
 * [OperationResult](OperationResult.md)
 * [OrderedGroupingFactor](OrderedGroupingFactor.md)
 * [Output](Output.md)
 * [OutputDisplay](OutputDisplay.md)
 * [ReferencedAnalysisOperation](ReferencedAnalysisOperation.md)
 * [ReferencedOperationRelationship](ReferencedOperationRelationship.md)
 * [ResultGroup](ResultGroup.md)
 * [WhereClause](WhereClause.md)
     * [AnalysisSet](AnalysisSet.md) - A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set based upon the intent-to-treat principle. [ICH E9]
     * [DataSubset](DataSubset.md) - A subset of data identified by selection criteria for inclusion in the analysis.
     * [Group](Group.md) - A subdivision of the subject population or analysis dataset record set based on a defined factor.
         * [AnalysisGroup](AnalysisGroup.md) - A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A, subjects whose gender is male).
         * [DataGroup](DataGroup.md) - A subdivision of the analysis dataset records based on a defined factor.

### Mixins


### Slots

 * [analyses](analyses.md)
 * [analysisCategorizations](analysisCategorizations.md)
 * [analysisGroupings](analysisGroupings.md)
 * [analysisId](analysisId.md)
     * [ReferencedAnalysisOperation➞analysisId](ReferencedAnalysisOperation_analysisId.md)
 * [analysisSetId](analysisSetId.md)
 * [analysisSets](analysisSets.md)
 * [categories](categories.md)
 * [categoryIds](categoryIds.md)
     * [Output➞categoryIds](Output_categoryIds.md)
 * [comparator](comparator.md)
 * [compoundExpression](compoundExpression.md)
     * [AnalysisSet➞compoundExpression](AnalysisSet_compoundExpression.md)
     * [DataSubset➞compoundExpression](DataSubset_compoundExpression.md)
     * [Group➞compoundExpression](Group_compoundExpression.md)
 * [condition](condition.md)
 * [dataDriven](dataDriven.md) - Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
 * [dataGrouping](dataGrouping.md)
 * [dataSubsetId](dataSubsetId.md)
 * [dataSubsets](dataSubsets.md)
 * [dataset](dataset.md)
 * [description](description.md)
 * [display](display.md)
 * [displaySections](displaySections.md)
 * [displayTitle](displayTitle.md)
 * [fileSpecifications](fileSpecifications.md)
 * [fileType](fileType.md)
 * [formattedValue](formattedValue.md)
 * [globalDisplaySections](globalDisplaySections.md)
 * [groupId](groupId.md)
 * [groupValue](groupValue.md)
 * [groupingId](groupingId.md)
 * [groupingVariable](groupingVariable.md) - For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
 * [groups](groups.md)
     * [DataGroupingFactor➞groups](DataGroupingFactor_groups.md)
     * [SubjectGroupingFactor➞groups](SubjectGroupingFactor_groups.md)
 * [id](id.md)
 * [label](label.md)
 * [level](level.md)
     * [OrderedListItem➞level](OrderedListItem_level.md)
 * [listItems](listItems.md)
 * [listOfPlannedAnalyses](listOfPlannedAnalyses.md)
 * [listOfPlannedOutputs](listOfPlannedOutputs.md)
 * [location](location.md)
 * [logicalOperator](logicalOperator.md)
 * [methodId](methodId.md)
 * [methods](methods.md)
 * [name](name.md)
 * [operationId](operationId.md)
 * [operations](operations.md)
 * [order](order.md)
     * [DisplaySubSection➞order](DisplaySubSection_order.md)
     * [OrderedGroupingFactor➞order](OrderedGroupingFactor_order.md)
     * [OrderedListItem➞order](OrderedListItem_order.md)
     * [OutputDisplay➞order](OutputDisplay_order.md)
 * [orderedGroupings](orderedGroupings.md)
 * [outputDisplays](outputDisplays.md)
 * [outputId](outputId.md)
 * [outputs](outputs.md)
 * [rawValue](rawValue.md)
 * [referencedAnalysisOperations](referencedAnalysisOperations.md)
 * [referencedOperationId](referencedOperationId.md)
 * [referencedOperationRelationships](referencedOperationRelationships.md)
 * [referencedOperationRole](referencedOperationRole.md)
 * [resultGroups](resultGroups.md)
 * [resultPattern](resultPattern.md)
 * [results](results.md)
 * [sectionType](sectionType.md)
 * [style](style.md)
 * [subCategorizations](subCategorizations.md)
 * [subSections](subSections.md)
 * [sublist](sublist.md)
 * [text](text.md)
 * [value](value.md)
 * [variable](variable.md)
 * [version](version.md)
 * [whereClauses](whereClauses.md)
     * [CompoundGroupExpression➞whereClauses](CompoundGroupExpression_whereClauses.md)
     * [CompoundSetExpression➞whereClauses](CompoundSetExpression_whereClauses.md)
     * [CompoundSubsetExpression➞whereClauses](CompoundSubsetExpression_whereClauses.md)

### Enums

 * [Comparator](Comparator.md)
 * [FileType](FileType.md)
 * [LogicalOperator](LogicalOperator.md)
 * [OperationRole](OperationRole.md)
 * [SectionType](SectionType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
