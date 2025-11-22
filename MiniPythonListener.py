# Generated from MiniPython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPythonParser import MiniPythonParser
else:
    from MiniPythonParser import MiniPythonParser

# This class defines a complete listener for a parse tree produced by MiniPythonParser.
class MiniPythonListener(ParseTreeListener):

    # Enter a parse tree produced by MiniPythonParser#file_input.
    def enterFile_input(self, ctx:MiniPythonParser.File_inputContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#file_input.
    def exitFile_input(self, ctx:MiniPythonParser.File_inputContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#stmt.
    def enterStmt(self, ctx:MiniPythonParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#stmt.
    def exitStmt(self, ctx:MiniPythonParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#small_stmt.
    def enterSmall_stmt(self, ctx:MiniPythonParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#small_stmt.
    def exitSmall_stmt(self, ctx:MiniPythonParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:MiniPythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:MiniPythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#compound_stmt.
    def enterCompound_stmt(self, ctx:MiniPythonParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#compound_stmt.
    def exitCompound_stmt(self, ctx:MiniPythonParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniPythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniPythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#block.
    def enterBlock(self, ctx:MiniPythonParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#block.
    def exitBlock(self, ctx:MiniPythonParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#test.
    def enterTest(self, ctx:MiniPythonParser.TestContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#test.
    def exitTest(self, ctx:MiniPythonParser.TestContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#expr.
    def enterExpr(self, ctx:MiniPythonParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#expr.
    def exitExpr(self, ctx:MiniPythonParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#or_test.
    def enterOr_test(self, ctx:MiniPythonParser.Or_testContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#or_test.
    def exitOr_test(self, ctx:MiniPythonParser.Or_testContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#and_test.
    def enterAnd_test(self, ctx:MiniPythonParser.And_testContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#and_test.
    def exitAnd_test(self, ctx:MiniPythonParser.And_testContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#not_test.
    def enterNot_test(self, ctx:MiniPythonParser.Not_testContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#not_test.
    def exitNot_test(self, ctx:MiniPythonParser.Not_testContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#comparison.
    def enterComparison(self, ctx:MiniPythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#comparison.
    def exitComparison(self, ctx:MiniPythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#comp_op.
    def enterComp_op(self, ctx:MiniPythonParser.Comp_opContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#comp_op.
    def exitComp_op(self, ctx:MiniPythonParser.Comp_opContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#arith_expr.
    def enterArith_expr(self, ctx:MiniPythonParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#arith_expr.
    def exitArith_expr(self, ctx:MiniPythonParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#term.
    def enterTerm(self, ctx:MiniPythonParser.TermContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#term.
    def exitTerm(self, ctx:MiniPythonParser.TermContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#factor.
    def enterFactor(self, ctx:MiniPythonParser.FactorContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#factor.
    def exitFactor(self, ctx:MiniPythonParser.FactorContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#atom.
    def enterAtom(self, ctx:MiniPythonParser.AtomContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#atom.
    def exitAtom(self, ctx:MiniPythonParser.AtomContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#list_literal.
    def enterList_literal(self, ctx:MiniPythonParser.List_literalContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#list_literal.
    def exitList_literal(self, ctx:MiniPythonParser.List_literalContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#assignment.
    def enterAssignment(self, ctx:MiniPythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#assignment.
    def exitAssignment(self, ctx:MiniPythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#assignment_op.
    def enterAssignment_op(self, ctx:MiniPythonParser.Assignment_opContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#assignment_op.
    def exitAssignment_op(self, ctx:MiniPythonParser.Assignment_opContext):
        pass



del MiniPythonParser