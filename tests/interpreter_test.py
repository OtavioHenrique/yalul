from yalul.interpreter import Interpreter
from yalul.interpreters.environment import Environment
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.func_call import FuncCall
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable
from yalul.parsers.ast.nodes.statements.func import Func
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


class TestInterpreterInterpretPrintStatement:
    """
    Test Interpreter interpret_print_statement
    """

    def test_interpreting_print_statements(self, capsys):
        """Test interpreter interpreting multiple statements"""
        env = Environment({}, {})
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            Print(Grouping(String('Gabriela')))
        ])

        Interpreter.interpret_print_statement(ast.statements[0], env, error)

        captured = capsys.readouterr()

        assert captured.out == 'Gabriela\n'


class TestInterpreterInterpretVariableDeclarationStatement:
    """
    Test Interpreter interpret_variable_declaration_statement
    """

    def test_interpreting_variable_declaration_statements(self):
        """Test interpreter interpreting multiple statements"""
        env = Environment({}, {})
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            VariableDeclaration('name', String('Gabriela'))
        ])

        Interpreter.interpret_variable_declaration(ast.statements[0], env, error)

        assert env.get_variable('name') == 'Gabriela'


class TestInterpreterInterpretWhileStatement:
    """
    Test Interpreter interpret_while_statement
    """

    def test_interpreting_while_statement(self):
        """Test running a normal while statement"""

        env = Environment({
            'a': 0
        }, {})

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


class TestInterpreterInterpretFuncStatement:
    """
    Test Interpreter interpret_func_statement
    """

    def test_interpreting_func_statement(self):
        """Test running a normal func statement"""

        env = Environment({}, {})

        error = InterpreterErrors()

        func_name = 'sum'
        func_parameters = [String('a'), String('b')]
        func_block = Block([
            Return(
                Grouping(
                    Binary(
                        Variable('a'),
                        Token(TokenType.SUM, '+'),
                        Variable('b')
                    )
                )
            )
        ])

        ast = AbstractSyntaxTree([
            Func(
                func_name,
                func_parameters,
                func_block
            )
        ])

        Interpreter.interpret_func_statement(ast.statements[0], env, error)

        func = env.get_variable(func_name)

        assert func['name'] == func_name
        assert func['parameters'] == func_parameters
        assert func['block'] == func_block


class TestInterpreterInterpretFuncCall:
    """
    Test Interpreter interpret_func_call
    """

    def test_interpreting_func_call(self):
        """Test running a normal func call"""

        env = Environment({}, {})

        error = InterpreterErrors()

        func_name = 'sum'
        func_parameters = [String('a'), String('b')]
        func_block = Block([
            Return(
                Grouping(
                    Binary(
                        Variable('a'),
                        Token(TokenType.SUM, '+'),
                        Variable('b')
                    )
                )
            )
        ])

        ast = AbstractSyntaxTree([
            Func(
                func_name,
                func_parameters,
                func_block
            )
        ])

        Interpreter.interpret_func_statement(ast.statements[0], env, error)

        func_call = FuncCall(Variable('sum'), [Integer(1), Integer(41)])

        assert Interpreter.interpret_func_call(func_call, env, error) == 42


class TestInterpreterInterpretIfStatement:
    """
    Test Interpreter interpret_if_statement
    """

    def test_interpreting_if_statement(self):
        """Test running a normal if statement without else"""

        env = Environment({
            'a': 0
        }, {})

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
        """Test running a normal if statement with else block"""

        env = Environment({
            'a': 0
        }, {})

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
