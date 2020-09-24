
'''
Basic arithmetic operations
'''
from io import IncrementalNewlineDecoder
import operator
from typing import NamedTuple

class Operator(object):

    def __init__(self,opcode="",desc="",num_params=None):
        self.opcode = opcode
        self.desc = desc
        self.num_params = num_params

    def __call__(self, *args):
        pass

class Add(Operator):

    def __call__(self, a1, a2):
        res, error = operator.add(a1,a2), None
        return res, error

class Sub(Operator):

    def __call__(self, a1, a2):
        res, error = operator.sub(a1, a2), None
        return res, error

class Div(Operator):

    def __call__(self, a1, a2):
        res, error = None, None
        if a2 == 0:
            error = "Division by zero"
            return res, error
        res = a1 / a2
        return res if not res.is_integer() else int(res), error

class Mul(Operator):

    def __call__(self, a1, a2):
        res, error = operator.mul(a1, a2), None
        return res, error

# Comperison operators
class Greater(Operator):

    def __call__(self, x, y):
        return x > y, None

class Less(Operator):

    def __call__(self, x, y):
        return x < y, None

class Equal(Operator):
    def __call__(self, x,y):
        return x == y, None

class GreaterEqual(Operator):
    def __call__(self, x, y):
        return x >= y, None

class LessEqual(Operator):
    def __call__(self, x,y):
        return x <= y, None

class NotEqual(Operator):
    def __call__(self, x,y):
        return x != y, None

class Mod(Operator):
    def __call__(self, x, y):
        return x % y, None
    
class Increment(Operator):
    def __call__(self, x):
        return x+1, None

class Decrement(Operator):
    def __call__(self, x):
        return x-1, None

# Bitwise operators
_is = isinstance
class And(Operator):
    def __call__(self, x, y):
        res, err = None, None
        if _is(x, int) and _is(y, int):
            return y & x, err
        return res, f"operand(s) must be type(s) of 'int'"

class Or(Operator):
    def __call__(self, x, y):
        res, err = None, None
        if _is(x, int) and _is(y, int):
            return x | y, None
        return res, f"operand(s) must be type(s) of 'int'"

class Xor(Operator):
    def __call__(self, x, y):
        res, err = None, None
        if _is(x, int) and _is(y, int):
            return x ^ y, None
        return res, f"operand(s) must be type(s) of 'int'" 

class Not(Operator):
    def __call__(self, x):
        res, err = None, None
        if _is(x, int):
            return ~x, None
        return res, f"operand(s) must be type(s) of 'int'" 

class RightShift(Operator):
    def __call__(self, x, y):
        res, err = None, None
        if _is(x, int) and _is(y, int):
            return x >> y, None
        return res, f"operand(s) must be type(s) of 'int'" 

class LeftShift(Operator):
    def __call__(self, x, y):
        res, err = None, None
        if _is(x, int) and _is(y, int):
            return x << y, None
        return res, f"operand(s) must be type(s) of 'int'" 

basic_operators = [
    # arithmetic operators
    Add(opcode="+", desc="addition",num_params=2),
    Sub(opcode="-",desc="subtraction",num_params=2),
    Mul(opcode="*", desc="multiplication", num_params=2),
    Div(opcode="/",desc="division",num_params=2),
    Mod(opcode="%", desc="Modulus", num_params=2),
    Increment(opcode="++", desc="Increment", num_params=1),
    Decrement(opcode="--", desc="Decrement", num_params=1),
    # comparison operators
    Greater(opcode=">",desc="Greater than",num_params=2),
    GreaterEqual(opcode=">=", desc="Greater than or equal", num_params=2),
    Less(opcode="<",desc="Less than", num_params=2),
    LessEqual(opcode="<=",desc="Less than or equal", num_params=2),
    NotEqual(opcode="!=", desc="Not equal", num_params=2),
    Equal(opcode="==", desc="Equal", num_params=2),
    # Bitwise operators
    And(opcode="&",desc="Bitwise AND", num_params=2),
    Or(opcode="|", desc="Bitwise OR", num_params=2),
    Xor(opcode="^",desc="Bitwise XOR", num_params=2),
    Not(opcode="~", desc="Bitwise NOT", num_params=1),
    RightShift(opcode=">>",desc="Bitwise shift right", num_params=2),
    LeftShift(opcode="<<", desc="Bitwise shift left", num_params=2)
    ]
