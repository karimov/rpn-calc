
'''
Basic arithmetic operations
'''
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
        res, error = operator.add(a2,a1), None
        return res, error

class Sub(Operator):

    def __call__(self, a1, a2):
        res, error = operator.sub(a2, a1), None
        return res, error

class Div(Operator):

    def __call__(self, a1, a2):
        res, error = None, None
        if a1 == 0:
            error = "Division by zero"
            return res, error
        res = a2 / a1
        return res if not res.is_integer() else int(res), error

class Mul(Operator):

    def __call__(self, a1, a2):
        res, error = operator.mul(a2, a1), None
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

basic_operators = [
    # arithmetic operators
    Add(opcode="+", desc="addition",num_params=2),
    Sub(opcode="-",desc="subtraction",num_params=2),
    Mul(opcode="*", desc="multiplication", num_params=2),
    Div(opcode="/",desc="division",num_params=2),
    # comparison operators
    Greater(opcode=">",desc="Greater than",num_params=2),
    GreaterEqual(opcode=">=", desc="Greater than or equal", num_params=2),
    Less(opcode="<",desc="Less than", num_params=2),
    LessEqual(opcode="<=",desc="Less than or equal", num_params=2),
    NotEqual(opcode="!=", desc="Not equal", num_params=2),
    Equal(opcode="==", desc="Equal", num_params=2)
    ]
