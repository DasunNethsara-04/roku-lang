class Interpreter:
    def __init__(self, content: str):
        self.lines = content.strip().split(";")
        self.token: list = []
        
    def tokenizer(self, command: str) -> list[str]:
        return command.split()
        
    def parser(self, token: list[str]):
        if token == [] or token == None:
            pass
        if token[0] == "PRINT":
            print(" ".join(token[1:]))
        elif token[0] == "ADD":
            num1, num2 = int(token[1]), int(token[2])
            print(num1 + num2)
        
    def worker(self):
        for line in self.lines[:-1]:
            token: list[str] = self.tokenizer(line)
            self.parser(token)
            