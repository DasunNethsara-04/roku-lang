import sys
from typing import Final

from Interpreter import Interpreter


# possible keywords
KEYWORDS: Final = (
    "print",
    "read",
    "let",
    "final",
)

if __name__ == "__main__":
    try:
        data: Interpreter = Interpreter(open(sys.argv[1]).read())
        data.worker()
    except Exception as e:
        print(e)