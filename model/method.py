from typing import List, Union
from uuid import UUID

from .operation import Operation 

class Method():
  methodId: Union[UUID, None] = None
  label: str
  description: str
  operations: List[Operation] = []