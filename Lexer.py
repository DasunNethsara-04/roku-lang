import re
from Keywords import Keywords


class Lexer:
    def __init__(self, content: str) -> None:
        self.content: str = content
        self.cursor: int = 0
        self.tokens: list = []

    def tokenizer(self) -> list[dict]:
        while self.cursor < len(self.content):
            char = self.content[self.cursor]
            
            # Handle spaces
            if char == Keywords.SPACE.value:
                self.cursor += 1
            
            # Handle identifiers and keywords
            elif re.match(r"[a-zA-Z]", char):
                word: str = ""
                while self.cursor < len(self.content) and re.match(r"[a-zA-Z0-9_]", self.content[self.cursor]):
                    word += self.content[self.cursor]
                    self.cursor += 1
                # Check if the word is a keyword
                if word in (keyword.value for keyword in Keywords):
                    self.tokens.append({"type": "KEYWORD", "value": word})
                else:
                    self.tokens.append({"type": "IDENTIFIER", "value": word})
            
            # Handle numbers
            elif re.match(r"[0-9]", char):
                number: str = ""
                while self.cursor < len(self.content) and re.match(r"[0-9]", self.content[self.cursor]):
                    number += self.content[self.cursor]
                    self.cursor += 1
                self.tokens.append({"type": "NUMBER", "value": number})
            
            # Handle operators
            elif char in (op.value for op in Keywords if op.name.isupper() and "ASSIGN" not in op.name):
                self.tokens.append({"type": "OPERATOR", "value": char})
                self.cursor += 1
            
            # Handle strings
            elif char == Keywords.QUOTE.value:
                self.cursor += 1  # Skip the opening quote
                string: str = ""
                while self.cursor < len(self.content) and self.content[self.cursor] != Keywords.QUOTE.value:
                    string += self.content[self.cursor]
                    self.cursor += 1
                self.tokens.append({"type": "STRING", "value": string})
                self.cursor += 1  # Skip the closing quote
            
            # Handle single-character tokens like punctuation
            elif char in (symbol.value for symbol in Keywords if len(symbol.value) == 1):
                self.tokens.append({"type": "SYMBOL", "value": char})
                self.cursor += 1
            
            else:
                # Skip unknown characters
                self.cursor += 1
        
        return self.tokens
