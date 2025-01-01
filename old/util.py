from typing import Any
import colorama

class Util:
    def __init__(self):
        pass
    
    def cast_num_type(self, num: str|Any) -> int|float|ValueError:
        """
        Casts a given input to either an integer or a float, and raises a ValueError if it's not a number.
        
        Args:
            num (str | Any): Get a number to cast

        Raises:
            ValueError: If the `num` is not in a valid type

        Returns:
            int|float|ValueError: casted value or a error
        """
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError:
                raise ValueError(f"Invalid input: '{num}' is not a number.")
            
    def colorize_text(self, type: str, message: str) -> str:
        """Colorizes the given message based on the specified type.

        Args:
            type (str): Type of the message
                            > error
                            
                            > warning
            message (str): The message that needs to colorize

        Returns:
            str: Colorized ASCII string
        """
        if type == "success":
            return f"{colorama.Fore.GREEN}{message}{colorama.Style.RESET_ALL}"
        elif type == "warning":
            return f"{colorama.Fore.YELLOW}{message}{colorama.Style.RESET_ALL}"
        elif type == "error":
            return f"{colorama.Fore.RED}{message}{colorama.Style.RESET_ALL}"
        else:
            return message
        