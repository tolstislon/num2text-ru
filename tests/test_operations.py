from decimal import Decimal

import pytest

from num2text_ru import Num2Text


@pytest.fixture(params=(Num2Text, Decimal, float))
def float_type(request):
    return request.param


@pytest.fixture(params=(Num2Text, int))
def int_type(request):
    return request.param


class TestNum2TextIntAdd:

    def test_num2text_int_add_num2text_int(self, int_type):
        assert str(Num2Text(1) + int_type(3)) == 'четыре'

    def test_num2text_int_add_num2text_float(self, float_type):
        assert str(Num2Text(1) + float_type(3.14)) == 'четыре целых четырнадцать сотых'


class TestNum2TextFloatAdd:

    def test_num2text_float_add_num2text_float(self, float_type):
        assert str(Num2Text(3.14) + float_type(0.15)) == 'три целых двадцать девять сотых'

    def test_num2text_float_add_num2text_int(self, int_type):
        assert str(Num2Text(3.14) + int_type(1)) == 'четыре целых четырнадцать сотых'


class TestNum2TextIntSubtract:

    def test_num2text_int_sub_num2text_int(self, int_type):
        assert str(Num2Text(3) - int_type(2)) == 'один'

    def test_num2text_int_sub_num2text_float(self, float_type):
        assert str(Num2Text(3) - float_type(1.5)) == 'одна целая пять десятых'


class TestNum2TextFloatSubtract:

    def test_num2text_float_sub_num2text_float(self, float_type):
        assert str(Num2Text(3.1) - float_type(1.5)) == 'одна целая шесть десятых'

    def test_name2text_float_sub_num2text_int(self, int_type):
        assert str(Num2Text(3.1) - int_type(3)) == 'ноль целых одна десятая'


class TestNum2TextIntMultiplication:

    def test_num2text_int_mul_num2text_int(self, int_type):
        assert str(Num2Text(2) * int_type(2)) == 'четыре'

    def test_num2text_int_mul_num2text_float(self, float_type):
        assert str(Num2Text(2) * float_type(1.5)) == 'три целых ноль десятых'


class TestNum2TextFloatMultiplication:

    def test_num2text_float_mul_num2text_float(self, float_type):
        assert str(Num2Text(2.1) * float_type(1.2)) == 'две целых пятьдесят две сотых'

    def test_num2text_float_mul_num2text_int(self, int_type):
        assert str(Num2Text(2.1) * int_type(2)) == 'четыре целых две десятых'


class TestNum2TextIntDivision:

    def test_num2text_int_div_num2text_int(self, int_type):
        assert str(Num2Text(5) / int_type(2)) == 'две целых пять десятых'

    def test_num2text_int_div_num2text_float(self, float_type):
        assert str(Num2Text(5) / float_type(2.5)) == 'две целых ноль десятых'


class TestNum2TextFloatDivision:

    def test_num2text_float_div_num2text_float(self, float_type):
        assert str(Num2Text(5.1) / float_type(1.2)) == 'четыре целых двадцать пять сотых'

    def test_num2text_float_div_num2text_int(self, int_type):
        assert str(Num2Text(5.2) / int_type(2)) == 'две целых шесть десятых'


class TestNum2TextIntFloorDiv:

    def test_num2text_int_floor_div_num2text_int(self, int_type):
        assert str(Num2Text(3) // int_type(2)) == 'один'

    def test_num2text_int_floor_div_num2text_float(self, float_type):
        assert str(Num2Text(3) // float_type(1.1)) == 'две целых ноль десятых'


class TestNum2TextFloatFloorDiv:

    def test_num2text_float_div_num2text_float(self, float_type):
        assert str(Num2Text(5.1) // float_type(1.2)) == 'четыре целых ноль десятых'

    def test_num2text_float_div_num2text_int(self, int_type):
        assert str(Num2Text(5.2) // int_type(2)) == 'две целых ноль десятых'


class TestNum2TextIntMod:

    def test_num2text_int_mod_num2text_int(self, int_type):
        assert str(Num2Text(5) % int_type(3)) == 'два'

    def test_num2text_int_mod_num2text_float(self, float_type):
        assert str(Num2Text(3) % float_type(2.5)) == 'ноль целых пять десятых'


class TestNum2TextFloatMod:

    def test_num2text_float_mod_num2text_float(self, float_type):
        assert str(Num2Text(5.5) % float_type(1.5)) == 'одна целая ноль десятых'

    def test_num2text_float_mod_num2text_int(self, int_type):
        assert str(Num2Text(5.2) % int_type(3)) == 'две целых две десятых'


class TestNum2TextIntPow:

    def test_num2text_int_pow_num2text_int(self, int_type):
        assert str(Num2Text(5) ** int_type(3)) == 'сто двадцать пять'

    def test_num2text_int_pow_num2text_float(self, float_type):
        assert str(Num2Text(5) ** float_type(2.0)) == 'двадцать пять целых ноль десятых'


class TestNum2TextFloatPow:

    def test_num2text_float_pow_num2text_float(self, float_type):
        assert str(Num2Text(5.5) ** float_type(2.0)) == 'тридцать целых двадцать пять сотых'

    def test_num2text_float_pow_num2text_int(self, int_type):
        assert str(Num2Text(5.2) ** int_type(3)) == 'сто сорок целых шестьсот восемь тысячных'


class TestNum2TextBool:

    @pytest.mark.parametrize('value', (1, 1, 1, -120.1))
    def test_num2text_bool_true(self, value):
        assert Num2Text(value)

    @pytest.mark.parametrize('value', (0, 0.0))
    def test_num2text_bool_false(self, value):
        assert not Num2Text(value)


class TestNum2TextCompare:

    def test_num2text_lt(self):
        assert Num2Text(1.2) > Num2Text(1)

    def test_num2text_lt_neg(self):
        assert not Num2Text(1.2) < Num2Text(1)

    @pytest.mark.parametrize('value', (1, 1.2))
    def test_num2text_le(self, value):
        assert Num2Text(value) >= Num2Text(1)

    def test_num2text_le_neg(self):
        assert not Num2Text(1.2) <= Num2Text(1)

    def test_num2text_eq(self):
        assert Num2Text(1.0) == Num2Text(1)

    def test_num2text_eq_neg(self):
        assert not Num2Text(1.1) == Num2Text(1)

    def test_num2text_ne(self):
        assert Num2Text(1.1) != Num2Text(1)

    def test_num2text_ne_neg(self):
        assert not Num2Text(1.0) != Num2Text(1)
