from typing import List, Union, Optional
from uuid import UUID

from .analysis import Analysis
from .analysis_categorization import AnalysisCategorization
from .analysis_method import AnalysisMethod
from .analysis_set import AnalysisSet
from .data_subset import DataSubset
from .display_sections import DisplaySection
from .method import Method
from .nested_list import NestedList
from .output import Output
from .subject_grouping_factor import SubjectGroupingFactor

class ReportingEvent():
    name: str
    listOfPlannedAnalyses: Union[dict, NestedList]
    listOfPlannedOutputs: Optional[Union[dict, NestedList]] = None
    analysisSets: List[Union[dict, AnalysisSet]] = []
    analysisGroupings: List[Union[dict, SubjectGroupingFactor]] = []
    dataSubsets: List[Union[dict, DataSubset]] = []
    globalDisplaySections: List[Union[dict, DisplaySection]] = []
    analysisCategorizations: List[Union[dict, AnalysisCategorization]] = []
    analyses: List[Union[dict, Analysis]] = []
    methods: List[Union[dict, AnalysisMethod]] = []
    outputs: List[Union[dict, Output]] = []
