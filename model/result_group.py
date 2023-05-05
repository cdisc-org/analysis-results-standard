from typing import List, Union, Optional
from uuid import UUID

class ResultGroup():
    groupingId: Union[UUID, str]
    groupId: Optional[str] = None
    groupValue: Optional[str] = None