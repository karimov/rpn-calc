import rpn
import sys

def main_interactive():
    calc = rpn.RpnCalc()
    calc.run()

def main_cli(expression):
    calc = rpn.RpnCalc()
    commands = calc.parser(expression)
    for res, err in calc.evaluate_cli(commands):
        if err is not None:
            print(err)
        if res is not None:
            print(res)

def main():
    # use stdin if it is full
    if not sys.stdin.isatty():
        input_stream = sys.stdin
        main_cli(input_stream.read())
    elif len(sys.argv) == 1:
        main_interactive()
    else:
        exp = " ".join(sys.argv[1:]) # TODO: escape '*'
        main_cli(exp)



if  __name__ == "__main__":
    main()