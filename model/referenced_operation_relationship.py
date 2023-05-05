from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

class OperationRole(Enum):
    NUMERATOR = "NUMERATOR"
    DENOMINATOR = "DENOMINATOR"

class ReferencedOperationRelationship():
    referencedOperationRelationshipId: Union[UUID, None] = None
    referencedOperationRole: Union[str, "OperationRole"] = None
    operationId: str
    analysisId: Optional[str] = None
    description: Optional[str] = None