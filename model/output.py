from typing import List, Union, Optional
from uuid import UUID

from .file import File
from .output_display import OutputDisplay

class Output():
    outputId: Union[UUID, None] = None
    version: int
    fileSpecifications: Optional[Union[Union[dict, File], List[Union[dict, File]]]] = []
    outputDisplays: Optional[Union[Union[dict, OutputDisplay], List[Union[dict, OutputDisplay]]]] = []
    categoryIds: Optional[Union[str, List[str]]] = []
