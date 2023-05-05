from typing import List, Union
from uuid import UUID

class Analysis():
    analysisId: Union[UUID, None] = None
    version: str
    categoryIds: List = []
    analysisSetId: str
    orderedGroupings: List = []
    dataSubsetId: str
    dataset: str
    variable: str
    methodId: str
    referencedAnalysisOperations: List = []
    results: str
