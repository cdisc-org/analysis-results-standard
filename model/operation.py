from typing import List, Union
from uuid import UUID

class Operation():
    operationId: Union[UUID, None] = None
    name: str
    label: str
    referencedOperationRelationships: List = []
    resultPattern: str