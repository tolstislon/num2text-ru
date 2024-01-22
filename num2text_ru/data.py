from typing import Final, Tuple

from .enums import Genus
from .types import Names, Unit


UNITS: Final[Tuple[Unit, ...]] = (
    Unit("ноль"),
    Unit("один", "одна", "одно"),
    Unit("два", "две"),
    Unit("три"),
    Unit("четыре"),
    Unit("пять"),
    Unit("шесть"),
    Unit("семь"),
    Unit("восемь"),
    Unit("девять"),
)

TEENS: Final[Tuple[Unit, ...]] = (
    Unit("десять"),
    Unit("одиннадцать"),
    Unit("двенадцать"),
    Unit("тринадцать"),
    Unit("четырнадцать"),
    Unit("пятнадцать"),
    Unit("шестнадцать"),
    Unit("семнадцать"),
    Unit("восемнадцать"),
    Unit("девятнадцать"),
)

TENS: Final[Tuple[Tuple[Unit, ...], Unit, Unit, Unit, Unit, Unit, Unit, Unit, Unit]] = (
    TEENS,
    Unit("двадцать"),
    Unit("тридцать"),
    Unit("сорок"),
    Unit("пятьдесят"),
    Unit("шестьдесят"),
    Unit("семьдесят"),
    Unit("восемьдесят"),
    Unit("девяносто"),
)

HUNDREDS: Final[Tuple[Unit, ...]] = (
    Unit("сто"),
    Unit("двести"),
    Unit("триста"),
    Unit("четыреста"),
    Unit("пятьсот"),
    Unit("шестьсот"),
    Unit("семьсот"),
    Unit("восемьсот"),
    Unit("девятьсот"),
)

NAMES_OF_DEGREES: Final[Tuple[Names, ...]] = (
    Names("тысяча", "тысячи", "тысяч", Genus.FEMININE),
    Names("миллион", "миллиона", "миллионов", Genus.MASCULINE),
    Names("миллиард", "миллиарда", "миллиардов", Genus.MASCULINE),
    Names("триллион", "триллиона", "триллионов", Genus.MASCULINE),
    Names("квадриллион", "квадриллиона", "квадриллионов", Genus.MASCULINE),
    Names("квинтиллион", "квинтиллиона", "квинтиллионов", Genus.MASCULINE),
    Names("секстиллион", "секстиллиона", "секстиллионов", Genus.MASCULINE),
)

MINUS: Final[str] = "минус"

NAMES_OF_DECIMALS: Final[Tuple[Names, ...]] = (
    Names("целая", "целых", "целых", Genus.FEMININE),
    Names("десятая", "десятых", "десятых", Genus.FEMININE),
    Names("сотая", "сотых", "сотых", Genus.FEMININE),
    Names("тысячная", "тысячных", "тысячных", Genus.FEMININE),
    Names("десятитысячная", "десятитысячных", "десятитысячных", Genus.FEMININE),
    Names("стотысячная", "стотысячных", "стотысячных", Genus.FEMININE),
    Names("миллионная", "миллионных", "миллионных", Genus.FEMININE),
    Names("десятимиллионная", "десятимиллионных", "десятимиллионных", Genus.FEMININE),
    Names("стомиллионная", "стомиллионных", "стомиллионных", Genus.FEMININE),
    Names("миллиардная", "миллиардных", "миллиардных", Genus.FEMININE),
    Names("десятимиллиардная", "десятимиллиардных", "десятимиллиардных", Genus.FEMININE),
    Names("стомиллиардная", "стомиллиардных", "стомиллиардных", Genus.FEMININE),
)
