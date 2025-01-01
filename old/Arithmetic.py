from util import Util

class ArithmeticOperations:
    """
    Class for performing arithmetic operations.
    """
    def __init__(self) -> None:
        self.util = Util()
    
    def add(self, *nums) -> int|float|ValueError:
        """
        Perform addition of provided numbers.
        
        Args:
            *nums (int|float): The numbers to be added.
        
        Returns:
            int|float: The sum of the provided numbers.
        
        Raises:
            ValueError: If the input is not a valid number.
        """
        nums = nums[0]
        total: int|float = 0
        for num in nums:
            try:
                num: int | float | ValueError = self.util.cast_num_type(num)
                if not isinstance(num, (int, float)):
                    raise ValueError(f"Invalid input: {num}")
            except ValueError as e:
                raise ValueError(f"Invalid input: {num}") from e
            total += num
        return total
            
    
    def subtract(self, *nums: int|float) -> int|float:
        """
        Perform subtraction of provided numbers.
        
        Args:
            *nums (int|float): The numbers to be subtracted.
        
        Returns:
            int|float: The result of the subtraction.
        
        Raises:
            ValueError: If the input is not a valid number or if there are less than two numbers provided for subtraction.
        """
        nums = nums[0]
        if len(nums) < 2:
            raise ValueError("At least two numbers are required for subtraction")
        
        try:
            cur_val = self.util.cast_num_type(nums[0])
            for num in nums[1:]:
                num = self.util.cast_num_type(num)
                cur_val -= num
            return cur_val
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}") from e
    
    def multiply(self, *nums: int|float) -> int|float|ValueError:
        """
        Perform multiplication of provided numbers.
        
        Args:
            *nums (int|float): The numbers to be multiplied.
        
        Returns:
            int|float: The product of the provided numbers.
        
        Raises:
            ValueError: If the input is not a valid number or if there are less than two numbers provided for multiplication.
        """
        nums = nums[0]
        if len(nums) < 2:
            raise ValueError("At least two numbers are required for multiplication")
        
        mul: int|float = 1
        for num in nums:
            try:
                num: int | float | ValueError = self.util.cast_num_type(num)
                if not isinstance(num, (int, float)):
                    raise ValueError(f"Invalid input: {num}")
            except ValueError as e:
                raise ValueError(f"Invalid input: {num}") from e
            mul *= num
        return mul
    
    def divide(self, dividend: int|float, divisor: int|float) -> int|float|ValueError:
        """
        Perform division of the dividend by the divisor.
        
        Args:
            dividend (int|float): The dividend.
            divisor (int|float): The divisor.
        
        Returns:
        int|float: The result of the division.
        
        Raises:
        ValueError: If the divisor is zero.
        """
        num1, num2 = self.util.cast_num_type(dividend), self.util.cast_num_type(divisor)
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2
    
    def modulus(self, num1: int|float, num2: int|float) -> int | float | ValueError:
        """
        Perform modulo operation on the two numbers.
        
        Args:
            num1 (int|float): The first number.
            num2 (int|float): The second number.
        
        Returns:
            int|float: The remainder of the division.
        
        Raises:
            ValueError: If the divisor is zero.
        """
        num1, num2 = self.util.cast_num_type(num1), self.util.cast_num_type(num2)
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        
        return num1 % num2
        num1, num2 = self.util.cast_num_type(num1), self.util.cast_num_type(num2)
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        
        return num1 % num2