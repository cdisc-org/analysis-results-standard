from typing import List, Union, Optional
from uuid import UUID


class DisplaySubSection():
    displaySectionId: Union[UUID, None] = None
    order: int
    text: str
