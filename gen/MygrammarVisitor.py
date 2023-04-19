# Generated from C:/Users/hanna/Desktop/yapis\Mygrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MygrammarParser import MygrammarParser
else:
    from MygrammarParser import MygrammarParser

# This class defines a complete generic visitor for a parse tree produced by MygrammarParser.

class MygrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MygrammarParser#program.
    def visitProgram(self, ctx:MygrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#func.
    def visitFunc(self, ctx:MygrammarParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#func_statement.
    def visitFunc_statement(self, ctx:MygrammarParser.Func_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#statement.
    def visitStatement(self, ctx:MygrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#equal.
    def visitEqual(self, ctx:MygrammarParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#operation.
    def visitOperation(self, ctx:MygrammarParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#change_type.
    def visitChange_type(self, ctx:MygrammarParser.Change_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#sum.
    def visitSum(self, ctx:MygrammarParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#other_op.
    def visitOther_op(self, ctx:MygrammarParser.Other_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#input.
    def visitInput(self, ctx:MygrammarParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#return_statement.
    def visitReturn_statement(self, ctx:MygrammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#show_statement.
    def visitShow_statement(self, ctx:MygrammarParser.Show_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#use_func.
    def visitUse_func(self, ctx:MygrammarParser.Use_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#for_statement.
    def visitFor_statement(self, ctx:MygrammarParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#if_statement.
    def visitIf_statement(self, ctx:MygrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MygrammarParser#if_condition.
    def visitIf_condition(self, ctx:MygrammarParser.If_conditionContext):
        return self.visitChildren(ctx)



del MygrammarParser