from typing import List, Union, Optional
from enum import Enum

class Comparator(Enum):
    EQ = "EQ"
    NE = "NE"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"
    IN = "IN"
    NOTIN = "NOTIN"

class Condition():
    dataset: Optional[str] = None
    variable: Optional[str] = None
    comparator: Optional[Union[str, "Comparator"]] = None
    value: Optional[Union[str, List[str]]]
