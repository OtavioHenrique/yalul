from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.parsers.ast.nodes.statements.expression import Expression
from yalul.interpreters.expression import ExpressionInterpreter

INTERPRETERS = {}


class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def run(self):
        for statement in self.ast.statements:
            error = InterpreterErrors()

            response = self.interpret(statement, error)

            if error.errors:
                for interpreter_error in error.errors:
                    print(interpreter_error)

                next
            else:
                print(response)

    def interpret(self, statement, error):
        if INTERPRETERS.get(type(statement)):
            return None
        elif isinstance(statement, Expression):
            return ExpressionInterpreter.execute(statement, error)
        else:
            return None
