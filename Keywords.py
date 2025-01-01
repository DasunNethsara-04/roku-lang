from enum import Enum

class Keywords(Enum):
    """
    Keyword for the language
    """
    PRINT: str = "print"
    
    # variables
    LET: str = "let"
    CONSTANT: str = "final"
    
    # control flow
    IF: str = "if"
    ELIF: str = "elif"
    ELSE: str = "else"
    
    # loops
    WHILE: str = "while"
    FOR: str = "for"
    IN: str = "in"
    RANGE: str = "range"
    BREAK: str = "break"
    CONTINUE: str = "continue"
    
    # functions
    FUNCTION: str = "func"
    RETURN: str = "return"
    
    # data types
    
    TRUE: str = "true"
    FALSE: str = "false"
    NULL: str = "null"
    STRING: str = "string"
    NUMBER: str = "number"
    BOOLEAN: str = "boolean"
    
    # operators
    # arithmetic
    ADD: str = "+"
    SUBTRACT: str = "-"
    MULTIPLY: str = "*"
    DIVIDE: str = "/"
    MODULUS: str = "%"
    
    # comparison
    EQUAL: str = "=="
    NOT_EQUAL: str = "!="
    LESS_THAN: str = "<"
    GREATER_THAN: str = ">"
    LESS_THAN_EQUAL: str = "<="
    GREATER_THAN_EQUAL: str = ">="
    
    # logical
    AND: str = "&&"
    OR: str = "||"
    NOT: str = "!"
    
    # assignment
    ASSIGN: str = "="
    ADD_ASSIGN: str = "+="
    SUBTRACT_ASSIGN: str = "-="
    MULTIPLY_ASSIGN: str = "*="
    DIVIDE_ASSIGN: str = "/="
    MODULUS_ASSIGN: str = "%="
    
    # scope
    LEFT_PAREN: str = "("
    RIGHT_PAREN: str = ")"
    LEFT_BRACE: str = "{"
    RIGHT_BRACE: str = "}"
    LEFT_BRACKET: str = "["
    RIGHT_BRACKET: str = "]"
    
    # punctuation
    COMMA: str = ","
    COLON: str = ":"
    SEMICOLON: str = ";"
    DOT: str = "."
    
    # other
    EOF: str = "EOF"
    UNKNOWN: str = "UNKNOWN"
    
    # comments
    COMMENT: str = "//"
    
    # escape characters
    NEWLINE: str = "\n"
    BACKSLASH: str = "\\"
    TAB: str = "\t"
    QUOTE: str = "\""
    
    # special characters
    SPACE: str = " "
    UNDERSCORE: str = "_"
    SINGLE_QUOTE: str = "'"
    BACKTICK: str = "`"
    DOLLAR: str = "$"
    PERCENT: str = "%"
    CARET: str = "^"
    AMPERSAND: str = "&"