from typing import List, Union
from uuid import UUID

class Operation():
  operationId: Union[UUID, None] = None
  label: str
  referencedOperationRelationships: List = []
  operations: List = []