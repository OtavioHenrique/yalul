from yalul.interpreter import Interpreter
from yalul.interpreters.environment import Environment
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable
from yalul.parsers.ast.nodes.statements.if_statement import If
from yalul.parsers.ast.nodes.statements.print import Print
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration
from yalul.parsers.ast.nodes.statements.while_statement import While


class TestInterpreter:
    """Test Interpreter"""

    def test_interpreter_running_multiple_statements(self, capsys):
        """Test interpreter interpreting multiple statements"""
        ast = AbstractSyntaxTree([
            Print(Grouping(Integer(1))),
            Print(Grouping(Integer(41)))
        ])

        interpreter = Interpreter(ast)
        interpreter.run()
        captured = capsys.readouterr()

        assert captured.out == '1\n41\n'


class TestInterpreterInterpretWhileStatement:
    """
    Test Interpreter interpret_while_statement
    """

    def test_interpreting_while_statement(self):
        """Test runing a normal while statement"""
        env = Environment({
            'a': 0
        })

        error = InterpreterErrors()

        ast = AbstractSyntaxTree([
            While(
                Grouping(Binary(
                    Integer(10),
                    Token(TokenType.GREATER, '>'),
                    Variable('a')
                )),
                Block([
                    VarAssignment('a', Binary(
                        Variable('a'),
                        Token(TokenType.SUM, '+'),
                        Integer(1)
                    ))
                ])
            )
        ])

        Interpreter.interpret_while_statement(ast.statements[0], env, error)

        assert env.get_variable('a') == 10


class TestInterpreterInterpretIfStatement:
    """
    Test Interpreter interpret_if_statement
    """

    def test_interpreting_if_statement(self):
        """Test runing a normal if statement without else"""
        env = Environment({
            'a': 0
        })

        error = InterpreterErrors()

        ast = AbstractSyntaxTree([
            If(
                Grouping(Binary(
                    Integer(10),
                    Token(TokenType.GREATER, '>'),
                    Variable('a')
                )),
                Block([
                    VarAssignment('a', Integer(10))
                ]),
                None
            )
        ])

        Interpreter.interpret_if_statement(ast.statements[0], env, error)

        assert env.get_variable('a') == 10

    def test_interpreting_if_else_statement(self):
        """Test runing a normal if statement with else block"""
        env = Environment({
            'a': 0
        })

        error = InterpreterErrors()

        ast = AbstractSyntaxTree([
            If(
                Grouping(Binary(
                    Integer(10),
                    Token(TokenType.LESS, '<'),
                    Variable('a')
                )),
                Block([
                    VarAssignment('a', Integer(10))
                ]),
                Block([
                    VarAssignment('a', Integer(42))
                ])
            )
        ])

        Interpreter.interpret_if_statement(ast.statements[0], env, error)

        assert env.get_variable('a') == 42
