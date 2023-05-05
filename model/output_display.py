from typing import List, Union
from uuid import UUID

from .display import Display

class OutputDisplay():
    # outputDisplayId: Union[UUID, None] = None
    order: int
    display: Display
