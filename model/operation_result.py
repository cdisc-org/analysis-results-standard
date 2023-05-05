from typing import List, Union, Optional
from uuid import UUID

from .result_group import ResultGroup

class OperationResult():
    operationId: str
    resultGroups: List[ResultGroup] = []
    rawValue: Optional[str] = None
    formattedValue: Optional[str] = None