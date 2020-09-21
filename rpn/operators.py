
'''
Basic arithmetic operations
'''
import operator

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


basic_operators = [
    Add(opcode="+", desc="addition",num_params=2),
    Sub(opcode="-",desc="subtraction",num_params=2),
    Mul(opcode="*", desc="multiplication", num_params=2),
    Div(opcode="/",desc="division",num_params=2),
    ]
