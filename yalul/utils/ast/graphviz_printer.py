import uuid

from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
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
    """
    GraphvizPrinter will render and export all given ast as graphviz graphs
    """
    def __init__(self, ast):
        """
        Construct a new GraphvizPrinter object.

        :ast: A Yalul's abstract syntax tree
        :return: returns nothing
        """
        self.ast = ast

    def generate_pdf(self):
        graph = Digraph(comment='AST', node_attr={'shape': 'record', 'height': '.1'})

        for statement in self.ast:
            self.__render_statement(graph, statement)

        graph.render('test-output/round-table.gv', view=True)

    def __render_statement(self, graph, statement, previous_node=None, identifier=None):
        if type(statement) == VariableDeclaration:
            self.__render_var_declaration_statement(graph, statement, previous_node, identifier)
        if type(statement) == Block:
            self.__render_block_statement(graph, identifier, previous_node, statement)
        if isinstance(statement, Expression):
            self.__render_expression(graph, statement, previous_node, statement)

    def __render_var_declaration_statement(self, graph, statement, previous_node=None, identifier=None):
        var_declaration_name = '{}{}'.format('VarDeclaration', identifier)

        graph.node(var_declaration_name, '<f0> Name|<f1> Variable Declaration|<f2> Value')

        self.__render_expression(graph, statement.initializer, '{}:f2'.format(var_declaration_name))

        identifier_name = 'Identifier{}'.format(identifier)

        graph.node(identifier_name, '<f0> Identifier |<f2> {}'.format(statement.name))
        graph.edge('{}:f0'.format(var_declaration_name), '{}:f0'.format(identifier_name))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(var_declaration_name))

    def __render_block_statement(self, graph, identifier, previous_node, statement):
        block_name = '{}{}'.format('Block', identifier)

        graph.node(block_name, '<f0> Block | <f1> Statements')

        for block_statement in statement.statements:
            self.__render_statement(graph, block_statement, '{}:f1'.format(block_name), str(uuid.uuid4()))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(block_name))

    def __render_expression(self, graph, expression, previous_node=None, identifier=None):
        if type(expression) in VALUES_TYPES:
            expression_name = '{}{}'.format(type(expression).__name__, identifier)

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
            binary_operation_name = '{}{}'.format('BinaryOperation', identifier)

            graph.node(binary_operation_name, '<f0> Left | <f1> Binary Operation |<f2> Right')
            graph.node('Operator{}'.format(identifier), '<f0> {}'.format(expression.operator))
            graph.edge('{}:f1'.format(binary_operation_name), 'Operator{}:f0'.format(identifier))
            self.__render_expression(graph, expression.left, '{}:f0'.format(binary_operation_name), str(uuid.uuid4()))
            self.__render_expression(graph, expression.right, '{}:f2'.format(binary_operation_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f1'.format(binary_operation_name))
        elif type(expression) == Grouping:
            grouping_name = '{}{}'.format(type(expression).__name__, identifier)

            graph.node(grouping_name, '<f0> Grouping | <f1> Expression')

            self.__render_expression(graph, expression.value, '{}:f1'.format(grouping_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f0'.format(grouping_name))
