import pytest
from num2text_ru import Num2Text


INT_PARAMS = (
    (0, 'ноль'),
    (1, 'один'),
    (2, 'два'),
    (13, 'тринадцать'),
    (55, 'пятьдесят пять'),
    (732, 'семьсот тридцать два'),
    (5_825, 'пять тысяч восемьсот двадцать пять'),
    (12_311, 'двенадцать тысяч триста одиннадцать'),
    (105_001, 'сто пять тысяч один'),
    (1_432_899, 'один миллион четыреста тридцать две тысячи восемьсот девяносто девять'),
    (22_000_000, 'двадцать два миллиона'),
    (22_000_507_001, 'двадцать два миллиарда пятьсот семь тысяч один'),
    (32_000_007_000_001, 'тридцать два триллиона семь миллионов один'),
    (12_000_007_001_000_001, 'двенадцать квадриллионов семь миллиардов один миллион один'),
    (21_000_000_007_001_000_015, 'двадцать один квинтиллион семь миллиардов один миллион пятнадцать'),
)

FLOAT_PARAMS = (
    (1.2, 'одна целая две десятых'),
    (5.22, 'пять целых двадцать две сотых'),
    (12.121, 'двенадцать целых сто двадцать одна тысячная'),
    (21.3125, 'двадцать одна целая три тысячи сто двадцать пять десятитысячных'),
    (123.43122, 'сто двадцать три целых сорок три тысячи сто двадцать две стотысячных'),
    (0.431227, 'ноль целых четыреста тридцать одна тысяча двести двадцать семь миллионных'),
    (3.4312271, 'три целых четыре миллиона триста двенадцать тысяч двести семьдесят одна десятимиллионная'),
    (6.14312271, 'шесть целых четырнадцать миллионов триста двенадцать тысяч двести семьдесят одна стомиллионная'),
    (11.000000002, 'одиннадцать целых две миллиардных'),
    (13.0000000001, 'тринадцать целых одна десятимиллиардная'),
    (0.00000000001, 'ноль целых одна стомиллиардная'),
    (0.0, 'ноль целых ноль десятых')
)

STATIC_NDIGITS_PARAMS = (
    (1, 2, 'одна целая ноль сотых'),
    (1, 0, 'один'),
    (1.1, 3, 'одна целая сто тысячных'),
    (3.14, 1, 'три целых одна десятая'),
    (3.16, 1, 'три целых две десятых'),
    (3.1, 6, 'три целых сто тысяч миллионных'),
)


def ids(x):
    if isinstance(x, str):
        return 'i'
    return x


@pytest.mark.parametrize('number, expected', INT_PARAMS, ids=ids)
@pytest.mark.parametrize('value_type', (int, str))
@pytest.mark.parametrize('is_negative', (False, True))
def test_int_text(number, expected, value_type, is_negative):
    if is_negative:
        number = -number
    value = Num2Text(value_type(number))
    assert str(value) == f'{"минус " if number < 0 else ""}{expected}'


@pytest.mark.parametrize('number, expected', FLOAT_PARAMS, ids=ids)
@pytest.mark.parametrize('value_type', (float, str))
@pytest.mark.parametrize('is_negative', (False, True))
def test_float_text(number, expected, value_type, is_negative):
    if is_negative:
        number = -number
    value = Num2Text(value_type(number))
    assert str(value) == f'{"минус " if number < 0 else ""}{expected}'


@pytest.mark.parametrize('number, ndigits, expected', STATIC_NDIGITS_PARAMS, ids=ids)
def test_static_ndigits(number, ndigits, expected):
    value = Num2Text(number, ndigits=ndigits)
    assert str(value) == expected


def test_zero_ndigits():
    value = Num2Text(2.13, ndigits=0)
    assert str(value) == 'два'
    print(Num2Text(3.14))
