from util import Util
from colorama import Fore
class Interpreter:
    def __init__(self, content: str):
        self.content: str = content
        self.lines: list[str] = self.content.split(";")
        self.util: Util = Util()
        
        
    def tokenizer(self, line: str) -> list[str] | TypeError:
        try: 
            token: list[str] = line.split()
        except TypeError:
            return TypeError("Invalid")
        return token
    
    def parser(self, token):
        if len(token) < 1:
            pass
        elif token[0] == "PRINT":
            print((" ").join(token[1:]))
        elif token[0] == "ADD":
            try:
                num1, num2 = self.util.cast_num_type(token[1]), self.util.cast_num_type(token[2])
                print(num1 + num2)
            except ValueError as e:
                print(self.util.colorize_text("error", f"Error: {e}"))
            
    
    def execute(self):
        for line in self.lines:
            tokenized_list: list[str] = self.tokenizer(line)
            if isinstance(tokenized_list, list):
                self.parser(tokenized_list)