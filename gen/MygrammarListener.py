# Generated from C:/Users/hanna/Desktop/yapis\Mygrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MygrammarParser import MygrammarParser
else:
    from MygrammarParser import MygrammarParser

# This class defines a complete listener for a parse tree produced by MygrammarParser.
class MygrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MygrammarParser#program.
    def enterProgram(self, ctx:MygrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MygrammarParser#program.
    def exitProgram(self, ctx:MygrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MygrammarParser#func.
    def enterFunc(self, ctx:MygrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by MygrammarParser#func.
    def exitFunc(self, ctx:MygrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by MygrammarParser#func_statement.
    def enterFunc_statement(self, ctx:MygrammarParser.Func_statementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#func_statement.
    def exitFunc_statement(self, ctx:MygrammarParser.Func_statementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#statement.
    def enterStatement(self, ctx:MygrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#statement.
    def exitStatement(self, ctx:MygrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#equal.
    def enterEqual(self, ctx:MygrammarParser.EqualContext):
        pass

    # Exit a parse tree produced by MygrammarParser#equal.
    def exitEqual(self, ctx:MygrammarParser.EqualContext):
        pass


    # Enter a parse tree produced by MygrammarParser#operation.
    def enterOperation(self, ctx:MygrammarParser.OperationContext):
        pass

    # Exit a parse tree produced by MygrammarParser#operation.
    def exitOperation(self, ctx:MygrammarParser.OperationContext):
        pass


    # Enter a parse tree produced by MygrammarParser#change_type.
    def enterChange_type(self, ctx:MygrammarParser.Change_typeContext):
        pass

    # Exit a parse tree produced by MygrammarParser#change_type.
    def exitChange_type(self, ctx:MygrammarParser.Change_typeContext):
        pass


    # Enter a parse tree produced by MygrammarParser#sum.
    def enterSum(self, ctx:MygrammarParser.SumContext):
        pass

    # Exit a parse tree produced by MygrammarParser#sum.
    def exitSum(self, ctx:MygrammarParser.SumContext):
        pass


    # Enter a parse tree produced by MygrammarParser#other_op.
    def enterOther_op(self, ctx:MygrammarParser.Other_opContext):
        pass

    # Exit a parse tree produced by MygrammarParser#other_op.
    def exitOther_op(self, ctx:MygrammarParser.Other_opContext):
        pass


    # Enter a parse tree produced by MygrammarParser#input.
    def enterInput(self, ctx:MygrammarParser.InputContext):
        pass

    # Exit a parse tree produced by MygrammarParser#input.
    def exitInput(self, ctx:MygrammarParser.InputContext):
        pass


    # Enter a parse tree produced by MygrammarParser#return_statement.
    def enterReturn_statement(self, ctx:MygrammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#return_statement.
    def exitReturn_statement(self, ctx:MygrammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#show_statement.
    def enterShow_statement(self, ctx:MygrammarParser.Show_statementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#show_statement.
    def exitShow_statement(self, ctx:MygrammarParser.Show_statementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#use_func.
    def enterUse_func(self, ctx:MygrammarParser.Use_funcContext):
        pass

    # Exit a parse tree produced by MygrammarParser#use_func.
    def exitUse_func(self, ctx:MygrammarParser.Use_funcContext):
        pass


    # Enter a parse tree produced by MygrammarParser#for_statement.
    def enterFor_statement(self, ctx:MygrammarParser.For_statementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#for_statement.
    def exitFor_statement(self, ctx:MygrammarParser.For_statementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#if_statement.
    def enterIf_statement(self, ctx:MygrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by MygrammarParser#if_statement.
    def exitIf_statement(self, ctx:MygrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by MygrammarParser#if_condition.
    def enterIf_condition(self, ctx:MygrammarParser.If_conditionContext):
        pass

    # Exit a parse tree produced by MygrammarParser#if_condition.
    def exitIf_condition(self, ctx:MygrammarParser.If_conditionContext):
        pass



del MygrammarParser