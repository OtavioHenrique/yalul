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

    def __render_expression(self, graph, expression, previous_node=None):
        if type(expression) in VALUES_TYPES:
            if type(expression) == Null:
                graph.node(type(expression).__name__, '<f0> {}'.format(type(expression).__name__))
            elif type(expression) == Boolean:
                graph.node(type(expression).__name__, '<f0> {} | <f1> {}'.format(type(expression).__name__, expression.value))
            else:
                graph.node(type(expression).__name__,
                           '<f0> {} | <f1> {}'.format(type(expression).__name__, expression.value))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f0'.format(type(expression).__name__))
