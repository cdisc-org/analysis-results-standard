from typing import List, Union
from uuid import UUID

class AnalysisCategory():
    analysisCategoryId: Union[UUID, None] = None
    label: str = ""
    subCategorizations: List = []
