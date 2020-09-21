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

def display(iterable, type=None, bg=ColorsSet.White, bracket=None, mode='dec'):
    disable = '\u001b[0m'
    print(f"{bg}{bracket[0] if bracket else ''}{disable}",end='')
    for item in display_basic(iterable, type, mode):
        _print(item, code=bg)
    print(f"{bg}{bracket[1] if bracket else ''}{disable}",end='')

def display_basic(iterable, type, mode='dec'):
    modes = {"hex": "{:x}".format,
        "bin": "{:b}".format,
        "oct": "{:o}".format,
        "dec":"{:d}".format}

    if type == "register":
        for key, val in iterable.items():
            yield f"{key}={val}"
    elif type == "macros":
        for key, val in iterable.items():
            yield f"{key}:{val}"
    elif type == 'stack':
        for num in iterable:
            yield f"{modes[mode](num)}"
    else:
        yield f"{iterable}\n"

def _print(token, code, start=' ', end=''):
    sys.stdout.write(f"{code}{start}{token}{end}")
    sys.stdout.write('\u001b[0m')
    sys.stdout.flush()

def banner(msg, code=ColorsSet.White):
    _print(msg, code)
    print()

def help(buffer):
    pass

