# test_complex.py
import pytest
from complex import Complex


def test_default_constructor():
    z = Complex()
    assert z.real == 0
    assert z.imag == 0


def test_constructor_values():
    z = Complex(3, -4)
    assert z.real == 3
    assert z.imag == -4


def test_str_format():
    z = Complex(1, 2)
    assert str(z) == "1+2i"
    z = Complex(1, -2)
    assert str(z) == "1-2i"


def test_repr_format():
    z = Complex(1, 2)
    assert repr(z) == "Complex(1, 2)"


def test_add_complex():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)
    res = z1 + z2
    assert res.real == 4
    assert res.imag == 6


def test_add_int_right_and_left():
    z = Complex(1, 2)
    res1 = z + 3 #her tester vi høyre og venstre side med ikke komplekse tall.
    res2 = 3 + z
    assert res1.real == 4 and res1.imag == 2
    assert res2.real == 4 and res2.imag == 2


def test_sub_complex():
    z1 = Complex(1, 2)
    z2 = Complex(3, 5)
    res = z1 - z2
    assert res.real == -2
    assert res.imag == -3


def test_rsub_int_minus_complex():
    z = Complex(1, 2)
    res = 5 - z       # bruker __rsub__
    assert res.real == 4
    assert res.imag == -2


def test_mul_complex():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)
    res = z1 * z2
    # fasit fra innebygd complex
    c = complex(1, 2) * complex(3, 4)
    assert res.real == pytest.approx(c.real)
    assert res.imag == pytest.approx(c.imag)


def test_mul_int_right_and_left():
    z = Complex(1, -2)
    res1 = z * 3
    res2 = 3 * z
    assert res1.real == 3 and res1.imag == -6
    assert res2.real == 3 and res2.imag == -6


def test_is_complex_helper_with_int():
    z = Complex(1, 2)
    rhs = z.is_complex(5)
    assert isinstance(rhs, Complex)
    assert rhs.real == 5
    assert rhs.imag == 0


def test_is_complex_helper_with_complex():
    z = Complex(1, 2)
    rhs = z.is_complex(Complex(3, 4))
    assert isinstance(rhs, Complex)
    assert rhs.real == 3
    assert rhs.imag == 4
