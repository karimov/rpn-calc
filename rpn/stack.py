
class Command(object):

    def __init__(self, opcode, desc, num_params):
        self.opcode = opcode
        self.desc = desc
        self.num_params = num_params

    def __call__(self):
        pass

class Stack(object):

    def __init__(self):
        self._stack = []
        self._commands = {"pick":(self.pick,1),
                            "dup": (self.dup, 0),
                            "dupn": (self.dupn,1),
                            "drop": (self.drop,0),
                            "dropn":(self.dropn,1),
                            "swap":(self.swap,0),
                            "roll": (self.roll, 1),
                            "rolld":(self.rolld,1)}

    def append(self, value):
        self._stack.append(value)

    def pop(self, n=-1):
        return self._stack.pop(n)

    def extend(self, alist):
        self._stack.extend(alist)

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def __iter__(self):
        return iter(self._stack)

    def add_command(self, command):
        self._commands[command.opcode] = command

    def run_command(self, cmd):
        num_params = self._commands[cmd][1]
        func = self._commands[cmd][0]
        if num_params > 0:
            args = self._stack[len(self)-num_params]
            res, err = func(args)
            return res, err
        res, err = func()
        return res, err

    def popn(self, n=1):
        '''
            Return generator function of n elements
        '''
        i = 0
        while i < n:
            yield self._stack.pop()
            i += 1

    def read_stack(self, n=1):
        '''
        Returns n elements of stack
        '''
        return self._stack[:n]

    def clear_stack(self):
        '''
        Removes all elements of stack
        '''
        self._stack = []

    def peak(self):
        if len(self) > 0:
            return self._stack[-1]
        return None

    def pick(self, n): # TDO: fix to pick right item
        res, err = None, None
        if len(self) >= n: # [1 2 3 4 5] l=5, n=3 return 3
            top = self.peak()
            if isinstance(top, int):
                return self._stack[len(self)-n],  err
            return res, err
        return res, f"{n}: out of stack size"

    def drop(self):
        res, err = None, None
        if len(self) > 0:
            return self.pop(), None
        return None, f"Stack is empty"

    def dropn(self, n):
        if len(self) > n:
            top = self._stack[-1]
            if isinstance(top, int):
                self._stack = self._stack[:len(self)-n-1]
            return None, None
        return None, f"{n}: out of stack size"

    def dup(self):
        if len(self) > 0:
            top = self._stack[len(self)-1]
            self.append(top)
            return None, None
        return None, f"Stack is empty"

    def dupn(self, n): # TODO: fix to duplicate right items
        if len(self) >= n:
            if isinstance(n, int):
                top_n = self._stack[len(self)-n:]
                self._stack.extend(top_n)
            return None, None
        return None, f"{n}: out of stack size"

    def roll(self, n):
        res, err = None, None
        if n < 0:
            return self.rolld(-n)
        if not isinstance(n, int):
            return res, err
        i = 0
        while i < n:
            top = self._stack.pop()
            self._stack.insert(0, top)
            i += 1
        return res, err

    def rolld(self, n): # TODO: fix to right rotation
        res, err = None, None
        if n < 0:
            return self.roll(-n)
        if not isinstance(n, int):
            return res, err
        i = 0
        while i < n:
            bottom = self._stack.pop(0)
            self._stack.append(bottom)
            i += 1

        return res, err

    def swap(self):
        res, err = None, None
        if len(self) >= 2:
            i, j = len(self)-1, len(self)-2
            self._stack[i], self._stack[j] = self._stack[j], self._stack[i]
            return res, err
        return res, err


"""
Stack control:
  -  Stack Manipulation commands

      ☐ pick       Pick the -n'th item from the stack
      ☐ repeat     Repeat an operation n times, e.g. '3 repeat +'
      ☐ depth      Push the current stack depth
      ☐ drop       Drops the top item from the stack
      ☐ dropn      Drops n items from the stack
      ☐ dup        Duplicates the top stack item
      ☐ dupn       Duplicates the top n stack items in order
      ☐ roll       Roll the stack upwards by n
      ☐ rolld      Roll the stack downwards by n
      ☐ stack      Toggles stack display from horizontal to vertical
      ☐ swap       Swap the top 2 stack items

"""
