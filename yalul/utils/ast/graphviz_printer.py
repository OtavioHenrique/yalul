import uuid

from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration
from yalul.parsers.ast.nodes.statements.expression import Expression
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.expressions.values.float import Float
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean
from graphviz import Digraph

VALUES_TYPES = [
    Integer,
    Null,
    String,
    Float,
    Boolean,
    Variable
]


class GraphvizPrinter:
    def __init__(self, ast):
        self.ast = ast

    def generate_pdf(self):
        dot = Digraph(comment='AST', node_attr={'shape': 'record', 'height': '.1'})

        for statement in self.ast:
            if type(statement) == VariableDeclaration:
                dot.node('VariableDeclaration', '<f0> Name|<f1> Variable Declaration|<f2> Value')
                self.__render_expression(dot, statement.initializer, 'VariableDeclaration:f2')
                dot.node('Identifier', '<f0> Identifier |<f2> {}'.format(statement.name))
                dot.edge('VariableDeclaration:f0', 'Identifier:f0')
            if isinstance(statement, Expression):
                self.__render_expression(dot, statement)

        dot.render('test-output/round-table.gv', view=True)

    def __render_expression(self, graph, expression, previous_node=None, count='0'):
        if type(expression) in VALUES_TYPES:
            expression_name = '{}{}'.format(type(expression).__name__, count)

            if type(expression) == Null:
                graph.node(expression_name, '<f0> {}'.format(type(expression).__name__))
            elif type(expression) == Boolean:
                graph.node(expression_name, '<f0> {} | <f1> {}'.format(type(expression).__name__, expression.value))
            else:
                graph.node(expression_name,
                           '<f0> {} | <f1> {}'.format(type(expression).__name__, expression.value))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f0'.format(expression_name))
        elif type(expression) == Binary:
            binary_operation_name = '{}{}'.format('BinaryOperation', count)

            graph.node(binary_operation_name, '<f0> Left | <f1> Binary Operation |<f2> Right')
            graph.node('Operator{}'.format(count), '<f0> {}'.format(expression.operator))
            graph.edge('{}:f1'.format(binary_operation_name), 'Operator{}:f0'.format(count))
            self.__render_expression(graph, expression.left, '{}:f0'.format(binary_operation_name), str(uuid.uuid4()))
            self.__render_expression(graph, expression.right, '{}:f2'.format(binary_operation_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f1'.format(binary_operation_name))

