from typing import List, Union
from uuid import UUID

class AnalysisCategorization():
    analysisCategorizationId: Union[UUID, None] = None
    label: str = ""
    categories: List = []
