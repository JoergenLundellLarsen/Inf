
from Complex import Complex


def almost_equal(a, b, eps=1e-9):
    return abs(a - b) < eps


def test_constructor():
    z = Complex()
    assert z.real == 0, "Default real should be 0"
    assert z.imag == 0, "Default imag should be 0"

    z2 = Complex(3, -2)
    assert z2.real == 3
    assert z2.imag == -2


def test_str_repr():
    z = Complex(1, 2)
    assert str(z) == "1+2i"
    assert repr(z) == "Complex(1, 2)"

    z = Complex(3, -4)
    assert str(z) == "3-4i"


def test_addition():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)
    r = z1 + z2
    assert r.real == 4
    assert r.imag == 6

    # blandet med int
    r2 = z1 + 5
    assert r2.real == 6
    assert r2.imag == 2

    r3 = 5 + z1
    assert r3.real == 6
    assert r3.imag == 2


def test_subtraction():
    z1 = Complex(5, 3)
    z2 = Complex(2, 1)
    r = z1 - z2
    assert r.real == 3
    assert r.imag == 2

    r2 = 10 - z1
    assert r2.real == 5
    assert r2.imag == -3


def test_multiplication():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)

    r = z1 * z2
    c = complex(1, 2) * complex(3, 4)

    assert almost_equal(r.real, c.real)
    assert almost_equal(r.imag, c.imag)

    # med int
    r2 = z1 * 3
    assert r2.real == 3
    assert r2.imag == 6


def test_is_complex():
    z = Complex(1, 2)

    c1 = z.is_complex(5)
    assert c1.real == 5 and c1.imag == 0

    c2 = z.is_complex(Complex(4, -1))
    assert c2.real == 4 and c2.imag == -1


def run_all_tests():
    print("Running tests...")

    test_constructor()
    print(" constructor OK")

    test_str_repr()
    print(" str/repr OK")

    test_addition()
    print(" addition OK")

    test_subtraction()
    print(" subtraction OK")

    test_multiplication()
    print(" multiplication OK")

    test_is_complex()
    print(" is_complex OK")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_all_tests()
