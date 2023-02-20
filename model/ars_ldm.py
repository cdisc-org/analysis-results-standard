# Auto generated from ars_ldm.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-20T17:32:15
# Schema: ARS-Schema
#
# id: https://www.cdisc.org/ars/1-0
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
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
from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://www.cdisc.org/ars/1-0/')


# Types

# Class references
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


class OutputId(extended_str):
    pass


class DisplayId(extended_str):
    pass


class DisplaySubSectionId(extended_str):
    pass


class WhereClauseId(extended_str):
    pass


class AnalysisSetId(WhereClauseId):
    pass


class GroupingFactorId(extended_str):
    pass


class SubjectGroupingFactorId(GroupingFactorId):
    pass


class DataGroupingFactorId(GroupingFactorId):
    pass


class GroupId(WhereClauseId):
    pass


class AnalysisGroupId(GroupId):
    pass


class DataGroupId(GroupId):
    pass


class DataSubsetId(WhereClauseId):
    pass


@dataclass
class NamedObject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/NamedObject")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NamedObject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/NamedObject")

    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class ReportingEvent(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/ReportingEvent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReportingEvent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/ReportingEvent")

    name: str = None
    listOfPlannedAnalyses: Union[dict, "NestedList"] = None
    listOfPlannedOutputs: Optional[Union[dict, "NestedList"]] = None
    analysisSets: Optional[Union[Dict[Union[str, AnalysisSetId], Union[dict, "AnalysisSet"]], List[Union[dict, "AnalysisSet"]]]] = empty_dict()
    analysisGroupings: Optional[Union[Dict[Union[str, SubjectGroupingFactorId], Union[dict, "SubjectGroupingFactor"]], List[Union[dict, "SubjectGroupingFactor"]]]] = empty_dict()
    dataSubsets: Optional[Union[Dict[Union[str, DataSubsetId], Union[dict, "DataSubset"]], List[Union[dict, "DataSubset"]]]] = empty_dict()
    globalDisplaySections: Optional[Union[Union[dict, "DisplaySection"], List[Union[dict, "DisplaySection"]]]] = empty_list()
    analysisCategorizations: Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, "AnalysisCategorization"]], List[Union[dict, "AnalysisCategorization"]]]] = empty_dict()
    analyses: Optional[Union[Dict[Union[str, AnalysisId], Union[dict, "Analysis"]], List[Union[dict, "Analysis"]]]] = empty_dict()
    outputs: Optional[Union[Dict[Union[str, OutputId], Union[dict, "Output"]], List[Union[dict, "Output"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.listOfPlannedAnalyses):
            self.MissingRequiredField("listOfPlannedAnalyses")
        if not isinstance(self.listOfPlannedAnalyses, NestedList):
            self.listOfPlannedAnalyses = NestedList(**as_dict(self.listOfPlannedAnalyses))

        if self.listOfPlannedOutputs is not None and not isinstance(self.listOfPlannedOutputs, NestedList):
            self.listOfPlannedOutputs = NestedList(**as_dict(self.listOfPlannedOutputs))

        self._normalize_inlined_as_list(slot_name="analysisSets", slot_type=AnalysisSet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="analysisGroupings", slot_type=SubjectGroupingFactor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dataSubsets", slot_type=DataSubset, key_name="id", keyed=True)

        if not isinstance(self.globalDisplaySections, list):
            self.globalDisplaySections = [self.globalDisplaySections] if self.globalDisplaySections is not None else []
        self.globalDisplaySections = [v if isinstance(v, DisplaySection) else DisplaySection(**as_dict(v)) for v in self.globalDisplaySections]

        self._normalize_inlined_as_list(slot_name="analysisCategorizations", slot_type=AnalysisCategorization, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="analyses", slot_type=Analysis, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="outputs", slot_type=Output, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class NestedList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/NestedList")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NestedList"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/NestedList")

    listItems: Optional[Union[Union[dict, "OrderedListItem"], List[Union[dict, "OrderedListItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.listItems, list):
            self.listItems = [self.listItems] if self.listItems is not None else []
        self.listItems = [v if isinstance(v, OrderedListItem) else OrderedListItem(**as_dict(v)) for v in self.listItems]

        super().__post_init__(**kwargs)


@dataclass
class OrderedListItem(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OrderedListItem")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OrderedListItem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OrderedListItem")

    name: str = None
    order: int = None
    sublist: Optional[Union[dict, NestedList]] = None
    analysisRef: Optional[Union[str, AnalysisId]] = None
    outputRef: Optional[Union[str, OutputId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.sublist is not None and not isinstance(self.sublist, NestedList):
            self.sublist = NestedList(**as_dict(self.sublist))

        if self.analysisRef is not None and not isinstance(self.analysisRef, AnalysisId):
            self.analysisRef = AnalysisId(self.analysisRef)

        if self.outputRef is not None and not isinstance(self.outputRef, OutputId):
            self.outputRef = OutputId(self.outputRef)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisCategorization(YAMLRoot):
    """
    An implementer-defined categorization of analyses/outputs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisCategorization")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalysisCategorization"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisCategorization")

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
    An implementer-defined category of analyses/outputs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisCategory")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalysisCategory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisCategory")

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
class Analysis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Analysis")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Analysis")

    id: Union[str, AnalysisId] = None
    version: Optional[int] = None
    categoryRefs: Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]] = empty_list()
    analysisSetRef: Optional[Union[str, AnalysisSetId]] = None
    orderedGroupings: Optional[Union[Union[dict, "OrderedGroupingFactor"], List[Union[dict, "OrderedGroupingFactor"]]]] = empty_list()
    dataSubsetRef: Optional[Union[str, DataSubsetId]] = None
    dataset: Optional[str] = None
    variable: Optional[str] = None
    method: Optional[Union[dict, "AnalysisMethod"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisId):
            self.id = AnalysisId(self.id)

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if not isinstance(self.categoryRefs, list):
            self.categoryRefs = [self.categoryRefs] if self.categoryRefs is not None else []
        self.categoryRefs = [v if isinstance(v, AnalysisCategoryId) else AnalysisCategoryId(v) for v in self.categoryRefs]

        if self.analysisSetRef is not None and not isinstance(self.analysisSetRef, AnalysisSetId):
            self.analysisSetRef = AnalysisSetId(self.analysisSetRef)

        if not isinstance(self.orderedGroupings, list):
            self.orderedGroupings = [self.orderedGroupings] if self.orderedGroupings is not None else []
        self.orderedGroupings = [v if isinstance(v, OrderedGroupingFactor) else OrderedGroupingFactor(**as_dict(v)) for v in self.orderedGroupings]

        if self.dataSubsetRef is not None and not isinstance(self.dataSubsetRef, DataSubsetId):
            self.dataSubsetRef = DataSubsetId(self.dataSubsetRef)

        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        if self.variable is not None and not isinstance(self.variable, str):
            self.variable = str(self.variable)

        if self.method is not None and not isinstance(self.method, AnalysisMethod):
            self.method = AnalysisMethod(**as_dict(self.method))

        super().__post_init__(**kwargs)


@dataclass
class OrderedGroupingFactor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OrderedGroupingFactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OrderedGroupingFactor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OrderedGroupingFactor")

    order: int = None
    groupingRef: Optional[Union[str, GroupingFactorId]] = None
    dataGrouping: Optional[Union[dict, "DataGroupingFactor"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.groupingRef is not None and not isinstance(self.groupingRef, GroupingFactorId):
            self.groupingRef = GroupingFactorId(self.groupingRef)

        if self.dataGrouping is not None and not isinstance(self.dataGrouping, DataGroupingFactor):
            self.dataGrouping = DataGroupingFactor(**as_dict(self.dataGrouping))

        super().__post_init__(**kwargs)


@dataclass
class AnalysisMethod(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisMethod")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalysisMethod"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisMethod")

    id: Union[str, AnalysisMethodId] = None
    name: str = None
    operations: Union[Dict[Union[str, OperationId], Union[dict, "Operation"]], List[Union[dict, "Operation"]]] = empty_dict()
    label: Optional[str] = None
    description: Optional[str] = None

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

        super().__post_init__(**kwargs)


@dataclass
class Operation(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Operation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Operation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Operation")

    id: Union[str, OperationId] = None
    name: str = None
    label: Optional[str] = None
    referencedResultRelationships: Optional[Union[Union[dict, "ReferencedResultRelationship"], List[Union[dict, "ReferencedResultRelationship"]]]] = empty_list()
    resultPattern: Optional[str] = None
    results: Optional[Union[Union[dict, "OperationResult"], List[Union[dict, "OperationResult"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationId):
            self.id = OperationId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.referencedResultRelationships, list):
            self.referencedResultRelationships = [self.referencedResultRelationships] if self.referencedResultRelationships is not None else []
        self.referencedResultRelationships = [v if isinstance(v, ReferencedResultRelationship) else ReferencedResultRelationship(**as_dict(v)) for v in self.referencedResultRelationships]

        if self.resultPattern is not None and not isinstance(self.resultPattern, str):
            self.resultPattern = str(self.resultPattern)

        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, OperationResult) else OperationResult(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)


@dataclass
class ReferencedResultRelationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/ReferencedResultRelationship")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReferencedResultRelationship"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/ReferencedResultRelationship")

    referencedResultRole: Union[str, "OperationRole"] = None
    operationRef: Union[str, OperationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.referencedResultRole):
            self.MissingRequiredField("referencedResultRole")
        if not isinstance(self.referencedResultRole, OperationRole):
            self.referencedResultRole = OperationRole(self.referencedResultRole)

        if self._is_empty(self.operationRef):
            self.MissingRequiredField("operationRef")
        if not isinstance(self.operationRef, OperationId):
            self.operationRef = OperationId(self.operationRef)

        super().__post_init__(**kwargs)


@dataclass
class OperationResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OperationResult")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OperationResult"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OperationResult")

    groupRefs: Optional[Union[Union[str, AnalysisGroupId], List[Union[str, AnalysisGroupId]]]] = empty_list()
    rawValue: Optional[str] = None
    formattedValue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.groupRefs, list):
            self.groupRefs = [self.groupRefs] if self.groupRefs is not None else []
        self.groupRefs = [v if isinstance(v, AnalysisGroupId) else AnalysisGroupId(v) for v in self.groupRefs]

        if self.rawValue is not None and not isinstance(self.rawValue, str):
            self.rawValue = str(self.rawValue)

        if self.formattedValue is not None and not isinstance(self.formattedValue, str):
            self.formattedValue = str(self.formattedValue)

        super().__post_init__(**kwargs)


@dataclass
class Output(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Output")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Output"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Output")

    id: Union[str, OutputId] = None
    version: Optional[int] = None
    fileSpecifications: Optional[Union[Union[dict, "File"], List[Union[dict, "File"]]]] = empty_list()
    outputDisplays: Optional[Union[Union[dict, "OutputDisplay"], List[Union[dict, "OutputDisplay"]]]] = empty_list()
    categoryRefs: Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OutputId):
            self.id = OutputId(self.id)

        if self.version is not None and not isinstance(self.version, int):
            self.version = int(self.version)

        if not isinstance(self.fileSpecifications, list):
            self.fileSpecifications = [self.fileSpecifications] if self.fileSpecifications is not None else []
        self.fileSpecifications = [v if isinstance(v, File) else File(**as_dict(v)) for v in self.fileSpecifications]

        if not isinstance(self.outputDisplays, list):
            self.outputDisplays = [self.outputDisplays] if self.outputDisplays is not None else []
        self.outputDisplays = [v if isinstance(v, OutputDisplay) else OutputDisplay(**as_dict(v)) for v in self.outputDisplays]

        if not isinstance(self.categoryRefs, list):
            self.categoryRefs = [self.categoryRefs] if self.categoryRefs is not None else []
        self.categoryRefs = [v if isinstance(v, AnalysisCategoryId) else AnalysisCategoryId(v) for v in self.categoryRefs]

        super().__post_init__(**kwargs)


@dataclass
class File(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/File")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/File")

    name: str = None
    fileType: Optional[Union[str, "FileType"]] = None
    location: Optional[str] = None
    style: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fileType is not None and not isinstance(self.fileType, FileType):
            self.fileType = FileType(self.fileType)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.style is not None and not isinstance(self.style, str):
            self.style = str(self.style)

        super().__post_init__(**kwargs)


@dataclass
class OutputDisplay(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OutputDisplay")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OutputDisplay"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/OutputDisplay")

    order: int = None
    display: Optional[Union[dict, "Display"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.display is not None and not isinstance(self.display, Display):
            self.display = Display(**as_dict(self.display))

        super().__post_init__(**kwargs)


@dataclass
class Display(NamedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Display")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Display"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Display")

    id: Union[str, DisplayId] = None
    name: str = None
    version: Optional[int] = None
    displayTitle: Optional[str] = None
    displaySections: Optional[Union[Union[dict, "DisplaySection"], List[Union[dict, "DisplaySection"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisplayId):
            self.id = DisplayId(self.id)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DisplaySection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DisplaySection"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DisplaySection")

    sectionType: Optional[Union[str, "SectionType"]] = None
    subSections: Optional[Union[Dict[Union[str, DisplaySubSectionId], Union[dict, "DisplaySubSection"]], List[Union[dict, "DisplaySubSection"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sectionType is not None and not isinstance(self.sectionType, SectionType):
            self.sectionType = SectionType(self.sectionType)

        self._normalize_inlined_as_list(slot_name="subSections", slot_type=DisplaySubSection, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DisplaySubSection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DisplaySubSection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DisplaySubSection"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DisplaySubSection")

    id: Union[str, DisplaySubSectionId] = None
    order: int = None
    text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisplaySubSectionId):
            self.id = DisplaySubSectionId(self.id)

        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass
class WhereClause(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/WhereClause")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "WhereClause"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/WhereClause")

    id: Union[str, WhereClauseId] = None
    condition: Optional[Union[dict, "Condition"]] = None
    compoundExpression: Optional[Union[dict, "CompoundExpression"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WhereClauseId):
            self.id = WhereClauseId(self.id)

        if self.condition is not None and not isinstance(self.condition, Condition):
            self.condition = Condition(**as_dict(self.condition))

        if self.compoundExpression is not None and not isinstance(self.compoundExpression, CompoundExpression):
            self.compoundExpression = CompoundExpression(**as_dict(self.compoundExpression))

        super().__post_init__(**kwargs)


@dataclass
class Condition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Condition")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Condition")

    dataset: Optional[str] = None
    variable: Optional[str] = None
    comparator: Optional[Union[str, "Comparator"]] = None
    value: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        if self.variable is not None and not isinstance(self.variable, str):
            self.variable = str(self.variable)

        if self.comparator is not None and not isinstance(self.comparator, Comparator):
            self.comparator = Comparator(self.comparator)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundExpression")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundExpression")

    logicalOperator: Union[str, "AndOr"] = None
    whereClauses: Optional[Union[Union[str, WhereClauseId], List[Union[str, WhereClauseId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.logicalOperator):
            self.MissingRequiredField("logicalOperator")
        if not isinstance(self.logicalOperator, AndOr):
            self.logicalOperator = AndOr(self.logicalOperator)

        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, WhereClauseId) else WhereClauseId(v) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundSetExpression(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundSetExpression")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CompoundSetExpression"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundSetExpression")

    logicalOperator: Union[str, "AndOr"] = None
    whereClauses: Optional[Union[Union[str, AnalysisSetId], List[Union[str, AnalysisSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, AnalysisSetId) else AnalysisSetId(v) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundGroupExpression(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundGroupExpression")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CompoundGroupExpression"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundGroupExpression")

    logicalOperator: Union[str, "AndOr"] = None
    whereClauses: Optional[Union[Union[str, GroupId], List[Union[str, GroupId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.whereClauses, list):
            self.whereClauses = [self.whereClauses] if self.whereClauses is not None else []
        self.whereClauses = [v if isinstance(v, GroupId) else GroupId(v) for v in self.whereClauses]

        super().__post_init__(**kwargs)


@dataclass
class CompoundSubsetExpression(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundSubsetExpression")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CompoundSubsetExpression"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/CompoundSubsetExpression")

    logicalOperator: Union[str, "AndOr"] = None
    whereClauses: Optional[Union[Dict[Union[str, WhereClauseId], Union[dict, WhereClause]], List[Union[dict, WhereClause]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="whereClauses", slot_type=WhereClause, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisSet(WhereClause):
    """
    A set of subjects whose data are to be included in the main analyses. This should be defined in the statistical
    section of the protocol. NOTE: There are a number of potential analysis sets, including, for example, the set
    based upon the intent-to-treat principle. [ICH E9]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalysisSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisSet")

    id: Union[str, AnalysisSetId] = None
    order: int = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSetExpression]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisSetId):
            self.id = AnalysisSetId(self.id)

        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/GroupingFactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GroupingFactor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/GroupingFactor")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/SubjectGroupingFactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SubjectGroupingFactor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/SubjectGroupingFactor")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataGroupingFactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataGroupingFactor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataGroupingFactor")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Group")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/Group")

    id: Union[str, GroupId] = None
    order: int = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundGroupExpression]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroupId):
            self.id = GroupId(self.id)

        if self._is_empty(self.order):
            self.MissingRequiredField("order")
        if not isinstance(self.order, int):
            self.order = int(self.order)

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalysisGroup"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/AnalysisGroup")

    id: Union[str, AnalysisGroupId] = None
    order: int = None

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataGroup"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataGroup")

    id: Union[str, DataGroupId] = None
    order: int = None

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataSubset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataSubset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/ars/1-0/DataSubset")

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


# Enumerations
class FileType(EnumDefinitionImpl):

    pdf = PermissibleValue(text="pdf")
    rtf = PermissibleValue(text="rtf")
    txt = PermissibleValue(text="txt")

    _defn = EnumDefinition(
        name="FileType",
    )

class AndOr(EnumDefinitionImpl):

    AND = PermissibleValue(text="AND")
    OR = PermissibleValue(text="OR")

    _defn = EnumDefinition(
        name="AndOr",
    )

class Comparator(EnumDefinitionImpl):

    EQ = PermissibleValue(text="EQ")
    NE = PermissibleValue(text="NE")
    GT = PermissibleValue(text="GT")
    GE = PermissibleValue(text="GE")
    LT = PermissibleValue(text="LT")
    LE = PermissibleValue(text="LE")
    IN = PermissibleValue(text="IN")
    NOTIN = PermissibleValue(text="NOTIN")

    _defn = EnumDefinition(
        name="Comparator",
    )

class SectionType(EnumDefinitionImpl):

    Title = PermissibleValue(text="Title")
    Footnote = PermissibleValue(text="Footnote")
    Abbreviation = PermissibleValue(text="Abbreviation")
    Legend = PermissibleValue(text="Legend")

    _defn = EnumDefinition(
        name="SectionType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Rowlabel Header",
                PermissibleValue(text="Rowlabel Header") )

class OperationRole(EnumDefinitionImpl):

    NUMERATOR = PermissibleValue(text="NUMERATOR")
    DENOMINATOR = PermissibleValue(text="DENOMINATOR")

    _defn = EnumDefinition(
        name="OperationRole",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=str)

slots.listOfPlannedAnalyses = Slot(uri=DEFAULT_.listOfPlannedAnalyses, name="listOfPlannedAnalyses", curie=DEFAULT_.curie('listOfPlannedAnalyses'),
                   model_uri=DEFAULT_.listOfPlannedAnalyses, domain=None, range=Union[dict, NestedList])

slots.listOfPlannedOutputs = Slot(uri=DEFAULT_.listOfPlannedOutputs, name="listOfPlannedOutputs", curie=DEFAULT_.curie('listOfPlannedOutputs'),
                   model_uri=DEFAULT_.listOfPlannedOutputs, domain=None, range=Optional[Union[dict, NestedList]])

slots.analysisSets = Slot(uri=DEFAULT_.analysisSets, name="analysisSets", curie=DEFAULT_.curie('analysisSets'),
                   model_uri=DEFAULT_.analysisSets, domain=None, range=Optional[Union[Dict[Union[str, AnalysisSetId], Union[dict, AnalysisSet]], List[Union[dict, AnalysisSet]]]])

slots.analysisGroupings = Slot(uri=DEFAULT_.analysisGroupings, name="analysisGroupings", curie=DEFAULT_.curie('analysisGroupings'),
                   model_uri=DEFAULT_.analysisGroupings, domain=None, range=Optional[Union[Dict[Union[str, SubjectGroupingFactorId], Union[dict, SubjectGroupingFactor]], List[Union[dict, SubjectGroupingFactor]]]])

slots.groupingVariable = Slot(uri=DEFAULT_.groupingVariable, name="groupingVariable", curie=DEFAULT_.curie('groupingVariable'),
                   model_uri=DEFAULT_.groupingVariable, domain=None, range=Optional[str])

slots.dataDriven = Slot(uri=DEFAULT_.dataDriven, name="dataDriven", curie=DEFAULT_.curie('dataDriven'),
                   model_uri=DEFAULT_.dataDriven, domain=None, range=Union[bool, Bool])

slots.groups = Slot(uri=DEFAULT_.groups, name="groups", curie=DEFAULT_.curie('groups'),
                   model_uri=DEFAULT_.groups, domain=None, range=Optional[Union[Dict[Union[str, GroupId], Union[dict, Group]], List[Union[dict, Group]]]])

slots.dataSubsets = Slot(uri=DEFAULT_.dataSubsets, name="dataSubsets", curie=DEFAULT_.curie('dataSubsets'),
                   model_uri=DEFAULT_.dataSubsets, domain=None, range=Optional[Union[Dict[Union[str, DataSubsetId], Union[dict, DataSubset]], List[Union[dict, DataSubset]]]])

slots.analyses = Slot(uri=DEFAULT_.analyses, name="analyses", curie=DEFAULT_.curie('analyses'),
                   model_uri=DEFAULT_.analyses, domain=None, range=Optional[Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]]])

slots.analysisCategorizations = Slot(uri=DEFAULT_.analysisCategorizations, name="analysisCategorizations", curie=DEFAULT_.curie('analysisCategorizations'),
                   model_uri=DEFAULT_.analysisCategorizations, domain=None, range=Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, AnalysisCategorization]], List[Union[dict, AnalysisCategorization]]]])

slots.categories = Slot(uri=DEFAULT_.categories, name="categories", curie=DEFAULT_.curie('categories'),
                   model_uri=DEFAULT_.categories, domain=None, range=Union[Dict[Union[str, AnalysisCategoryId], Union[dict, AnalysisCategory]], List[Union[dict, AnalysisCategory]]])

slots.categoryRefs = Slot(uri=DEFAULT_.categoryRefs, name="categoryRefs", curie=DEFAULT_.curie('categoryRefs'),
                   model_uri=DEFAULT_.categoryRefs, domain=None, range=Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]])

slots.subCategorizations = Slot(uri=DEFAULT_.subCategorizations, name="subCategorizations", curie=DEFAULT_.curie('subCategorizations'),
                   model_uri=DEFAULT_.subCategorizations, domain=None, range=Optional[Union[Dict[Union[str, AnalysisCategorizationId], Union[dict, AnalysisCategorization]], List[Union[dict, AnalysisCategorization]]]])

slots.outputs = Slot(uri=DEFAULT_.outputs, name="outputs", curie=DEFAULT_.curie('outputs'),
                   model_uri=DEFAULT_.outputs, domain=None, range=Optional[Union[Dict[Union[str, OutputId], Union[dict, Output]], List[Union[dict, Output]]]])

slots.listItems = Slot(uri=DEFAULT_.listItems, name="listItems", curie=DEFAULT_.curie('listItems'),
                   model_uri=DEFAULT_.listItems, domain=None, range=Optional[Union[Union[dict, OrderedListItem], List[Union[dict, OrderedListItem]]]])

slots.order = Slot(uri=DEFAULT_.order, name="order", curie=DEFAULT_.curie('order'),
                   model_uri=DEFAULT_.order, domain=None, range=int)

slots.sublist = Slot(uri=DEFAULT_.sublist, name="sublist", curie=DEFAULT_.curie('sublist'),
                   model_uri=DEFAULT_.sublist, domain=None, range=Optional[Union[dict, NestedList]])

slots.analysisRef = Slot(uri=DEFAULT_.analysisRef, name="analysisRef", curie=DEFAULT_.curie('analysisRef'),
                   model_uri=DEFAULT_.analysisRef, domain=None, range=Optional[Union[str, AnalysisId]])

slots.analysisSetRef = Slot(uri=DEFAULT_.analysisSetRef, name="analysisSetRef", curie=DEFAULT_.curie('analysisSetRef'),
                   model_uri=DEFAULT_.analysisSetRef, domain=None, range=Optional[Union[str, AnalysisSetId]])

slots.orderedGroupings = Slot(uri=DEFAULT_.orderedGroupings, name="orderedGroupings", curie=DEFAULT_.curie('orderedGroupings'),
                   model_uri=DEFAULT_.orderedGroupings, domain=None, range=Optional[Union[Union[dict, OrderedGroupingFactor], List[Union[dict, OrderedGroupingFactor]]]])

slots.groupingRef = Slot(uri=DEFAULT_.groupingRef, name="groupingRef", curie=DEFAULT_.curie('groupingRef'),
                   model_uri=DEFAULT_.groupingRef, domain=None, range=Optional[Union[str, GroupingFactorId]])

slots.dataGrouping = Slot(uri=DEFAULT_.dataGrouping, name="dataGrouping", curie=DEFAULT_.curie('dataGrouping'),
                   model_uri=DEFAULT_.dataGrouping, domain=None, range=Optional[Union[dict, DataGroupingFactor]])

slots.dataSubsetRef = Slot(uri=DEFAULT_.dataSubsetRef, name="dataSubsetRef", curie=DEFAULT_.curie('dataSubsetRef'),
                   model_uri=DEFAULT_.dataSubsetRef, domain=None, range=Optional[Union[str, DataSubsetId]])

slots.method = Slot(uri=DEFAULT_.method, name="method", curie=DEFAULT_.curie('method'),
                   model_uri=DEFAULT_.method, domain=None, range=Optional[Union[dict, AnalysisMethod]])

slots.description = Slot(uri=DEFAULT_.description, name="description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.operations = Slot(uri=DEFAULT_.operations, name="operations", curie=DEFAULT_.curie('operations'),
                   model_uri=DEFAULT_.operations, domain=None, range=Union[Dict[Union[str, OperationId], Union[dict, Operation]], List[Union[dict, Operation]]])

slots.resultPattern = Slot(uri=DEFAULT_.resultPattern, name="resultPattern", curie=DEFAULT_.curie('resultPattern'),
                   model_uri=DEFAULT_.resultPattern, domain=None, range=Optional[str])

slots.results = Slot(uri=DEFAULT_.results, name="results", curie=DEFAULT_.curie('results'),
                   model_uri=DEFAULT_.results, domain=None, range=Optional[Union[Union[dict, OperationResult], List[Union[dict, OperationResult]]]])

slots.groupRefs = Slot(uri=DEFAULT_.groupRefs, name="groupRefs", curie=DEFAULT_.curie('groupRefs'),
                   model_uri=DEFAULT_.groupRefs, domain=None, range=Optional[Union[Union[str, AnalysisGroupId], List[Union[str, AnalysisGroupId]]]])

slots.rawValue = Slot(uri=DEFAULT_.rawValue, name="rawValue", curie=DEFAULT_.curie('rawValue'),
                   model_uri=DEFAULT_.rawValue, domain=None, range=Optional[str])

slots.formattedValue = Slot(uri=DEFAULT_.formattedValue, name="formattedValue", curie=DEFAULT_.curie('formattedValue'),
                   model_uri=DEFAULT_.formattedValue, domain=None, range=Optional[str])

slots.referencedResultRelationships = Slot(uri=DEFAULT_.referencedResultRelationships, name="referencedResultRelationships", curie=DEFAULT_.curie('referencedResultRelationships'),
                   model_uri=DEFAULT_.referencedResultRelationships, domain=None, range=Optional[Union[Union[dict, ReferencedResultRelationship], List[Union[dict, ReferencedResultRelationship]]]])

slots.referencedResultRole = Slot(uri=DEFAULT_.referencedResultRole, name="referencedResultRole", curie=DEFAULT_.curie('referencedResultRole'),
                   model_uri=DEFAULT_.referencedResultRole, domain=None, range=Union[str, "OperationRole"])

slots.operationRef = Slot(uri=DEFAULT_.operationRef, name="operationRef", curie=DEFAULT_.curie('operationRef'),
                   model_uri=DEFAULT_.operationRef, domain=None, range=Union[str, OperationId])

slots.outputRef = Slot(uri=DEFAULT_.outputRef, name="outputRef", curie=DEFAULT_.curie('outputRef'),
                   model_uri=DEFAULT_.outputRef, domain=None, range=Optional[Union[str, OutputId]])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.version = Slot(uri=DEFAULT_.version, name="version", curie=DEFAULT_.curie('version'),
                   model_uri=DEFAULT_.version, domain=None, range=Optional[int])

slots.displayTitle = Slot(uri=DEFAULT_.displayTitle, name="displayTitle", curie=DEFAULT_.curie('displayTitle'),
                   model_uri=DEFAULT_.displayTitle, domain=None, range=Optional[str])

slots.fileSpecifications = Slot(uri=DEFAULT_.fileSpecifications, name="fileSpecifications", curie=DEFAULT_.curie('fileSpecifications'),
                   model_uri=DEFAULT_.fileSpecifications, domain=None, range=Optional[Union[Union[dict, File], List[Union[dict, File]]]])

slots.fileType = Slot(uri=DEFAULT_.fileType, name="fileType", curie=DEFAULT_.curie('fileType'),
                   model_uri=DEFAULT_.fileType, domain=None, range=Optional[Union[str, "FileType"]])

slots.location = Slot(uri=DEFAULT_.location, name="location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.location, domain=None, range=Optional[str])

slots.style = Slot(uri=DEFAULT_.style, name="style", curie=DEFAULT_.curie('style'),
                   model_uri=DEFAULT_.style, domain=None, range=Optional[str])

slots.outputDisplays = Slot(uri=DEFAULT_.outputDisplays, name="outputDisplays", curie=DEFAULT_.curie('outputDisplays'),
                   model_uri=DEFAULT_.outputDisplays, domain=None, range=Optional[Union[Union[dict, OutputDisplay], List[Union[dict, OutputDisplay]]]])

slots.display = Slot(uri=DEFAULT_.display, name="display", curie=DEFAULT_.curie('display'),
                   model_uri=DEFAULT_.display, domain=None, range=Optional[Union[dict, Display]])

slots.globalDisplaySections = Slot(uri=DEFAULT_.globalDisplaySections, name="globalDisplaySections", curie=DEFAULT_.curie('globalDisplaySections'),
                   model_uri=DEFAULT_.globalDisplaySections, domain=None, range=Optional[Union[Union[dict, DisplaySection], List[Union[dict, DisplaySection]]]])

slots.displaySections = Slot(uri=DEFAULT_.displaySections, name="displaySections", curie=DEFAULT_.curie('displaySections'),
                   model_uri=DEFAULT_.displaySections, domain=None, range=Optional[Union[Union[dict, DisplaySection], List[Union[dict, DisplaySection]]]])

slots.sectionType = Slot(uri=DEFAULT_.sectionType, name="sectionType", curie=DEFAULT_.curie('sectionType'),
                   model_uri=DEFAULT_.sectionType, domain=None, range=Optional[Union[str, "SectionType"]])

slots.subSections = Slot(uri=DEFAULT_.subSections, name="subSections", curie=DEFAULT_.curie('subSections'),
                   model_uri=DEFAULT_.subSections, domain=None, range=Optional[Union[Dict[Union[str, DisplaySubSectionId], Union[dict, DisplaySubSection]], List[Union[dict, DisplaySubSection]]]])

slots.text = Slot(uri=DEFAULT_.text, name="text", curie=DEFAULT_.curie('text'),
                   model_uri=DEFAULT_.text, domain=None, range=Optional[str])

slots.logicalOperator = Slot(uri=DEFAULT_.logicalOperator, name="logicalOperator", curie=DEFAULT_.curie('logicalOperator'),
                   model_uri=DEFAULT_.logicalOperator, domain=None, range=Union[str, "AndOr"])

slots.condition = Slot(uri=DEFAULT_.condition, name="condition", curie=DEFAULT_.curie('condition'),
                   model_uri=DEFAULT_.condition, domain=None, range=Optional[Union[dict, Condition]])

slots.compoundExpression = Slot(uri=DEFAULT_.compoundExpression, name="compoundExpression", curie=DEFAULT_.curie('compoundExpression'),
                   model_uri=DEFAULT_.compoundExpression, domain=None, range=Optional[Union[dict, CompoundExpression]])

slots.whereClauses = Slot(uri=DEFAULT_.whereClauses, name="whereClauses", curie=DEFAULT_.curie('whereClauses'),
                   model_uri=DEFAULT_.whereClauses, domain=None, range=Optional[Union[Union[str, WhereClauseId], List[Union[str, WhereClauseId]]]])

slots.dataset = Slot(uri=DEFAULT_.dataset, name="dataset", curie=DEFAULT_.curie('dataset'),
                   model_uri=DEFAULT_.dataset, domain=None, range=Optional[str])

slots.variable = Slot(uri=DEFAULT_.variable, name="variable", curie=DEFAULT_.curie('variable'),
                   model_uri=DEFAULT_.variable, domain=None, range=Optional[str])

slots.comparator = Slot(uri=DEFAULT_.comparator, name="comparator", curie=DEFAULT_.curie('comparator'),
                   model_uri=DEFAULT_.comparator, domain=None, range=Optional[Union[str, "Comparator"]])

slots.value = Slot(uri=DEFAULT_.value, name="value", curie=DEFAULT_.curie('value'),
                   model_uri=DEFAULT_.value, domain=None, range=Optional[Union[str, List[str]]])

slots.label = Slot(uri=DEFAULT_.label, name="label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.label, domain=None, range=Optional[str])

slots.Output_categoryRefs = Slot(uri=DEFAULT_.categoryRefs, name="Output_categoryRefs", curie=DEFAULT_.curie('categoryRefs'),
                   model_uri=DEFAULT_.Output_categoryRefs, domain=Output, range=Optional[Union[Union[str, AnalysisCategoryId], List[Union[str, AnalysisCategoryId]]]])

slots.CompoundSetExpression_whereClauses = Slot(uri=DEFAULT_.whereClauses, name="CompoundSetExpression_whereClauses", curie=DEFAULT_.curie('whereClauses'),
                   model_uri=DEFAULT_.CompoundSetExpression_whereClauses, domain=CompoundSetExpression, range=Optional[Union[Union[str, AnalysisSetId], List[Union[str, AnalysisSetId]]]])

slots.CompoundGroupExpression_whereClauses = Slot(uri=DEFAULT_.whereClauses, name="CompoundGroupExpression_whereClauses", curie=DEFAULT_.curie('whereClauses'),
                   model_uri=DEFAULT_.CompoundGroupExpression_whereClauses, domain=CompoundGroupExpression, range=Optional[Union[Union[str, GroupId], List[Union[str, GroupId]]]])

slots.CompoundSubsetExpression_whereClauses = Slot(uri=DEFAULT_.whereClauses, name="CompoundSubsetExpression_whereClauses", curie=DEFAULT_.curie('whereClauses'),
                   model_uri=DEFAULT_.CompoundSubsetExpression_whereClauses, domain=CompoundSubsetExpression, range=Optional[Union[Dict[Union[str, WhereClauseId], Union[dict, WhereClause]], List[Union[dict, WhereClause]]]])

slots.AnalysisSet_compoundExpression = Slot(uri=DEFAULT_.compoundExpression, name="AnalysisSet_compoundExpression", curie=DEFAULT_.curie('compoundExpression'),
                   model_uri=DEFAULT_.AnalysisSet_compoundExpression, domain=AnalysisSet, range=Optional[Union[dict, CompoundSetExpression]])

slots.SubjectGroupingFactor_groups = Slot(uri=DEFAULT_.groups, name="SubjectGroupingFactor_groups", curie=DEFAULT_.curie('groups'),
                   model_uri=DEFAULT_.SubjectGroupingFactor_groups, domain=SubjectGroupingFactor, range=Optional[Union[Dict[Union[str, AnalysisGroupId], Union[dict, "AnalysisGroup"]], List[Union[dict, "AnalysisGroup"]]]])

slots.DataGroupingFactor_groups = Slot(uri=DEFAULT_.groups, name="DataGroupingFactor_groups", curie=DEFAULT_.curie('groups'),
                   model_uri=DEFAULT_.DataGroupingFactor_groups, domain=DataGroupingFactor, range=Optional[Union[Dict[Union[str, DataGroupId], Union[dict, "DataGroup"]], List[Union[dict, "DataGroup"]]]])

slots.Group_compoundExpression = Slot(uri=DEFAULT_.compoundExpression, name="Group_compoundExpression", curie=DEFAULT_.curie('compoundExpression'),
                   model_uri=DEFAULT_.Group_compoundExpression, domain=Group, range=Optional[Union[dict, CompoundGroupExpression]])

slots.DataSubset_compoundExpression = Slot(uri=DEFAULT_.compoundExpression, name="DataSubset_compoundExpression", curie=DEFAULT_.curie('compoundExpression'),
                   model_uri=DEFAULT_.DataSubset_compoundExpression, domain=DataSubset, range=Optional[Union[dict, CompoundSubsetExpression]])
