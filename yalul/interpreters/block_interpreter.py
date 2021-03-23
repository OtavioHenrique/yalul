from yalul.interpreters.environment import Environment
from yalul.interpreter import Interpreter
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return


class BlockInterpreter:
    """
    ExpressionInterpreter interprets all statements of type expression
    """

    def __init__(self, statements, environment, errors):
        self.statements = statements
        self.environment = environment
        self.errors = errors

    def execute(self):
        """
        Interpret given expression
        """

        block_env = Environment(self.env.show_environment_table())

        for statement in self.statements:
            result = Interpreter.interpret(statement, block_env, self.errors)

            if type(statement) == Return:
                return result
