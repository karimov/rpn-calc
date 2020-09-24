'''
This module containts implementations of 
trigonometric, mathematical functions,
 as well as numeric utilities.

'''

from math import atan, cosh
from .operators import Operator

import math

# Trigonometric operators
class Cos(Operator):
    def __call__(self, x):
        '''Return the cosine of x (measured in radians)'''
        return math.cos(x), None

class Sin(Operator):
    def __call__(self, x):
        '''Return the sine of x (measured in radians)'''
        return math.sin(x), None

class Tan(Operator):
    def __call__(self, x):
        '''Return the tangent of x (measured in radians)'''
        return math.tan(x), None

class Acos(Operator):
    def __call__(self, x):
        '''Return the arccosine of x (measured in radians)'''
        res, err = None, None
        if not (-1 <= x <= 1):
            return res, "value error"
        return math.acos(x), err

class Asin(Operator):
    def __call__(self, x):
        '''Return the arcsine of x (measured in radians)'''
        res, err = None, None
        if not (-1 <= x <= 1):
            return res, "value error"
        return math.asin(x), err

class Atan(Operator):
    def __call__(self, x):
        '''Return the arctangent of x (measured in radians)'''
        return math.atan(x), None

class Cosh(Operator):
    def __call__(self, x):
        '''Return the hyperbolic cosine of x.'''
        res, err = None, None
        return math.cosh(x), err

class Sinh(Operator):
    def __call__(self, x):
        '''Return the hyperbolic sine of x.'''
        res, err = None, None
        return math.sinh(x), err

class Tanh(Operator):
    def __call__(self, x):
        '''Return the hyperbolic tangent of x.'''
        res, err = None, None
        return math.tanh(x), err

# Mathematical operators
class Exp(Operator):
    def __call__(self, x):
        '''Return e raised to the power of x.'''
        res, err = None, None
        if not (-999999 <= x <= 709):
            return res, "x out of range"
        return math.exp(x), err

class Fact(Operator):
    def __call__(self, x):
        '''Find x!.
            Raise a ValueError if x is negative or non-integral.
        '''
        res, err = None, None
        if x < 0:
            return res, "x cannot be negative value"
        if not isinstance(x, int):
            return res, "x must be integral value"
        return math.factorial(x), err

class Sqrt(Operator):
    def __call__(self, x):
        '''Return the square root of x.'''
        res, err = None, None
        if not x > 0:
            return res, "x must be positive number"
        return math.sqrt(x), err

class Log(Operator):
    def __call__(self, x, base=math.e):
        '''log(x, [base=math.e])
            Return the logarithm of x to the given base.

            If the base not specified, returns the natural logarithm (base e) of x.
        '''
        res, err = None, None
        if not (x > 0 and base > 0):
            return res, "x and base must be > 0"
        if base != math.e:
            x, base = base, x
        return math.log(x, base), err

Ln = Log

class Pow(Operator):
    def __call__(self, y, x):
        ''' Returns x**y (x to the power of y) '''
        return x**y, None


# Numeric utilities
'''
   Numeric Utilities

      ceil       Ceiling
      floor      Floor
      round      Round
      ip         Integer part
      fp         Floating part
      sign       Push -1, 0, or 0 depending on the sign
      abs        Absolute value
      max        Max
      min        Min
'''
# class Round(operators):
#     def __call__(self, number, ndigits=None):
#         '''Round a number to a given precision in decimal digits.
            
#             The return value is an integer if ndigits is omitted or None.  Otherwise
#             the return value has the same type as the number.  ndigits may be negative.
#         '''
#         res, err = None, None            




functional_operators = [
    # Trigonometric operators
    Cos(opcode="cos", desc="Cosine",num_params=1),
    Sin(opcode="sin", desc="Sine", num_params=1),
    Tan(opcode="tan", desc="Tangent", num_params=1),
    Acos(opcode="acos",desc="Arc Cosine", num_params=1),
    Asin(opcode="asin", desc="Arc sine", num_params=1),
    Atan(opcode="atan",desc="Arc tangent", num_params=1),
    Cosh(opcode="cosh", desc="Hyperbolic Cosine", num_params=1),
    Sinh(opcode="sinh", desc="Hyperbolic Sine", num_params=1),
    Tanh(opcode="tanh", desc="Hyperbolic tangent", num_params=1),
    # Mathematical operators
    Exp(opcode="exp",desc="Exponentiation",num_params=1),
    Fact(opcode="fact", desc="Factorial", num_params=1),
    Sqrt(opcode="sqrt", desc="Square Root", num_params=1),
    Ln(opcode="ln", desc="Natural logarithm",num_params=1),
    Log(opcode="log", desc="Logarithm", num_params=2),
    Pow(opcode="pow", desc="Raise a number to a power", num_params=2),
]
