from yalul.interpreters.expressions.binary import BinaryInterpreter
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.value import Value
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable


class ExpressionInterpreter:
    """
    ExpressionInterpreter interprets all statements of type expression
    """

    @staticmethod
    def execute(expression, environment, error):
        """
        Interpret given expression
        """
        expression_type = type(expression)

        if isinstance(expression, Value):
            return expression.value
        elif expression_type == Binary:
            left_value = ExpressionInterpreter.execute(expression.left, environment, error)
            right_value = ExpressionInterpreter.execute(expression.right, environment, error)
            operator = expression.operator.type

            return BinaryInterpreter(operator, left_value, right_value, error).execute()
        elif expression_type == Grouping:
            return ExpressionInterpreter.execute(expression.value, environment, error)
        elif expression_type == Variable:
            return environment.get_variable(expression.value)
