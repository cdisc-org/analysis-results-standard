
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

from .ars_ldm import *

@dataclass
class ArsLdmAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # NamedObject methods
    # --
    def fetch_NamedObject(self, id_value: str) -> NamedObject:
        """
        Retrieves an instance of `NamedObject` via a primary key

        :param id_value:
        :return: NamedObject with matching ID
        """
        q = FetchById(id=id_value, target_class=NamedObject.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_NamedObject(self,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[NamedObject]:
        """
        Queries for instances of `NamedObject`

        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(NamedObject.class_name,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ReportingEvent methods
    # --
    def fetch_ReportingEvent(self, id_value: str) -> ReportingEvent:
        """
        Retrieves an instance of `ReportingEvent` via a primary key

        :param id_value:
        :return: ReportingEvent with matching ID
        """
        q = FetchById(id=id_value, target_class=ReportingEvent.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ReportingEvent(self,
             id: Union[str, MatchExpression] = None,
             version: Union[str, MatchExpression] = None,
             listOfPlannedAnalyses: Union[str, MatchExpression] = None,
             listOfPlannedOutputs: Union[str, MatchExpression] = None,
             analysisSets: Union[str, MatchExpression] = None,
             analysisGroupings: Union[str, MatchExpression] = None,
             dataSubsets: Union[str, MatchExpression] = None,
             dataGroupings: Union[str, MatchExpression] = None,
             globalDisplaySections: Union[str, MatchExpression] = None,
             analysisCategorizations: Union[str, MatchExpression] = None,
             analyses: Union[str, MatchExpression] = None,
             methods: Union[str, MatchExpression] = None,
             outputs: Union[str, MatchExpression] = None,
             referenceDocuments: Union[str, MatchExpression] = None,
             terminologyExtensions: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReportingEvent]:
        """
        Queries for instances of `ReportingEvent`

        :param id: The assigned identifying value for the instance of the class.
        :param version: None
        :param listOfPlannedAnalyses: A structured list of the analyses defined for the reporting event.
        :param listOfPlannedOutputs: An optional structured list of the outputs defined for the reporting event.
        :param analysisSets: The analysis sets (subject populations) defined for the reporting event.
        :param analysisGroupings: Characteristics used to subdivide the subject population (e.g., treatment, sex, age group).
        :param dataSubsets: Subsets of data identified by selection criteria for inclusion in analysis definitions.
        :param dataGroupings: Characteristics used to subdivide data records in analysis datasets (e.g., visit, system organ class).
        :param globalDisplaySections: None
        :param analysisCategorizations: Sets of related implementer-defined categories that can be used to categorize analyses or outputs.
        :param analyses: The analyses defined for the reporting event.
        :param methods: The defined methods used to analyze any analysis variable.
        :param outputs: The outputs defined for the reporting event.
        :param referenceDocuments: None
        :param terminologyExtensions: Any sponsor-defined extensions to extensible terminology.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReportingEvent.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 listOfPlannedAnalyses=listOfPlannedAnalyses,
                                                 
                                                 listOfPlannedOutputs=listOfPlannedOutputs,
                                                 
                                                 analysisSets=analysisSets,
                                                 
                                                 analysisGroupings=analysisGroupings,
                                                 
                                                 dataSubsets=dataSubsets,
                                                 
                                                 dataGroupings=dataGroupings,
                                                 
                                                 globalDisplaySections=globalDisplaySections,
                                                 
                                                 analysisCategorizations=analysisCategorizations,
                                                 
                                                 analyses=analyses,
                                                 
                                                 methods=methods,
                                                 
                                                 outputs=outputs,
                                                 
                                                 referenceDocuments=referenceDocuments,
                                                 
                                                 terminologyExtensions=terminologyExtensions,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # NestedList methods
    # --
    def fetch_NestedList(self, id_value: str) -> NestedList:
        """
        Retrieves an instance of `NestedList` via a primary key

        :param id_value:
        :return: NestedList with matching ID
        """
        q = FetchById(id=id_value, target_class=NestedList.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_NestedList(self,
             listItems: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[NestedList]:
        """
        Queries for instances of `NestedList`

        :param listItems: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(NestedList.class_name,
                                                 
                                                 listItems=listItems,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedListItem methods
    # --
    def fetch_OrderedListItem(self, id_value: str) -> OrderedListItem:
        """
        Retrieves an instance of `OrderedListItem` via a primary key

        :param id_value:
        :return: OrderedListItem with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedListItem.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedListItem(self,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             sublist: Union[str, MatchExpression] = None,
             analysisId: Union[str, MatchExpression] = None,
             outputId: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedListItem]:
        """
        Queries for instances of `OrderedListItem`

        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param sublist: A sub-list of items (analyses or outputs) that may be further organized within sub-lists.
        :param analysisId: The identifier of the referenced analysis.
        :param outputId: The identifier of the referenced output.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedListItem.class_name,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 sublist=sublist,
                                                 
                                                 analysisId=analysisId,
                                                 
                                                 outputId=outputId,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisCategorization methods
    # --
    def fetch_AnalysisCategorization(self, id_value: str) -> AnalysisCategorization:
        """
        Retrieves an instance of `AnalysisCategorization` via a primary key

        :param id_value:
        :return: AnalysisCategorization with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisCategorization.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisCategorization(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             categories: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisCategorization]:
        """
        Queries for instances of `AnalysisCategorization`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param categories: Implementer-defined categories of analyses/outputs, each of which may include one or more sub-categorization.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisCategorization.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 categories=categories,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisCategory methods
    # --
    def fetch_AnalysisCategory(self, id_value: str) -> AnalysisCategory:
        """
        Retrieves an instance of `AnalysisCategory` via a primary key

        :param id_value:
        :return: AnalysisCategory with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisCategory.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisCategory(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             subCategorizations: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisCategory]:
        """
        Queries for instances of `AnalysisCategory`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param subCategorizations: Sets of related implementer-defined sub-categories that can be used to categorize analyses or outputs.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisCategory.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 subCategorizations=subCategorizations,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Analysis methods
    # --
    def fetch_Analysis(self, id_value: str) -> Analysis:
        """
        Retrieves an instance of `Analysis` via a primary key

        :param id_value:
        :return: Analysis with matching ID
        """
        q = FetchById(id=id_value, target_class=Analysis.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Analysis(self,
             id: Union[str, MatchExpression] = None,
             version: Union[str, MatchExpression] = None,
             categoryIds: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             reason: Union[str, MatchExpression] = None,
             purpose: Union[str, MatchExpression] = None,
             documentRefs: Union[str, MatchExpression] = None,
             analysisSetId: Union[str, MatchExpression] = None,
             orderedGroupings: Union[str, MatchExpression] = None,
             dataSubsetId: Union[str, MatchExpression] = None,
             dataset: Union[str, MatchExpression] = None,
             variable: Union[str, MatchExpression] = None,
             methodId: Union[str, MatchExpression] = None,
             referencedAnalysisOperations: Union[str, MatchExpression] = None,
             programmingCode: Union[str, MatchExpression] = None,
             results: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Analysis]:
        """
        Queries for instances of `Analysis`

        :param id: The assigned identifying value for the instance of the class.
        :param version: None
        :param categoryIds: References to any implementer-defined categories that apply to the analysis.
        :param description: A textual description of the instance of the class.
        :param reason: The rationale for performing this analysis. It indicates when the analysis was planned.
        :param purpose: The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).
        :param documentRefs: None
        :param analysisSetId: The identifier of the referenced analysis set.
        :param orderedGroupings: An ordered list of grouping factors used in the analysis.
        :param dataSubsetId: The identifier of the referenced data subset.
        :param dataset: None
        :param variable: None
        :param methodId: A reference to the set of one or more statistical operations performed for the analysis.
        :param referencedAnalysisOperations: Indications of which analysis contains the results for each referenced operation.
        :param programmingCode: Programming statements and/or a reference to the program used to perform the specific analysis.
        :param results: None
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Analysis.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 categoryIds=categoryIds,
                                                 
                                                 description=description,
                                                 
                                                 reason=reason,
                                                 
                                                 purpose=purpose,
                                                 
                                                 documentRefs=documentRefs,
                                                 
                                                 analysisSetId=analysisSetId,
                                                 
                                                 orderedGroupings=orderedGroupings,
                                                 
                                                 dataSubsetId=dataSubsetId,
                                                 
                                                 dataset=dataset,
                                                 
                                                 variable=variable,
                                                 
                                                 methodId=methodId,
                                                 
                                                 referencedAnalysisOperations=referencedAnalysisOperations,
                                                 
                                                 programmingCode=programmingCode,
                                                 
                                                 results=results,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedGroupingFactor methods
    # --
    def fetch_OrderedGroupingFactor(self, id_value: str) -> OrderedGroupingFactor:
        """
        Retrieves an instance of `OrderedGroupingFactor` via a primary key

        :param id_value:
        :return: OrderedGroupingFactor with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedGroupingFactor.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedGroupingFactor(self,
             order: Union[str, MatchExpression] = None,
             groupingId: Union[str, MatchExpression] = None,
             resultsByGroup: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedGroupingFactor]:
        """
        Queries for instances of `OrderedGroupingFactor`

        :param order: The ordinal of the instance with respect to other instances.
        :param groupingId: The identifier of the referenced subject or data grouping factor.
        :param resultsByGroup: Indicates whether a result is expected for each group in the grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedGroupingFactor.class_name,
                                                 
                                                 order=order,
                                                 
                                                 groupingId=groupingId,
                                                 
                                                 resultsByGroup=resultsByGroup,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ReferencedAnalysisOperation methods
    # --
    def fetch_ReferencedAnalysisOperation(self, id_value: str) -> ReferencedAnalysisOperation:
        """
        Retrieves an instance of `ReferencedAnalysisOperation` via a primary key

        :param id_value:
        :return: ReferencedAnalysisOperation with matching ID
        """
        q = FetchById(id=id_value, target_class=ReferencedAnalysisOperation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ReferencedAnalysisOperation(self,
             referencedOperationRelationshipId: Union[str, MatchExpression] = None,
             analysisId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReferencedAnalysisOperation]:
        """
        Queries for instances of `ReferencedAnalysisOperation`

        :param referencedOperationRelationshipId: The identifier of the defined referenced operation relationship.
        :param analysisId: The identifier of the referenced analysis.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReferencedAnalysisOperation.class_name,
                                                 
                                                 referencedOperationRelationshipId=referencedOperationRelationshipId,
                                                 
                                                 analysisId=analysisId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OperationResult methods
    # --
    def fetch_OperationResult(self, id_value: str) -> OperationResult:
        """
        Retrieves an instance of `OperationResult` via a primary key

        :param id_value:
        :return: OperationResult with matching ID
        """
        q = FetchById(id=id_value, target_class=OperationResult.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OperationResult(self,
             operationId: Union[str, MatchExpression] = None,
             resultGroups: Union[str, MatchExpression] = None,
             rawValue: Union[str, MatchExpression] = None,
             formattedValue: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OperationResult]:
        """
        Queries for instances of `OperationResult`

        :param operationId: The identifier of the referenced operation.
        :param resultGroups: None
        :param rawValue: None
        :param formattedValue: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OperationResult.class_name,
                                                 
                                                 operationId=operationId,
                                                 
                                                 resultGroups=resultGroups,
                                                 
                                                 rawValue=rawValue,
                                                 
                                                 formattedValue=formattedValue,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ResultGroup methods
    # --
    def fetch_ResultGroup(self, id_value: str) -> ResultGroup:
        """
        Retrieves an instance of `ResultGroup` via a primary key

        :param id_value:
        :return: ResultGroup with matching ID
        """
        q = FetchById(id=id_value, target_class=ResultGroup.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ResultGroup(self,
             groupingId: Union[str, MatchExpression] = None,
             groupId: Union[str, MatchExpression] = None,
             groupValue: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ResultGroup]:
        """
        Queries for instances of `ResultGroup`

        :param groupingId: The identifier of the referenced subject or data grouping factor.
        :param groupId: The identifier of a referenced predefined group within a grouping.
        :param groupValue: The data value used as a group within a data-driven grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ResultGroup.class_name,
                                                 
                                                 groupingId=groupingId,
                                                 
                                                 groupId=groupId,
                                                 
                                                 groupValue=groupValue,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisMethod methods
    # --
    def fetch_AnalysisMethod(self, id_value: str) -> AnalysisMethod:
        """
        Retrieves an instance of `AnalysisMethod` via a primary key

        :param id_value:
        :return: AnalysisMethod with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisMethod.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisMethod(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             operations: Union[str, MatchExpression] = None,
             documentRefs: Union[str, MatchExpression] = None,
             codeTemplate: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisMethod]:
        """
        Queries for instances of `AnalysisMethod`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param description: A textual description of the instance of the class.
        :param operations: The calculations performed for the method. Each operation generates a statistical result.
        :param documentRefs: None
        :param codeTemplate: Template programming statements and/or a reference to the template program used to perform the specific analysis.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisMethod.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 description=description,
                                                 
                                                 operations=operations,
                                                 
                                                 documentRefs=documentRefs,
                                                 
                                                 codeTemplate=codeTemplate,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Operation methods
    # --
    def fetch_Operation(self, id_value: str) -> Operation:
        """
        Retrieves an instance of `Operation` via a primary key

        :param id_value:
        :return: Operation with matching ID
        """
        q = FetchById(id=id_value, target_class=Operation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Operation(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             referencedOperationRelationships: Union[str, MatchExpression] = None,
             resultPattern: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Operation]:
        """
        Queries for instances of `Operation`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param referencedOperationRelationships: None
        :param resultPattern: None
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Operation.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 referencedOperationRelationships=referencedOperationRelationships,
                                                 
                                                 resultPattern=resultPattern,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ReferencedOperationRelationship methods
    # --
    def fetch_ReferencedOperationRelationship(self, id_value: str) -> ReferencedOperationRelationship:
        """
        Retrieves an instance of `ReferencedOperationRelationship` via a primary key

        :param id_value:
        :return: ReferencedOperationRelationship with matching ID
        """
        q = FetchById(id=id_value, target_class=ReferencedOperationRelationship.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ReferencedOperationRelationship(self,
             id: Union[str, MatchExpression] = None,
             referencedOperationRole: Union[str, MatchExpression] = None,
             operationId: Union[str, MatchExpression] = None,
             analysisId: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReferencedOperationRelationship]:
        """
        Queries for instances of `ReferencedOperationRelationship`

        :param id: The assigned identifying value for the instance of the class.
        :param referencedOperationRole: None
        :param operationId: The identifier of the referenced operation.
        :param analysisId: The identifier of the referenced analysis.
        :param description: A textual description of the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReferencedOperationRelationship.class_name,
                                                 
                                                 id=id,
                                                 
                                                 referencedOperationRole=referencedOperationRole,
                                                 
                                                 operationId=operationId,
                                                 
                                                 analysisId=analysisId,
                                                 
                                                 description=description,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisOutputProgrammingCode methods
    # --
    def fetch_AnalysisOutputProgrammingCode(self, id_value: str) -> AnalysisOutputProgrammingCode:
        """
        Retrieves an instance of `AnalysisOutputProgrammingCode` via a primary key

        :param id_value:
        :return: AnalysisOutputProgrammingCode with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisOutputProgrammingCode.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisOutputProgrammingCode(self,
             context: Union[str, MatchExpression] = None,
             code: Union[str, MatchExpression] = None,
             documentRef: Union[str, MatchExpression] = None,
             parameters: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisOutputProgrammingCode]:
        """
        Queries for instances of `AnalysisOutputProgrammingCode`

        :param context: The name and version of the computer language used for the actual programming statements provided.
        :param code: Programming statements used to perform the specific analysis.
        :param documentRef: None
        :param parameters: Parameter values used to generate or execute the programming code.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisOutputProgrammingCode.class_name,
                                                 
                                                 context=context,
                                                 
                                                 code=code,
                                                 
                                                 documentRef=documentRef,
                                                 
                                                 parameters=parameters,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisProgrammingCodeTemplate methods
    # --
    def fetch_AnalysisProgrammingCodeTemplate(self, id_value: str) -> AnalysisProgrammingCodeTemplate:
        """
        Retrieves an instance of `AnalysisProgrammingCodeTemplate` via a primary key

        :param id_value:
        :return: AnalysisProgrammingCodeTemplate with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisProgrammingCodeTemplate.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisProgrammingCodeTemplate(self,
             context: Union[str, MatchExpression] = None,
             code: Union[str, MatchExpression] = None,
             documentRef: Union[str, MatchExpression] = None,
             parameters: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisProgrammingCodeTemplate]:
        """
        Queries for instances of `AnalysisProgrammingCodeTemplate`

        :param context: The name and version of the computer language used for the actual programming statements provided.
        :param code: Programming statements used to perform the specific analysis.
        :param documentRef: None
        :param parameters: Parameters whose values will be used to generate or execute the programming code for a specific analysis.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisProgrammingCodeTemplate.class_name,
                                                 
                                                 context=context,
                                                 
                                                 code=code,
                                                 
                                                 documentRef=documentRef,
                                                 
                                                 parameters=parameters,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CodeParameter methods
    # --
    def fetch_CodeParameter(self, id_value: str) -> CodeParameter:
        """
        Retrieves an instance of `CodeParameter` via a primary key

        :param id_value:
        :return: CodeParameter with matching ID
        """
        q = FetchById(id=id_value, target_class=CodeParameter.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CodeParameter(self,
             description: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CodeParameter]:
        """
        Queries for instances of `CodeParameter`

        :param description: A textual description of the instance of the class.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CodeParameter.class_name,
                                                 
                                                 description=description,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisOutputCodeParameter methods
    # --
    def fetch_AnalysisOutputCodeParameter(self, id_value: str) -> AnalysisOutputCodeParameter:
        """
        Retrieves an instance of `AnalysisOutputCodeParameter` via a primary key

        :param id_value:
        :return: AnalysisOutputCodeParameter with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisOutputCodeParameter.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisOutputCodeParameter(self,
             value: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisOutputCodeParameter]:
        """
        Queries for instances of `AnalysisOutputCodeParameter`

        :param value: The value of the parameter.
        :param description: A textual description of the instance of the class.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisOutputCodeParameter.class_name,
                                                 
                                                 value=value,
                                                 
                                                 description=description,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # TemplateCodeParameter methods
    # --
    def fetch_TemplateCodeParameter(self, id_value: str) -> TemplateCodeParameter:
        """
        Retrieves an instance of `TemplateCodeParameter` via a primary key

        :param id_value:
        :return: TemplateCodeParameter with matching ID
        """
        q = FetchById(id=id_value, target_class=TemplateCodeParameter.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_TemplateCodeParameter(self,
             valueSource: Union[str, MatchExpression] = None,
             value: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[TemplateCodeParameter]:
        """
        Queries for instances of `TemplateCodeParameter`

        :param valueSource: A reference to the prespecified source of the value for the parameter.
        :param value: The value to be used for the parameter when the method is used in an analysis. Multiple values may be specified to indicate a choice.
        :param description: A textual description of the instance of the class.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(TemplateCodeParameter.class_name,
                                                 
                                                 valueSource=valueSource,
                                                 
                                                 value=value,
                                                 
                                                 description=description,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Output methods
    # --
    def fetch_Output(self, id_value: str) -> Output:
        """
        Retrieves an instance of `Output` via a primary key

        :param id_value:
        :return: Output with matching ID
        """
        q = FetchById(id=id_value, target_class=Output.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Output(self,
             id: Union[str, MatchExpression] = None,
             version: Union[str, MatchExpression] = None,
             fileSpecifications: Union[str, MatchExpression] = None,
             displays: Union[str, MatchExpression] = None,
             categoryIds: Union[str, MatchExpression] = None,
             documentRefs: Union[str, MatchExpression] = None,
             programmingCode: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Output]:
        """
        Queries for instances of `Output`

        :param id: The assigned identifying value for the instance of the class.
        :param version: None
        :param fileSpecifications: None
        :param displays: None
        :param categoryIds: References to any implementer-defined categories that apply to the output.
        :param documentRefs: None
        :param programmingCode: Programming statements and/or a reference to the program used to perform the specific output.
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Output.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 fileSpecifications=fileSpecifications,
                                                 
                                                 displays=displays,
                                                 
                                                 categoryIds=categoryIds,
                                                 
                                                 documentRefs=documentRefs,
                                                 
                                                 programmingCode=programmingCode,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OutputFile methods
    # --
    def fetch_OutputFile(self, id_value: str) -> OutputFile:
        """
        Retrieves an instance of `OutputFile` via a primary key

        :param id_value:
        :return: OutputFile with matching ID
        """
        q = FetchById(id=id_value, target_class=OutputFile.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OutputFile(self,
             fileType: Union[str, MatchExpression] = None,
             location: Union[str, MatchExpression] = None,
             style: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OutputFile]:
        """
        Queries for instances of `OutputFile`

        :param fileType: None
        :param location: None
        :param style: None
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OutputFile.class_name,
                                                 
                                                 fileType=fileType,
                                                 
                                                 location=location,
                                                 
                                                 style=style,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedDisplay methods
    # --
    def fetch_OrderedDisplay(self, id_value: str) -> OrderedDisplay:
        """
        Retrieves an instance of `OrderedDisplay` via a primary key

        :param id_value:
        :return: OrderedDisplay with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedDisplay.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedDisplay(self,
             order: Union[str, MatchExpression] = None,
             display: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedDisplay]:
        """
        Queries for instances of `OrderedDisplay`

        :param order: The ordinal of the instance with respect to other instances.
        :param display: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedDisplay.class_name,
                                                 
                                                 order=order,
                                                 
                                                 display=display,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OutputDisplay methods
    # --
    def fetch_OutputDisplay(self, id_value: str) -> OutputDisplay:
        """
        Retrieves an instance of `OutputDisplay` via a primary key

        :param id_value:
        :return: OutputDisplay with matching ID
        """
        q = FetchById(id=id_value, target_class=OutputDisplay.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OutputDisplay(self,
             id: Union[str, MatchExpression] = None,
             version: Union[str, MatchExpression] = None,
             displayTitle: Union[str, MatchExpression] = None,
             displaySections: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OutputDisplay]:
        """
        Queries for instances of `OutputDisplay`

        :param id: The assigned identifying value for the instance of the class.
        :param version: None
        :param displayTitle: None
        :param displaySections: None
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OutputDisplay.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 displayTitle=displayTitle,
                                                 
                                                 displaySections=displaySections,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DisplaySection methods
    # --
    def fetch_DisplaySection(self, id_value: str) -> DisplaySection:
        """
        Retrieves an instance of `DisplaySection` via a primary key

        :param id_value:
        :return: DisplaySection with matching ID
        """
        q = FetchById(id=id_value, target_class=DisplaySection.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DisplaySection(self,
             sectionType: Union[str, MatchExpression] = None,
             orderedSubSections: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DisplaySection]:
        """
        Queries for instances of `DisplaySection`

        :param sectionType: None
        :param orderedSubSections: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DisplaySection.class_name,
                                                 
                                                 sectionType=sectionType,
                                                 
                                                 orderedSubSections=orderedSubSections,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedDisplaySubSection methods
    # --
    def fetch_OrderedDisplaySubSection(self, id_value: str) -> OrderedDisplaySubSection:
        """
        Retrieves an instance of `OrderedDisplaySubSection` via a primary key

        :param id_value:
        :return: OrderedDisplaySubSection with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedDisplaySubSection.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedDisplaySubSection(self,
             order: Union[str, MatchExpression] = None,
             subSection: Union[str, MatchExpression] = None,
             subSectionId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedDisplaySubSection]:
        """
        Queries for instances of `OrderedDisplaySubSection`

        :param order: The ordinal of the instance with respect to other instances.
        :param subSection: None
        :param subSectionId: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedDisplaySubSection.class_name,
                                                 
                                                 order=order,
                                                 
                                                 subSection=subSection,
                                                 
                                                 subSectionId=subSectionId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedSubSection methods
    # --
    def fetch_OrderedSubSection(self, id_value: str) -> OrderedSubSection:
        """
        Retrieves an instance of `OrderedSubSection` via a primary key

        :param id_value:
        :return: OrderedSubSection with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedSubSection.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedSubSection(self,
             order: Union[str, MatchExpression] = None,
             subSection: Union[str, MatchExpression] = None,
             subSectionId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedSubSection]:
        """
        Queries for instances of `OrderedSubSection`

        :param order: The ordinal of the instance with respect to other instances.
        :param subSection: None
        :param subSectionId: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedSubSection.class_name,
                                                 
                                                 order=order,
                                                 
                                                 subSection=subSection,
                                                 
                                                 subSectionId=subSectionId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OrderedSubSectionRef methods
    # --
    def fetch_OrderedSubSectionRef(self, id_value: str) -> OrderedSubSectionRef:
        """
        Retrieves an instance of `OrderedSubSectionRef` via a primary key

        :param id_value:
        :return: OrderedSubSectionRef with matching ID
        """
        q = FetchById(id=id_value, target_class=OrderedSubSectionRef.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OrderedSubSectionRef(self,
             order: Union[str, MatchExpression] = None,
             subSection: Union[str, MatchExpression] = None,
             subSectionId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedSubSectionRef]:
        """
        Queries for instances of `OrderedSubSectionRef`

        :param order: The ordinal of the instance with respect to other instances.
        :param subSection: NOT USED
        :param subSectionId: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedSubSectionRef.class_name,
                                                 
                                                 order=order,
                                                 
                                                 subSection=subSection,
                                                 
                                                 subSectionId=subSectionId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DisplaySubSection methods
    # --
    def fetch_DisplaySubSection(self, id_value: str) -> DisplaySubSection:
        """
        Retrieves an instance of `DisplaySubSection` via a primary key

        :param id_value:
        :return: DisplaySubSection with matching ID
        """
        q = FetchById(id=id_value, target_class=DisplaySubSection.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DisplaySubSection(self,
             id: Union[str, MatchExpression] = None,
             text: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DisplaySubSection]:
        """
        Queries for instances of `DisplaySubSection`

        :param id: The assigned identifying value for the instance of the class.
        :param text: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DisplaySubSection.class_name,
                                                 
                                                 id=id,
                                                 
                                                 text=text,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # GlobalDisplaySection methods
    # --
    def fetch_GlobalDisplaySection(self, id_value: str) -> GlobalDisplaySection:
        """
        Retrieves an instance of `GlobalDisplaySection` via a primary key

        :param id_value:
        :return: GlobalDisplaySection with matching ID
        """
        q = FetchById(id=id_value, target_class=GlobalDisplaySection.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_GlobalDisplaySection(self,
             sectionType: Union[str, MatchExpression] = None,
             subSections: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[GlobalDisplaySection]:
        """
        Queries for instances of `GlobalDisplaySection`

        :param sectionType: None
        :param subSections: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(GlobalDisplaySection.class_name,
                                                 
                                                 sectionType=sectionType,
                                                 
                                                 subSections=subSections,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # WhereClause methods
    # --
    def fetch_WhereClause(self, id_value: str) -> WhereClause:
        """
        Retrieves an instance of `WhereClause` via a primary key

        :param id_value:
        :return: WhereClause with matching ID
        """
        q = FetchById(id=id_value, target_class=WhereClause.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_WhereClause(self,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[WhereClause]:
        """
        Queries for instances of `WhereClause`

        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(WhereClause.class_name,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # WhereClauseCondition methods
    # --
    def fetch_WhereClauseCondition(self, id_value: str) -> WhereClauseCondition:
        """
        Retrieves an instance of `WhereClauseCondition` via a primary key

        :param id_value:
        :return: WhereClauseCondition with matching ID
        """
        q = FetchById(id=id_value, target_class=WhereClauseCondition.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_WhereClauseCondition(self,
             dataset: Union[str, MatchExpression] = None,
             variable: Union[str, MatchExpression] = None,
             comparator: Union[str, MatchExpression] = None,
             value: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[WhereClauseCondition]:
        """
        Queries for instances of `WhereClauseCondition`

        :param dataset: None
        :param variable: None
        :param comparator: None
        :param value: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(WhereClauseCondition.class_name,
                                                 
                                                 dataset=dataset,
                                                 
                                                 variable=variable,
                                                 
                                                 comparator=comparator,
                                                 
                                                 value=value,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # WhereClauseCompoundExpression methods
    # --
    def fetch_WhereClauseCompoundExpression(self, id_value: str) -> WhereClauseCompoundExpression:
        """
        Retrieves an instance of `WhereClauseCompoundExpression` via a primary key

        :param id_value:
        :return: WhereClauseCompoundExpression with matching ID
        """
        q = FetchById(id=id_value, target_class=WhereClauseCompoundExpression.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_WhereClauseCompoundExpression(self,
             logicalOperator: Union[str, MatchExpression] = None,
             whereClauses: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[WhereClauseCompoundExpression]:
        """
        Queries for instances of `WhereClauseCompoundExpression`

        :param logicalOperator: None
        :param whereClauses: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(WhereClauseCompoundExpression.class_name,
                                                 
                                                 logicalOperator=logicalOperator,
                                                 
                                                 whereClauses=whereClauses,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CompoundSetExpression methods
    # --
    def fetch_CompoundSetExpression(self, id_value: str) -> CompoundSetExpression:
        """
        Retrieves an instance of `CompoundSetExpression` via a primary key

        :param id_value:
        :return: CompoundSetExpression with matching ID
        """
        q = FetchById(id=id_value, target_class=CompoundSetExpression.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CompoundSetExpression(self,
             logicalOperator: Union[str, MatchExpression] = None,
             whereClauses: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CompoundSetExpression]:
        """
        Queries for instances of `CompoundSetExpression`

        :param logicalOperator: None
        :param whereClauses: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CompoundSetExpression.class_name,
                                                 
                                                 logicalOperator=logicalOperator,
                                                 
                                                 whereClauses=whereClauses,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CompoundGroupExpression methods
    # --
    def fetch_CompoundGroupExpression(self, id_value: str) -> CompoundGroupExpression:
        """
        Retrieves an instance of `CompoundGroupExpression` via a primary key

        :param id_value:
        :return: CompoundGroupExpression with matching ID
        """
        q = FetchById(id=id_value, target_class=CompoundGroupExpression.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CompoundGroupExpression(self,
             logicalOperator: Union[str, MatchExpression] = None,
             whereClauses: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CompoundGroupExpression]:
        """
        Queries for instances of `CompoundGroupExpression`

        :param logicalOperator: None
        :param whereClauses: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CompoundGroupExpression.class_name,
                                                 
                                                 logicalOperator=logicalOperator,
                                                 
                                                 whereClauses=whereClauses,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CompoundSubsetExpression methods
    # --
    def fetch_CompoundSubsetExpression(self, id_value: str) -> CompoundSubsetExpression:
        """
        Retrieves an instance of `CompoundSubsetExpression` via a primary key

        :param id_value:
        :return: CompoundSubsetExpression with matching ID
        """
        q = FetchById(id=id_value, target_class=CompoundSubsetExpression.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CompoundSubsetExpression(self,
             logicalOperator: Union[str, MatchExpression] = None,
             whereClauses: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CompoundSubsetExpression]:
        """
        Queries for instances of `CompoundSubsetExpression`

        :param logicalOperator: None
        :param whereClauses: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CompoundSubsetExpression.class_name,
                                                 
                                                 logicalOperator=logicalOperator,
                                                 
                                                 whereClauses=whereClauses,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisSet methods
    # --
    def fetch_AnalysisSet(self, id_value: str) -> AnalysisSet:
        """
        Retrieves an instance of `AnalysisSet` via a primary key

        :param id_value:
        :return: AnalysisSet with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisSet.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisSet(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisSet]:
        """
        Queries for instances of `AnalysisSet`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisSet.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # GroupingFactor methods
    # --
    def fetch_GroupingFactor(self, id_value: str) -> GroupingFactor:
        """
        Retrieves an instance of `GroupingFactor` via a primary key

        :param id_value:
        :return: GroupingFactor with matching ID
        """
        q = FetchById(id=id_value, target_class=GroupingFactor.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_GroupingFactor(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             groupingVariable: Union[str, MatchExpression] = None,
             dataDriven: Union[str, MatchExpression] = None,
             groups: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[GroupingFactor]:
        """
        Queries for instances of `GroupingFactor`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: The pre-specified groups within the grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(GroupingFactor.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 groupingVariable=groupingVariable,
                                                 
                                                 dataDriven=dataDriven,
                                                 
                                                 groups=groups,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SubjectGroupingFactor methods
    # --
    def fetch_SubjectGroupingFactor(self, id_value: str) -> SubjectGroupingFactor:
        """
        Retrieves an instance of `SubjectGroupingFactor` via a primary key

        :param id_value:
        :return: SubjectGroupingFactor with matching ID
        """
        q = FetchById(id=id_value, target_class=SubjectGroupingFactor.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SubjectGroupingFactor(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             groupingVariable: Union[str, MatchExpression] = None,
             dataDriven: Union[str, MatchExpression] = None,
             groups: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SubjectGroupingFactor]:
        """
        Queries for instances of `SubjectGroupingFactor`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: The pre-specified groups within the grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SubjectGroupingFactor.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 groupingVariable=groupingVariable,
                                                 
                                                 dataDriven=dataDriven,
                                                 
                                                 groups=groups,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DataGroupingFactor methods
    # --
    def fetch_DataGroupingFactor(self, id_value: str) -> DataGroupingFactor:
        """
        Retrieves an instance of `DataGroupingFactor` via a primary key

        :param id_value:
        :return: DataGroupingFactor with matching ID
        """
        q = FetchById(id=id_value, target_class=DataGroupingFactor.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DataGroupingFactor(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             groupingVariable: Union[str, MatchExpression] = None,
             dataDriven: Union[str, MatchExpression] = None,
             groups: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataGroupingFactor]:
        """
        Queries for instances of `DataGroupingFactor`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: The pre-specified groups within the grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataGroupingFactor.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 groupingVariable=groupingVariable,
                                                 
                                                 dataDriven=dataDriven,
                                                 
                                                 groups=groups,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Group methods
    # --
    def fetch_Group(self, id_value: str) -> Group:
        """
        Retrieves an instance of `Group` via a primary key

        :param id_value:
        :return: Group with matching ID
        """
        q = FetchById(id=id_value, target_class=Group.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Group(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Group]:
        """
        Queries for instances of `Group`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Group.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisGroup methods
    # --
    def fetch_AnalysisGroup(self, id_value: str) -> AnalysisGroup:
        """
        Retrieves an instance of `AnalysisGroup` via a primary key

        :param id_value:
        :return: AnalysisGroup with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisGroup.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisGroup(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisGroup]:
        """
        Queries for instances of `AnalysisGroup`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisGroup.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DataGroup methods
    # --
    def fetch_DataGroup(self, id_value: str) -> DataGroup:
        """
        Retrieves an instance of `DataGroup` via a primary key

        :param id_value:
        :return: DataGroup with matching ID
        """
        q = FetchById(id=id_value, target_class=DataGroup.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DataGroup(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataGroup]:
        """
        Queries for instances of `DataGroup`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataGroup.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DataSubset methods
    # --
    def fetch_DataSubset(self, id_value: str) -> DataSubset:
        """
        Retrieves an instance of `DataSubset` via a primary key

        :param id_value:
        :return: DataSubset with matching ID
        """
        q = FetchById(id=id_value, target_class=DataSubset.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DataSubset(self,
             id: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             level: Union[str, MatchExpression] = None,
             order: Union[str, MatchExpression] = None,
             condition: Union[str, MatchExpression] = None,
             compoundExpression: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataSubset]:
        """
        Queries for instances of `DataSubset`

        :param id: The assigned identifying value for the instance of the class.
        :param label: None
        :param level: The level of the entry within a hierarchical structure.
        :param order: The ordinal of the instance with respect to other instances.
        :param condition: None
        :param compoundExpression: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataSubset.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 level=level,
                                                 
                                                 order=order,
                                                 
                                                 condition=condition,
                                                 
                                                 compoundExpression=compoundExpression,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ReferenceDocument methods
    # --
    def fetch_ReferenceDocument(self, id_value: str) -> ReferenceDocument:
        """
        Retrieves an instance of `ReferenceDocument` via a primary key

        :param id_value:
        :return: ReferenceDocument with matching ID
        """
        q = FetchById(id=id_value, target_class=ReferenceDocument.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ReferenceDocument(self,
             id: Union[str, MatchExpression] = None,
             location: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReferenceDocument]:
        """
        Queries for instances of `ReferenceDocument`

        :param id: The assigned identifying value for the instance of the class.
        :param location: None
        :param name: The name for the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReferenceDocument.class_name,
                                                 
                                                 id=id,
                                                 
                                                 location=location,
                                                 
                                                 name=name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DocumentReference methods
    # --
    def fetch_DocumentReference(self, id_value: str) -> DocumentReference:
        """
        Retrieves an instance of `DocumentReference` via a primary key

        :param id_value:
        :return: DocumentReference with matching ID
        """
        q = FetchById(id=id_value, target_class=DocumentReference.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DocumentReference(self,
             referenceDocumentId: Union[str, MatchExpression] = None,
             pageRefs: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DocumentReference]:
        """
        Queries for instances of `DocumentReference`

        :param referenceDocumentId: None
        :param pageRefs: A list of references to specific parts of a document, which may be referenced as a list of one or more page numbers, a range of page numbers, or a list of named destinations in the document (e.g. bookmarks).
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DocumentReference.class_name,
                                                 
                                                 referenceDocumentId=referenceDocumentId,
                                                 
                                                 pageRefs=pageRefs,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # PageRef methods
    # --
    def fetch_PageRef(self, id_value: str) -> PageRef:
        """
        Retrieves an instance of `PageRef` via a primary key

        :param id_value:
        :return: PageRef with matching ID
        """
        q = FetchById(id=id_value, target_class=PageRef.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_PageRef(self,
             refType: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             pageNames: Union[str, MatchExpression] = None,
             pageNumbers: Union[str, MatchExpression] = None,
             firstPage: Union[str, MatchExpression] = None,
             lastPage: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[PageRef]:
        """
        Queries for instances of `PageRef`

        :param refType: The type of reference for page references.
        :param label: Alternative label to provide a more specific and description to a page link.
        :param pageNames: One or more named document references which each correspond with a page.
        :param pageNumbers: One or more page numbers.
        :param firstPage: The page number of the first page in a range of pages.
        :param lastPage: The page number of the last page in a range of pages.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(PageRef.class_name,
                                                 
                                                 refType=refType,
                                                 
                                                 label=label,
                                                 
                                                 pageNames=pageNames,
                                                 
                                                 pageNumbers=pageNumbers,
                                                 
                                                 firstPage=firstPage,
                                                 
                                                 lastPage=lastPage,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # PageNumberListRef methods
    # --
    def fetch_PageNumberListRef(self, id_value: str) -> PageNumberListRef:
        """
        Retrieves an instance of `PageNumberListRef` via a primary key

        :param id_value:
        :return: PageNumberListRef with matching ID
        """
        q = FetchById(id=id_value, target_class=PageNumberListRef.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_PageNumberListRef(self,
             refType: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             pageNames: Union[str, MatchExpression] = None,
             pageNumbers: Union[str, MatchExpression] = None,
             firstPage: Union[str, MatchExpression] = None,
             lastPage: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[PageNumberListRef]:
        """
        Queries for instances of `PageNumberListRef`

        :param refType: The type of reference for page references.
        :param label: Alternative label to provide a more specific and description to a page link.
        :param pageNames: NOT USED
        :param pageNumbers: One or more page numbers.
        :param firstPage: NOT USED
        :param lastPage: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(PageNumberListRef.class_name,
                                                 
                                                 refType=refType,
                                                 
                                                 label=label,
                                                 
                                                 pageNames=pageNames,
                                                 
                                                 pageNumbers=pageNumbers,
                                                 
                                                 firstPage=firstPage,
                                                 
                                                 lastPage=lastPage,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # PageNumberRangeRef methods
    # --
    def fetch_PageNumberRangeRef(self, id_value: str) -> PageNumberRangeRef:
        """
        Retrieves an instance of `PageNumberRangeRef` via a primary key

        :param id_value:
        :return: PageNumberRangeRef with matching ID
        """
        q = FetchById(id=id_value, target_class=PageNumberRangeRef.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_PageNumberRangeRef(self,
             refType: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             pageNames: Union[str, MatchExpression] = None,
             pageNumbers: Union[str, MatchExpression] = None,
             firstPage: Union[str, MatchExpression] = None,
             lastPage: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[PageNumberRangeRef]:
        """
        Queries for instances of `PageNumberRangeRef`

        :param refType: The type of reference for page references.
        :param label: Alternative label to provide a more specific and description to a page link.
        :param pageNames: NOT USED
        :param pageNumbers: NOT USED
        :param firstPage: The page number of the first page in a range of pages.
        :param lastPage: The page number of the last page in a range of pages.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(PageNumberRangeRef.class_name,
                                                 
                                                 refType=refType,
                                                 
                                                 label=label,
                                                 
                                                 pageNames=pageNames,
                                                 
                                                 pageNumbers=pageNumbers,
                                                 
                                                 firstPage=firstPage,
                                                 
                                                 lastPage=lastPage,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # PageNameRef methods
    # --
    def fetch_PageNameRef(self, id_value: str) -> PageNameRef:
        """
        Retrieves an instance of `PageNameRef` via a primary key

        :param id_value:
        :return: PageNameRef with matching ID
        """
        q = FetchById(id=id_value, target_class=PageNameRef.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_PageNameRef(self,
             refType: Union[str, MatchExpression] = None,
             label: Union[str, MatchExpression] = None,
             pageNames: Union[str, MatchExpression] = None,
             pageNumbers: Union[str, MatchExpression] = None,
             firstPage: Union[str, MatchExpression] = None,
             lastPage: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[PageNameRef]:
        """
        Queries for instances of `PageNameRef`

        :param refType: The type of reference for page references.
        :param label: Alternative label to provide a more specific and description to a page link.
        :param pageNames: One or more named document references which each correspond with a page.
        :param pageNumbers: NOT USED
        :param firstPage: NOT USED
        :param lastPage: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(PageNameRef.class_name,
                                                 
                                                 refType=refType,
                                                 
                                                 label=label,
                                                 
                                                 pageNames=pageNames,
                                                 
                                                 pageNumbers=pageNumbers,
                                                 
                                                 firstPage=firstPage,
                                                 
                                                 lastPage=lastPage,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # TerminologyExtension methods
    # --
    def fetch_TerminologyExtension(self, id_value: str) -> TerminologyExtension:
        """
        Retrieves an instance of `TerminologyExtension` via a primary key

        :param id_value:
        :return: TerminologyExtension with matching ID
        """
        q = FetchById(id=id_value, target_class=TerminologyExtension.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_TerminologyExtension(self,
             id: Union[str, MatchExpression] = None,
             enumeration: Union[str, MatchExpression] = None,
             sponsorTerms: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[TerminologyExtension]:
        """
        Queries for instances of `TerminologyExtension`

        :param id: The assigned identifying value for the instance of the class.
        :param enumeration: The name of the extensible enumeration.
        :param sponsorTerms: The sponsor-defined terms added to the extensible terminology.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(TerminologyExtension.class_name,
                                                 
                                                 id=id,
                                                 
                                                 enumeration=enumeration,
                                                 
                                                 sponsorTerms=sponsorTerms,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SponsorTerm methods
    # --
    def fetch_SponsorTerm(self, id_value: str) -> SponsorTerm:
        """
        Retrieves an instance of `SponsorTerm` via a primary key

        :param id_value:
        :return: SponsorTerm with matching ID
        """
        q = FetchById(id=id_value, target_class=SponsorTerm.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SponsorTerm(self,
             id: Union[str, MatchExpression] = None,
             submissionValue: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SponsorTerm]:
        """
        Queries for instances of `SponsorTerm`

        :param id: The assigned identifying value for the instance of the class.
        :param submissionValue: The specific value expected for submissions.
        :param description: A textual description of the instance of the class.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SponsorTerm.class_name,
                                                 
                                                 id=id,
                                                 
                                                 submissionValue=submissionValue,
                                                 
                                                 description=description,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ExtensibleTerminologyTerm methods
    # --
    def fetch_ExtensibleTerminologyTerm(self, id_value: str) -> ExtensibleTerminologyTerm:
        """
        Retrieves an instance of `ExtensibleTerminologyTerm` via a primary key

        :param id_value:
        :return: ExtensibleTerminologyTerm with matching ID
        """
        q = FetchById(id=id_value, target_class=ExtensibleTerminologyTerm.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ExtensibleTerminologyTerm(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ExtensibleTerminologyTerm]:
        """
        Queries for instances of `ExtensibleTerminologyTerm`

        :param controlledTerm: One of the permissible values from the referenced enumeration.
        :param sponsorTermId: The identifier of the referenced sponsor term.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ExtensibleTerminologyTerm.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisReason methods
    # --
    def fetch_AnalysisReason(self, id_value: str) -> AnalysisReason:
        """
        Retrieves an instance of `AnalysisReason` via a primary key

        :param id_value:
        :return: AnalysisReason with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisReason.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisReason(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisReason]:
        """
        Queries for instances of `AnalysisReason`

        :param controlledTerm: One of the permissible values from the referenced enumeration.
        :param sponsorTermId: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisReason.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SponsorAnalysisReason methods
    # --
    def fetch_SponsorAnalysisReason(self, id_value: str) -> SponsorAnalysisReason:
        """
        Retrieves an instance of `SponsorAnalysisReason` via a primary key

        :param id_value:
        :return: SponsorAnalysisReason with matching ID
        """
        q = FetchById(id=id_value, target_class=SponsorAnalysisReason.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SponsorAnalysisReason(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SponsorAnalysisReason]:
        """
        Queries for instances of `SponsorAnalysisReason`

        :param controlledTerm: NOT USED
        :param sponsorTermId: A reference to a sponsor term in the TerminologyExtension with enumeration=AnalysisReasonEnum
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SponsorAnalysisReason.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnalysisPurpose methods
    # --
    def fetch_AnalysisPurpose(self, id_value: str) -> AnalysisPurpose:
        """
        Retrieves an instance of `AnalysisPurpose` via a primary key

        :param id_value:
        :return: AnalysisPurpose with matching ID
        """
        q = FetchById(id=id_value, target_class=AnalysisPurpose.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnalysisPurpose(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisPurpose]:
        """
        Queries for instances of `AnalysisPurpose`

        :param controlledTerm: One of the permissible values from the referenced enumeration.
        :param sponsorTermId: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisPurpose.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SponsorAnalysisPurpose methods
    # --
    def fetch_SponsorAnalysisPurpose(self, id_value: str) -> SponsorAnalysisPurpose:
        """
        Retrieves an instance of `SponsorAnalysisPurpose` via a primary key

        :param id_value:
        :return: SponsorAnalysisPurpose with matching ID
        """
        q = FetchById(id=id_value, target_class=SponsorAnalysisPurpose.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SponsorAnalysisPurpose(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SponsorAnalysisPurpose]:
        """
        Queries for instances of `SponsorAnalysisPurpose`

        :param controlledTerm: NOT USED
        :param sponsorTermId: A reference to a sponsor term in the TerminologyExtension with enumeration=AnalysisPurposeEnum
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SponsorAnalysisPurpose.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OperationRole methods
    # --
    def fetch_OperationRole(self, id_value: str) -> OperationRole:
        """
        Retrieves an instance of `OperationRole` via a primary key

        :param id_value:
        :return: OperationRole with matching ID
        """
        q = FetchById(id=id_value, target_class=OperationRole.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OperationRole(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OperationRole]:
        """
        Queries for instances of `OperationRole`

        :param controlledTerm: One of the permissible values from the referenced enumeration.
        :param sponsorTermId: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OperationRole.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SponsorOperationRole methods
    # --
    def fetch_SponsorOperationRole(self, id_value: str) -> SponsorOperationRole:
        """
        Retrieves an instance of `SponsorOperationRole` via a primary key

        :param id_value:
        :return: SponsorOperationRole with matching ID
        """
        q = FetchById(id=id_value, target_class=SponsorOperationRole.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SponsorOperationRole(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SponsorOperationRole]:
        """
        Queries for instances of `SponsorOperationRole`

        :param controlledTerm: NOT USED
        :param sponsorTermId: A reference to a sponsor term in the TerminologyExtension with enumeration=OperationRoleEnum
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SponsorOperationRole.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OutputFileType methods
    # --
    def fetch_OutputFileType(self, id_value: str) -> OutputFileType:
        """
        Retrieves an instance of `OutputFileType` via a primary key

        :param id_value:
        :return: OutputFileType with matching ID
        """
        q = FetchById(id=id_value, target_class=OutputFileType.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OutputFileType(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OutputFileType]:
        """
        Queries for instances of `OutputFileType`

        :param controlledTerm: One of the permissible values from the referenced enumeration.
        :param sponsorTermId: NOT USED
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OutputFileType.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # SponsorOutputFileType methods
    # --
    def fetch_SponsorOutputFileType(self, id_value: str) -> SponsorOutputFileType:
        """
        Retrieves an instance of `SponsorOutputFileType` via a primary key

        :param id_value:
        :return: SponsorOutputFileType with matching ID
        """
        q = FetchById(id=id_value, target_class=SponsorOutputFileType.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SponsorOutputFileType(self,
             controlledTerm: Union[str, MatchExpression] = None,
             sponsorTermId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SponsorOutputFileType]:
        """
        Queries for instances of `SponsorOutputFileType`

        :param controlledTerm: NOT USED
        :param sponsorTermId: A reference to a sponsor term in the TerminologyExtension with enumeration=OutputFileTypeEnum
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SponsorOutputFileType.class_name,
                                                 
                                                 controlledTerm=controlledTerm,
                                                 
                                                 sponsorTermId=sponsorTermId,
                                                 
                                                 _extra=_extra)
        return results
    

