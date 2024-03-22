

CREATE TABLE "AnalysisMethod" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"documentRefs" TEXT, 
	operations TEXT NOT NULL, 
	"codeTemplate" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisOutputCategorization" (
	id TEXT NOT NULL, 
	label TEXT, 
	categories TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisOutputCategory" (
	id TEXT NOT NULL, 
	label TEXT, 
	"subCategorizations" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisOutputCodeParameter" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY (name, description, label, value)
);

CREATE TABLE "AnalysisOutputProgrammingCode" (
	context TEXT NOT NULL, 
	code TEXT, 
	"documentRef" TEXT, 
	parameters TEXT, 
	PRIMARY KEY (context, code, "documentRef", parameters)
);

CREATE TABLE "AnalysisProgrammingCodeTemplate" (
	context TEXT NOT NULL, 
	code TEXT, 
	"documentRef" TEXT, 
	parameters TEXT, 
	PRIMARY KEY (context, code, "documentRef", parameters)
);

CREATE TABLE "AnalysisSet" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"compoundExpression" TEXT, 
	condition TEXT, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "CompoundGroupExpression" (
	"logicalOperator" VARCHAR(3) NOT NULL, 
	"whereClauses" TEXT, 
	PRIMARY KEY ("logicalOperator", "whereClauses")
);

CREATE TABLE "CompoundSetExpression" (
	"logicalOperator" VARCHAR(3) NOT NULL, 
	"whereClauses" TEXT, 
	PRIMARY KEY ("logicalOperator", "whereClauses")
);

CREATE TABLE "CompoundSubsetExpression" (
	"logicalOperator" VARCHAR(3) NOT NULL, 
	"whereClauses" TEXT, 
	PRIMARY KEY ("logicalOperator", "whereClauses")
);

CREATE TABLE "DataSubset" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"compoundExpression" TEXT, 
	condition TEXT, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DisplaySubSection" (
	id TEXT NOT NULL, 
	text TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Group" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"compoundExpression" TEXT, 
	condition TEXT, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "GroupingFactor" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"groupingDataset" TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	groups TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ListOfContents" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	"contentsList" TEXT NOT NULL, 
	PRIMARY KEY (name, description, label, "contentsList")
);

CREATE TABLE "NestedList" (
	"listItems" TEXT, 
	PRIMARY KEY ("listItems")
);

CREATE TABLE "Operation" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	"order" INTEGER NOT NULL, 
	"referencedOperationRelationships" TEXT, 
	"resultPattern" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Output" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"categoryIds" TEXT, 
	"documentRefs" TEXT, 
	"programmingCode" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OutputDisplay" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"displayTitle" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PageNameRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	"pageNumbers" INTEGER, 
	"pageNames" TEXT NOT NULL, 
	"firstPage" INTEGER, 
	"lastPage" INTEGER, 
	PRIMARY KEY (label, "refType", "pageNumbers", "pageNames", "firstPage", "lastPage")
);

CREATE TABLE "PageNumberListRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	"pageNumbers" INTEGER NOT NULL, 
	"pageNames" TEXT, 
	"firstPage" INTEGER, 
	"lastPage" INTEGER, 
	PRIMARY KEY (label, "refType", "pageNumbers", "pageNames", "firstPage", "lastPage")
);

CREATE TABLE "PageNumberRangeRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	"pageNumbers" INTEGER, 
	"pageNames" TEXT, 
	"firstPage" INTEGER NOT NULL, 
	"lastPage" INTEGER NOT NULL, 
	PRIMARY KEY (label, "refType", "pageNumbers", "pageNames", "firstPage", "lastPage")
);

CREATE TABLE "ReferenceDocument" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	location TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReportingEvent" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"mainListOfContents" TEXT NOT NULL, 
	"otherListsOfContents" TEXT, 
	"referenceDocuments" TEXT, 
	"analysisOutputCategorizations" TEXT, 
	"analysisSets" TEXT, 
	"dataSubsets" TEXT, 
	"analysisGroupings" TEXT, 
	methods TEXT, 
	analyses TEXT, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SponsorTerm" (
	id TEXT NOT NULL, 
	"submissionValue" TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TemplateCodeParameter" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	"valueSource" TEXT, 
	value TEXT, 
	PRIMARY KEY (name, description, label, "valueSource", value)
);

CREATE TABLE "WhereClause" (
	condition TEXT, 
	"compoundExpression" TEXT, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	PRIMARY KEY (condition, "compoundExpression", level, "order")
);

CREATE TABLE "WhereClauseCondition" (
	dataset TEXT, 
	variable TEXT, 
	comparator VARCHAR(5), 
	value TEXT, 
	PRIMARY KEY (dataset, variable, comparator, value)
);

CREATE TABLE "Analysis" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	id TEXT NOT NULL, 
	version INTEGER, 
	reason TEXT NOT NULL, 
	purpose TEXT NOT NULL, 
	"documentRefs" TEXT, 
	"categoryIds" TEXT, 
	dataset TEXT, 
	variable TEXT, 
	"analysisSetId" TEXT, 
	"dataSubsetId" TEXT, 
	"methodId" TEXT NOT NULL, 
	"programmingCode" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("analysisSetId") REFERENCES "AnalysisSet" (id), 
	FOREIGN KEY("dataSubsetId") REFERENCES "DataSubset" (id), 
	FOREIGN KEY("methodId") REFERENCES "AnalysisMethod" (id)
);

CREATE TABLE "AnalysisPurpose" (
	"controlledTerm" VARCHAR(27) NOT NULL, 
	"sponsorTermId" TEXT, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "AnalysisReason" (
	"controlledTerm" VARCHAR(30) NOT NULL, 
	"sponsorTermId" TEXT, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "DisplaySection" (
	"sectionType" VARCHAR(15), 
	"orderedSubSections" TEXT, 
	"OutputDisplay_id" TEXT, 
	PRIMARY KEY ("sectionType", "orderedSubSections", "OutputDisplay_id"), 
	FOREIGN KEY("OutputDisplay_id") REFERENCES "OutputDisplay" (id)
);

CREATE TABLE "DocumentReference" (
	"referenceDocumentId" TEXT NOT NULL, 
	"pageRefs" TEXT, 
	PRIMARY KEY ("referenceDocumentId", "pageRefs"), 
	FOREIGN KEY("referenceDocumentId") REFERENCES "ReferenceDocument" (id)
);

CREATE TABLE "GlobalDisplaySection" (
	"sectionType" VARCHAR(15), 
	"subSections" TEXT, 
	"ReportingEvent_id" TEXT, 
	PRIMARY KEY ("sectionType", "subSections", "ReportingEvent_id"), 
	FOREIGN KEY("ReportingEvent_id") REFERENCES "ReportingEvent" (id)
);

CREATE TABLE "OperationRole" (
	"controlledTerm" VARCHAR(11) NOT NULL, 
	"sponsorTermId" TEXT, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "OrderedDisplay" (
	"order" INTEGER NOT NULL, 
	display TEXT NOT NULL, 
	"Output_id" TEXT, 
	PRIMARY KEY ("order", display, "Output_id"), 
	FOREIGN KEY(display) REFERENCES "OutputDisplay" (id), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "OrderedSubSection" (
	"order" INTEGER NOT NULL, 
	"subSection" TEXT NOT NULL, 
	"subSectionId" TEXT, 
	PRIMARY KEY ("order", "subSection", "subSectionId"), 
	FOREIGN KEY("subSection") REFERENCES "DisplaySubSection" (id), 
	FOREIGN KEY("subSectionId") REFERENCES "DisplaySubSection" (id)
);

CREATE TABLE "OrderedSubSectionRef" (
	"order" INTEGER NOT NULL, 
	"subSection" TEXT, 
	"subSectionId" TEXT NOT NULL, 
	PRIMARY KEY ("order", "subSection", "subSectionId"), 
	FOREIGN KEY("subSection") REFERENCES "DisplaySubSection" (id), 
	FOREIGN KEY("subSectionId") REFERENCES "DisplaySubSection" (id)
);

CREATE TABLE "OutputFile" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	"fileType" TEXT, 
	location TEXT, 
	style TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY (name, description, label, "fileType", location, style, "Output_id"), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "OutputFileType" (
	"controlledTerm" VARCHAR(3) NOT NULL, 
	"sponsorTermId" TEXT, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "ReferencedAnalysisSet" (
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	"subClauseId" TEXT NOT NULL, 
	PRIMARY KEY (level, "order", "subClauseId"), 
	FOREIGN KEY("subClauseId") REFERENCES "AnalysisSet" (id)
);

CREATE TABLE "ReferencedDataSubset" (
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	"subClauseId" TEXT NOT NULL, 
	PRIMARY KEY (level, "order", "subClauseId"), 
	FOREIGN KEY("subClauseId") REFERENCES "DataSubset" (id)
);

CREATE TABLE "ReferencedGroup" (
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	"subClauseId" TEXT NOT NULL, 
	PRIMARY KEY (level, "order", "subClauseId"), 
	FOREIGN KEY("subClauseId") REFERENCES "Group" (id)
);

CREATE TABLE "ResultGroup" (
	"groupingId" TEXT NOT NULL, 
	"groupId" TEXT, 
	"groupValue" TEXT, 
	PRIMARY KEY ("groupingId", "groupId", "groupValue"), 
	FOREIGN KEY("groupingId") REFERENCES "GroupingFactor" (id), 
	FOREIGN KEY("groupId") REFERENCES "Group" (id)
);

CREATE TABLE "SponsorAnalysisPurpose" (
	"controlledTerm" TEXT, 
	"sponsorTermId" TEXT NOT NULL, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "SponsorAnalysisReason" (
	"controlledTerm" TEXT, 
	"sponsorTermId" TEXT NOT NULL, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "SponsorOperationRole" (
	"controlledTerm" TEXT, 
	"sponsorTermId" TEXT NOT NULL, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "SponsorOutputFileType" (
	"controlledTerm" TEXT, 
	"sponsorTermId" TEXT NOT NULL, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "TerminologyExtension" (
	id TEXT NOT NULL, 
	enumeration VARCHAR(19), 
	"sponsorTerms" TEXT NOT NULL, 
	"ReportingEvent_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReportingEvent_id") REFERENCES "ReportingEvent" (id)
);

CREATE TABLE "OperationResult" (
	"operationId" TEXT NOT NULL, 
	"resultGroups" TEXT, 
	"rawValue" TEXT, 
	"formattedValue" TEXT, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("operationId", "resultGroups", "rawValue", "formattedValue", "Analysis_id"), 
	FOREIGN KEY("operationId") REFERENCES "Operation" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);

CREATE TABLE "OrderedGroupingFactor" (
	"order" INTEGER NOT NULL, 
	"groupingId" TEXT NOT NULL, 
	"resultsByGroup" BOOLEAN NOT NULL, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("order", "groupingId", "resultsByGroup", "Analysis_id"), 
	FOREIGN KEY("groupingId") REFERENCES "GroupingFactor" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);

CREATE TABLE "OrderedListItem" (
	name TEXT NOT NULL, 
	description TEXT, 
	label TEXT, 
	"analysisId" TEXT, 
	"outputId" TEXT, 
	sublist TEXT, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	PRIMARY KEY (name, description, label, "analysisId", "outputId", sublist, level, "order"), 
	FOREIGN KEY("analysisId") REFERENCES "Analysis" (id), 
	FOREIGN KEY("outputId") REFERENCES "Output" (id)
);

CREATE TABLE "ReferencedOperationRelationship" (
	id TEXT NOT NULL, 
	"referencedOperationRole" TEXT NOT NULL, 
	"operationId" TEXT NOT NULL, 
	"analysisId" TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("operationId") REFERENCES "Operation" (id), 
	FOREIGN KEY("analysisId") REFERENCES "Analysis" (id)
);

CREATE TABLE "ReferencedAnalysisOperation" (
	"referencedOperationRelationshipId" TEXT NOT NULL, 
	"analysisId" TEXT NOT NULL, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("referencedOperationRelationshipId", "analysisId", "Analysis_id"), 
	FOREIGN KEY("referencedOperationRelationshipId") REFERENCES "ReferencedOperationRelationship" (id), 
	FOREIGN KEY("analysisId") REFERENCES "Analysis" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);
