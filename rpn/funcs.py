'''
This module containts implementations of 
trigonometric, mathematical functions,
 as well as numeric utilities.

'''

from math import atan, cosh
from os import terminal_size
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
        return math.log(x, base), err

Ln = Log

class Pow(Operator):
    def __call__(self, x, y):
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
class Round(Operator):
    def __call__(self, number, ndigits=None):
        '''Round a number to a given precision in decimal digits.
            
            The return value is an integer if ndigits is omitted or None.  Otherwise
            the return value has the same type as the number.  ndigits may be negative.
        '''
        res, err = None, None
        try:
            res = round(number=number, ndigits=ndigits)
        except Exception as e:
            return None, e
        return res, err

Roundn = Round

class Ceil(Operator):
    def __call__(self, x):
        ''' Return the ceiling of x as an Integral.
            This is the smallest integer >= x.
        '''
        res, err = None, None
        try:
            res = math.ceil(x)
        except Exception as e:
            return res,e
        return res, err

class Floor(Operator):
    def __call__(self, x):
        '''Return the floor of x as an Integral.
            This is the largest integer <= x.
        '''
        res, err = None, None
        try:
            res = math.floor(x)
        except Exception as e:
            return res,e
        return res, err


class Abs(Operator):
    def __call__(self, x):
        '''Return the absolute value of the argument.'''
        res, err = None, None
        try:
            res = abs(x)
        except Exception as e:
            return res,e
        return res, err

class Min(Operator):
    def __call__(self, x, y):
        '''Returns the lowest of x or y	'''
        res, err = None, None
        try:
            res = min([x,y])
        except Exception as e:
            return res,e
        return res, err

class Max(Operator):
    def __call__(self, x, y):
        '''Returns the heighest  of x or y	'''
        res, err = None, None
        try:
            res = max([x,y])
        except Exception as e:
            return res,e
        return res, err

class Modf(Operator):
    def __init__(self, ip=False, fp=False,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.fp = fp

    def __call__(self, x):
        '''Returns fractional and integral parts of x.
            Result carry sign of x and both are float 
        '''
        res, err = None, None
        try:
            res = math.modf(x)
        except Exception as e:
            return res, e
        
        if self.ip is True:
            return res[1], err
        if self.fp is True:
            return res[0], err
        return res, err


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
    # Numeric utilities
    Round(opcode="round", desc="Round the number to ceiling", num_params=1),
    Roundn(opcode="roundn", desc="Round the number to a given precision", num_params=2),
    Modf(ip=True,opcode="ip", desc="Integral part",num_params=1),
    Modf(fp=True,opcode="fp", desc="Floating part",num_params=1),
    Ceil(opcode="ceil", desc="Ceiling", num_params=1),
    Floor(opcode="floor", desc="Floor", num_params=1),
    Abs(opcode="abs", desc="Absolute value", num_params=1),
    Min(opcode="min", desc="Minimum of two number", num_params=2),
    Max(opcode="max", desc="Maximum", num_params=2)

]
