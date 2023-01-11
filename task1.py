from math import gcd

class Rational:
    def __init__(self, numerator: int, denominator: int):

        self.numerator = int(numerator / gcd(numerator, denominator))
        self.denominator = int(denominator / gcd(numerator, denominator))  

    def print_frac(self):
        print(self.numerator, '/', self.denominator, sep='')

    def print_float(self):
        print(self.numerator / self.denominator)

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        g = gcd(self.denominator, other.denominator)
        lcm = int(abs(self.denominator * other.denominator) / g)
        new_num = int(self.numerator * lcm/self.denominator + \
                  other.numerator * lcm / other.denominator)
        return Rational(new_num, lcm)

    def __sub__ (self, other):
        g = gcd(self.denominator, other.denominator)
        lcm = int(abs(self.denominator * other.denominator) / g)
        new_num = int(self.numerator * lcm/self.denominator - \
                  other.numerator * lcm / other.denominator)
        return Rational(new_num, lcm)

    def __mul__ (self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__ (self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        g = gcd(self.denominator, other.denominator)
        lcm = int(abs(self.denominator * other.denominator) / g)
        if  self.numerator == other.numerator and self.denominator == other.denominator:
            return '=='
        if  self.numerator * lcm/self.denominator >  other.numerator  * lcm/other.denominator:
            return '>'
        else:
            return '<'

