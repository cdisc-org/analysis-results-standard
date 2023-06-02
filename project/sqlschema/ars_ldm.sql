

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
	"codeTemplate" TEXT, 
	PRIMARY KEY (id)
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

CREATE TABLE "CodeParameter" (
	name TEXT NOT NULL, 
	description TEXT, 
	"valueSource" TEXT, 
	PRIMARY KEY (name, description, "valueSource")
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

CREATE TABLE "DataGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
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

CREATE TABLE "DisplaySection" (
	"sectionType" VARCHAR(15), 
	"subSections" TEXT, 
	PRIMARY KEY ("sectionType", "subSections")
);

CREATE TABLE "DisplaySubSection" (
	id TEXT NOT NULL, 
	"order" INTEGER NOT NULL, 
	text TEXT, 
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
	id TEXT NOT NULL, 
	version INTEGER, 
	"categoryIds" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OutputDisplay" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"displayTitle" TEXT, 
	"displaySections" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PageNameList" (
	"pageNames" INTEGER NOT NULL, 
	PRIMARY KEY ("pageNames")
);

CREATE TABLE "PageNameRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	pages TEXT, 
	PRIMARY KEY (label, "refType", pages)
);

CREATE TABLE "PageNumberList" (
	"pageNumbers" INTEGER NOT NULL, 
	PRIMARY KEY ("pageNumbers")
);

CREATE TABLE "PageNumberListRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	pages TEXT, 
	PRIMARY KEY (label, "refType", pages)
);

CREATE TABLE "PageNumberRangeRef" (
	label TEXT, 
	"refType" VARCHAR(16) NOT NULL, 
	pages TEXT, 
	PRIMARY KEY (label, "refType", pages)
);

CREATE TABLE "PageRange" (
	"firstPage" INTEGER NOT NULL, 
	"lastPage" INTEGER NOT NULL, 
	PRIMARY KEY ("firstPage", "lastPage")
);

CREATE TABLE "PageRef" (
	"refType" VARCHAR(16) NOT NULL, 
	label TEXT, 
	pages TEXT, 
	PRIMARY KEY ("refType", label, pages)
);

CREATE TABLE "ProgrammingCodeTemplate" (
	context TEXT NOT NULL, 
	parameters TEXT, 
	"templateCode" TEXT, 
	PRIMARY KEY (context, parameters, "templateCode")
);

CREATE TABLE "ReferenceDocument" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	location TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReportingEvent" (
	name TEXT NOT NULL, 
	"listOfPlannedAnalyses" TEXT NOT NULL, 
	"listOfPlannedOutputs" TEXT, 
	"analysisSets" TEXT, 
	"analysisGroupings" TEXT, 
	"dataSubsets" TEXT, 
	"dataGroupings" TEXT, 
	"globalDisplaySections" TEXT, 
	"analysisCategorizations" TEXT, 
	analyses TEXT, 
	methods TEXT, 
	outputs TEXT, 
	"referenceDocuments" TEXT, 
	"terminologyExtentions" TEXT, 
	PRIMARY KEY (name, "listOfPlannedAnalyses", "listOfPlannedOutputs", "analysisSets", "analysisGroupings", "dataSubsets", "dataGroupings", "globalDisplaySections", "analysisCategorizations", analyses, methods, outputs, "referenceDocuments", "terminologyExtentions")
);

CREATE TABLE "SponsorTerm" (
	id TEXT NOT NULL, 
	"submissionValue" TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SubjectGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TerminologyExtension" (
	enumeration VARCHAR(15), 
	"sponsorTerms" TEXT NOT NULL, 
	PRIMARY KEY (enumeration, "sponsorTerms")
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
	"analysisSetId" TEXT, 
	"dataSubsetId" TEXT, 
	dataset TEXT, 
	variable TEXT, 
	"methodId" TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("analysisSetId") REFERENCES "AnalysisSet" (id), 
	FOREIGN KEY("dataSubsetId") REFERENCES "DataSubset" (id), 
	FOREIGN KEY("methodId") REFERENCES "AnalysisMethod" (id)
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

CREATE TABLE "File" (
	name TEXT NOT NULL, 
	"fileType" TEXT, 
	location TEXT, 
	style TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY (name, "fileType", location, style, "Output_id"), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "OrderedDisplay" (
	"order" INTEGER NOT NULL, 
	display TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY ("order", display, "Output_id"), 
	FOREIGN KEY(display) REFERENCES "OutputDisplay" (id), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "ResultGroup" (
	"groupingId" TEXT, 
	"groupId" TEXT, 
	"groupValue" TEXT, 
	PRIMARY KEY ("groupingId", "groupId", "groupValue"), 
	FOREIGN KEY("groupId") REFERENCES "Group" (id)
);

CREATE TABLE "DocumentRef" (
	"referenceDocumentId" TEXT NOT NULL, 
	"pageRefs" TEXT, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("referenceDocumentId", "pageRefs", "Analysis_id"), 
	FOREIGN KEY("referenceDocumentId") REFERENCES "ReferenceDocument" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
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
