# Generated from C:/Users/hanna/Desktop/yapis\Mygrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,5,0,40,8,
        0,10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,
        1,55,9,1,3,1,57,8,1,1,1,1,1,1,1,1,1,1,1,4,1,64,8,1,11,1,12,1,65,
        1,2,1,2,3,2,70,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,3,4,3,81,
        8,3,11,3,12,3,82,1,4,1,4,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,4,1,4,
        1,4,1,4,5,4,97,8,4,10,4,12,4,100,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        108,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,121,8,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,130,8,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,139,8,7,5,7,141,8,7,10,7,12,7,144,9,7,1,8,1,8,1,8,1,8,1,
        9,1,9,1,10,1,10,1,10,1,10,4,10,156,8,10,11,10,12,10,157,1,11,1,11,
        1,11,1,11,1,11,3,11,165,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        5,12,174,8,12,10,12,12,12,177,9,12,3,12,179,8,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,4,13,192,8,13,11,13,12,13,
        193,1,14,1,14,1,14,1,14,1,14,1,14,1,14,4,14,203,8,14,11,14,12,14,
        204,1,14,1,14,1,14,1,14,4,14,211,8,14,11,14,12,14,212,3,14,215,8,
        14,1,15,1,15,1,15,3,15,220,8,15,1,15,1,15,1,15,1,15,3,15,226,8,15,
        5,15,228,8,15,10,15,12,15,231,9,15,1,15,0,0,16,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,0,3,2,0,1,1,3,3,1,0,5,8,1,0,10,11,254,0,
        35,1,0,0,0,2,46,1,0,0,0,4,69,1,0,0,0,6,77,1,0,0,0,8,84,1,0,0,0,10,
        107,1,0,0,0,12,109,1,0,0,0,14,120,1,0,0,0,16,145,1,0,0,0,18,149,
        1,0,0,0,20,151,1,0,0,0,22,159,1,0,0,0,24,168,1,0,0,0,26,182,1,0,
        0,0,28,195,1,0,0,0,30,219,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,
        37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,41,1,0,0,0,37,35,1,0,0,
        0,38,40,3,6,3,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,
        47,5,3,0,0,47,56,5,12,0,0,48,53,5,3,0,0,49,50,5,14,0,0,50,52,5,3,
        0,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,57,
        1,0,0,0,55,53,1,0,0,0,56,48,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,
        58,59,5,13,0,0,59,60,5,15,0,0,60,63,5,23,0,0,61,62,5,22,0,0,62,64,
        3,4,2,0,63,61,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,
        66,3,1,0,0,0,67,70,3,6,3,0,68,70,3,20,10,0,69,67,1,0,0,0,69,68,1,
        0,0,0,70,5,1,0,0,0,71,78,3,8,4,0,72,78,3,24,12,0,73,78,3,22,11,0,
        74,78,3,2,1,0,75,78,3,26,13,0,76,78,3,28,14,0,77,71,1,0,0,0,77,72,
        1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,
        78,80,1,0,0,0,79,81,5,23,0,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,
        0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,89,5,3,0,0,85,86,5,14,0,0,86,
        88,5,3,0,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,
        0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,9,0,0,93,98,3,10,5,0,94,95,
        5,14,0,0,95,97,3,10,5,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,
        0,98,99,1,0,0,0,99,9,1,0,0,0,100,98,1,0,0,0,101,108,3,12,6,0,102,
        108,3,14,7,0,103,108,3,24,12,0,104,108,3,16,8,0,105,108,3,18,9,0,
        106,108,5,1,0,0,107,101,1,0,0,0,107,102,1,0,0,0,107,103,1,0,0,0,
        107,104,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,11,1,0,0,0,109,
        110,5,12,0,0,110,111,5,2,0,0,111,112,5,13,0,0,112,113,5,3,0,0,113,
        13,1,0,0,0,114,115,5,12,0,0,115,116,5,3,0,0,116,117,5,5,0,0,117,
        118,5,3,0,0,118,121,5,13,0,0,119,121,5,3,0,0,120,114,1,0,0,0,120,
        119,1,0,0,0,121,122,1,0,0,0,122,129,5,5,0,0,123,124,5,12,0,0,124,
        125,5,3,0,0,125,126,5,5,0,0,126,127,5,3,0,0,127,130,5,13,0,0,128,
        130,5,3,0,0,129,123,1,0,0,0,129,128,1,0,0,0,130,142,1,0,0,0,131,
        138,5,5,0,0,132,133,5,12,0,0,133,134,5,3,0,0,134,135,5,5,0,0,135,
        136,5,3,0,0,136,139,5,13,0,0,137,139,5,3,0,0,138,132,1,0,0,0,138,
        137,1,0,0,0,139,141,1,0,0,0,140,131,1,0,0,0,141,144,1,0,0,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,15,1,0,0,0,144,142,1,0,0,0,145,146,
        7,0,0,0,146,147,7,1,0,0,147,148,7,0,0,0,148,17,1,0,0,0,149,150,5,
        27,0,0,150,19,1,0,0,0,151,152,5,26,0,0,152,153,5,3,0,0,153,155,5,
        13,0,0,154,156,5,23,0,0,155,154,1,0,0,0,156,157,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,21,1,0,0,0,159,164,5,25,0,0,160,165,
        5,3,0,0,161,165,5,29,0,0,162,165,5,1,0,0,163,165,3,24,12,0,164,160,
        1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,166,
        1,0,0,0,166,167,5,13,0,0,167,23,1,0,0,0,168,169,5,3,0,0,169,178,
        5,12,0,0,170,175,5,3,0,0,171,172,5,14,0,0,172,174,5,3,0,0,173,171,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,178,170,1,0,0,0,178,179,1,0,0,0,179,180,
        1,0,0,0,180,181,5,13,0,0,181,25,1,0,0,0,182,183,5,20,0,0,183,184,
        5,3,0,0,184,185,5,15,0,0,185,186,5,3,0,0,186,187,5,13,0,0,187,188,
        5,15,0,0,188,191,5,23,0,0,189,190,5,22,0,0,190,192,3,6,3,0,191,189,
        1,0,0,0,192,193,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,27,1,
        0,0,0,195,196,5,18,0,0,196,197,3,30,15,0,197,198,5,13,0,0,198,199,
        5,15,0,0,199,202,5,23,0,0,200,201,5,22,0,0,201,203,3,6,3,0,202,200,
        1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,214,
        1,0,0,0,206,207,5,19,0,0,207,210,5,23,0,0,208,209,5,22,0,0,209,211,
        3,6,3,0,210,208,1,0,0,0,211,212,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,215,1,0,0,0,214,206,1,0,0,0,214,215,1,0,0,0,215,29,1,
        0,0,0,216,220,5,3,0,0,217,220,5,1,0,0,218,220,3,24,12,0,219,216,
        1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,229,1,0,0,0,221,225,
        7,2,0,0,222,226,5,3,0,0,223,226,5,1,0,0,224,226,3,24,12,0,225,222,
        1,0,0,0,225,223,1,0,0,0,225,224,1,0,0,0,226,228,1,0,0,0,227,221,
        1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,31,1,
        0,0,0,231,229,1,0,0,0,26,35,41,53,56,65,69,77,82,89,98,107,120,129,
        138,142,157,164,175,178,193,204,212,214,219,225,229
    ]

class MygrammarParser ( Parser ):

    grammarFileName = "Mygrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '", "'+'", "'-'", "'*'", "'/'", "'='", "'!='", "'=='", 
                     "'('", "')'", "','", "':'", "';'", "'.'", "'if('", 
                     "'else:'", "'for('", "'in'", "'****'", "'\\n'", "'\\t'", 
                     "'show('", "'return('", "'input()'" ]

    symbolicNames = [ "<INVALID>", "INT", "TYPE", "ID", "WHITESPACE", "PLUS", 
                      "MINUS", "MULT", "DIVIDER", "ASSIGN", "NEQ", "EQ", 
                      "LPAREN", "RPAREN", "COMMA", "COLON", "SEMI", "DOT", 
                      "IF", "ELSE", "FOR", "IN", "INSIDE", "NLINE", "TAB", 
                      "SHOW", "RETURN", "INPUT", "WS", "STR" ]

    RULE_program = 0
    RULE_func = 1
    RULE_func_statement = 2
    RULE_statement = 3
    RULE_equal = 4
    RULE_operation = 5
    RULE_change_type = 6
    RULE_sum = 7
    RULE_other_op = 8
    RULE_input = 9
    RULE_return_statement = 10
    RULE_show_statement = 11
    RULE_use_func = 12
    RULE_for_statement = 13
    RULE_if_statement = 14
    RULE_if_condition = 15

    ruleNames =  [ "program", "func", "func_statement", "statement", "equal", 
                   "operation", "change_type", "sum", "other_op", "input", 
                   "return_statement", "show_statement", "use_func", "for_statement", 
                   "if_statement", "if_condition" ]

    EOF = Token.EOF
    INT=1
    TYPE=2
    ID=3
    WHITESPACE=4
    PLUS=5
    MINUS=6
    MULT=7
    DIVIDER=8
    ASSIGN=9
    NEQ=10
    EQ=11
    LPAREN=12
    RPAREN=13
    COMMA=14
    COLON=15
    SEMI=16
    DOT=17
    IF=18
    ELSE=19
    FOR=20
    IN=21
    INSIDE=22
    NLINE=23
    TAB=24
    SHOW=25
    RETURN=26
    INPUT=27
    WS=28
    STR=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MygrammarParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.FuncContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.FuncContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MygrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MygrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 32
                    self.func() 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34865160) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(MygrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def LPAREN(self):
            return self.getToken(MygrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(MygrammarParser.COLON, 0)

        def NLINE(self):
            return self.getToken(MygrammarParser.NLINE, 0)

        def INSIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.INSIDE)
            else:
                return self.getToken(MygrammarParser.INSIDE, i)

        def func_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.Func_statementContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.Func_statementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.COMMA)
            else:
                return self.getToken(MygrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = MygrammarParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MygrammarParser.ID)
            self.state = 47
            self.match(MygrammarParser.LPAREN)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 48
                self.match(MygrammarParser.ID)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 49
                    self.match(MygrammarParser.COMMA)
                    self.state = 50
                    self.match(MygrammarParser.ID)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 58
            self.match(MygrammarParser.RPAREN)
            self.state = 59
            self.match(MygrammarParser.COLON)
            self.state = 60
            self.match(MygrammarParser.NLINE)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.match(MygrammarParser.INSIDE)
                self.state = 62
                self.func_statement()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MygrammarParser.StatementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MygrammarParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MygrammarParser.RULE_func_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_statement" ):
                listener.enterFunc_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_statement" ):
                listener.exitFunc_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_statement" ):
                return visitor.visitFunc_statement(self)
            else:
                return visitor.visitChildren(self)




    def func_statement(self):

        localctx = MygrammarParser.Func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 18, 20, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.statement()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.return_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equal(self):
            return self.getTypedRuleContext(MygrammarParser.EqualContext,0)


        def use_func(self):
            return self.getTypedRuleContext(MygrammarParser.Use_funcContext,0)


        def show_statement(self):
            return self.getTypedRuleContext(MygrammarParser.Show_statementContext,0)


        def func(self):
            return self.getTypedRuleContext(MygrammarParser.FuncContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MygrammarParser.For_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MygrammarParser.If_statementContext,0)


        def NLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.NLINE)
            else:
                return self.getToken(MygrammarParser.NLINE, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MygrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 71
                self.equal()
                pass

            elif la_ == 2:
                self.state = 72
                self.use_func()
                pass

            elif la_ == 3:
                self.state = 73
                self.show_statement()
                pass

            elif la_ == 4:
                self.state = 74
                self.func()
                pass

            elif la_ == 5:
                self.state = 75
                self.for_statement()
                pass

            elif la_ == 6:
                self.state = 76
                self.if_statement()
                pass


            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.match(MygrammarParser.NLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MygrammarParser.ASSIGN, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.OperationContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.OperationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.COMMA)
            else:
                return self.getToken(MygrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)




    def equal(self):

        localctx = MygrammarParser.EqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MygrammarParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 85
                self.match(MygrammarParser.COMMA)
                self.state = 86
                self.match(MygrammarParser.ID)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(MygrammarParser.ASSIGN)
            self.state = 93
            self.operation()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 94
                self.match(MygrammarParser.COMMA)
                self.state = 95
                self.operation()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def change_type(self):
            return self.getTypedRuleContext(MygrammarParser.Change_typeContext,0)


        def sum_(self):
            return self.getTypedRuleContext(MygrammarParser.SumContext,0)


        def use_func(self):
            return self.getTypedRuleContext(MygrammarParser.Use_funcContext,0)


        def other_op(self):
            return self.getTypedRuleContext(MygrammarParser.Other_opContext,0)


        def input_(self):
            return self.getTypedRuleContext(MygrammarParser.InputContext,0)


        def INT(self):
            return self.getToken(MygrammarParser.INT, 0)

        def getRuleIndex(self):
            return MygrammarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = MygrammarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operation)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.change_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.sum_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.use_func()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.other_op()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.input_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.match(MygrammarParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Change_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MygrammarParser.LPAREN, 0)

        def TYPE(self):
            return self.getToken(MygrammarParser.TYPE, 0)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MygrammarParser.ID, 0)

        def getRuleIndex(self):
            return MygrammarParser.RULE_change_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChange_type" ):
                listener.enterChange_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChange_type" ):
                listener.exitChange_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChange_type" ):
                return visitor.visitChange_type(self)
            else:
                return visitor.visitChildren(self)




    def change_type(self):

        localctx = MygrammarParser.Change_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_change_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MygrammarParser.LPAREN)
            self.state = 110
            self.match(MygrammarParser.TYPE)
            self.state = 111
            self.match(MygrammarParser.RPAREN)
            self.state = 112
            self.match(MygrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.PLUS)
            else:
                return self.getToken(MygrammarParser.PLUS, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.LPAREN)
            else:
                return self.getToken(MygrammarParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.RPAREN)
            else:
                return self.getToken(MygrammarParser.RPAREN, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)




    def sum_(self):

        localctx = MygrammarParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 114
                self.match(MygrammarParser.LPAREN)
                self.state = 115
                self.match(MygrammarParser.ID)
                self.state = 116
                self.match(MygrammarParser.PLUS)
                self.state = 117
                self.match(MygrammarParser.ID)
                self.state = 118
                self.match(MygrammarParser.RPAREN)
                pass
            elif token in [3]:
                self.state = 119
                self.match(MygrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 122
            self.match(MygrammarParser.PLUS)
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 123
                self.match(MygrammarParser.LPAREN)
                self.state = 124
                self.match(MygrammarParser.ID)
                self.state = 125
                self.match(MygrammarParser.PLUS)
                self.state = 126
                self.match(MygrammarParser.ID)
                self.state = 127
                self.match(MygrammarParser.RPAREN)
                pass
            elif token in [3]:
                self.state = 128
                self.match(MygrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 131
                self.match(MygrammarParser.PLUS)
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 132
                    self.match(MygrammarParser.LPAREN)
                    self.state = 133
                    self.match(MygrammarParser.ID)
                    self.state = 134
                    self.match(MygrammarParser.PLUS)
                    self.state = 135
                    self.match(MygrammarParser.ID)
                    self.state = 136
                    self.match(MygrammarParser.RPAREN)
                    pass
                elif token in [3]:
                    self.state = 137
                    self.match(MygrammarParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.INT)
            else:
                return self.getToken(MygrammarParser.INT, i)

        def PLUS(self):
            return self.getToken(MygrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MygrammarParser.MINUS, 0)

        def DIVIDER(self):
            return self.getToken(MygrammarParser.DIVIDER, 0)

        def MULT(self):
            return self.getToken(MygrammarParser.MULT, 0)

        def getRuleIndex(self):
            return MygrammarParser.RULE_other_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_op" ):
                listener.enterOther_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_op" ):
                listener.exitOther_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_op" ):
                return visitor.visitOther_op(self)
            else:
                return visitor.visitChildren(self)




    def other_op(self):

        localctx = MygrammarParser.Other_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_other_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==1 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==1 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(MygrammarParser.INPUT, 0)

        def getRuleIndex(self):
            return MygrammarParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = MygrammarParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MygrammarParser.INPUT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MygrammarParser.RETURN, 0)

        def ID(self):
            return self.getToken(MygrammarParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def NLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.NLINE)
            else:
                return self.getToken(MygrammarParser.NLINE, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MygrammarParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MygrammarParser.RETURN)
            self.state = 152
            self.match(MygrammarParser.ID)
            self.state = 153
            self.match(MygrammarParser.RPAREN)
            self.state = 155 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 154
                    self.match(MygrammarParser.NLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 157 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Show_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(MygrammarParser.SHOW, 0)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MygrammarParser.ID, 0)

        def STR(self):
            return self.getToken(MygrammarParser.STR, 0)

        def INT(self):
            return self.getToken(MygrammarParser.INT, 0)

        def use_func(self):
            return self.getTypedRuleContext(MygrammarParser.Use_funcContext,0)


        def getRuleIndex(self):
            return MygrammarParser.RULE_show_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow_statement" ):
                listener.enterShow_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow_statement" ):
                listener.exitShow_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShow_statement" ):
                return visitor.visitShow_statement(self)
            else:
                return visitor.visitChildren(self)




    def show_statement(self):

        localctx = MygrammarParser.Show_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_show_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MygrammarParser.SHOW)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(MygrammarParser.ID)
                pass

            elif la_ == 2:
                self.state = 161
                self.match(MygrammarParser.STR)
                pass

            elif la_ == 3:
                self.state = 162
                self.match(MygrammarParser.INT)
                pass

            elif la_ == 4:
                self.state = 163
                self.use_func()
                pass


            self.state = 166
            self.match(MygrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Use_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def LPAREN(self):
            return self.getToken(MygrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.COMMA)
            else:
                return self.getToken(MygrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_use_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUse_func" ):
                listener.enterUse_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUse_func" ):
                listener.exitUse_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUse_func" ):
                return visitor.visitUse_func(self)
            else:
                return visitor.visitChildren(self)




    def use_func(self):

        localctx = MygrammarParser.Use_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_use_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MygrammarParser.ID)
            self.state = 169
            self.match(MygrammarParser.LPAREN)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 170
                self.match(MygrammarParser.ID)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 171
                    self.match(MygrammarParser.COMMA)
                    self.state = 172
                    self.match(MygrammarParser.ID)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 180
            self.match(MygrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MygrammarParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.COLON)
            else:
                return self.getToken(MygrammarParser.COLON, i)

        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def NLINE(self):
            return self.getToken(MygrammarParser.NLINE, 0)

        def INSIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.INSIDE)
            else:
                return self.getToken(MygrammarParser.INSIDE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MygrammarParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MygrammarParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MygrammarParser.FOR)
            self.state = 183
            self.match(MygrammarParser.ID)
            self.state = 184
            self.match(MygrammarParser.COLON)
            self.state = 185
            self.match(MygrammarParser.ID)
            self.state = 186
            self.match(MygrammarParser.RPAREN)
            self.state = 187
            self.match(MygrammarParser.COLON)
            self.state = 188
            self.match(MygrammarParser.NLINE)
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 189
                self.match(MygrammarParser.INSIDE)
                self.state = 190
                self.statement()
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MygrammarParser.IF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(MygrammarParser.If_conditionContext,0)


        def RPAREN(self):
            return self.getToken(MygrammarParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(MygrammarParser.COLON, 0)

        def NLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.NLINE)
            else:
                return self.getToken(MygrammarParser.NLINE, i)

        def INSIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.INSIDE)
            else:
                return self.getToken(MygrammarParser.INSIDE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MygrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return MygrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MygrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MygrammarParser.IF)
            self.state = 196
            self.if_condition()
            self.state = 197
            self.match(MygrammarParser.RPAREN)
            self.state = 198
            self.match(MygrammarParser.COLON)
            self.state = 199
            self.match(MygrammarParser.NLINE)
            self.state = 202 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 200
                self.match(MygrammarParser.INSIDE)
                self.state = 201
                self.statement()
                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 206
                self.match(MygrammarParser.ELSE)
                self.state = 207
                self.match(MygrammarParser.NLINE)
                self.state = 210 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 208
                    self.match(MygrammarParser.INSIDE)
                    self.state = 209
                    self.statement()
                    self.state = 212 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==22):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.ID)
            else:
                return self.getToken(MygrammarParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.INT)
            else:
                return self.getToken(MygrammarParser.INT, i)

        def use_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MygrammarParser.Use_funcContext)
            else:
                return self.getTypedRuleContext(MygrammarParser.Use_funcContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.EQ)
            else:
                return self.getToken(MygrammarParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MygrammarParser.NEQ)
            else:
                return self.getToken(MygrammarParser.NEQ, i)

        def getRuleIndex(self):
            return MygrammarParser.RULE_if_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_condition" ):
                listener.enterIf_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_condition" ):
                listener.exitIf_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = MygrammarParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 216
                self.match(MygrammarParser.ID)
                pass

            elif la_ == 2:
                self.state = 217
                self.match(MygrammarParser.INT)
                pass

            elif la_ == 3:
                self.state = 218
                self.use_func()
                pass


            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 222
                    self.match(MygrammarParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 223
                    self.match(MygrammarParser.INT)
                    pass

                elif la_ == 3:
                    self.state = 224
                    self.use_func()
                    pass


                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





