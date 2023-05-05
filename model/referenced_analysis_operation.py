from typing import Union, Optional
from uuid import UUID


class ReferencedAnalysisOperation():
    analysisId: Union[UUID, str] = None
    referencedOperationId: Optional[str] = None
