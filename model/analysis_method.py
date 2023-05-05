from typing import List, Union, Optional
from uuid import UUID

from .operation import Operation

class AnalysisMethod():
    analysisMethodid: Union[UUID, str] = None
    name: str = None
    operations: List[Operation] = []
    label: Optional[str] = None
    description: Optional[str] = None
