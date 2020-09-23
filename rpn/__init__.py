"""
Module level details

In this module, very basics of rpncalc operations are planed to implement
* Arithmetics
* Stack manipulation
* Display modes
"""
import sys
from .operators import basic_operators, Operator
from.stack import Stack #Command
from .utility import display, ColorsSet, banner

class RpnCalc(object):
    """"
    RpnCalc: doc string
    TODO: process till last token bypassing unknown tokens
    """
    def __init__(self):
        '''Initializes empty stack to start off'''
        self.stack = Stack()
        self._operators = {op.opcode:op for op in basic_operators}
        self.display_mode = 'dec'
        self._macros = {}
        self._register = {}

    def set_display_mode(self, mode):
        '''Setup display mode'''
        self.display_mode = mode # TODO: check if such mode supported

    def add_operator(self, operator):
        '''
        Adding new operator'
        May override existing operator wit same opcode
        '''
        self._operators[operator.opcode] = operator

    def parser(self, expression):
        '''New parse takes care of special case with some stack commands'''
        cmd_list = []
        last_num = None
        tokens_list = expression.strip().split()
        i = 0
        n = len(tokens_list)
        while i < n:
            token = tokens_list[i]
            number, err = RpnCalc.convert(token)
            if err is False:
                cmd_list.append(number)
            elif token == "repeat": # Handle special case
                if n < 3:
                    i += 1
                    continue
                last_cmd = cmd_list[-1]
                if isinstance(last_cmd, int) and i+1 < n:
                    next_token = tokens_list[i+1]
                    num, err = RpnCalc.convert(next_token)
                    if err is False:
                        cmd_list.pop()
                        cmd_list.extend([num]*last_cmd)
                        i += 1
                    else:
                        cmd_list.pop()
                        cmd_list.extend([next_token]*last_cmd)
                        i += 1
                else:
                    i += 1
                    continue
            elif token == "macro":
                 macro = self.parser(" ".join(tokens_list[i+1:]))
                 var_name = macro[0]
                 self._macros[var_name] = macro[1:]
                 break
            else:
                cmd_list.append(tokens_list[i])
            i += 1

        return cmd_list

    def evaluate(self, commands):
        '''Push to stack and pop results'''
        for cmd in commands:
            res, err = self.run_command(cmd)
            if err is not None:
                display(err, bg=ColorsSet.Yellow) # TODO: change the way of printing the result
            if res is not None:
                display(res, bg=ColorsSet.Green)

    def run_command(self, cmd): # TODO: checkout chain of responsibilities pattern
        res, err = None, None
        if isinstance(cmd, (float, int)):
            self.stack.append(cmd)
            return res, err

        elif cmd in ["dec","hex","bin","ocd"]:
            self.set_display_mode(mode=cmd)

        elif cmd == "r":
            display(self._register)
            return res, err
        elif cmd == "m":
            display(self._macros)
            return res, err
        elif cmd in self._macros:
            macro_cmds = self._macros[cmd]
            self.evaluate(macro_cmds)
            return res, err
        elif cmd in self._register:
            val = self._register[cmd]
            self.run_command(val)
            return res, err
        elif cmd == "quit":
            sys.exit(0)
        elif cmd == "repeat":
            return res, f"Takes two arguments"
        elif cmd.endswith("=") and cmd[:-1].isalpha():
            if len(self.stack) < 0:
                return res, f"Not enough elements in the stack"
            val = self.stack.pop()
            self._register[cmd[:-1]] = val
            return res, err
        elif cmd in self.stack._commands:
            res, err = self.stack.run_command(cmd)
            return res, err
        elif cmd not in self._operators:
            return res, f"Unknown operator: {cmd}"
        elif cmd in self._operators:
            op = self._operators[cmd]
            if len(self.stack) < op.num_params:
                return res, f"Not enough elements in the stack"
            args = list(self.stack.popn(n=op.num_params))
            res, err = op(*args)
            if err is not None or type(res) is bool:
                self.stack.extend(args[::-1])
                return res, err
            self.stack.append(res) # TODO: res is vector value

        return res, err

    def run(self): # TODO: must be decoupled
        banner("Welcome rpn v0.1 interactive mode")
        banner("rpn is a simple app of rpn calculator.")
        banner("type 'help' for more information.")
        banner("type 'quit' to exit.")
        while True:
            try:
                commands = self.parser(input("> "))
                self.evaluate(commands)
                if len(self._register) > 0:
                    display(self._register, "register",bg=ColorsSet.BrightBlue,bracket="[]")
                display(self.stack, 'stack', bg=ColorsSet.BrightWhite,mode=self.display_mode)
            except KeyboardInterrupt:
                sys.exit(1)

    @staticmethod
    def convert(token): # TODO: complex numbers
        """
            Convert numeric elements (include hex, bin literals) to float or integer if possible.
            value, error = convert(token)
            If token can be converted into a number, return error = False and the
            converted value in value. Otherwise return error = True, and value
            contains the input argument.
        """
        try:
            if token.startswith("0x"):
                number = int(token, 16)
            elif token.startswith("0b"):
                number = int(token, 2)
            else:
                number = int(token)
            return number, False
        except:
            pass

        try:
            number = float(token)
            return number, False
        except:
            return token, True
