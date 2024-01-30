import re
from abc import ABCMeta, abstractmethod
from decimal import Decimal
from typing import List, Optional, Tuple, Union

from .values import HUNDREDS, MINUS, NAMES_OF_DECIMALS, NAMES_OF_DEGREES, TEENS, TENS, UNITS
from .enums import Genus, Plural
from .exceptions import (
    InvalidNumberException, LargeNumberException, NumberTooBigException,
    ValueIsNotANumber,
)
from .types import Names


def converts_numbers(rest: int, genus: Genus) -> Tuple[Plural, List[str]]:
    """Converts numbers"""
    prev = 0
    plural = Plural.GENITIVE
    name = []
    use_teens = 10 <= rest % 100 <= 19
    data = ((TEENS, 10), (HUNDREDS, 1000)) if use_teens else ((UNITS, 10), (TENS, 100), (HUNDREDS, 1000))
    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x
        if x == 10 and use_teens:
            plural = Plural.GENITIVE
            name.append(TEENS[cur].get(genus))
        elif cur == 0:
            continue
        elif x == 10:
            name.append(names[cur].get(genus))
            if 2 <= cur <= 4:
                plural = Plural.PLURAL
            elif cur == 1:
                plural = Plural.SINGULAR
            else:
                plural = Plural.GENITIVE
        else:
            name.append(names[cur - 1].get(genus))
    return plural, name


def int2text(num: int, name: Names) -> str:
    if num == 0:
        return f"{UNITS[0].get(name.genus)} {name.genitive}"
    rest = abs(num)
    if rest >= 10 ** 20:
        raise NumberTooBigException()
    count = 0
    words = []
    values = (name, *NAMES_OF_DEGREES)
    while rest > 0:
        plural, nme = converts_numbers(rest % 1000, values[count].genus)
        rest = int(rest / 1000)
        if count == 0:
            words.append(name.get(plural))
        if nme and count > 0:
            if len(NAMES_OF_DEGREES) < count:
                raise LargeNumberException()
            words.append(NAMES_OF_DEGREES[count - 1].get(plural))
        words.extend(nme)
        count += 1
    words.reverse()
    return " ".join(words).strip()


def orix(value) -> Union[int, float, Decimal]:
    if isinstance(value, (int, float, Decimal)):
        return value
    if isinstance(value, str):
        value = value.replace(",", ".")
        if re.match(r"^-?\d+$", value):
            return int(value)
        elif re.match(r"^-?\d+\.\d+$", value):
            return float(value)
        else:
            try:
                return float(value)
            except ValueError:
                pass
    raise ValueIsNotANumber(value)


def find_ndigits(value) -> int:
    if match := re.match(r"^-?\d+\.([0-9]*[1-9])(0*)$", f"{value:.11f}"):
        return len(match.group(1))
    return 0


def get_values(value: Union[int, float, Decimal, str]) -> Tuple[Union[int, Decimal], int]:
    value = orix(value)
    if isinstance(value, int):
        return value, 0
    else:
        ndigits = find_ndigits(value)
        number = Decimal(value)
        quantize = Decimal(10) ** -ndigits
        return number.quantize(quantize), ndigits


def minus(value: Union[int, float, Decimal], string: str) -> str:
    if value < 0:
        return f"{MINUS} {string.strip()}"
    return string.strip()


def num2text(num: Union[int, float, Decimal], names: Union[Names, Tuple[Names, ...]], ndigits: int = 2) -> str:
    if isinstance(names, Names):
        names = (names,)
    if isinstance(num, int):
        return minus(num, int2text(num, names[0]))
    if isinstance(num, (float, Decimal)):
        value = f"{num:.{ndigits or 1}f}"
        data = value.split(".")
        if len(data) == 1:
            return minus(num, int2text(int(num), names[0]))
        integral, exp = data
        return minus(num, f"{int2text(int(integral), names[0])} {int2text(int(exp), names[1])}")
    raise InvalidNumberException(num)


class MetaNum2Text(metaclass=ABCMeta):
    ndigits: int = 0
    names = (Names("", "", "", Genus.MASCULINE),)

    @abstractmethod
    def _process(self) -> str: ...

    def __init__(self, value: Union[int, float, Decimal, str], ndigits: Optional[int] = None):
        self.value, _ndigits = get_values(value)
        self.ndigits = ndigits if ndigits is not None else _ndigits
        self.text: str = self._process()

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value})"

    def __add__(self, other):
        return Num2Text(self.value + Num2Text(other).value)

    def __sub__(self, other):
        return Num2Text(self.value - Num2Text(other).value)

    def __mul__(self, other):
        return Num2Text(self.value * Num2Text(other).value)

    def __truediv__(self, other):
        return Num2Text(self.value / Num2Text(other).value)

    def __floordiv__(self, other):
        return Num2Text(self.value // Num2Text(other).value)

    def __mod__(self, other):
        return Num2Text(self.value % Num2Text(other).value)

    def __pow__(self, power, modulo=None):
        return Num2Text(self.value ** Num2Text(power).value)

    def __bool__(self):
        return bool(self.value)

    def __lt__(self, other):
        return self.value < Num2Text(other).value

    def __le__(self, other):
        return self.value <= Num2Text(other).value

    def __eq__(self, other):
        return self.value == Num2Text(other).value


class Int2Text(MetaNum2Text):
    names = (Names("", "", "", Genus.MASCULINE),)
    ndigits = 0

    def __init__(self, value: Union[int, str]):
        super().__init__(value)

    def _process(self) -> str:
        return num2text(int(self.value), self.names, self.ndigits)


class Float2Text(MetaNum2Text):
    ndigits = None
    names: Tuple[Names, ...] = NAMES_OF_DECIMALS

    def _process(self) -> str:
        value = f"{self.value:.{self.ndigits or 1}f}"
        integral, exp = value.split(".")
        if len(exp) + 1 > len(self.names):
            raise LargeNumberException()
        return num2text(num=Decimal(self.value), names=(self.names[0], self.names[len(exp)]), ndigits=self.ndigits)


class Num2Text:

    def __new__(
        cls, value: Union[int, float, Decimal, str], ndigits: Optional[int] = None
    ) -> Union[Int2Text, Float2Text]:
        if isinstance(value, (Int2Text, Float2Text)):
            return value
        value = orix(value)
        if ndigits == 0 and isinstance(value, float):
            value = int(round(value, 0))
        return Int2Text(value) if isinstance(value, int) and not ndigits else Float2Text(value, ndigits=ndigits)
