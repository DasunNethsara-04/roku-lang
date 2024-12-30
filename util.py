from typing import Any
import colorama

class Util:
    def __init__(self):
        pass
    
    def cast_num_type(self, num: str|Any) -> int|float|ValueError:
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError:
                raise ValueError(f"Invalid input: '{num}' is not a number.")
            
    def colorize_text(self, type: str, message):
        if type == "success":
            return f"{colorama.Fore.GREEN}{message}{colorama.Style.RESET_ALL}"
        elif type == "warning":
            return f"{colorama.Fore.YELLOW}{message}{colorama.Style.RESET_ALL}"
        elif type == "error":
            return f"{colorama.Fore.RED}{message}{colorama.Style.RESET_ALL}"
        else:
            return message
        