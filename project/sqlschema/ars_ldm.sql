

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
	PRIMARY KEY (id)
);

CREATE TABLE "AnalysisSet" (
	id TEXT NOT NULL, 
	condition TEXT, 
	label TEXT, 
	"order" INTEGER NOT NULL, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "CompoundExpression" (
	"logicalOperator" VARCHAR(3) NOT NULL, 
	"whereClauses" TEXT, 
	PRIMARY KEY ("logicalOperator", "whereClauses")
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

CREATE TABLE "Condition" (
	dataset TEXT, 
	variable TEXT, 
	comparator VARCHAR(5), 
	value TEXT, 
	PRIMARY KEY (dataset, variable, comparator, value)
);

CREATE TABLE "DataGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataSubset" (
	id TEXT NOT NULL, 
	condition TEXT, 
	label TEXT, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Display" (
	name TEXT NOT NULL, 
	id TEXT NOT NULL, 
	version INTEGER, 
	"displayTitle" TEXT, 
	"displaySections" TEXT, 
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
	id TEXT NOT NULL, 
	condition TEXT, 
	label TEXT, 
	"order" INTEGER NOT NULL, 
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

CREATE TABLE "ReportingEvent" (
	name TEXT NOT NULL, 
	"listOfPlannedAnalyses" TEXT NOT NULL, 
	"listOfPlannedOutputs" TEXT, 
	"analysisSets" TEXT, 
	"analysisGroupings" TEXT, 
	"dataSubsets" TEXT, 
	"globalDisplaySections" TEXT, 
	"analysisCategorizations" TEXT, 
	analyses TEXT, 
	methods TEXT, 
	outputs TEXT, 
	PRIMARY KEY (name, "listOfPlannedAnalyses", "listOfPlannedOutputs", "analysisSets", "analysisGroupings", "dataSubsets", "globalDisplaySections", "analysisCategorizations", analyses, methods, outputs)
);

CREATE TABLE "SubjectGroupingFactor" (
	id TEXT NOT NULL, 
	label TEXT, 
	"groupingVariable" TEXT, 
	"dataDriven" BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "WhereClause" (
	id TEXT NOT NULL, 
	condition TEXT, 
	"compoundExpression" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Analysis" (
	id TEXT NOT NULL, 
	version INTEGER, 
	"categoryIds" TEXT, 
	"analysisSetId" TEXT, 
	"dataSubsetId" TEXT, 
	dataset TEXT, 
	variable TEXT, 
	"methodId" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("analysisSetId") REFERENCES "AnalysisSet" (id), 
	FOREIGN KEY("dataSubsetId") REFERENCES "DataSubset" (id), 
	FOREIGN KEY("methodId") REFERENCES "AnalysisMethod" (id)
);

CREATE TABLE "AnalysisGroup" (
	id TEXT NOT NULL, 
	condition TEXT, 
	label TEXT, 
	"order" INTEGER NOT NULL, 
	"compoundExpression" TEXT, 
	"SubjectGroupingFactor_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SubjectGroupingFactor_id") REFERENCES "SubjectGroupingFactor" (id)
);

CREATE TABLE "DataGroup" (
	id TEXT NOT NULL, 
	condition TEXT, 
	label TEXT, 
	"order" INTEGER NOT NULL, 
	"compoundExpression" TEXT, 
	"DataGroupingFactor_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataGroupingFactor_id") REFERENCES "DataGroupingFactor" (id)
);

CREATE TABLE "File" (
	name TEXT NOT NULL, 
	"fileType" VARCHAR(3), 
	location TEXT, 
	style TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY (name, "fileType", location, style, "Output_id"), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "OutputDisplay" (
	"order" INTEGER NOT NULL, 
	display TEXT, 
	"Output_id" TEXT, 
	PRIMARY KEY ("order", display, "Output_id"), 
	FOREIGN KEY(display) REFERENCES "Display" (id), 
	FOREIGN KEY("Output_id") REFERENCES "Output" (id)
);

CREATE TABLE "ResultGroup" (
	"groupingId" TEXT, 
	"groupId" TEXT, 
	"groupValue" TEXT, 
	PRIMARY KEY ("groupingId", "groupId", "groupValue"), 
	FOREIGN KEY("groupId") REFERENCES "Group" (id)
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
	"dataGrouping" TEXT, 
	"Analysis_id" TEXT, 
	PRIMARY KEY ("order", "groupingId", "dataGrouping", "Analysis_id"), 
	FOREIGN KEY("dataGrouping") REFERENCES "DataGroupingFactor" (id), 
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);

CREATE TABLE "OrderedListItem" (
	name TEXT NOT NULL, 
	"order" INTEGER NOT NULL, 
	sublist TEXT, 
	"analysisId" TEXT, 
	"outputId" TEXT, 
	PRIMARY KEY (name, "order", sublist, "analysisId", "outputId"), 
	FOREIGN KEY("analysisId") REFERENCES "Analysis" (id), 
	FOREIGN KEY("outputId") REFERENCES "Output" (id)
);

CREATE TABLE "ReferencedOperationRelationship" (
	id TEXT NOT NULL, 
	"referencedOperationRole" VARCHAR(11) NOT NULL, 
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