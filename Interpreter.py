class Interpreter:
    """
    A simple interpreter for a custom language.
    """

    def __init__(self, content: str):
        """
        Initialize the Interpreter with the input content.
        
        Args:
            content (str): The input program as a string.
        """
        self.lines = content.strip().split(";")
        self.token: list = []
        
    def tokenizer(self, command: str) -> list[str]:
        """
        Split a command string into tokens.
        
        Args:
            command (str): A single command string.
        
        Returns:
            list[str]: List of tokens.
        """
        return command.split()
        
    def parser(self, token: list[str]):
        """
        Parse and execute a tokenized command.
        
        Args:
            token (list[str]): List of tokens representing a command.
        """
        if token == [] or token == None:
            pass
        if token[0] == "PRINT":
            # Print all arguments after PRINT command
            print(" ".join(token[1:]))
        elif token[0] == "ADD":
            # Add two numbers and print the result
            num1, num2 = int(token[1]), int(token[2])
            print(num1 + num2)
        
    def worker(self):
        """
        Process all lines in the input content.
        Tokenize each line and pass to the parser.
        """
        for line in self.lines[:-1]:
            token: list[str] = self.tokenizer(line)
            self.parser(token)
            