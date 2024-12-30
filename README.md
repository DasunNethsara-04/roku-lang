# RokuLang Interpreter

RokuLang is a simple interpreted programming language designed for learning and experimentation. The language supports basic arithmetic operations and printing output, making it an excellent starting point for understanding interpreters and scripting.

## Features
- Print text or values to the console.
- Perform basic arithmetic operations: Addition, Subtraction, Multiplication, Division, and Modulus.

## Quick Start

### Example Script (`program1.rk`):
```plaintext
PRINT "Hello World";
ADD 1 2 3;
SUB 15 1 4;
MUL 5 6 2;
DIV 6 3;
MOD 9 3;
```

### Output:
```
Hello World
6
10
60
2.0
0
```

## Usage

### Step 1: Clone the Repository
```bash
git https://github.com/DasunNethsara-04/roku-lang.git
cd roku-lang
```

### Step 2: Prepare Your Environment
Ensure you have Python 3.10 or higher installed.

### Step 3: Write Your Script
Create a `.rk` script file (e.g., `program1.rk`) and write your RokuLang code.

### Step 4: Run the Interpreter
```bash
python main.py program1.rk
```

## RokuLang Commands

| Command   | Description                                                | Example                       |
|-----------|------------------------------------------------------------|-------------------------------|
| `PRINT`   | Prints text or values to the console.                      | `PRINT "Hello, World!";`     |
| `ADD`     | Adds multiple numbers.                                     | `ADD 1 2 3;`                 |
| `SUB`     | Subtracts multiple numbers sequentially.                   | `SUB 10 2 3;`                |
| `MUL`     | Multiplies multiple numbers.                               | `MUL 2 3 4;`                 |
| `DIV`     | Divides two numbers (numerator, denominator).              | `DIV 8 4;`                   |
| `MOD`     | Finds the modulus (remainder) of two numbers.              | `MOD 10 3;`                  |

## File Structure
```
├── Arithmetic.py       # Handles arithmetic operations
├── util.py             # Utility functions for the interpreter
├── Interpreter.py      # Main interpreter for RokuLang
├── main.py             # Main entrypoint of the interpreter
├── program1.rk         # Sample RokuLang file
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance RokuLang.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
Enjoy experimenting with RokuLang! 🚀
