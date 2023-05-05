from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

class FileType(Enum):
    PDF = "pdf"
    RTF = "rtf"
    TXT = "txt"


class File():
    name: str = None
    fileType: Optional[Union[str, "FileType"]] = None
    location: Optional[str] = None
    style: Optional[str] = None