
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

        :param name: None
        
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
             listOfPlannedAnalyses: Union[str, MatchExpression] = None,
             listOfPlannedOutputs: Union[str, MatchExpression] = None,
             analysisSets: Union[str, MatchExpression] = None,
             analysisGroupings: Union[str, MatchExpression] = None,
             dataSubsets: Union[str, MatchExpression] = None,
             globalDisplaySections: Union[str, MatchExpression] = None,
             analysisCategorizations: Union[str, MatchExpression] = None,
             analyses: Union[str, MatchExpression] = None,
             methods: Union[str, MatchExpression] = None,
             outputs: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReportingEvent]:
        """
        Queries for instances of `ReportingEvent`

        :param listOfPlannedAnalyses: None
        :param listOfPlannedOutputs: None
        :param analysisSets: None
        :param analysisGroupings: None
        :param dataSubsets: None
        :param globalDisplaySections: None
        :param analysisCategorizations: None
        :param analyses: None
        :param methods: None
        :param outputs: None
        :param name: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReportingEvent.class_name,
                                                 
                                                 listOfPlannedAnalyses=listOfPlannedAnalyses,
                                                 
                                                 listOfPlannedOutputs=listOfPlannedOutputs,
                                                 
                                                 analysisSets=analysisSets,
                                                 
                                                 analysisGroupings=analysisGroupings,
                                                 
                                                 dataSubsets=dataSubsets,
                                                 
                                                 globalDisplaySections=globalDisplaySections,
                                                 
                                                 analysisCategorizations=analysisCategorizations,
                                                 
                                                 analyses=analyses,
                                                 
                                                 methods=methods,
                                                 
                                                 outputs=outputs,
                                                 
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

        :param level: None
        :param order: None
        :param sublist: None
        :param analysisId: None
        :param outputId: None
        :param name: None
        
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

        :param id: None
        :param label: None
        :param categories: None
        
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

        :param id: None
        :param label: None
        :param subCategorizations: None
        
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
             analysisSetId: Union[str, MatchExpression] = None,
             orderedGroupings: Union[str, MatchExpression] = None,
             dataSubsetId: Union[str, MatchExpression] = None,
             dataset: Union[str, MatchExpression] = None,
             variable: Union[str, MatchExpression] = None,
             methodId: Union[str, MatchExpression] = None,
             referencedAnalysisOperations: Union[str, MatchExpression] = None,
             results: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Analysis]:
        """
        Queries for instances of `Analysis`

        :param id: None
        :param version: None
        :param categoryIds: None
        :param analysisSetId: None
        :param orderedGroupings: None
        :param dataSubsetId: None
        :param dataset: None
        :param variable: None
        :param methodId: None
        :param referencedAnalysisOperations: None
        :param results: None
        :param name: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Analysis.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 categoryIds=categoryIds,
                                                 
                                                 analysisSetId=analysisSetId,
                                                 
                                                 orderedGroupings=orderedGroupings,
                                                 
                                                 dataSubsetId=dataSubsetId,
                                                 
                                                 dataset=dataset,
                                                 
                                                 variable=variable,
                                                 
                                                 methodId=methodId,
                                                 
                                                 referencedAnalysisOperations=referencedAnalysisOperations,
                                                 
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
             dataGrouping: Union[str, MatchExpression] = None,
             resultsByGroup: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OrderedGroupingFactor]:
        """
        Queries for instances of `OrderedGroupingFactor`

        :param order: None
        :param groupingId: None
        :param dataGrouping: None
        :param resultsByGroup: Indicates whether a result is expected for each group in the grouping.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OrderedGroupingFactor.class_name,
                                                 
                                                 order=order,
                                                 
                                                 groupingId=groupingId,
                                                 
                                                 dataGrouping=dataGrouping,
                                                 
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
             referencedOperationId: Union[str, MatchExpression] = None,
             analysisId: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ReferencedAnalysisOperation]:
        """
        Queries for instances of `ReferencedAnalysisOperation`

        :param referencedOperationId: None
        :param analysisId: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ReferencedAnalysisOperation.class_name,
                                                 
                                                 referencedOperationId=referencedOperationId,
                                                 
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

        :param operationId: None
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

        :param groupingId: None
        :param groupId: None
        :param groupValue: None
        
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
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnalysisMethod]:
        """
        Queries for instances of `AnalysisMethod`

        :param id: None
        :param label: None
        :param description: None
        :param operations: None
        :param name: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnalysisMethod.class_name,
                                                 
                                                 id=id,
                                                 
                                                 label=label,
                                                 
                                                 description=description,
                                                 
                                                 operations=operations,
                                                 
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

        :param id: None
        :param label: None
        :param referencedOperationRelationships: None
        :param resultPattern: None
        :param name: None
        
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

        :param id: None
        :param referencedOperationRole: None
        :param operationId: None
        :param analysisId: None
        :param description: None
        
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
             outputDisplays: Union[str, MatchExpression] = None,
             categoryIds: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Output]:
        """
        Queries for instances of `Output`

        :param id: None
        :param version: None
        :param fileSpecifications: None
        :param outputDisplays: None
        :param categoryIds: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Output.class_name,
                                                 
                                                 id=id,
                                                 
                                                 version=version,
                                                 
                                                 fileSpecifications=fileSpecifications,
                                                 
                                                 outputDisplays=outputDisplays,
                                                 
                                                 categoryIds=categoryIds,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # File methods
    # --
    def fetch_File(self, id_value: str) -> File:
        """
        Retrieves an instance of `File` via a primary key

        :param id_value:
        :return: File with matching ID
        """
        q = FetchById(id=id_value, target_class=File.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_File(self,
             fileType: Union[str, MatchExpression] = None,
             location: Union[str, MatchExpression] = None,
             style: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[File]:
        """
        Queries for instances of `File`

        :param fileType: None
        :param location: None
        :param style: None
        :param name: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(File.class_name,
                                                 
                                                 fileType=fileType,
                                                 
                                                 location=location,
                                                 
                                                 style=style,
                                                 
                                                 name=name,
                                                 
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
             order: Union[str, MatchExpression] = None,
             display: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OutputDisplay]:
        """
        Queries for instances of `OutputDisplay`

        :param order: None
        :param display: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OutputDisplay.class_name,
                                                 
                                                 order=order,
                                                 
                                                 display=display,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Display methods
    # --
    def fetch_Display(self, id_value: str) -> Display:
        """
        Retrieves an instance of `Display` via a primary key

        :param id_value:
        :return: Display with matching ID
        """
        q = FetchById(id=id_value, target_class=Display.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Display(self,
             id: Union[str, MatchExpression] = None,
             version: Union[str, MatchExpression] = None,
             displayTitle: Union[str, MatchExpression] = None,
             displaySections: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Display]:
        """
        Queries for instances of `Display`

        :param id: None
        :param version: None
        :param displayTitle: None
        :param displaySections: None
        :param name: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Display.class_name,
                                                 
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
             subSections: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DisplaySection]:
        """
        Queries for instances of `DisplaySection`

        :param sectionType: None
        :param subSections: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DisplaySection.class_name,
                                                 
                                                 sectionType=sectionType,
                                                 
                                                 subSections=subSections,
                                                 
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
             order: Union[str, MatchExpression] = None,
             text: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DisplaySubSection]:
        """
        Queries for instances of `DisplaySubSection`

        :param id: None
        :param order: None
        :param text: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DisplaySubSection.class_name,
                                                 
                                                 id=id,
                                                 
                                                 order=order,
                                                 
                                                 text=text,
                                                 
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

        :param level: None
        :param order: None
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
    # Condition methods
    # --
    def fetch_Condition(self, id_value: str) -> Condition:
        """
        Retrieves an instance of `Condition` via a primary key

        :param id_value:
        :return: Condition with matching ID
        """
        q = FetchById(id=id_value, target_class=Condition.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Condition(self,
             dataset: Union[str, MatchExpression] = None,
             variable: Union[str, MatchExpression] = None,
             comparator: Union[str, MatchExpression] = None,
             value: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Condition]:
        """
        Queries for instances of `Condition`

        :param dataset: None
        :param variable: None
        :param comparator: None
        :param value: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Condition.class_name,
                                                 
                                                 dataset=dataset,
                                                 
                                                 variable=variable,
                                                 
                                                 comparator=comparator,
                                                 
                                                 value=value,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CompoundExpression methods
    # --
    def fetch_CompoundExpression(self, id_value: str) -> CompoundExpression:
        """
        Retrieves an instance of `CompoundExpression` via a primary key

        :param id_value:
        :return: CompoundExpression with matching ID
        """
        q = FetchById(id=id_value, target_class=CompoundExpression.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CompoundExpression(self,
             logicalOperator: Union[str, MatchExpression] = None,
             whereClauses: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CompoundExpression]:
        """
        Queries for instances of `CompoundExpression`

        :param logicalOperator: None
        :param whereClauses: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CompoundExpression.class_name,
                                                 
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

        :param id: None
        :param label: None
        :param level: None
        :param order: None
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

        :param id: None
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: None
        
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

        :param id: None
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: None
        
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

        :param id: None
        :param label: None
        :param groupingVariable: For groupings based on a single variable, a reference to the dataset variable upon which grouping is based.
        :param dataDriven: Indicates whether the groups defined by the grouping are prespecified (false) or obtained from distinct data values of the groupingVariable (true).
        :param groups: None
        
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

        :param id: None
        :param label: None
        :param level: None
        :param order: None
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

        :param id: None
        :param label: None
        :param level: None
        :param order: None
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

        :param id: None
        :param label: None
        :param level: None
        :param order: None
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

        :param id: None
        :param label: None
        :param level: None
        :param order: None
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
    

