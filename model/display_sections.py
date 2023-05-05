from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

from .display_subsection import DisplaySubSection

class SectionType(Enum):
    TITLE = "Title"
    FOOTNOTE = "Footnote"
    ABBREVIATION = "Abbreviation"
    LEGEND = "Legend"

class DisplaySection():
    sectionType: Optional[Union[str, SectionType]] = None
    subSections: List[DisplaySubSection] = []
