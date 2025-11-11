class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}{self.imag:+}i"

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def __add__(self, rhs):
        rhs = self.is_complex(rhs)
        return Complex(self.real + rhs.real,
                       self.imag + rhs.imag)

    def __radd__(self, rhs):
        return self.__add__(rhs)

    def __sub__(self, rhs):
        rhs = self.is_complex(rhs)
        return Complex(self.real - rhs.real,
                       self.imag - rhs.imag)

    def __rsub__(self, rhs):
        rhs = self.is_complex(rhs)
        return Complex(rhs.real - self.real,
                       rhs.imag - self.imag)

    def __mul__(self, rhs):
        rhs = self.is_complex(rhs)
        a, b = self.real, self.imag
        c, d = rhs.real, rhs.imag
        return Complex(a*c - b*d, a*d + b*c)

    def __rmul__(self, rhs):
        return self.__mul__(rhs)
    
    def is_complex(self, rhs):
        if not isinstance(rhs,Complex): 
            rhs = Complex(rhs,0)
            return rhs
        else:
            return rhs
