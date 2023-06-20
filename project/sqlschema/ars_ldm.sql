

CREATE TABLE "AnalysisCategorization" (
	id TEXT NOT NULL, 
	label TEXT, 
	categories TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisCategory" (
	id TEXT NOT NULL, 
	label TEXT, 
	"subCategorizations" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisMethod" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	operations TEXT NOT NULL, 
	"documentRefs" TEXT, 
	"codeTemplate" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisOutputCodeParameter" (
	name TEXT NOT NULL, 
	description TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY (name, description, value)
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
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	id TEXT NOT NULL, 
	label TEXT, 
	"compoundExpression" TEXT, 
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
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	id TEXT NOT NULL, 
	label TEXT, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DisplaySubSection" (
	id TEXT NOT NULL, 
	text TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Group" (
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	id TEXT NOT NULL, 
	label TEXT, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NestedList" (
	"listItems" TEXT, 
	PRIMARY KEY ("listItems")
);

CREATE TABLE "Operation" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	label TEXT, 
	"referencedOperationRelationships" TEXT, 
	"resultPattern" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Output" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"categoryIds" TEXT, 
	"documentRefs" TEXT, 
	"programmingCode" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OutputDisplay" (
	name TEXT NOT NULL, 
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
	id TEXT NOT NULL, 
	location TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReportingEvent" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"listOfPlannedAnalyses" TEXT NOT NULL, 
	"listOfPlannedOutputs" TEXT, 
	"analysisSets" TEXT, 
	"dataSubsets" TEXT, 
	"analysisCategorizations" TEXT, 
	analyses TEXT, 
	methods TEXT, 
	outputs TEXT, 
	"referenceDocuments" TEXT, 
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
	"valueSource" TEXT, 
	value TEXT, 
	PRIMARY KEY (name, description, "valueSource", value)
);

CREATE TABLE "WhereClause" (
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (level, "order", condition, "compoundExpression")
);

CREATE TABLE "WhereClauseCompoundExpression" (
	"logicalOperator" VARCHAR(3) NOT NULL, 
	"whereClauses" TEXT, 
	PRIMARY KEY ("logicalOperator", "whereClauses")
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
	id TEXT NOT NULL, 
	version INTEGER, 
	"categoryIds" TEXT, 
	description TEXT, 
	reason TEXT NOT NULL, 
	purpose TEXT NOT NULL, 
	"documentRefs" TEXT, 
	"analysisSetId" TEXT, 
	"dataSubsetId" TEXT, 
	dataset TEXT, 
	variable TEXT, 
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

CREATE TABLE "DataGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	"ReportingEvent_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReportingEvent_id") REFERENCES "ReportingEvent" (id)
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
	display TEXT, 
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
	"fileType" TEXT, 
	location TEXT, 
	style TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY (name, "fileType", location, style, "Output_id"), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "OutputFileType" (
	"controlledTerm" VARCHAR(3) NOT NULL, 
	"sponsorTermId" TEXT, 
	PRIMARY KEY ("controlledTerm", "sponsorTermId"), 
	FOREIGN KEY("sponsorTermId") REFERENCES "SponsorTerm" (id)
);

CREATE TABLE "ResultGroup" (
	"groupingId" TEXT, 
	"groupId" TEXT, 
	"groupValue" TEXT, 
	PRIMARY KEY ("groupingId", "groupId", "groupValue"), 
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

CREATE TABLE "SubjectGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	"ReportingEvent_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReportingEvent_id") REFERENCES "ReportingEvent" (id)
);

CREATE TABLE "TerminologyExtension" (
	id TEXT NOT NULL, 
	enumeration VARCHAR(19), 
	"sponsorTerms" TEXT NOT NULL, 
	"ReportingEvent_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReportingEvent_id") REFERENCES "ReportingEvent" (id)
);

CREATE TABLE "AnalysisGroup" (
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	id TEXT NOT NULL, 
	label TEXT, 
	"compoundExpression" TEXT, 
	"SubjectGroupingFactor_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SubjectGroupingFactor_id") REFERENCES "SubjectGroupingFactor" (id)
);

CREATE TABLE "DataGroup" (
	level INTEGER, 
	"order" INTEGER, 
	condition TEXT, 
	id TEXT NOT NULL, 
	label TEXT, 
	"compoundExpression" TEXT, 
	"DataGroupingFactor_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataGroupingFactor_id") REFERENCES "DataGroupingFactor" (id)
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
	"groupingId" TEXT, 
	"resultsByGroup" BOOLEAN NOT NULL, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("order", "groupingId", "resultsByGroup", "Analysis_id"), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);

CREATE TABLE "OrderedListItem" (
	name TEXT NOT NULL, 
	level INTEGER NOT NULL, 
	"order" INTEGER NOT NULL, 
	sublist TEXT, 
	"analysisId" TEXT, 
	"outputId" TEXT, 
	PRIMARY KEY (name, level, "order", sublist, "analysisId", "outputId"), 
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
	"referencedOperationId" TEXT, 
	"analysisId" TEXT NOT NULL, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("referencedOperationId", "analysisId", "Analysis_id"), 
	FOREIGN KEY("referencedOperationId") REFERENCES "ReferencedOperationRelationship" (id), 
	FOREIGN KEY("analysisId") REFERENCES "Analysis" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);
