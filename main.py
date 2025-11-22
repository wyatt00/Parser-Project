import sys
from antlr4 import FileStream, CommonTokenStream
from MiniPythonLexer import MiniPythonLexer
from MiniPythonParser import MiniPythonParser

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 main.py <input_file.py>")
        sys.exit(1)

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = MiniPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniPythonParser(token_stream)

    tree = parser.file_input()
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main(sys.argv)
