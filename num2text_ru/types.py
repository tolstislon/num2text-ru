from dataclasses import dataclass, field
from typing import Optional
from .enums import Genus, Plural


@dataclass(frozen=True)
class Unit:
    _m: str
    _f: Optional[str] = field(default=None)
    _n: Optional[str] = field(default=None)

    def get(self, genus: Genus) -> str:
        if genus is Genus.MASCULINE:
            return self._m
        if genus is Genus.FEMININE:
            return self._f if self._f is not None else self._m
        if genus is Genus.NEUTER:
            return self._n if self._n is not None else self._m


@dataclass(frozen=True)
class Names:
    singular: str
    plural: str
    genitive: str
    genus: Genus

    def get(self, plural: Plural) -> str:
        if plural is Plural.SINGULAR:
            return self.singular
        if plural is Plural.PLURAL:
            return self.plural
        if plural is Plural.GENITIVE:
            return self.genitive
