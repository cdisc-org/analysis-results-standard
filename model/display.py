from typing import List, Union, Optional
from uuid import UUID

class Display():
    displayid: Union[UUID, None] = None
    name: str = None
    version: Optional[int] = None
    displayTitle: Optional[str] = None
    displaySections: Optional[Union[Union[dict, DisplaySection], List[Union[dict, DisplaySection]]]] = []
