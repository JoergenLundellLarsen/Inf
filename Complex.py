class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __mul__(self, rhs):
        #(a + bj)(c + dj) = (ac − bd) + (ad + bc)j
        rhs = self.check_if_complex(rhs) 
        a, b = self.real, self.imag
        c, d = rhs.real, rhs.imag
        return Complex(a*c - b*d, a*d + b*c)
    
    def __str__(self):
        return f"{self.real}{self.imag:+}i"
    
    def __add__(self, rhs):
        rhs = self.check_if_complex(rhs)
        a, b = self.real, self.imag
        c, d = rhs.real, rhs.imag
        return Complex(a+c, b+d)
    
    def __sub__(self, rhs):
        rhs = self.check_if_complex(rhs)
        a, b = self.real, self.imag
        c, d = rhs.real, rhs.imag
        return Complex(a-c, b-d)
    
    def __repr__(self):
        return f"Complex ({self.real},{self.imag})"
    
    def __eq__(self, rhs):
        return self.real == rhs.real and self.imag == rhs.imag
    
    def check_if_complex(self, value):
        if isinstance(value, Complex):
            return value
        elif isinstance(value, (int, float)):
            return Complex(value, 0)
