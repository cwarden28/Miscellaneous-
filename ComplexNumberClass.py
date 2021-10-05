import numpy as np
import math

class Complex(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        if self.im == 0:
            result = "%.2f+0.00i" % (self.re)
        elif self.re == 0:
            if self.im >= 0:
                result = "0.00+%.2fi" % (self.im)
            else:
                result = "0.00-%.2fi" % (abs(self.im))
        elif self.im > 0:
            result = "%.2f+%.2fi" % (self.re, self.im)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.im))
        return result
    def getRe(self):
        return self.re
    def getIm(self):
        return self.im
    def __add__(self, other):
        re_new = self.re + other.re
        im_new = self.im + other.im
        return Complex(re_new, im_new)
    def __sub__(self, other):
        re_new = self.re - other.re
        im_new = self.im - other.im
        return Complex(re_new, im_new)
    def __mul__(self, other):
        re_new = (self.re*other.re) - (self.im*other.im)
        im_new = (self.re*other.im) + (other.re*self.im)
        return Complex(re_new, im_new)
    def conjugate(self):
        return Complex(self.re, -1*self.im)
    def __truediv__(self, other):
        numerator = Complex.__mul__(self, Complex.conjugate(other))
        denominator = (other.re*Complex.conjugate(other).re) + (-1*other.im*Complex.conjugate(other).im)
        re_new = numerator.re/denominator
        im_new = numerator.im/denominator
        return Complex(re_new, im_new)
    def mod(self):
        r = math.sqrt(self.re ** 2 + self.im ** 2)
        return str('{:.2f}'.format(r) + '+' + "0.00i")

# Example
ct = Complex(4, 5)
dt = Complex(2, 3)

print(ct+dt,'\n',ct-dt,'\n',ct*dt,'\n',ct/dt, \
      '\n',Complex.mod(ct),'\n',Complex.mod(dt))
