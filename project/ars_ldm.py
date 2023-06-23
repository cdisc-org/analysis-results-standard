# Auto generated from ars_ldm.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-06-23T13:46:32
# Schema: ars_ldm
#
# id: https://www.cdisc.org/ars/1-0
# description: DRAFT Logical model to support both the prospective specification of analyses and the fully contextualized representation of the results of the analyses.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
ARS = CurieNamespace('ars', 'https://www.cdisc.org/ars/1-0/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = ARS


# Types

# Class references
class ReportingEventId(extended_str):
    pass


class AnalysisCategorizationId(extended_str):
    pass


class AnalysisCategoryId(extended_str):
    pass


class AnalysisId(extended_str):
    pass


class AnalysisMethodId(extended_str):
    pass


class OperationId(extended_str):
    pass


class ReferencedOperationRelationshipId(extended_str):
    pass


class OutputId(extended_str):
    pass


class OutputDisplayId(extended_str):
    pass


class DisplaySubSectionId(extended_str):
    pass


class AnalysisSetId(extended_str):
    pass


class GroupingFactorId(extended_str):
    pass


class SubjectGroupingFactorId(GroupingFactorId):
    pass


class DataGroupingFactorId(GroupingFactorId):
    pass


class GroupId(extended_str):
    pass


class AnalysisGroupId(GroupId):
    pass


class DataGroupId(GroupId):
    pass


class DataSubsetId(extended_str):
    pass


class ReferenceDocumentId(extended_str):
    pass


class TerminologyExtensionId(extended_str):
    pass


class SponsorTermId(extended_str):
    pass


@dataclass
class NamedObject(YAMLRoot):
    """
    An object with a name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.NamedObject
    class_class_curie: ClassVar[str] = "ars:NamedObject"
    class_name: ClassVar[str] = "NamedObject"
    class_model_uri: ClassVar[URIRef] = ARS.NamedObject

    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class ReportingEvent(NamedObject):
    """
    A set of analyses and outputs created to meet a specific reporting requirement, such as a CSR or interim analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ReportingEvent
    class_class_curie: ClassVar[str] = "ars:ReportingEvent"
    class_name: ClassVar[str] = "ReportingEvent"
    class_model_uri: ClassVar[URIRef] = ARS.ReportingEvent

    id: Union[str, ReportingEventId] = None
    name: str = None
    listOfPlannedAnalyses: Union[dict, "NestedList"] = None
    version: Optional[int] = None
    listOfPlannedOutputs: Optional[Union[dict, "NestedList"]] = None
    analysisSets: Optional[Union[Dict[Union[str, AnalysisSetId], Union[dict, "AnalysisSet"]], List[Union[dict, "AnalysisSet"]]]] = empty_dict()
    analysisGroupings: Optional[Union[Dict[Union[str, SubjectGroupingFactorId], Union[dict, "SubjectGroupingFactor"]], List[Union[dict, "SubjectGroupingFactor"]]]] = empty_dict()
    dataSubsets: Optional[Union[Dict[Union[str, DataSubsetId], Union[dict, "DataSubset"]], List[Union[dict, "DataSubset"]]]] = empty_dict()
    dataGroupings: Optional[Union[Dict[Union[str, DataGroupingFactorId], Union[dict, "DataGroupingFactor"]], List[Union[dict, "DataGroupingFactor"]]]] = empty_dict()
    globalDisplaySections: Optional[Union[Union[dict, "GlobalDisplaySection"], List[Union[dict, "GlobalDisplaySection"]]]] = empty_list()
    analysisCategorizations: Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, "AnalysisCategorization"]], List[Union[dict, "AnalysisCategorization"]]]] = empty_dict()
    analyses: Optional[Union[Dict[Union[str, AnalysisId], Union[dict, "Analysis"]], List[Union[dict, "Analysis"]]]] = empty_dict()
    methods: Optional[Union[Dict[Union[str, AnalysisMethodId], Union[dict, "AnalysisMethod"]], List[Union[dict, "AnalysisMethod"]]]] = empty_dict()
    outputs: Optional[Union[Dict[Union[str, OutputId], Union[dict, "Output"]], List[Union[dict, "Output"]]]] = empty_dict()
    referenceDocuments: Optional[Union[Dict[Union[str, ReferenceDocumentId], Union[dict, "ReferenceDocument"]], List[Union[dict, "ReferenceDocument"]]]] = empty_dict()
    terminologyExtensions: Optional[Union[Dict[Union[str, TerminologyExtensionId], Union[dict, "TerminologyExtension"]], List[Union[dict, "TerminologyExtension"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReportingEventId):
            self.id = ReportingEventId(self.id)

        if self._is_empty(self.listOfPlannedAnalyses):
            self.MissingRequiredField("listOfPlannedAnalyses")
        if not isinstance(self.listOfPlannedAnalyses, NestedList):
            self.listOfPlannedAnalyses = NestedList(**as_dict(self.listOfPlannedAnalyses))

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if self.listOfPlannedOutputs is not None and not isinstance(self.listOfPlannedOutputs, NestedList):
            self.listOfPlannedOutputs = NestedList(**as_dict(self.listOfPlannedOutputs))

        self._normalize_inlined_as_list(slot_name="analysisSets", slot_type=AnalysisSet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="analysisGroupings", slot_type=SubjectGroupingFactor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dataSubsets", slot_type=DataSubset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dataGroupings", slot_type=DataGroupingFactor, key_name="id", keyed=True)

        if not isinstance(self.globalDisplaySections, list):
            self.globalDisplaySections = [self.globalDisplaySections] if self.globalDisplaySections is not None else []
        self.globalDisplaySections = [v if isinstance(v, GlobalDisplaySection) else GlobalDisplaySection(**as_dict(v)) for v in self.globalDisplaySections]

        self._normalize_inlined_as_list(slot_name="analysisCategorizations", slot_type=AnalysisCategorization, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="analyses", slot_type=Analysis, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="methods", slot_type=AnalysisMethod, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="outputs", slot_type=Output, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="referenceDocuments", slot_type=ReferenceDocument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="terminologyExtensions", slot_type=TerminologyExtension, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class NestedList(YAMLRoot):
    """
    A list of items (analyses or outputs) that may be organized within sub-lists.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.NestedList
    class_class_curie: ClassVar[str] = "ars:NestedList"
    class_name: ClassVar[str] = "NestedList"
    class_model_uri: ClassVar[URIRef] = ARS.NestedList

    listItems: Optional[Union[Union[dict, "OrderedListItem"], List[Union[dict, "OrderedListItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.listItems, list):
            self.listItems = [self.listItems] if self.listItems is not None else []
        self.listItems = [v if isinstance(v, OrderedListItem) else OrderedListItem(**as_dict(v)) for v in self.listItems]

        super().__post_init__(**kwargs)


@dataclass
class OrderedListItem(NamedObject):
    """
    An item (analysis, output or sub-list) ordered relative to other items within a list or sub-list.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedListItem
    class_class_curie: ClassVar[str] = "ars:OrderedListItem"
    class_name: ClassVar[str] = "OrderedListItem"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedListItem

    name: str = None
    level: int = None
    order: int = None
    sublist: Optional[Union[dict, NestedList]] = None
    analysisId: Optional[Union[str, AnalysisId]] = None
    outputId: Optional[Union[str, OutputId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, int):
            self.level = int(self.level)

        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.sublist is not None and not isinstance(self.sublist, NestedList):
            self.sublist = NestedList(**as_dict(self.sublist))

        if self.analysisId is not None and not isinstance(self.analysisId, AnalysisId):
            self.analysisId = AnalysisId(self.analysisId)

        if self.outputId is not None and not isinstance(self.outputId, OutputId):
            self.outputId = OutputId(self.outputId)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisCategorization(YAMLRoot):
    """
    A set of related implementer-defined categories that can be used to categorize analyses or outputs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisCategorization
    class_class_curie: ClassVar[str] = "ars:AnalysisCategorization"
    class_name: ClassVar[str] = "AnalysisCategorization"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisCategorization

    id: Union[str, AnalysisCategorizationId] = None
    categories: Union[Dict[Union[str, AnalysisCategoryId], Union[dict, "AnalysisCategory"]], List[Union[dict, "AnalysisCategory"]]] = empty_dict()
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisCategorizationId):
            self.id = AnalysisCategorizationId(self.id)

        if self._is_empty(self.categories):
            self.MissingRequiredField("categories")
        self._normalize_inlined_as_list(slot_name="categories", slot_type=AnalysisCategory, key_name="id", keyed=True)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisCategory(YAMLRoot):
    """
    An implementer-defined category of analyses/outputs, which may include one or more sub-categorization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisCategory
    class_class_curie: ClassVar[str] = "ars:AnalysisCategory"
    class_name: ClassVar[str] = "AnalysisCategory"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisCategory

    id: Union[str, AnalysisCategoryId] = None
    label: Optional[str] = None
    subCategorizations: Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, AnalysisCategorization]], List[Union[dict, AnalysisCategorization]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisCategoryId):
            self.id = AnalysisCategoryId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        self._normalize_inlined_as_list(slot_name="subCategorizations", slot_type=AnalysisCategorization, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Analysis(NamedObject):
    """
    An analysis that is designed to meet a requirement of the reporting event. Each analysis is defined as a set of
    specifications, including:
    * The analysis variable that is the subject of the analysis.
    * The analysis method (set of statistical operations) that is performed for the analysis variable.
    * The analysis set (subject population) for which the analysis is performed.
    * The subset of data records on which the analysis is performed (optional).
    * One or more factors by which either subjects or data records are grouped for analysis (optional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.Analysis
    class_class_curie: ClassVar[str] = "ars:Analysis"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = ARS.Analysis

    id: Union[str, AnalysisId] = None
    name: str = None
    reason: Union[dict, "ExtensibleTerminologyTerm"] = None
    purpose: Union[dict, "ExtensibleTerminologyTerm"] = None
    methodId: Union[str, AnalysisMethodId] = None
    version: Optional[int] = None
    categoryIds: Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]] = empty_list()
    description: Optional[str] = None
    documentRefs: Optional[Union[Union[dict, "DocumentReference"], List[Union[dict, "DocumentReference"]]]] = empty_list()
    analysisSetId: Optional[Union[str, AnalysisSetId]] = None
    orderedGroupings: Optional[Union[Union[dict, "OrderedGroupingFactor"], List[Union[dict, "OrderedGroupingFactor"]]]] = empty_list()
    dataSubsetId: Optional[Union[str, DataSubsetId]] = None
    dataset: Optional[str] = None
    variable: Optional[str] = None
    referencedAnalysisOperations: Optional[Union[Union[dict, "ReferencedAnalysisOperation"], List[Union[dict, "ReferencedAnalysisOperation"]]]] = empty_list()
    programmingCode: Optional[Union[dict, "AnalysisOutputProgrammingCode"]] = None
    results: Optional[Union[Union[dict, "OperationResult"], List[Union[dict, "OperationResult"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisId):
            self.id = AnalysisId(self.id)

        if self._is_empty(self.reason):
            self.MissingRequiredField("reason")
        if not isinstance(self.reason, ExtensibleTerminologyTerm):
            self.reason = ExtensibleTerminologyTerm(**as_dict(self.reason))

        if self._is_empty(self.purpose):
            self.MissingRequiredField("purpose")
        if not isinstance(self.purpose, ExtensibleTerminologyTerm):
            self.purpose = ExtensibleTerminologyTerm(**as_dict(self.purpose))

        if self._is_empty(self.methodId):
            self.MissingRequiredField("methodId")
        if not isinstance(self.methodId, AnalysisMethodId):
            self.methodId = AnalysisMethodId(self.methodId)

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if not isinstance(self.categoryIds, list):
            self.categoryIds = [self.categoryIds] if self.categoryIds is not None else []
        self.categoryIds = [v if isinstance(v, AnalysisCategoryId) else AnalysisCategoryId(v) for v in self.categoryIds]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.documentRefs, list):
            self.documentRefs = [self.documentRefs] if self.documentRefs is not None else []
        self.documentRefs = [v if isinstance(v, DocumentReference) else DocumentReference(**as_dict(v)) for v in self.documentRefs]

        if self.analysisSetId is not None and not isinstance(self.analysisSetId, AnalysisSetId):
            self.analysisSetId = AnalysisSetId(self.analysisSetId)

        if not isinstance(self.orderedGroupings, list):
            self.orderedGroupings = [self.orderedGroupings] if self.orderedGroupings is not None else []
        self.orderedGroupings = [v if isinstance(v, OrderedGroupingFactor) else OrderedGroupingFactor(**as_dict(v)) for v in self.orderedGroupings]

        if self.dataSubsetId is not None and not isinstance(self.dataSubsetId, DataSubsetId):
            self.dataSubsetId = DataSubsetId(self.dataSubsetId)

        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        if self.variable is not None and not isinstance(self.variable, str):
            self.variable = str(self.variable)

        if not isinstance(self.referencedAnalysisOperations, list):
            self.referencedAnalysisOperations = [self.referencedAnalysisOperations] if self.referencedAnalysisOperations is not None else []
        self.referencedAnalysisOperations = [v if isinstance(v, ReferencedAnalysisOperation) else ReferencedAnalysisOperation(**as_dict(v)) for v in self.referencedAnalysisOperations]

        if self.programmingCode is not None and not isinstance(self.programmingCode, AnalysisOutputProgrammingCode):
            self.programmingCode = AnalysisOutputProgrammingCode(**as_dict(self.programmingCode))

        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, OperationResult) else OperationResult(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)


@dataclass
class OrderedGroupingFactor(YAMLRoot):
    """
    A reference to a defined factor by which subjects or data records are grouped for the analysis, ordered with
    respect to other grouping factors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedGroupingFactor
    class_class_curie: ClassVar[str] = "ars:OrderedGroupingFactor"
    class_name: ClassVar[str] = "OrderedGroupingFactor"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedGroupingFactor

    order: int = None
    resultsByGroup: Union[bool, Bool] = None
    groupingId: Optional[Union[str, GroupingFactorId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self._is_empty(self.resultsByGroup):
            self.MissingRequiredField("resultsByGroup")
        if not isinstance(self.resultsByGroup, Bool):
            self.resultsByGroup = Bool(self.resultsByGroup)

        if self.groupingId is not None and not isinstance(self.groupingId, GroupingFactorId):
            self.groupingId = GroupingFactorId(self.groupingId)

        super().__post_init__(**kwargs)


@dataclass
class ReferencedAnalysisOperation(YAMLRoot):
    """
    An indication of the analysis that contains results of a referenced operation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ReferencedAnalysisOperation
    class_class_curie: ClassVar[str] = "ars:ReferencedAnalysisOperation"
    class_name: ClassVar[str] = "ReferencedAnalysisOperation"
    class_model_uri: ClassVar[URIRef] = ARS.ReferencedAnalysisOperation

    referencedOperationRelationshipId: Union[str, ReferencedOperationRelationshipId] = None
    analysisId: Union[str, AnalysisId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.referencedOperationRelationshipId):
            self.MissingRequiredField("referencedOperationRelationshipId")
        if not isinstance(self.referencedOperationRelationshipId, ReferencedOperationRelationshipId):
            self.referencedOperationRelationshipId = ReferencedOperationRelationshipId(self.referencedOperationRelationshipId)

        if self._is_empty(self.analysisId):
            self.MissingRequiredField("analysisId")
        if not isinstance(self.analysisId, AnalysisId):
            self.analysisId = AnalysisId(self.analysisId)

        super().__post_init__(**kwargs)


@dataclass
class OperationResult(YAMLRoot):
    """
    The result of an analysis method operation performed on a subdivision of subjects or data records.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OperationResult
    class_class_curie: ClassVar[str] = "ars:OperationResult"
    class_name: ClassVar[str] = "OperationResult"
    class_model_uri: ClassVar[URIRef] = ARS.OperationResult

    operationId: Union[str, OperationId] = None
    resultGroups: Optional[Union[Union[dict, "ResultGroup"], List[Union[dict, "ResultGroup"]]]] = empty_list()
    rawValue: Optional[str] = None
    formattedValue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.operationId):
            self.MissingRequiredField("operationId")
        if not isinstance(self.operationId, OperationId):
            self.operationId = OperationId(self.operationId)

        if not isinstance(self.resultGroups, list):
            self.resultGroups = [self.resultGroups] if self.resultGroups is not None else []
        self.resultGroups = [v if isinstance(v, ResultGroup) else ResultGroup(**as_dict(v)) for v in self.resultGroups]

        if self.rawValue is not None and not isinstance(self.rawValue, str):
            self.rawValue = str(self.rawValue)

        if self.formattedValue is not None and not isinstance(self.formattedValue, str):
            self.formattedValue = str(self.formattedValue)

        super().__post_init__(**kwargs)


@dataclass
class ResultGroup(YAMLRoot):
    """
    For the specified grouping factor, an indication of the specific group of subjects or data records associated with
    the analysis result.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ResultGroup
    class_class_curie: ClassVar[str] = "ars:ResultGroup"
    class_name: ClassVar[str] = "ResultGroup"
    class_model_uri: ClassVar[URIRef] = ARS.ResultGroup

    groupingId: Optional[Union[str, GroupingFactorId]] = None
    groupId: Optional[Union[str, GroupId]] = None
    groupValue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.groupingId is not None and not isinstance(self.groupingId, GroupingFactorId):
            self.groupingId = GroupingFactorId(self.groupingId)

        if self.groupId is not None and not isinstance(self.groupId, GroupId):
            self.groupId = GroupId(self.groupId)

        if self.groupValue is not None and not isinstance(self.groupValue, str):
            self.groupValue = str(self.groupValue)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisMethod(NamedObject):
    """
    A set of one or more statistical operations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisMethod
    class_class_curie: ClassVar[str] = "ars:AnalysisMethod"
    class_name: ClassVar[str] = "AnalysisMethod"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisMethod

    id: Union[str, AnalysisMethodId] = None
    name: str = None
    operations: Union[Dict[Union[str, OperationId], Union[dict, "Operation"]], List[Union[dict, "Operation"]]] = empty_dict()
    label: Optional[str] = None
    description: Optional[str] = None
    documentRefs: Optional[Union[Union[dict, "DocumentReference"], List[Union[dict, "DocumentReference"]]]] = empty_list()
    codeTemplate: Optional[Union[dict, "AnalysisProgrammingCodeTemplate"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisMethodId):
            self.id = AnalysisMethodId(self.id)

        if self._is_empty(self.operations):
            self.MissingRequiredField("operations")
        self._normalize_inlined_as_list(slot_name="operations", slot_type=Operation, key_name="id", keyed=True)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.documentRefs, list):
            self.documentRefs = [self.documentRefs] if self.documentRefs is not None else []
        self.documentRefs = [v if isinstance(v, DocumentReference) else DocumentReference(**as_dict(v)) for v in self.documentRefs]

        if self.codeTemplate is not None and not isinstance(self.codeTemplate, AnalysisProgrammingCodeTemplate):
            self.codeTemplate = AnalysisProgrammingCodeTemplate(**as_dict(self.codeTemplate))

        super().__post_init__(**kwargs)


@dataclass
class Operation(NamedObject):
    """
    A statistical operation that produces a single analysis result value as part of an analysis method.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.Operation
    class_class_curie: ClassVar[str] = "ars:Operation"
    class_name: ClassVar[str] = "Operation"
    class_model_uri: ClassVar[URIRef] = ARS.Operation

    id: Union[str, OperationId] = None
    name: str = None
    label: Optional[str] = None
    referencedOperationRelationships: Optional[Union[Dict[Union[str, ReferencedOperationRelationshipId], Union[dict, "ReferencedOperationRelationship"]], List[Union[dict, "ReferencedOperationRelationship"]]]] = empty_dict()
    resultPattern: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationId):
            self.id = OperationId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        self._normalize_inlined_as_list(slot_name="referencedOperationRelationships", slot_type=ReferencedOperationRelationship, key_name="id", keyed=True)

        if self.resultPattern is not None and not isinstance(self.resultPattern, str):
            self.resultPattern = str(self.resultPattern)

        super().__post_init__(**kwargs)


@dataclass
class ReferencedOperationRelationship(YAMLRoot):
    """
    A reference to a statistical operation whose results are used in the calculation of the result for this operation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ReferencedOperationRelationship
    class_class_curie: ClassVar[str] = "ars:ReferencedOperationRelationship"
    class_name: ClassVar[str] = "ReferencedOperationRelationship"
    class_model_uri: ClassVar[URIRef] = ARS.ReferencedOperationRelationship

    id: Union[str, ReferencedOperationRelationshipId] = None
    referencedOperationRole: Union[dict, "ExtensibleTerminologyTerm"] = None
    operationId: Union[str, OperationId] = None
    analysisId: Optional[Union[str, AnalysisId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferencedOperationRelationshipId):
            self.id = ReferencedOperationRelationshipId(self.id)

        if self._is_empty(self.referencedOperationRole):
            self.MissingRequiredField("referencedOperationRole")
        if not isinstance(self.referencedOperationRole, ExtensibleTerminologyTerm):
            self.referencedOperationRole = ExtensibleTerminologyTerm(**as_dict(self.referencedOperationRole))

        if self._is_empty(self.operationId):
            self.MissingRequiredField("operationId")
        if not isinstance(self.operationId, OperationId):
            self.operationId = OperationId(self.operationId)

        if self.analysisId is not None and not isinstance(self.analysisId, AnalysisId):
            self.analysisId = AnalysisId(self.analysisId)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisOutputProgrammingCode(YAMLRoot):
    """
    Programming statements and/or a reference to the program used to perform a specific analysis or create a specific
    output.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisOutputProgrammingCode
    class_class_curie: ClassVar[str] = "ars:AnalysisOutputProgrammingCode"
    class_name: ClassVar[str] = "AnalysisOutputProgrammingCode"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisOutputProgrammingCode

    context: str = None
    code: Optional[str] = None
    documentRef: Optional[Union[dict, "DocumentReference"]] = None
    parameters: Optional[Union[Union[dict, "AnalysisOutputCodeParameter"], List[Union[dict, "AnalysisOutputCodeParameter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, str):
            self.context = str(self.context)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.documentRef is not None and not isinstance(self.documentRef, DocumentReference):
            self.documentRef = DocumentReference(**as_dict(self.documentRef))

        if not isinstance(self.parameters, list):
            self.parameters = [self.parameters] if self.parameters is not None else []
        self.parameters = [v if isinstance(v, AnalysisOutputCodeParameter) else AnalysisOutputCodeParameter(**as_dict(v)) for v in self.parameters]

        super().__post_init__(**kwargs)


@dataclass
class AnalysisProgrammingCodeTemplate(YAMLRoot):
    """
    Programming statements and/or a reference to a used as a template for creation of a program to perform method
    operations for a specific analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisProgrammingCodeTemplate
    class_class_curie: ClassVar[str] = "ars:AnalysisProgrammingCodeTemplate"
    class_name: ClassVar[str] = "AnalysisProgrammingCodeTemplate"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisProgrammingCodeTemplate

    context: str = None
    code: Optional[str] = None
    documentRef: Optional[Union[dict, "DocumentReference"]] = None
    parameters: Optional[Union[Union[dict, "TemplateCodeParameter"], List[Union[dict, "TemplateCodeParameter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, str):
            self.context = str(self.context)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.documentRef is not None and not isinstance(self.documentRef, DocumentReference):
            self.documentRef = DocumentReference(**as_dict(self.documentRef))

        if not isinstance(self.parameters, list):
            self.parameters = [self.parameters] if self.parameters is not None else []
        self.parameters = [v if isinstance(v, TemplateCodeParameter) else TemplateCodeParameter(**as_dict(v)) for v in self.parameters]

        super().__post_init__(**kwargs)


@dataclass
class CodeParameter(NamedObject):
    """
    A replacement parameter whose value is substituted in template programming code to create statements required for
    a specific analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.CodeParameter
    class_class_curie: ClassVar[str] = "ars:CodeParameter"
    class_name: ClassVar[str] = "CodeParameter"
    class_model_uri: ClassVar[URIRef] = ARS.CodeParameter

    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisOutputCodeParameter(CodeParameter):
    """
    A parameter whose value is used in programming code for a specific analysis or output.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisOutputCodeParameter
    class_class_curie: ClassVar[str] = "ars:AnalysisOutputCodeParameter"
    class_name: ClassVar[str] = "AnalysisOutputCodeParameter"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisOutputCodeParameter

    name: str = None
    value: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class TemplateCodeParameter(CodeParameter):
    """
    A replacement parameter whose value is substituted in template programming code to create statements required for
    a specific analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.TemplateCodeParameter
    class_class_curie: ClassVar[str] = "ars:TemplateCodeParameter"
    class_name: ClassVar[str] = "TemplateCodeParameter"
    class_model_uri: ClassVar[URIRef] = ARS.TemplateCodeParameter

    name: str = None
    valueSource: Optional[str] = None
    value: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.valueSource is not None and not isinstance(self.valueSource, str):
            self.valueSource = str(self.valueSource)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class Output(NamedObject):
    """
    A report of results and their evaluation based on planned analyses performed during the course of a trial.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.Output
    class_class_curie: ClassVar[str] = "ars:Output"
    class_name: ClassVar[str] = "Output"
    class_model_uri: ClassVar[URIRef] = ARS.Output

    id: Union[str, OutputId] = None
    name: str = None
    version: Optional[int] = None
    fileSpecifications: Optional[Union[Union[dict, "OutputFile"], List[Union[dict, "OutputFile"]]]] = empty_list()
    displays: Optional[Union[Union[dict, "OrderedDisplay"], List[Union[dict, "OrderedDisplay"]]]] = empty_list()
    categoryIds: Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]] = empty_list()
    documentRefs: Optional[Union[Union[dict, "DocumentReference"], List[Union[dict, "DocumentReference"]]]] = empty_list()
    programmingCode: Optional[Union[dict, AnalysisOutputProgrammingCode]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OutputId):
            self.id = OutputId(self.id)

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if not isinstance(self.fileSpecifications, list):
            self.fileSpecifications = [self.fileSpecifications] if self.fileSpecifications is not None else []
        self.fileSpecifications = [v if isinstance(v, OutputFile) else OutputFile(**as_dict(v)) for v in self.fileSpecifications]

        if not isinstance(self.displays, list):
            self.displays = [self.displays] if self.displays is not None else []
        self.displays = [v if isinstance(v, OrderedDisplay) else OrderedDisplay(**as_dict(v)) for v in self.displays]

        if not isinstance(self.categoryIds, list):
            self.categoryIds = [self.categoryIds] if self.categoryIds is not None else []
        self.categoryIds = [v if isinstance(v, AnalysisCategoryId) else AnalysisCategoryId(v) for v in self.categoryIds]

        if not isinstance(self.documentRefs, list):
            self.documentRefs = [self.documentRefs] if self.documentRefs is not None else []
        self.documentRefs = [v if isinstance(v, DocumentReference) else DocumentReference(**as_dict(v)) for v in self.documentRefs]

        if self.programmingCode is not None and not isinstance(self.programmingCode, AnalysisOutputProgrammingCode):
            self.programmingCode = AnalysisOutputProgrammingCode(**as_dict(self.programmingCode))

        super().__post_init__(**kwargs)


@dataclass
class OutputFile(NamedObject):
    """
    A file containing analysis output displays.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OutputFile
    class_class_curie: ClassVar[str] = "ars:OutputFile"
    class_name: ClassVar[str] = "OutputFile"
    class_model_uri: ClassVar[URIRef] = ARS.OutputFile

    name: str = None
    fileType: Optional[Union[dict, "ExtensibleTerminologyTerm"]] = None
    location: Optional[Union[str, URI]] = None
    style: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fileType is not None and not isinstance(self.fileType, ExtensibleTerminologyTerm):
            self.fileType = ExtensibleTerminologyTerm(**as_dict(self.fileType))

        if self.location is not None and not isinstance(self.location, URI):
            self.location = URI(self.location)

        if self.style is not None and not isinstance(self.style, str):
            self.style = str(self.style)

        super().__post_init__(**kwargs)


@dataclass
class OrderedDisplay(YAMLRoot):
    """
    A display ordered with respect to other displays in an analysis output.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedDisplay
    class_class_curie: ClassVar[str] = "ars:OrderedDisplay"
    class_name: ClassVar[str] = "OrderedDisplay"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedDisplay

    order: int = None
    display: Optional[Union[dict, "OutputDisplay"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.display is not None and not isinstance(self.display, OutputDisplay):
            self.display = OutputDisplay(**as_dict(self.display))

        super().__post_init__(**kwargs)


@dataclass
class OutputDisplay(NamedObject):
    """
    A tabular representation of the results of one or more analyses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OutputDisplay
    class_class_curie: ClassVar[str] = "ars:OutputDisplay"
    class_name: ClassVar[str] = "OutputDisplay"
    class_model_uri: ClassVar[URIRef] = ARS.OutputDisplay

    id: Union[str, OutputDisplayId] = None
    name: str = None
    version: Optional[int] = None
    displayTitle: Optional[str] = None
    displaySections: Optional[Union[Union[dict, "DisplaySection"], List[Union[dict, "DisplaySection"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OutputDisplayId):
            self.id = OutputDisplayId(self.id)

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if self.displayTitle is not None and not isinstance(self.displayTitle, str):
            self.displayTitle = str(self.displayTitle)

        if not isinstance(self.displaySections, list):
            self.displaySections = [self.displaySections] if self.displaySections is not None else []
        self.displaySections = [v if isinstance(v, DisplaySection) else DisplaySection(**as_dict(v)) for v in self.displaySections]

        super().__post_init__(**kwargs)


@dataclass
class DisplaySection(YAMLRoot):
    """
    A part of a tabular display containing one or more pieces of informational text (e.g., title, footnote).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DisplaySection
    class_class_curie: ClassVar[str] = "ars:DisplaySection"
    class_name: ClassVar[str] = "DisplaySection"
    class_model_uri: ClassVar[URIRef] = ARS.DisplaySection

    sectionType: Optional[Union[str, "DisplaySectionTypeEnum"]] = None
    orderedSubSections: Optional[Union[Union[dict, "OrderedDisplaySubSection"], List[Union[dict, "OrderedDisplaySubSection"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sectionType is not None and not isinstance(self.sectionType, DisplaySectionTypeEnum):
            self.sectionType = DisplaySectionTypeEnum(self.sectionType)

        if not isinstance(self.orderedSubSections, list):
            self.orderedSubSections = [self.orderedSubSections] if self.orderedSubSections is not None else []
        self.orderedSubSections = [v if isinstance(v, OrderedDisplaySubSection) else OrderedDisplaySubSection(**as_dict(v)) for v in self.orderedSubSections]

        super().__post_init__(**kwargs)


@dataclass
class OrderedDisplaySubSection(YAMLRoot):
    """
    A single subsection ordered with respect to other subsections in the same section of a display.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedDisplaySubSection
    class_class_curie: ClassVar[str] = "ars:OrderedDisplaySubSection"
    class_name: ClassVar[str] = "OrderedDisplaySubSection"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedDisplaySubSection

    order: int = None
    subSection: Optional[Union[dict, "DisplaySubSection"]] = None
    subSectionId: Optional[Union[str, DisplaySubSectionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.subSection is not None and not isinstance(self.subSection, DisplaySubSection):
            self.subSection = DisplaySubSection(**as_dict(self.subSection))

        if self.subSectionId is not None and not isinstance(self.subSectionId, DisplaySubSectionId):
            self.subSectionId = DisplaySubSectionId(self.subSectionId)

        super().__post_init__(**kwargs)


@dataclass
class OrderedSubSection(OrderedDisplaySubSection):
    """
    A subsection ordered with respect to other subsections of the same type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedSubSection
    class_class_curie: ClassVar[str] = "ars:OrderedSubSection"
    class_name: ClassVar[str] = "OrderedSubSection"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedSubSection

    order: int = None
    subSection: Union[dict, "DisplaySubSection"] = None
    subSectionId: Optional[Union[str, DisplaySubSectionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subSection):
            self.MissingRequiredField("subSection")
        if not isinstance(self.subSection, DisplaySubSection):
            self.subSection = DisplaySubSection(**as_dict(self.subSection))

        if self.subSectionId is not None and not isinstance(self.subSectionId, DisplaySubSectionId):
            self.subSectionId = DisplaySubSectionId(self.subSectionId)

        super().__post_init__(**kwargs)


@dataclass
class OrderedSubSectionRef(OrderedDisplaySubSection):
    """
    A reference to a subsection defined either globally or in another display section, ordered with respect to other
    subsections of the same type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OrderedSubSectionRef
    class_class_curie: ClassVar[str] = "ars:OrderedSubSectionRef"
    class_name: ClassVar[str] = "OrderedSubSectionRef"
    class_model_uri: ClassVar[URIRef] = ARS.OrderedSubSectionRef

    order: int = None
    subSectionId: Union[str, DisplaySubSectionId] = None
    subSection: Optional[Union[dict, "DisplaySubSection"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subSectionId):
            self.MissingRequiredField("subSectionId")
        if not isinstance(self.subSectionId, DisplaySubSectionId):
            self.subSectionId = DisplaySubSectionId(self.subSectionId)

        if self.subSection is not None and not isinstance(self.subSection, DisplaySubSection):
            self.subSection = DisplaySubSection(**as_dict(self.subSection))

        super().__post_init__(**kwargs)


@dataclass
class DisplaySubSection(YAMLRoot):
    """
    An occurrence of a display section containing text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DisplaySubSection
    class_class_curie: ClassVar[str] = "ars:DisplaySubSection"
    class_name: ClassVar[str] = "DisplaySubSection"
    class_model_uri: ClassVar[URIRef] = ARS.DisplaySubSection

    id: Union[str, DisplaySubSectionId] = None
    text: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisplaySubSectionId):
            self.id = DisplaySubSectionId(self.id)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass
class GlobalDisplaySection(YAMLRoot):
    """
    A global definition for part of a tabular display containing one or more pieces of informational text that may be
    used in multiple displays.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.GlobalDisplaySection
    class_class_curie: ClassVar[str] = "ars:GlobalDisplaySection"
    class_name: ClassVar[str] = "GlobalDisplaySection"
    class_model_uri: ClassVar[URIRef] = ARS.GlobalDisplaySection

    sectionType: Optional[Union[str, "DisplaySectionTypeEnum"]] = None
    subSections: Optional[Union[Dict[Union[str, DisplaySubSectionId], Union[dict, DisplaySubSection]], List[Union[dict, DisplaySubSection]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sectionType is not None and not isinstance(self.sectionType, DisplaySectionTypeEnum):
            self.sectionType = DisplaySectionTypeEnum(self.sectionType)

        self._normalize_inlined_as_list(slot_name="subSections", slot_type=DisplaySubSection, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class WhereClause(YAMLRoot):
    """
    Selection criteria defined as either a simple condition ([variable] [comparator] [value(s)]) or a compound
    expression that may combine simple conditions or compound expressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.WhereClause
    class_class_curie: ClassVar[str] = "ars:WhereClause"
    class_name: ClassVar[str] = "WhereClause"
    class_model_uri: ClassVar[URIRef] = ARS.WhereClause

    level: Optional[int] = None
    order: Optional[int] = None
    condition: Optional[Union[dict, "WhereClauseCondition"]] = None
    compoundExpression: Optional[Union[dict, "WhereClauseCompoundExpression"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.level is not None and not isinstance(self.level, int):
            self.level = int(self.level)

        if self.order is not None and not isinstance(self.order, int):
            self.order = int(self.order)

        if self.condition is not None and not isinstance(self.condition, WhereClauseCondition):
            self.condition = WhereClauseCondition(**as_dict(self.condition))

        if self.compoundExpression is not None and not isinstance(self.compoundExpression, WhereClauseCompoundExpression):
            self.compoundExpression = WhereClauseCompoundExpression(**as_dict(self.compoundExpression))

        super().__post_init__(**kwargs)


@dataclass
class WhereClauseCondition(YAMLRoot):
    """
    A simple selection criterion exressed as [dataset].[variable] [comparator] [value(s)]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.WhereClauseCondition
    class_class_curie: ClassVar[str] = "ars:WhereClauseCondition"
    class_name: ClassVar[str] = "WhereClauseCondition"
    class_model_uri: ClassVar[URIRef] = ARS.WhereClauseCondition

    dataset: Optional[str] = None
    variable: Optional[str] = None
    comparator: Optional[Union[str, "ConditionComparatorEnum"]] = None
    value: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        if self.variable is not None and not isinstance(self.variable, str):
            self.variable = str(self.variable)

        if self.comparator is not None and not isinstance(self.comparator, ConditionComparatorEnum):
            self.comparator = ConditionComparatorEnum(self.comparator)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class WhereClauseCompoundExpression(YAMLRoot):
    """
    A compound expression consisting of either two or more where clauses combined with the `AND` or `OR` logical
    operator, or a single where clause negated with the `NOT` logical operator.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.WhereClauseCompoundExpression
    class_class_curie: ClassVar[str] = "ars:WhereClauseCompoundExpression"
    class_name: ClassVar[str] = "WhereClauseCompoundExpression"
    class_model_uri: ClassVar[URIRef] = ARS.WhereClauseCompoundExpression

    logicalOperator: Union[str, "ExpressionLogicalOperatorEnum"] = None
    whereClauses: Optional[Union[Union[dict, WhereClause], List[Union[dict, WhereClause]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.logicalOperator):
            self.MissingRequiredField("logicalOperator")
        if not isinstance(self.logicalOperator, ExpressionLogicalOperatorEnum):
            self.logicalOperator = ExpressionLogicalOperatorEnum(self.logicalOperator)

        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, WhereClause) else WhereClause(**as_dict(v)) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundSetExpression(WhereClauseCompoundExpression):
    """
    A compound expression consisting of either two or more identified analysis sets combined with the `AND` or `OR`
    logical operator, or a single identified analysis set negated with the `NOT` logical operator.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.CompoundSetExpression
    class_class_curie: ClassVar[str] = "ars:CompoundSetExpression"
    class_name: ClassVar[str] = "CompoundSetExpression"
    class_model_uri: ClassVar[URIRef] = ARS.CompoundSetExpression

    logicalOperator: Union[str, "ExpressionLogicalOperatorEnum"] = None
    whereClauses: Optional[Union[Union[str, AnalysisSetId], List[Union[str, AnalysisSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, AnalysisSetId) else AnalysisSetId(v) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundGroupExpression(WhereClauseCompoundExpression):
    """
    A compound expression consisting of either two or more identified group combined with the `AND` or `OR` logical
    operator, or a single identified group negated with the `NOT` logical operator.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.CompoundGroupExpression
    class_class_curie: ClassVar[str] = "ars:CompoundGroupExpression"
    class_name: ClassVar[str] = "CompoundGroupExpression"
    class_model_uri: ClassVar[URIRef] = ARS.CompoundGroupExpression

    logicalOperator: Union[str, "ExpressionLogicalOperatorEnum"] = None
    whereClauses: Optional[Union[Union[str, GroupId], List[Union[str, GroupId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, GroupId) else GroupId(v) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundSubsetExpression(WhereClauseCompoundExpression):
    """
    A compound expression consisting of either two or more where clauses combined with the `AND` or `OR` logical
    operator, or a single where clause negated with the `NOT` logical operator.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.CompoundSubsetExpression
    class_class_curie: ClassVar[str] = "ars:CompoundSubsetExpression"
    class_name: ClassVar[str] = "CompoundSubsetExpression"
    class_model_uri: ClassVar[URIRef] = ARS.CompoundSubsetExpression

    logicalOperator: Union[str, "ExpressionLogicalOperatorEnum"] = None
    whereClauses: Optional[Union[Union[dict, WhereClause], List[Union[dict, WhereClause]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, WhereClause) else WhereClause(**as_dict(v)) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class AnalysisSet(WhereClause):
    """
    A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical
    section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set
    based upon the intent-to-treat principle. [ICH E9]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisSet
    class_class_curie: ClassVar[str] = "ars:AnalysisSet"
    class_name: ClassVar[str] = "AnalysisSet"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisSet

    id: Union[str, AnalysisSetId] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSetExpression]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisSetId):
            self.id = AnalysisSetId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.compoundExpression is not None and not isinstance(self.compoundExpression, CompoundSetExpression):
            self.compoundExpression = CompoundSetExpression(**as_dict(self.compoundExpression))

        super().__post_init__(**kwargs)


@dataclass
class GroupingFactor(YAMLRoot):
    """
    A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.GroupingFactor
    class_class_curie: ClassVar[str] = "ars:GroupingFactor"
    class_name: ClassVar[str] = "GroupingFactor"
    class_model_uri: ClassVar[URIRef] = ARS.GroupingFactor

    id: Union[str, GroupingFactorId] = None
    dataDriven: Union[bool, Bool] = None
    label: Optional[str] = None
    groupingVariable: Optional[str] = None
    groups: Optional[Union[Dict[Union[str, GroupId], Union[dict, "Group"]], List[Union[dict, "Group"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroupingFactorId):
            self.id = GroupingFactorId(self.id)

        if self._is_empty(self.dataDriven):
            self.MissingRequiredField("dataDriven")
        if not isinstance(self.dataDriven, Bool):
            self.dataDriven = Bool(self.dataDriven)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.groupingVariable is not None and not isinstance(self.groupingVariable, str):
            self.groupingVariable = str(self.groupingVariable)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=Group, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SubjectGroupingFactor(GroupingFactor):
    """
    A factor used to subdivide the subject population for comparative analysis (e.g., treatment, sex, race, age).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SubjectGroupingFactor
    class_class_curie: ClassVar[str] = "ars:SubjectGroupingFactor"
    class_name: ClassVar[str] = "SubjectGroupingFactor"
    class_model_uri: ClassVar[URIRef] = ARS.SubjectGroupingFactor

    id: Union[str, SubjectGroupingFactorId] = None
    dataDriven: Union[bool, Bool] = None
    groups: Optional[Union[Dict[Union[str, AnalysisGroupId], Union[dict, "AnalysisGroup"]], List[Union[dict, "AnalysisGroup"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubjectGroupingFactorId):
            self.id = SubjectGroupingFactorId(self.id)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=AnalysisGroup, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DataGroupingFactor(GroupingFactor):
    """
    A factor used to subdivide data records in an analysis dataset for analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DataGroupingFactor
    class_class_curie: ClassVar[str] = "ars:DataGroupingFactor"
    class_name: ClassVar[str] = "DataGroupingFactor"
    class_model_uri: ClassVar[URIRef] = ARS.DataGroupingFactor

    id: Union[str, DataGroupingFactorId] = None
    dataDriven: Union[bool, Bool] = None
    groups: Optional[Union[Dict[Union[str, DataGroupId], Union[dict, "DataGroup"]], List[Union[dict, "DataGroup"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGroupingFactorId):
            self.id = DataGroupingFactorId(self.id)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=DataGroup, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Group(WhereClause):
    """
    A subdivision of the subject population or analysis dataset record set based on a defined factor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.Group
    class_class_curie: ClassVar[str] = "ars:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = ARS.Group

    id: Union[str, GroupId] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundGroupExpression]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroupId):
            self.id = GroupId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.compoundExpression is not None and not isinstance(self.compoundExpression, CompoundGroupExpression):
            self.compoundExpression = CompoundGroupExpression(**as_dict(self.compoundExpression))

        super().__post_init__(**kwargs)


@dataclass
class AnalysisGroup(Group):
    """
    A subdivision of the subject population based on a defined factor (e.g., subjects whose treatment is Drug A,
    subjects whose gender is male).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisGroup
    class_class_curie: ClassVar[str] = "ars:AnalysisGroup"
    class_name: ClassVar[str] = "AnalysisGroup"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisGroup

    id: Union[str, AnalysisGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisGroupId):
            self.id = AnalysisGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataGroup(Group):
    """
    A subdivision of the analysis dataset records based on a defined factor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DataGroup
    class_class_curie: ClassVar[str] = "ars:DataGroup"
    class_name: ClassVar[str] = "DataGroup"
    class_model_uri: ClassVar[URIRef] = ARS.DataGroup

    id: Union[str, DataGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGroupId):
            self.id = DataGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataSubset(WhereClause):
    """
    A subset of data identified by selection criteria for inclusion in the analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DataSubset
    class_class_curie: ClassVar[str] = "ars:DataSubset"
    class_name: ClassVar[str] = "DataSubset"
    class_model_uri: ClassVar[URIRef] = ARS.DataSubset

    id: Union[str, DataSubsetId] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSubsetExpression]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubsetId):
            self.id = DataSubsetId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.compoundExpression is not None and not isinstance(self.compoundExpression, CompoundSubsetExpression):
            self.compoundExpression = CompoundSubsetExpression(**as_dict(self.compoundExpression))

        super().__post_init__(**kwargs)


@dataclass
class ReferenceDocument(NamedObject):
    """
    An external document containing supporting documentation or programming code.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ReferenceDocument
    class_class_curie: ClassVar[str] = "ars:ReferenceDocument"
    class_name: ClassVar[str] = "ReferenceDocument"
    class_model_uri: ClassVar[URIRef] = ARS.ReferenceDocument

    id: Union[str, ReferenceDocumentId] = None
    name: str = None
    location: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceDocumentId):
            self.id = ReferenceDocumentId(self.id)

        if self.location is not None and not isinstance(self.location, URI):
            self.location = URI(self.location)

        super().__post_init__(**kwargs)


@dataclass
class DocumentReference(YAMLRoot):
    """
    A reference to an external document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.DocumentReference
    class_class_curie: ClassVar[str] = "ars:DocumentReference"
    class_name: ClassVar[str] = "DocumentReference"
    class_model_uri: ClassVar[URIRef] = ARS.DocumentReference

    referenceDocumentId: Union[str, ReferenceDocumentId] = None
    pageRefs: Optional[Union[Union[dict, "PageRef"], List[Union[dict, "PageRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.referenceDocumentId):
            self.MissingRequiredField("referenceDocumentId")
        if not isinstance(self.referenceDocumentId, ReferenceDocumentId):
            self.referenceDocumentId = ReferenceDocumentId(self.referenceDocumentId)

        if not isinstance(self.pageRefs, list):
            self.pageRefs = [self.pageRefs] if self.pageRefs is not None else []
        self.pageRefs = [v if isinstance(v, PageRef) else PageRef(**as_dict(v)) for v in self.pageRefs]

        super().__post_init__(**kwargs)


@dataclass
class PageRef(YAMLRoot):
    """
    A reference to a specific part of a document as indicated by a list of one or more page numbers, a range of page
    numbers, or a list of named destinations in the document (e.g. bookmarks).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.PageRef
    class_class_curie: ClassVar[str] = "ars:PageRef"
    class_name: ClassVar[str] = "PageRef"
    class_model_uri: ClassVar[URIRef] = ARS.PageRef

    refType: Union[str, "PageRefTypeEnum"] = None
    label: Optional[str] = None
    pageNames: Optional[Union[str, List[str]]] = empty_list()
    pageNumbers: Optional[Union[int, List[int]]] = empty_list()
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.refType):
            self.MissingRequiredField("refType")
        if not isinstance(self.refType, PageRefTypeEnum):
            self.refType = PageRefTypeEnum(self.refType)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.pageNames, list):
            self.pageNames = [self.pageNames] if self.pageNames is not None else []
        self.pageNames = [v if isinstance(v, str) else str(v) for v in self.pageNames]

        if not isinstance(self.pageNumbers, list):
            self.pageNumbers = [self.pageNumbers] if self.pageNumbers is not None else []
        self.pageNumbers = [v if isinstance(v, int) else int(v) for v in self.pageNumbers]

        if self.firstPage is not None and not isinstance(self.firstPage, int):
            self.firstPage = int(self.firstPage)

        if self.lastPage is not None and not isinstance(self.lastPage, int):
            self.lastPage = int(self.lastPage)

        super().__post_init__(**kwargs)


@dataclass
class PageNumberListRef(PageRef):
    """
    One or more individual pages in the reference document, referenced by page number.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.PageNumberListRef
    class_class_curie: ClassVar[str] = "ars:PageNumberListRef"
    class_name: ClassVar[str] = "PageNumberListRef"
    class_model_uri: ClassVar[URIRef] = ARS.PageNumberListRef

    refType: Union[str, "PageRefTypeEnum"] = None
    pageNumbers: Union[int, List[int]] = None
    pageNames: Optional[Union[str, List[str]]] = empty_list()
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.refType):
            self.MissingRequiredField("refType")
        if not isinstance(self.refType, PageRefTypeEnum):
            self.refType = PageRefTypeEnum(self.refType)

        if self._is_empty(self.pageNumbers):
            self.MissingRequiredField("pageNumbers")
        if not isinstance(self.pageNumbers, list):
            self.pageNumbers = [self.pageNumbers] if self.pageNumbers is not None else []
        self.pageNumbers = [v if isinstance(v, int) else int(v) for v in self.pageNumbers]

        if not isinstance(self.pageNames, list):
            self.pageNames = [self.pageNames] if self.pageNames is not None else []
        self.pageNames = [v if isinstance(v, str) else str(v) for v in self.pageNames]

        if self.firstPage is not None and not isinstance(self.firstPage, int):
            self.firstPage = int(self.firstPage)

        if self.lastPage is not None and not isinstance(self.lastPage, int):
            self.lastPage = int(self.lastPage)

        super().__post_init__(**kwargs)


@dataclass
class PageNumberRangeRef(PageRef):
    """
    A range of pages in the reference document, indicated by the first and last page number in the range.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.PageNumberRangeRef
    class_class_curie: ClassVar[str] = "ars:PageNumberRangeRef"
    class_name: ClassVar[str] = "PageNumberRangeRef"
    class_model_uri: ClassVar[URIRef] = ARS.PageNumberRangeRef

    refType: Union[str, "PageRefTypeEnum"] = None
    firstPage: int = None
    lastPage: int = None
    pageNumbers: Optional[Union[int, List[int]]] = empty_list()
    pageNames: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.refType):
            self.MissingRequiredField("refType")
        if not isinstance(self.refType, PageRefTypeEnum):
            self.refType = PageRefTypeEnum(self.refType)

        if self._is_empty(self.firstPage):
            self.MissingRequiredField("firstPage")
        if not isinstance(self.firstPage, int):
            self.firstPage = int(self.firstPage)

        if self._is_empty(self.lastPage):
            self.MissingRequiredField("lastPage")
        if not isinstance(self.lastPage, int):
            self.lastPage = int(self.lastPage)

        if not isinstance(self.pageNumbers, list):
            self.pageNumbers = [self.pageNumbers] if self.pageNumbers is not None else []
        self.pageNumbers = [v if isinstance(v, int) else int(v) for v in self.pageNumbers]

        if not isinstance(self.pageNames, list):
            self.pageNames = [self.pageNames] if self.pageNames is not None else []
        self.pageNames = [v if isinstance(v, str) else str(v) for v in self.pageNames]

        super().__post_init__(**kwargs)


@dataclass
class PageNameRef(PageRef):
    """
    One or more pages in the reference document, referenced by named destination.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.PageNameRef
    class_class_curie: ClassVar[str] = "ars:PageNameRef"
    class_name: ClassVar[str] = "PageNameRef"
    class_model_uri: ClassVar[URIRef] = ARS.PageNameRef

    refType: Union[str, "PageRefTypeEnum"] = None
    pageNames: Union[str, List[str]] = None
    pageNumbers: Optional[Union[int, List[int]]] = empty_list()
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.refType):
            self.MissingRequiredField("refType")
        if not isinstance(self.refType, PageRefTypeEnum):
            self.refType = PageRefTypeEnum(self.refType)

        if self._is_empty(self.pageNames):
            self.MissingRequiredField("pageNames")
        if not isinstance(self.pageNames, list):
            self.pageNames = [self.pageNames] if self.pageNames is not None else []
        self.pageNames = [v if isinstance(v, str) else str(v) for v in self.pageNames]

        if not isinstance(self.pageNumbers, list):
            self.pageNumbers = [self.pageNumbers] if self.pageNumbers is not None else []
        self.pageNumbers = [v if isinstance(v, int) else int(v) for v in self.pageNumbers]

        if self.firstPage is not None and not isinstance(self.firstPage, int):
            self.firstPage = int(self.firstPage)

        if self.lastPage is not None and not isinstance(self.lastPage, int):
            self.lastPage = int(self.lastPage)

        super().__post_init__(**kwargs)


@dataclass
class TerminologyExtension(YAMLRoot):
    """
    An extensible set of controlled terminology that has been extended with at least one sponsor-defined term.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.TerminologyExtension
    class_class_curie: ClassVar[str] = "ars:TerminologyExtension"
    class_name: ClassVar[str] = "TerminologyExtension"
    class_model_uri: ClassVar[URIRef] = ARS.TerminologyExtension

    id: Union[str, TerminologyExtensionId] = None
    sponsorTerms: Union[Dict[Union[str, SponsorTermId], Union[dict, "SponsorTerm"]], List[Union[dict, "SponsorTerm"]]] = empty_dict()
    enumeration: Optional[Union[str, "ExtensibleTerminologyEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TerminologyExtensionId):
            self.id = TerminologyExtensionId(self.id)

        if self._is_empty(self.sponsorTerms):
            self.MissingRequiredField("sponsorTerms")
        self._normalize_inlined_as_list(slot_name="sponsorTerms", slot_type=SponsorTerm, key_name="id", keyed=True)

        if self.enumeration is not None and not isinstance(self.enumeration, ExtensibleTerminologyEnum):
            self.enumeration = ExtensibleTerminologyEnum(self.enumeration)

        super().__post_init__(**kwargs)


@dataclass
class SponsorTerm(YAMLRoot):
    """
    A sponsor-defined term that is included in an extensible set of controlled terminology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SponsorTerm
    class_class_curie: ClassVar[str] = "ars:SponsorTerm"
    class_name: ClassVar[str] = "SponsorTerm"
    class_model_uri: ClassVar[URIRef] = ARS.SponsorTerm

    id: Union[str, SponsorTermId] = None
    submissionValue: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SponsorTermId):
            self.id = SponsorTermId(self.id)

        if self._is_empty(self.submissionValue):
            self.MissingRequiredField("submissionValue")
        if not isinstance(self.submissionValue, str):
            self.submissionValue = str(self.submissionValue)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ExtensibleTerminologyTerm(YAMLRoot):
    """
    The term used for an attribute whose terminology is extensible.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.ExtensibleTerminologyTerm
    class_class_curie: ClassVar[str] = "ars:ExtensibleTerminologyTerm"
    class_name: ClassVar[str] = "ExtensibleTerminologyTerm"
    class_model_uri: ClassVar[URIRef] = ARS.ExtensibleTerminologyTerm

    controlledTerm: Optional[str] = None
    sponsorTermId: Optional[Union[str, SponsorTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.controlledTerm is not None and not isinstance(self.controlledTerm, str):
            self.controlledTerm = str(self.controlledTerm)

        if self.sponsorTermId is not None and not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisReason(ExtensibleTerminologyTerm):
    """
    The rationale for performing this analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisReason
    class_class_curie: ClassVar[str] = "ars:AnalysisReason"
    class_name: ClassVar[str] = "AnalysisReason"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisReason

    controlledTerm: Union[str, "AnalysisReasonEnum"] = None
    sponsorTermId: Optional[Union[str, SponsorTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.controlledTerm):
            self.MissingRequiredField("controlledTerm")
        if not isinstance(self.controlledTerm, AnalysisReasonEnum):
            self.controlledTerm = AnalysisReasonEnum(self.controlledTerm)

        if self.sponsorTermId is not None and not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        super().__post_init__(**kwargs)


@dataclass
class SponsorAnalysisReason(ExtensibleTerminologyTerm):
    """
    The sponsor-defined rationale for performing this analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SponsorAnalysisReason
    class_class_curie: ClassVar[str] = "ars:SponsorAnalysisReason"
    class_name: ClassVar[str] = "SponsorAnalysisReason"
    class_model_uri: ClassVar[URIRef] = ARS.SponsorAnalysisReason

    sponsorTermId: Union[str, SponsorTermId] = None
    controlledTerm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sponsorTermId):
            self.MissingRequiredField("sponsorTermId")
        if not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        if self.controlledTerm is not None and not isinstance(self.controlledTerm, str):
            self.controlledTerm = str(self.controlledTerm)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisPurpose(ExtensibleTerminologyTerm):
    """
    The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.AnalysisPurpose
    class_class_curie: ClassVar[str] = "ars:AnalysisPurpose"
    class_name: ClassVar[str] = "AnalysisPurpose"
    class_model_uri: ClassVar[URIRef] = ARS.AnalysisPurpose

    controlledTerm: Union[str, "AnalysisPurposeEnum"] = None
    sponsorTermId: Optional[Union[str, SponsorTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.controlledTerm):
            self.MissingRequiredField("controlledTerm")
        if not isinstance(self.controlledTerm, AnalysisPurposeEnum):
            self.controlledTerm = AnalysisPurposeEnum(self.controlledTerm)

        if self.sponsorTermId is not None and not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        super().__post_init__(**kwargs)


@dataclass
class SponsorAnalysisPurpose(ExtensibleTerminologyTerm):
    """
    The sponsor-defined purpose of the analysis within the body of evidence (e.g., section in the clinical study
    report).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SponsorAnalysisPurpose
    class_class_curie: ClassVar[str] = "ars:SponsorAnalysisPurpose"
    class_name: ClassVar[str] = "SponsorAnalysisPurpose"
    class_model_uri: ClassVar[URIRef] = ARS.SponsorAnalysisPurpose

    sponsorTermId: Union[str, SponsorTermId] = None
    controlledTerm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sponsorTermId):
            self.MissingRequiredField("sponsorTermId")
        if not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        if self.controlledTerm is not None and not isinstance(self.controlledTerm, str):
            self.controlledTerm = str(self.controlledTerm)

        super().__post_init__(**kwargs)


@dataclass
class OperationRole(ExtensibleTerminologyTerm):
    """
    The role that the referenced operation's result plays in the calculation of the result of this operation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OperationRole
    class_class_curie: ClassVar[str] = "ars:OperationRole"
    class_name: ClassVar[str] = "OperationRole"
    class_model_uri: ClassVar[URIRef] = ARS.OperationRole

    controlledTerm: Union[str, "OperationRoleEnum"] = None
    sponsorTermId: Optional[Union[str, SponsorTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.controlledTerm):
            self.MissingRequiredField("controlledTerm")
        if not isinstance(self.controlledTerm, OperationRoleEnum):
            self.controlledTerm = OperationRoleEnum(self.controlledTerm)

        if self.sponsorTermId is not None and not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        super().__post_init__(**kwargs)


@dataclass
class SponsorOperationRole(ExtensibleTerminologyTerm):
    """
    The sponsor-defined role that the referenced operation's result plays in the calculation of the result of this
    operation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SponsorOperationRole
    class_class_curie: ClassVar[str] = "ars:SponsorOperationRole"
    class_name: ClassVar[str] = "SponsorOperationRole"
    class_model_uri: ClassVar[URIRef] = ARS.SponsorOperationRole

    sponsorTermId: Union[str, SponsorTermId] = None
    controlledTerm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sponsorTermId):
            self.MissingRequiredField("sponsorTermId")
        if not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        if self.controlledTerm is not None and not isinstance(self.controlledTerm, str):
            self.controlledTerm = str(self.controlledTerm)

        super().__post_init__(**kwargs)


@dataclass
class OutputFileType(ExtensibleTerminologyTerm):
    """
    The file format of the file containing output from analyses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.OutputFileType
    class_class_curie: ClassVar[str] = "ars:OutputFileType"
    class_name: ClassVar[str] = "OutputFileType"
    class_model_uri: ClassVar[URIRef] = ARS.OutputFileType

    controlledTerm: Union[str, "OutputFileTypeEnum"] = None
    sponsorTermId: Optional[Union[str, SponsorTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.controlledTerm):
            self.MissingRequiredField("controlledTerm")
        if not isinstance(self.controlledTerm, OutputFileTypeEnum):
            self.controlledTerm = OutputFileTypeEnum(self.controlledTerm)

        if self.sponsorTermId is not None and not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        super().__post_init__(**kwargs)


@dataclass
class SponsorOutputFileType(ExtensibleTerminologyTerm):
    """
    The sponsor-defined file format of the file containing output from analyses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ARS.SponsorOutputFileType
    class_class_curie: ClassVar[str] = "ars:SponsorOutputFileType"
    class_name: ClassVar[str] = "SponsorOutputFileType"
    class_model_uri: ClassVar[URIRef] = ARS.SponsorOutputFileType

    sponsorTermId: Union[str, SponsorTermId] = None
    controlledTerm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sponsorTermId):
            self.MissingRequiredField("sponsorTermId")
        if not isinstance(self.sponsorTermId, SponsorTermId):
            self.sponsorTermId = SponsorTermId(self.sponsorTermId)

        if self.controlledTerm is not None and not isinstance(self.controlledTerm, str):
            self.controlledTerm = str(self.controlledTerm)

        super().__post_init__(**kwargs)


# Enumerations
class OutputFileTypeEnum(EnumDefinitionImpl):
    """
    The file format of the file containing output from analyses.
    """
    pdf = PermissibleValue(
        text="pdf",
        description="Portable Document Format (PDF)")
    rtf = PermissibleValue(
        text="rtf",
        description="Rich Text Format (RTF)")
    txt = PermissibleValue(
        text="txt",
        description="Plain text")

    _defn = EnumDefinition(
        name="OutputFileTypeEnum",
        description="The file format of the file containing output from analyses.",
    )

class ExpressionLogicalOperatorEnum(EnumDefinitionImpl):
    """
    Boolean operators denoting a logical operation (e.g., and, or, not).
    """
    AND = PermissibleValue(text="AND")
    OR = PermissibleValue(text="OR")
    NOT = PermissibleValue(text="NOT")

    _defn = EnumDefinition(
        name="ExpressionLogicalOperatorEnum",
        description="Boolean operators denoting a logical operation (e.g., and, or, not).",
    )

class ConditionComparatorEnum(EnumDefinitionImpl):
    """
    Comparison operators indicating how the value of a variable is compared to a (list of) prespecified value(s).
    """
    EQ = PermissibleValue(
        text="EQ",
        description="Is equal to")
    NE = PermissibleValue(
        text="NE",
        description="Is not equal to")
    GT = PermissibleValue(
        text="GT",
        description="Is greater than")
    GE = PermissibleValue(
        text="GE",
        description="Is greater than or equal to")
    LT = PermissibleValue(
        text="LT",
        description="Is less than")
    LE = PermissibleValue(
        text="LE",
        description="Is less than or equal to")
    IN = PermissibleValue(
        text="IN",
        description="Is in")
    NOTIN = PermissibleValue(
        text="NOTIN",
        description="Is not in")

    _defn = EnumDefinition(
        name="ConditionComparatorEnum",
        description="""Comparison operators indicating how the value of a variable is compared to a (list of) prespecified value(s).""",
    )

class DisplaySectionTypeEnum(EnumDefinitionImpl):
    """
    Types of display section that contain one or more pieces of informational text.
    """
    Title = PermissibleValue(text="Title")
    Footnote = PermissibleValue(text="Footnote")
    Abbreviation = PermissibleValue(text="Abbreviation")
    Legend = PermissibleValue(text="Legend")

    _defn = EnumDefinition(
        name="DisplaySectionTypeEnum",
        description="Types of display section that contain one or more pieces of informational text.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Rowlabel Header",
            PermissibleValue(text="Rowlabel Header"))

class OperationRoleEnum(EnumDefinitionImpl):
    """
    The role that the referenced operation's result plays in the calculation of the result of this operation.
    """
    NUMERATOR = PermissibleValue(
        text="NUMERATOR",
        description="The dividend of a fraction.")
    DENOMINATOR = PermissibleValue(
        text="DENOMINATOR",
        description="The divisor of a fraction.")

    _defn = EnumDefinition(
        name="OperationRoleEnum",
        description="""The role that the referenced operation's result plays in the calculation of the result of this operation.""",
    )

class AnalysisReasonEnum(EnumDefinitionImpl):
    """
    The rationale for performing this analysis. It indicates when the analysis was planned.
    """
    _defn = EnumDefinition(
        name="AnalysisReasonEnum",
        description="The rationale for performing this analysis. It indicates when the analysis was planned.",
        code_set=NCIT.C117744,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SPECIFIED IN PROTOCOL",
            PermissibleValue(
                text="SPECIFIED IN PROTOCOL",
                description="The analysis is specified in a protocol.",
                meaning=NCIT.C117752))
        setattr(cls, "SPECIFIED IN SAP",
            PermissibleValue(
                text="SPECIFIED IN SAP",
                description="The analysis is specified in a statistical analysis plan.",
                meaning=NCIT.C117753))
        setattr(cls, "DATA DRIVEN",
            PermissibleValue(
                text="DATA DRIVEN",
                description="The analysis was triggered by findings in the data.",
                meaning=NCIT.C117750))
        setattr(cls, "REQUESTED BY REGULATORY AGENCY",
            PermissibleValue(
                text="REQUESTED BY REGULATORY AGENCY",
                description="The analysis has been requested by a regulatory agency.",
                meaning=NCIT.C117751))

class AnalysisPurposeEnum(EnumDefinitionImpl):
    """
    The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).
    """
    _defn = EnumDefinition(
        name="AnalysisPurposeEnum",
        description="""The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).""",
        code_set=NCIT.C117745,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PRIMARY OUTCOME MEASURE",
            PermissibleValue(
                text="PRIMARY OUTCOME MEASURE",
                description="""The outcome measure(s) of greatest importance specified in the protocol, usually the one(s) used in the power calculation, to evaluate the primary endpoint(s) associated with the primary study objective(s). (After Clinicaltrials.gov)""",
                meaning=NCIT.C98772))
        setattr(cls, "SECONDARY OUTCOME MEASURE",
            PermissibleValue(
                text="SECONDARY OUTCOME MEASURE",
                description="""The outcome measure(s) that is part of a pre-specified analysis plan used to evaluate the secondary endpoint(s) associated with secondary study objective(s) and/or used to evaluate any measure(s) ancillary to the primary or secondary endpoint(s). (After Clinicaltrials.gov).""",
                meaning=NCIT.C98781))
        setattr(cls, "EXPLORATORY OUTCOME MEASURE",
            PermissibleValue(
                text="EXPLORATORY OUTCOME MEASURE",
                description="""The outcome measure(s) that is part of a pre-specified analysis plan used to evaluate the exploratory endpoint(s) associated with exploratory study objective(s) and/or any other measures, excluding post-hoc measures, that are a focus of the study. (After clinicaltrials.gov)""",
                meaning=NCIT.C98724))

class ExtensibleTerminologyEnum(EnumDefinitionImpl):
    """
    Extensible ARS enumerations.
    """
    AnalysisReasonEnum = PermissibleValue(
        text="AnalysisReasonEnum",
        description="The rationale for performing this analysis. It indicates when the analysis was planned.",
        meaning=NCIT.C117744)
    AnalysisPurposeEnum = PermissibleValue(
        text="AnalysisPurposeEnum",
        description="""The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).""",
        meaning=NCIT.C117745)
    OperationRoleEnum = PermissibleValue(text="OperationRoleEnum")
    OutputFileTypeEnum = PermissibleValue(text="OutputFileTypeEnum")

    _defn = EnumDefinition(
        name="ExtensibleTerminologyEnum",
        description="Extensible ARS enumerations.",
    )

class PageRefTypeEnum(EnumDefinitionImpl):
    """
    Type of reference for page references.
    """
    PhysicalRef = PermissibleValue(
        text="PhysicalRef",
        description="References are to page numbers.")
    NamedDestination = PermissibleValue(
        text="NamedDestination",
        description="References are to named destinations in the referenced document.")

    _defn = EnumDefinition(
        name="PageRefTypeEnum",
        description="Type of reference for page references.",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=ARS.name, name="name", curie=ARS.curie('name'),
                   model_uri=ARS.name, domain=None, range=str)

slots.listOfPlannedAnalyses = Slot(uri=ARS.listOfPlannedAnalyses, name="listOfPlannedAnalyses", curie=ARS.curie('listOfPlannedAnalyses'),
                   model_uri=ARS.listOfPlannedAnalyses, domain=None, range=Union[dict, NestedList])

slots.listOfPlannedOutputs = Slot(uri=ARS.listOfPlannedOutputs, name="listOfPlannedOutputs", curie=ARS.curie('listOfPlannedOutputs'),
                   model_uri=ARS.listOfPlannedOutputs, domain=None, range=Optional[Union[dict, NestedList]])

slots.analysisSets = Slot(uri=ARS.analysisSets, name="analysisSets", curie=ARS.curie('analysisSets'),
                   model_uri=ARS.analysisSets, domain=None, range=Optional[Union[Dict[Union[str, AnalysisSetId], Union[dict, AnalysisSet]], List[Union[dict, AnalysisSet]]]])

slots.analysisGroupings = Slot(uri=ARS.analysisGroupings, name="analysisGroupings", curie=ARS.curie('analysisGroupings'),
                   model_uri=ARS.analysisGroupings, domain=None, range=Optional[Union[Dict[Union[str, SubjectGroupingFactorId], Union[dict, SubjectGroupingFactor]], List[Union[dict, SubjectGroupingFactor]]]])

slots.groupingVariable = Slot(uri=ARS.groupingVariable, name="groupingVariable", curie=ARS.curie('groupingVariable'),
                   model_uri=ARS.groupingVariable, domain=None, range=Optional[str])

slots.dataDriven = Slot(uri=ARS.dataDriven, name="dataDriven", curie=ARS.curie('dataDriven'),
                   model_uri=ARS.dataDriven, domain=None, range=Union[bool, Bool])

slots.groups = Slot(uri=ARS.groups, name="groups", curie=ARS.curie('groups'),
                   model_uri=ARS.groups, domain=None, range=Optional[Union[Dict[Union[str, GroupId], Union[dict, Group]], List[Union[dict, Group]]]])

slots.dataSubsets = Slot(uri=ARS.dataSubsets, name="dataSubsets", curie=ARS.curie('dataSubsets'),
                   model_uri=ARS.dataSubsets, domain=None, range=Optional[Union[Dict[Union[str, DataSubsetId], Union[dict, DataSubset]], List[Union[dict, DataSubset]]]])

slots.dataGroupings = Slot(uri=ARS.dataGroupings, name="dataGroupings", curie=ARS.curie('dataGroupings'),
                   model_uri=ARS.dataGroupings, domain=None, range=Optional[Union[Dict[Union[str, DataGroupingFactorId], Union[dict, DataGroupingFactor]], List[Union[dict, DataGroupingFactor]]]])

slots.analyses = Slot(uri=ARS.analyses, name="analyses", curie=ARS.curie('analyses'),
                   model_uri=ARS.analyses, domain=None, range=Optional[Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]]])

slots.reason = Slot(uri=ARS.reason, name="reason", curie=ARS.curie('reason'),
                   model_uri=ARS.reason, domain=None, range=Union[dict, ExtensibleTerminologyTerm])

slots.purpose = Slot(uri=ARS.purpose, name="purpose", curie=ARS.curie('purpose'),
                   model_uri=ARS.purpose, domain=None, range=Union[dict, ExtensibleTerminologyTerm])

slots.methods = Slot(uri=ARS.methods, name="methods", curie=ARS.curie('methods'),
                   model_uri=ARS.methods, domain=None, range=Optional[Union[Dict[Union[str, AnalysisMethodId], Union[dict, AnalysisMethod]], List[Union[dict, AnalysisMethod]]]])

slots.operations = Slot(uri=ARS.operations, name="operations", curie=ARS.curie('operations'),
                   model_uri=ARS.operations, domain=None, range=Union[Dict[Union[str, OperationId], Union[dict, Operation]], List[Union[dict, Operation]]])

slots.referencedOperationRelationshipId = Slot(uri=ARS.referencedOperationRelationshipId, name="referencedOperationRelationshipId", curie=ARS.curie('referencedOperationRelationshipId'),
                   model_uri=ARS.referencedOperationRelationshipId, domain=None, range=Union[str, ReferencedOperationRelationshipId])

slots.analysisCategorizations = Slot(uri=ARS.analysisCategorizations, name="analysisCategorizations", curie=ARS.curie('analysisCategorizations'),
                   model_uri=ARS.analysisCategorizations, domain=None, range=Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, AnalysisCategorization]], List[Union[dict, AnalysisCategorization]]]])

slots.categories = Slot(uri=ARS.categories, name="categories", curie=ARS.curie('categories'),
                   model_uri=ARS.categories, domain=None, range=Union[Dict[Union[str, AnalysisCategoryId], Union[dict, AnalysisCategory]], List[Union[dict, AnalysisCategory]]])

slots.categoryIds = Slot(uri=ARS.categoryIds, name="categoryIds", curie=ARS.curie('categoryIds'),
                   model_uri=ARS.categoryIds, domain=None, range=Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]])

slots.subCategorizations = Slot(uri=ARS.subCategorizations, name="subCategorizations", curie=ARS.curie('subCategorizations'),
                   model_uri=ARS.subCategorizations, domain=None, range=Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, AnalysisCategorization]], List[Union[dict, AnalysisCategorization]]]])

slots.outputs = Slot(uri=ARS.outputs, name="outputs", curie=ARS.curie('outputs'),
                   model_uri=ARS.outputs, domain=None, range=Optional[Union[Dict[Union[str, OutputId], Union[dict, Output]], List[Union[dict, Output]]]])

slots.listItems = Slot(uri=ARS.listItems, name="listItems", curie=ARS.curie('listItems'),
                   model_uri=ARS.listItems, domain=None, range=Optional[Union[Union[dict, OrderedListItem], List[Union[dict, OrderedListItem]]]])

slots.level = Slot(uri=ARS.level, name="level", curie=ARS.curie('level'),
                   model_uri=ARS.level, domain=None, range=Optional[int])

slots.order = Slot(uri=ARS.order, name="order", curie=ARS.curie('order'),
                   model_uri=ARS.order, domain=None, range=Optional[int])

slots.sublist = Slot(uri=ARS.sublist, name="sublist", curie=ARS.curie('sublist'),
                   model_uri=ARS.sublist, domain=None, range=Optional[Union[dict, NestedList]])

slots.analysisId = Slot(uri=ARS.analysisId, name="analysisId", curie=ARS.curie('analysisId'),
                   model_uri=ARS.analysisId, domain=None, range=Optional[Union[str, AnalysisId]])

slots.analysisSetId = Slot(uri=ARS.analysisSetId, name="analysisSetId", curie=ARS.curie('analysisSetId'),
                   model_uri=ARS.analysisSetId, domain=None, range=Optional[Union[str, AnalysisSetId]])

slots.orderedGroupings = Slot(uri=ARS.orderedGroupings, name="orderedGroupings", curie=ARS.curie('orderedGroupings'),
                   model_uri=ARS.orderedGroupings, domain=None, range=Optional[Union[Union[dict, OrderedGroupingFactor], List[Union[dict, OrderedGroupingFactor]]]])

slots.groupingId = Slot(uri=ARS.groupingId, name="groupingId", curie=ARS.curie('groupingId'),
                   model_uri=ARS.groupingId, domain=None, range=Optional[Union[str, GroupingFactorId]])

slots.resultsByGroup = Slot(uri=ARS.resultsByGroup, name="resultsByGroup", curie=ARS.curie('resultsByGroup'),
                   model_uri=ARS.resultsByGroup, domain=None, range=Union[bool, Bool])

slots.dataSubsetId = Slot(uri=ARS.dataSubsetId, name="dataSubsetId", curie=ARS.curie('dataSubsetId'),
                   model_uri=ARS.dataSubsetId, domain=None, range=Optional[Union[str, DataSubsetId]])

slots.methodId = Slot(uri=ARS.methodId, name="methodId", curie=ARS.curie('methodId'),
                   model_uri=ARS.methodId, domain=None, range=Union[str, AnalysisMethodId])

slots.description = Slot(uri=ARS.description, name="description", curie=ARS.curie('description'),
                   model_uri=ARS.description, domain=None, range=Optional[str])

slots.referencedAnalysisOperations = Slot(uri=ARS.referencedAnalysisOperations, name="referencedAnalysisOperations", curie=ARS.curie('referencedAnalysisOperations'),
                   model_uri=ARS.referencedAnalysisOperations, domain=None, range=Optional[Union[Union[dict, ReferencedAnalysisOperation], List[Union[dict, ReferencedAnalysisOperation]]]])

slots.resultPattern = Slot(uri=ARS.resultPattern, name="resultPattern", curie=ARS.curie('resultPattern'),
                   model_uri=ARS.resultPattern, domain=None, range=Optional[str])

slots.results = Slot(uri=ARS.results, name="results", curie=ARS.curie('results'),
                   model_uri=ARS.results, domain=None, range=Optional[Union[Union[dict, OperationResult], List[Union[dict, OperationResult]]]])

slots.resultGroups = Slot(uri=ARS.resultGroups, name="resultGroups", curie=ARS.curie('resultGroups'),
                   model_uri=ARS.resultGroups, domain=None, range=Optional[Union[Union[dict, ResultGroup], List[Union[dict, ResultGroup]]]])

slots.groupId = Slot(uri=ARS.groupId, name="groupId", curie=ARS.curie('groupId'),
                   model_uri=ARS.groupId, domain=None, range=Optional[Union[str, GroupId]])

slots.groupValue = Slot(uri=ARS.groupValue, name="groupValue", curie=ARS.curie('groupValue'),
                   model_uri=ARS.groupValue, domain=None, range=Optional[str])

slots.rawValue = Slot(uri=ARS.rawValue, name="rawValue", curie=ARS.curie('rawValue'),
                   model_uri=ARS.rawValue, domain=None, range=Optional[str])

slots.formattedValue = Slot(uri=ARS.formattedValue, name="formattedValue", curie=ARS.curie('formattedValue'),
                   model_uri=ARS.formattedValue, domain=None, range=Optional[str])

slots.referencedOperationRelationships = Slot(uri=ARS.referencedOperationRelationships, name="referencedOperationRelationships", curie=ARS.curie('referencedOperationRelationships'),
                   model_uri=ARS.referencedOperationRelationships, domain=None, range=Optional[Union[Dict[Union[str, ReferencedOperationRelationshipId], Union[dict, ReferencedOperationRelationship]], List[Union[dict, ReferencedOperationRelationship]]]])

slots.referencedOperationRole = Slot(uri=ARS.referencedOperationRole, name="referencedOperationRole", curie=ARS.curie('referencedOperationRole'),
                   model_uri=ARS.referencedOperationRole, domain=None, range=Union[dict, ExtensibleTerminologyTerm])

slots.operationId = Slot(uri=ARS.operationId, name="operationId", curie=ARS.curie('operationId'),
                   model_uri=ARS.operationId, domain=None, range=Union[str, OperationId])

slots.programmingCode = Slot(uri=ARS.programmingCode, name="programmingCode", curie=ARS.curie('programmingCode'),
                   model_uri=ARS.programmingCode, domain=None, range=Optional[Union[dict, AnalysisOutputProgrammingCode]])

slots.codeTemplate = Slot(uri=ARS.codeTemplate, name="codeTemplate", curie=ARS.curie('codeTemplate'),
                   model_uri=ARS.codeTemplate, domain=None, range=Optional[Union[dict, AnalysisProgrammingCodeTemplate]])

slots.context = Slot(uri=ARS.context, name="context", curie=ARS.curie('context'),
                   model_uri=ARS.context, domain=None, range=str)

slots.parameters = Slot(uri=ARS.parameters, name="parameters", curie=ARS.curie('parameters'),
                   model_uri=ARS.parameters, domain=None, range=Optional[Union[Union[dict, CodeParameter], List[Union[dict, CodeParameter]]]])

slots.code = Slot(uri=ARS.code, name="code", curie=ARS.curie('code'),
                   model_uri=ARS.code, domain=None, range=Optional[str])

slots.valueSource = Slot(uri=ARS.valueSource, name="valueSource", curie=ARS.curie('valueSource'),
                   model_uri=ARS.valueSource, domain=None, range=Optional[str])

slots.outputId = Slot(uri=ARS.outputId, name="outputId", curie=ARS.curie('outputId'),
                   model_uri=ARS.outputId, domain=None, range=Optional[Union[str, OutputId]])

slots.id = Slot(uri=ARS.id, name="id", curie=ARS.curie('id'),
                   model_uri=ARS.id, domain=None, range=URIRef)

slots.version = Slot(uri=ARS.version, name="version", curie=ARS.curie('version'),
                   model_uri=ARS.version, domain=None, range=Optional[int])

slots.displayTitle = Slot(uri=ARS.displayTitle, name="displayTitle", curie=ARS.curie('displayTitle'),
                   model_uri=ARS.displayTitle, domain=None, range=Optional[str])

slots.fileSpecifications = Slot(uri=ARS.fileSpecifications, name="fileSpecifications", curie=ARS.curie('fileSpecifications'),
                   model_uri=ARS.fileSpecifications, domain=None, range=Optional[Union[Union[dict, OutputFile], List[Union[dict, OutputFile]]]])

slots.fileType = Slot(uri=ARS.fileType, name="fileType", curie=ARS.curie('fileType'),
                   model_uri=ARS.fileType, domain=None, range=Optional[Union[dict, ExtensibleTerminologyTerm]])

slots.location = Slot(uri=ARS.location, name="location", curie=ARS.curie('location'),
                   model_uri=ARS.location, domain=None, range=Optional[Union[str, URI]])

slots.style = Slot(uri=ARS.style, name="style", curie=ARS.curie('style'),
                   model_uri=ARS.style, domain=None, range=Optional[str])

slots.displays = Slot(uri=ARS.displays, name="displays", curie=ARS.curie('displays'),
                   model_uri=ARS.displays, domain=None, range=Optional[Union[Union[dict, OrderedDisplay], List[Union[dict, OrderedDisplay]]]])

slots.display = Slot(uri=ARS.display, name="display", curie=ARS.curie('display'),
                   model_uri=ARS.display, domain=None, range=Optional[Union[dict, OutputDisplay]])

slots.globalDisplaySections = Slot(uri=ARS.globalDisplaySections, name="globalDisplaySections", curie=ARS.curie('globalDisplaySections'),
                   model_uri=ARS.globalDisplaySections, domain=None, range=Optional[Union[Union[dict, GlobalDisplaySection], List[Union[dict, GlobalDisplaySection]]]])

slots.displaySections = Slot(uri=ARS.displaySections, name="displaySections", curie=ARS.curie('displaySections'),
                   model_uri=ARS.displaySections, domain=None, range=Optional[Union[Union[dict, DisplaySection], List[Union[dict, DisplaySection]]]])

slots.sectionType = Slot(uri=ARS.sectionType, name="sectionType", curie=ARS.curie('sectionType'),
                   model_uri=ARS.sectionType, domain=None, range=Optional[Union[str, "DisplaySectionTypeEnum"]])

slots.orderedSubSections = Slot(uri=ARS.orderedSubSections, name="orderedSubSections", curie=ARS.curie('orderedSubSections'),
                   model_uri=ARS.orderedSubSections, domain=None, range=Optional[Union[Union[dict, OrderedDisplaySubSection], List[Union[dict, OrderedDisplaySubSection]]]])

slots.subSection = Slot(uri=ARS.subSection, name="subSection", curie=ARS.curie('subSection'),
                   model_uri=ARS.subSection, domain=None, range=Optional[Union[dict, DisplaySubSection]])

slots.subSectionId = Slot(uri=ARS.subSectionId, name="subSectionId", curie=ARS.curie('subSectionId'),
                   model_uri=ARS.subSectionId, domain=None, range=Optional[Union[str, DisplaySubSectionId]])

slots.subSections = Slot(uri=ARS.subSections, name="subSections", curie=ARS.curie('subSections'),
                   model_uri=ARS.subSections, domain=None, range=Optional[Union[Dict[Union[str, DisplaySubSectionId], Union[dict, DisplaySubSection]], List[Union[dict, DisplaySubSection]]]])

slots.text = Slot(uri=ARS.text, name="text", curie=ARS.curie('text'),
                   model_uri=ARS.text, domain=None, range=Optional[str])

slots.logicalOperator = Slot(uri=ARS.logicalOperator, name="logicalOperator", curie=ARS.curie('logicalOperator'),
                   model_uri=ARS.logicalOperator, domain=None, range=Union[str, "ExpressionLogicalOperatorEnum"])

slots.condition = Slot(uri=ARS.condition, name="condition", curie=ARS.curie('condition'),
                   model_uri=ARS.condition, domain=None, range=Optional[Union[dict, WhereClauseCondition]])

slots.compoundExpression = Slot(uri=ARS.compoundExpression, name="compoundExpression", curie=ARS.curie('compoundExpression'),
                   model_uri=ARS.compoundExpression, domain=None, range=Optional[Union[dict, WhereClauseCompoundExpression]])

slots.whereClauses = Slot(uri=ARS.whereClauses, name="whereClauses", curie=ARS.curie('whereClauses'),
                   model_uri=ARS.whereClauses, domain=None, range=Optional[Union[Union[dict, WhereClause], List[Union[dict, WhereClause]]]])

slots.dataset = Slot(uri=ARS.dataset, name="dataset", curie=ARS.curie('dataset'),
                   model_uri=ARS.dataset, domain=None, range=Optional[str])

slots.variable = Slot(uri=ARS.variable, name="variable", curie=ARS.curie('variable'),
                   model_uri=ARS.variable, domain=None, range=Optional[str])

slots.comparator = Slot(uri=ARS.comparator, name="comparator", curie=ARS.curie('comparator'),
                   model_uri=ARS.comparator, domain=None, range=Optional[Union[str, "ConditionComparatorEnum"]])

slots.value = Slot(uri=ARS.value, name="value", curie=ARS.curie('value'),
                   model_uri=ARS.value, domain=None, range=Optional[Union[str, List[str]]])

slots.label = Slot(uri=ARS.label, name="label", curie=ARS.curie('label'),
                   model_uri=ARS.label, domain=None, range=Optional[str])

slots.referenceDocuments = Slot(uri=ARS.referenceDocuments, name="referenceDocuments", curie=ARS.curie('referenceDocuments'),
                   model_uri=ARS.referenceDocuments, domain=None, range=Optional[Union[Dict[Union[str, ReferenceDocumentId], Union[dict, ReferenceDocument]], List[Union[dict, ReferenceDocument]]]])

slots.documentRefs = Slot(uri=ARS.documentRefs, name="documentRefs", curie=ARS.curie('documentRefs'),
                   model_uri=ARS.documentRefs, domain=None, range=Optional[Union[Union[dict, DocumentReference], List[Union[dict, DocumentReference]]]])

slots.documentRef = Slot(uri=ARS.documentRef, name="documentRef", curie=ARS.curie('documentRef'),
                   model_uri=ARS.documentRef, domain=None, range=Optional[Union[dict, DocumentReference]])

slots.referenceDocumentId = Slot(uri=ARS.referenceDocumentId, name="referenceDocumentId", curie=ARS.curie('referenceDocumentId'),
                   model_uri=ARS.referenceDocumentId, domain=None, range=Union[str, ReferenceDocumentId])

slots.pageRefs = Slot(uri=ARS.pageRefs, name="pageRefs", curie=ARS.curie('pageRefs'),
                   model_uri=ARS.pageRefs, domain=None, range=Optional[Union[Union[dict, PageRef], List[Union[dict, PageRef]]]])

slots.refType = Slot(uri=ARS.refType, name="refType", curie=ARS.curie('refType'),
                   model_uri=ARS.refType, domain=None, range=Union[str, "PageRefTypeEnum"])

slots.pageNumbers = Slot(uri=ARS.pageNumbers, name="pageNumbers", curie=ARS.curie('pageNumbers'),
                   model_uri=ARS.pageNumbers, domain=None, range=Optional[Union[int, List[int]]])

slots.pageNames = Slot(uri=ARS.pageNames, name="pageNames", curie=ARS.curie('pageNames'),
                   model_uri=ARS.pageNames, domain=None, range=Optional[Union[str, List[str]]])

slots.firstPage = Slot(uri=ARS.firstPage, name="firstPage", curie=ARS.curie('firstPage'),
                   model_uri=ARS.firstPage, domain=None, range=Optional[int])

slots.lastPage = Slot(uri=ARS.lastPage, name="lastPage", curie=ARS.curie('lastPage'),
                   model_uri=ARS.lastPage, domain=None, range=Optional[int])

slots.terminologyExtensions = Slot(uri=ARS.terminologyExtensions, name="terminologyExtensions", curie=ARS.curie('terminologyExtensions'),
                   model_uri=ARS.terminologyExtensions, domain=None, range=Optional[Union[Dict[Union[str, TerminologyExtensionId], Union[dict, TerminologyExtension]], List[Union[dict, TerminologyExtension]]]])

slots.enumeration = Slot(uri=ARS.enumeration, name="enumeration", curie=ARS.curie('enumeration'),
                   model_uri=ARS.enumeration, domain=None, range=Optional[Union[str, "ExtensibleTerminologyEnum"]])

slots.sponsorTerms = Slot(uri=ARS.sponsorTerms, name="sponsorTerms", curie=ARS.curie('sponsorTerms'),
                   model_uri=ARS.sponsorTerms, domain=None, range=Union[Dict[Union[str, SponsorTermId], Union[dict, SponsorTerm]], List[Union[dict, SponsorTerm]]])

slots.submissionValue = Slot(uri=ARS.submissionValue, name="submissionValue", curie=ARS.curie('submissionValue'),
                   model_uri=ARS.submissionValue, domain=None, range=str)

slots.controlledTerm = Slot(uri=ARS.controlledTerm, name="controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.controlledTerm, domain=None, range=Optional[str])

slots.sponsorTermId = Slot(uri=ARS.sponsorTermId, name="sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.sponsorTermId, domain=None, range=Optional[Union[str, SponsorTermId]])

slots.OrderedListItem_level = Slot(uri=ARS.level, name="OrderedListItem_level", curie=ARS.curie('level'),
                   model_uri=ARS.OrderedListItem_level, domain=OrderedListItem, range=int)

slots.OrderedListItem_order = Slot(uri=ARS.order, name="OrderedListItem_order", curie=ARS.curie('order'),
                   model_uri=ARS.OrderedListItem_order, domain=OrderedListItem, range=int)

slots.Analysis_categoryIds = Slot(uri=ARS.categoryIds, name="Analysis_categoryIds", curie=ARS.curie('categoryIds'),
                   model_uri=ARS.Analysis_categoryIds, domain=Analysis, range=Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]])

slots.Analysis_programmingCode = Slot(uri=ARS.programmingCode, name="Analysis_programmingCode", curie=ARS.curie('programmingCode'),
                   model_uri=ARS.Analysis_programmingCode, domain=Analysis, range=Optional[Union[dict, "AnalysisOutputProgrammingCode"]])

slots.OrderedGroupingFactor_order = Slot(uri=ARS.order, name="OrderedGroupingFactor_order", curie=ARS.curie('order'),
                   model_uri=ARS.OrderedGroupingFactor_order, domain=OrderedGroupingFactor, range=int)

slots.ReferencedAnalysisOperation_analysisId = Slot(uri=ARS.analysisId, name="ReferencedAnalysisOperation_analysisId", curie=ARS.curie('analysisId'),
                   model_uri=ARS.ReferencedAnalysisOperation_analysisId, domain=ReferencedAnalysisOperation, range=Union[str, AnalysisId])

slots.AnalysisOutputProgrammingCode_parameters = Slot(uri=ARS.parameters, name="AnalysisOutputProgrammingCode_parameters", curie=ARS.curie('parameters'),
                   model_uri=ARS.AnalysisOutputProgrammingCode_parameters, domain=AnalysisOutputProgrammingCode, range=Optional[Union[Union[dict, "AnalysisOutputCodeParameter"], List[Union[dict, "AnalysisOutputCodeParameter"]]]])

slots.AnalysisProgrammingCodeTemplate_parameters = Slot(uri=ARS.parameters, name="AnalysisProgrammingCodeTemplate_parameters", curie=ARS.curie('parameters'),
                   model_uri=ARS.AnalysisProgrammingCodeTemplate_parameters, domain=AnalysisProgrammingCodeTemplate, range=Optional[Union[Union[dict, "TemplateCodeParameter"], List[Union[dict, "TemplateCodeParameter"]]]])

slots.AnalysisOutputCodeParameter_value = Slot(uri=ARS.value, name="AnalysisOutputCodeParameter_value", curie=ARS.curie('value'),
                   model_uri=ARS.AnalysisOutputCodeParameter_value, domain=AnalysisOutputCodeParameter, range=Union[str, List[str]])

slots.TemplateCodeParameter_value = Slot(uri=ARS.value, name="TemplateCodeParameter_value", curie=ARS.curie('value'),
                   model_uri=ARS.TemplateCodeParameter_value, domain=TemplateCodeParameter, range=Optional[Union[str, List[str]]])

slots.Output_categoryIds = Slot(uri=ARS.categoryIds, name="Output_categoryIds", curie=ARS.curie('categoryIds'),
                   model_uri=ARS.Output_categoryIds, domain=Output, range=Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]])

slots.Output_programmingCode = Slot(uri=ARS.programmingCode, name="Output_programmingCode", curie=ARS.curie('programmingCode'),
                   model_uri=ARS.Output_programmingCode, domain=Output, range=Optional[Union[dict, AnalysisOutputProgrammingCode]])

slots.OrderedDisplay_order = Slot(uri=ARS.order, name="OrderedDisplay_order", curie=ARS.curie('order'),
                   model_uri=ARS.OrderedDisplay_order, domain=OrderedDisplay, range=int)

slots.OrderedDisplaySubSection_order = Slot(uri=ARS.order, name="OrderedDisplaySubSection_order", curie=ARS.curie('order'),
                   model_uri=ARS.OrderedDisplaySubSection_order, domain=OrderedDisplaySubSection, range=int)

slots.OrderedSubSection_subSection = Slot(uri=ARS.subSection, name="OrderedSubSection_subSection", curie=ARS.curie('subSection'),
                   model_uri=ARS.OrderedSubSection_subSection, domain=OrderedSubSection, range=Union[dict, "DisplaySubSection"])

slots.OrderedSubSection_subSectionId = Slot(uri=ARS.subSectionId, name="OrderedSubSection_subSectionId", curie=ARS.curie('subSectionId'),
                   model_uri=ARS.OrderedSubSection_subSectionId, domain=OrderedSubSection, range=Optional[Union[str, DisplaySubSectionId]])

slots.OrderedSubSectionRef_subSection = Slot(uri=ARS.subSection, name="OrderedSubSectionRef_subSection", curie=ARS.curie('subSection'),
                   model_uri=ARS.OrderedSubSectionRef_subSection, domain=OrderedSubSectionRef, range=Optional[Union[dict, "DisplaySubSection"]])

slots.OrderedSubSectionRef_subSectionId = Slot(uri=ARS.subSectionId, name="OrderedSubSectionRef_subSectionId", curie=ARS.curie('subSectionId'),
                   model_uri=ARS.OrderedSubSectionRef_subSectionId, domain=OrderedSubSectionRef, range=Union[str, DisplaySubSectionId])

slots.DisplaySubSection_text = Slot(uri=ARS.text, name="DisplaySubSection_text", curie=ARS.curie('text'),
                   model_uri=ARS.DisplaySubSection_text, domain=DisplaySubSection, range=str)

slots.WhereClauseCondition_value = Slot(uri=ARS.value, name="WhereClauseCondition_value", curie=ARS.curie('value'),
                   model_uri=ARS.WhereClauseCondition_value, domain=WhereClauseCondition, range=Optional[Union[str, List[str]]])

slots.CompoundSetExpression_whereClauses = Slot(uri=ARS.whereClauses, name="CompoundSetExpression_whereClauses", curie=ARS.curie('whereClauses'),
                   model_uri=ARS.CompoundSetExpression_whereClauses, domain=CompoundSetExpression, range=Optional[Union[Union[str, AnalysisSetId], List[Union[str, AnalysisSetId]]]])

slots.CompoundGroupExpression_whereClauses = Slot(uri=ARS.whereClauses, name="CompoundGroupExpression_whereClauses", curie=ARS.curie('whereClauses'),
                   model_uri=ARS.CompoundGroupExpression_whereClauses, domain=CompoundGroupExpression, range=Optional[Union[Union[str, GroupId], List[Union[str, GroupId]]]])

slots.CompoundSubsetExpression_whereClauses = Slot(uri=ARS.whereClauses, name="CompoundSubsetExpression_whereClauses", curie=ARS.curie('whereClauses'),
                   model_uri=ARS.CompoundSubsetExpression_whereClauses, domain=CompoundSubsetExpression, range=Optional[Union[Union[dict, WhereClause], List[Union[dict, WhereClause]]]])

slots.AnalysisSet_compoundExpression = Slot(uri=ARS.compoundExpression, name="AnalysisSet_compoundExpression", curie=ARS.curie('compoundExpression'),
                   model_uri=ARS.AnalysisSet_compoundExpression, domain=AnalysisSet, range=Optional[Union[dict, CompoundSetExpression]])

slots.SubjectGroupingFactor_groups = Slot(uri=ARS.groups, name="SubjectGroupingFactor_groups", curie=ARS.curie('groups'),
                   model_uri=ARS.SubjectGroupingFactor_groups, domain=SubjectGroupingFactor, range=Optional[Union[Dict[Union[str, AnalysisGroupId], Union[dict, "AnalysisGroup"]], List[Union[dict, "AnalysisGroup"]]]])

slots.DataGroupingFactor_groups = Slot(uri=ARS.groups, name="DataGroupingFactor_groups", curie=ARS.curie('groups'),
                   model_uri=ARS.DataGroupingFactor_groups, domain=DataGroupingFactor, range=Optional[Union[Dict[Union[str, DataGroupId], Union[dict, "DataGroup"]], List[Union[dict, "DataGroup"]]]])

slots.Group_compoundExpression = Slot(uri=ARS.compoundExpression, name="Group_compoundExpression", curie=ARS.curie('compoundExpression'),
                   model_uri=ARS.Group_compoundExpression, domain=Group, range=Optional[Union[dict, CompoundGroupExpression]])

slots.DataSubset_compoundExpression = Slot(uri=ARS.compoundExpression, name="DataSubset_compoundExpression", curie=ARS.curie('compoundExpression'),
                   model_uri=ARS.DataSubset_compoundExpression, domain=DataSubset, range=Optional[Union[dict, CompoundSubsetExpression]])

slots.PageRef_label = Slot(uri=ARS.label, name="PageRef_label", curie=ARS.curie('label'),
                   model_uri=ARS.PageRef_label, domain=PageRef, range=Optional[str])

slots.PageNumberListRef_refType = Slot(uri=ARS.refType, name="PageNumberListRef_refType", curie=ARS.curie('refType'),
                   model_uri=ARS.PageNumberListRef_refType, domain=PageNumberListRef, range=Union[str, "PageRefTypeEnum"])

slots.PageNumberListRef_pageNumbers = Slot(uri=ARS.pageNumbers, name="PageNumberListRef_pageNumbers", curie=ARS.curie('pageNumbers'),
                   model_uri=ARS.PageNumberListRef_pageNumbers, domain=PageNumberListRef, range=Union[int, List[int]])

slots.PageNumberListRef_pageNames = Slot(uri=ARS.pageNames, name="PageNumberListRef_pageNames", curie=ARS.curie('pageNames'),
                   model_uri=ARS.PageNumberListRef_pageNames, domain=PageNumberListRef, range=Optional[Union[str, List[str]]])

slots.PageNumberListRef_firstPage = Slot(uri=ARS.firstPage, name="PageNumberListRef_firstPage", curie=ARS.curie('firstPage'),
                   model_uri=ARS.PageNumberListRef_firstPage, domain=PageNumberListRef, range=Optional[int])

slots.PageNumberListRef_lastPage = Slot(uri=ARS.lastPage, name="PageNumberListRef_lastPage", curie=ARS.curie('lastPage'),
                   model_uri=ARS.PageNumberListRef_lastPage, domain=PageNumberListRef, range=Optional[int])

slots.PageNumberRangeRef_refType = Slot(uri=ARS.refType, name="PageNumberRangeRef_refType", curie=ARS.curie('refType'),
                   model_uri=ARS.PageNumberRangeRef_refType, domain=PageNumberRangeRef, range=Union[str, "PageRefTypeEnum"])

slots.PageNumberRangeRef_pageNumbers = Slot(uri=ARS.pageNumbers, name="PageNumberRangeRef_pageNumbers", curie=ARS.curie('pageNumbers'),
                   model_uri=ARS.PageNumberRangeRef_pageNumbers, domain=PageNumberRangeRef, range=Optional[Union[int, List[int]]])

slots.PageNumberRangeRef_pageNames = Slot(uri=ARS.pageNames, name="PageNumberRangeRef_pageNames", curie=ARS.curie('pageNames'),
                   model_uri=ARS.PageNumberRangeRef_pageNames, domain=PageNumberRangeRef, range=Optional[Union[str, List[str]]])

slots.PageNumberRangeRef_firstPage = Slot(uri=ARS.firstPage, name="PageNumberRangeRef_firstPage", curie=ARS.curie('firstPage'),
                   model_uri=ARS.PageNumberRangeRef_firstPage, domain=PageNumberRangeRef, range=int)

slots.PageNumberRangeRef_lastPage = Slot(uri=ARS.lastPage, name="PageNumberRangeRef_lastPage", curie=ARS.curie('lastPage'),
                   model_uri=ARS.PageNumberRangeRef_lastPage, domain=PageNumberRangeRef, range=int)

slots.PageNameRef_refType = Slot(uri=ARS.refType, name="PageNameRef_refType", curie=ARS.curie('refType'),
                   model_uri=ARS.PageNameRef_refType, domain=PageNameRef, range=Union[str, "PageRefTypeEnum"])

slots.PageNameRef_pageNumbers = Slot(uri=ARS.pageNumbers, name="PageNameRef_pageNumbers", curie=ARS.curie('pageNumbers'),
                   model_uri=ARS.PageNameRef_pageNumbers, domain=PageNameRef, range=Optional[Union[int, List[int]]])

slots.PageNameRef_pageNames = Slot(uri=ARS.pageNames, name="PageNameRef_pageNames", curie=ARS.curie('pageNames'),
                   model_uri=ARS.PageNameRef_pageNames, domain=PageNameRef, range=Union[str, List[str]])

slots.PageNameRef_firstPage = Slot(uri=ARS.firstPage, name="PageNameRef_firstPage", curie=ARS.curie('firstPage'),
                   model_uri=ARS.PageNameRef_firstPage, domain=PageNameRef, range=Optional[int])

slots.PageNameRef_lastPage = Slot(uri=ARS.lastPage, name="PageNameRef_lastPage", curie=ARS.curie('lastPage'),
                   model_uri=ARS.PageNameRef_lastPage, domain=PageNameRef, range=Optional[int])

slots.AnalysisReason_controlledTerm = Slot(uri=ARS.controlledTerm, name="AnalysisReason_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.AnalysisReason_controlledTerm, domain=AnalysisReason, range=Union[str, "AnalysisReasonEnum"])

slots.AnalysisReason_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="AnalysisReason_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.AnalysisReason_sponsorTermId, domain=AnalysisReason, range=Optional[Union[str, SponsorTermId]])

slots.SponsorAnalysisReason_controlledTerm = Slot(uri=ARS.controlledTerm, name="SponsorAnalysisReason_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.SponsorAnalysisReason_controlledTerm, domain=SponsorAnalysisReason, range=Optional[str])

slots.SponsorAnalysisReason_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="SponsorAnalysisReason_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.SponsorAnalysisReason_sponsorTermId, domain=SponsorAnalysisReason, range=Union[str, SponsorTermId])

slots.AnalysisPurpose_controlledTerm = Slot(uri=ARS.controlledTerm, name="AnalysisPurpose_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.AnalysisPurpose_controlledTerm, domain=AnalysisPurpose, range=Union[str, "AnalysisPurposeEnum"])

slots.AnalysisPurpose_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="AnalysisPurpose_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.AnalysisPurpose_sponsorTermId, domain=AnalysisPurpose, range=Optional[Union[str, SponsorTermId]])

slots.SponsorAnalysisPurpose_controlledTerm = Slot(uri=ARS.controlledTerm, name="SponsorAnalysisPurpose_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.SponsorAnalysisPurpose_controlledTerm, domain=SponsorAnalysisPurpose, range=Optional[str])

slots.SponsorAnalysisPurpose_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="SponsorAnalysisPurpose_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.SponsorAnalysisPurpose_sponsorTermId, domain=SponsorAnalysisPurpose, range=Union[str, SponsorTermId])

slots.OperationRole_controlledTerm = Slot(uri=ARS.controlledTerm, name="OperationRole_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.OperationRole_controlledTerm, domain=OperationRole, range=Union[str, "OperationRoleEnum"])

slots.OperationRole_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="OperationRole_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.OperationRole_sponsorTermId, domain=OperationRole, range=Optional[Union[str, SponsorTermId]])

slots.SponsorOperationRole_controlledTerm = Slot(uri=ARS.controlledTerm, name="SponsorOperationRole_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.SponsorOperationRole_controlledTerm, domain=SponsorOperationRole, range=Optional[str])

slots.SponsorOperationRole_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="SponsorOperationRole_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.SponsorOperationRole_sponsorTermId, domain=SponsorOperationRole, range=Union[str, SponsorTermId])

slots.OutputFileType_controlledTerm = Slot(uri=ARS.controlledTerm, name="OutputFileType_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.OutputFileType_controlledTerm, domain=OutputFileType, range=Union[str, "OutputFileTypeEnum"])

slots.OutputFileType_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="OutputFileType_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.OutputFileType_sponsorTermId, domain=OutputFileType, range=Optional[Union[str, SponsorTermId]])

slots.SponsorOutputFileType_controlledTerm = Slot(uri=ARS.controlledTerm, name="SponsorOutputFileType_controlledTerm", curie=ARS.curie('controlledTerm'),
                   model_uri=ARS.SponsorOutputFileType_controlledTerm, domain=SponsorOutputFileType, range=Optional[str])

slots.SponsorOutputFileType_sponsorTermId = Slot(uri=ARS.sponsorTermId, name="SponsorOutputFileType_sponsorTermId", curie=ARS.curie('sponsorTermId'),
                   model_uri=ARS.SponsorOutputFileType_sponsorTermId, domain=SponsorOutputFileType, range=Union[str, SponsorTermId])