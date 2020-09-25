import sys

class ColorsSet:
    Black = "\u001b[30m"
    Red ="\u001b[31m"
    Green ="\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"
    BrightBlue = "\u001b[34;1m"
    BrightYellow = "\u001b[33;1m"
    BrightWhite = "\u001b[37;1m"
    BrightGreen ="\u001b[32;1m"
    BrightRed ="\u001b[31;1m"
    BrightMagenta = "\u001b[35;1m"
    BrightCyan = "\u001b[36;1m"

class ColorSchema:
    STACK = ColorsSet.Blue
    REGISTER = ColorsSet.White
    MACRO = ColorsSet.Magenta
    WARNING = ColorsSet.Yellow
    FAIL = ColorsSet.Red
    ENDC = ColorsSet.Reset

def display(iterable, type=None, bg=ColorsSet.White, bracket=None, mode='default'):
    disable = '\u001b[0m'
    print(f"{bg}{bracket[0] if bracket else ''}{disable}",end='')
    for item in display_basic(iterable, type, mode):
        _print(item, code=bg)
    print(f"{bg}{bracket[1] if bracket else ''}{disable}",end='')

def display_basic(iterable, type, mode='default'):
    modes = {"hex": "{:x}".format,
        "bin": "{:b}".format,
        "oct": "{:o}".format,
        "dec":"{:d}".format,
        "default": "{}".format}

    if type == "register":
        for key, val in iterable.items():
            yield f"{key}={val}"
    elif type == "macros":
        for key, val in iterable.items():
            yield f"{key}:{val}"
    elif type == 'stack':
        for num in iterable:
            yield f"{modes[mode](num).upper()}"
    else:
        yield f"{iterable}\n"

def _print(token, code, start=' ', end=''):
    sys.stdout.write(f"{code}{start}{token}{end}")
    sys.stdout.write('\u001b[0m')
    sys.stdout.flush()

def banner(msg, code=ColorsSet.White):
    _print(msg, code)
    print()

def help():
    '''
    Example: Command Line Help:

    USAGE:

      rpn                          Launch in interactive mode
      rpn [expression]             Evaluate a one-line expression

    RC FILE

      rpn will execute the contents of ~/.rpnrc at startup if it exists.

    EXAMPLES

      rpn 1 2 + 3 + 4 + 5 +              => 15
      rpn pi cos                         => -1.0
      rpn                                => interactive mode

    Example: Command Set Help
    
    Arithmetic Operators

      +          Add
      -          Subtract
      *          Multiply
      /          Divide
      cla        Clear the stack and variables
      clr        Clear the stack
      clv        Clear the variables
      !          Boolean NOT
      !=         Not equal to
      %          Modulus
      ++         Increment
      --         Decrement

    Bitwise Operators

      &          Bitwise AND
      |          Bitwise OR
      ^          Bitwise XOR
      ~          Bitwise NOT
      <<         Bitwise shift left
      >>         Bitwise shift right

    Boolean Operators

      &&         Boolean AND
      ||         Boolean OR
      ^^         Boolean XOR

    Comparison Operators

      <          Less than
      <=         Less than or equal to
      ==         Equal to
      >          Greater than
      >=         Greater than or equal to

    Trigonometric Functions

      acos       Arc Cosine
      asin       Arc Sine
      atan       Arc Tangent
      cos        Cosine
      cosh       Hyperbolic Cosine
      sin        Sine
      sinh       Hyperbolic Sine
      tanh       Hyperbolic tangent

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

    Display Modes

      hex        Switch display mode to hexadecimal
      dec        Switch display mode to decimal (default)
      bin        Switch display mode to binary
      oct        Switch display mode to octal

    Constants

      e          Push e
      pi         Push Pi
      rand       Generate a random number

    Mathematic Functions

      exp        Exponentiation
      fact       Factorial
      sqrt       Square Root
      ln         Natural Logarithm
      log        Logarithm
      pow        Raise a number to a power

    Networking

      hnl        Host to network long
      hns        Host to network short
      nhl        Network to host long
      nhs        Network to host short

    Stack Manipulation

      pick       Pick the -n'th item from the stack
      repeat     Repeat an operation n times, e.g. '3 repeat +'
      depth      Push the current stack depth
      drop       Drops the top item from the stack
      dropn      Drops n items from the stack
      dup        Duplicates the top stack item
      dupn       Duplicates the top n stack items in order
      roll       Roll the stack upwards by n
      rolld      Roll the stack downwards by n
      stack      Toggles stack display from horizontal to vertical
      swap       Swap the top 2 stack items

    Macros and Variables

      macro      Defines a macro, e.g. 'macro kib 1024 *'
      x=         Assigns a variable, e.g. '1024 x='

    Other

      help       Print the help message
      exit       Exit the calculator
    '''

