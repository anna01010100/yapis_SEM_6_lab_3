from antlr4 import *
from gen.MygrammarLexer import MygrammarLexer
from gen.MygrammarParser import MygrammarParser
from antlr4.CommonTokenStream import CommonTokenStream
from GraphErrorListener import GraphErrorListener


def start_parse(input_string):
    input_stream = InputStream(input_string)
    lexer = MygrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MygrammarParser(stream)
    parser.removeErrorListeners()
    syntax_error_listener = GraphErrorListener()
    parser.addErrorListener(syntax_error_listener)
    tree = parser.program()


def file_reader(filename):
    with open(filename, 'r') as file:
        string1 = file.read()
    return string1


if __name__ == '__main__':
    start_parse(start_parse(file_reader('test_1')))
