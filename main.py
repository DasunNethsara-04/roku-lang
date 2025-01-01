import sys
import Executor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            content: str = open(sys.argv[1]).read()
        except FileNotFoundError | IndexError as e:
            print("File not found.\nError: ", e)
            sys.exit()
        finally:
            Executor.CodeExecutor(content)