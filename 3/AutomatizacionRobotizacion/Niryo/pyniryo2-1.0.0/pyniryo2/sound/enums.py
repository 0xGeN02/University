from enum import Enum, unique


@unique
class ManageSound(Enum):
    """
    Enumeration of the actions of sound database management
    """
    ADD = 1
    DELETE = 2


@unique
class Language(Enum):
    """
    Enumeration of the Text To Speech languages
    """
    ENGLISH = 0
    FRENCH = 1
    SPANISH = 3
    MANDARIN = 4
    PORTUGUESE = 5
