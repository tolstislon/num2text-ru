from enum import Enum


class Genus(Enum):
    MASCULINE = "m"
    FEMININE = "f"
    NEUTER = "n"


class Plural(Enum):
    SINGULAR = "s"
    PLURAL = "p"
    GENITIVE = "g"
