import sys
from Interpreter import Interpreter

if __name__ == "__main__":
    content = open(sys.argv[1]).read()
    interpreter: Interpreter = Interpreter(content)
    interpreter.execute()