class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, rhs):
        #(a + bj)(c + dj) = (ac − bd) + (ad + bc)j
        a, b = self.real, self.imag
        c, d = rhs.real, rhs.imag
        return Complex(a*c - b*d, a*d + b*c)

    def __repr__(self):
        return f"{self.real} + {self.imag}j"

z1 = Complex(1, 2)
z2 = Complex(3, 4)
print(z1 * z2)
