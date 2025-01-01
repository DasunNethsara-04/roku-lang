import Lexer
class CodeExecutor:
    def __init__(self, content: str) -> None:
        data: list[dict] = Lexer.Lexer(content).tokenizer()
        print(data)