# imports
from Arithmatic import ArithmeticOperations
from util import Util

class Interpreter:
    """
    This class is responsible for interpreting the given script.
    """
    def __init__(self, content: str) -> None:
        """
        Initializes the interpreter with the given script content.
        """
        self.content: str = content
        self.lines: list[str] = self.content.split(";")
        self.util: Util = Util()
        self.armt: ArithmeticOperations = ArithmeticOperations()
        
        
    def tokenizer(self, line: str) -> list[str] | TypeError:
        """
        Splits the given line into tokens and returns them as a list.
        """
        try: 
            token: list[str] = line.split()
        except TypeError:
            return TypeError("Invalid")
        return token
    
    def parser(self, token) -> None:
        """
        Parses the given token list and performs the corresponding action.
        """
        try:
            if len(token) < 1:
                pass
            elif token[0] == "PRINT":
                print((" ").join(token[1:]))
            elif token[0] == "ADD":
                result = self.armt.add(token[1:])
                print(result)
            elif token[0] == "SUB":
                result = self.armt.subtract(token[1:])
                print(result)
            elif token[0] == "MUL":
                result = self.armt.multiply(token[1:])
                print(result)
            elif token[0] == "DIV":
                result = self.armt.divide(token[1], token[2])
                print(result)
            elif token[0] == "MOD":
                result = self.armt.modulus(token[1], token[2])
                print(result)
        except Exception as e:
            print(self.util.colorize_text("error", f"Error: {str(e)}"))
            
    
    def execute(self) -> None:
        """
        Executes the script by tokenizing, parsing, and performing actions.
        """
        for line in self.lines:
            tokenized_list: list[str] = self.tokenizer(line)
            if isinstance(tokenized_list, list):
                self.parser(tokenized_list)