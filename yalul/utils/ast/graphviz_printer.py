from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration
from yalul.parsers.ast.nodes.statements.expression import Expression
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from graphviz import Digraph


class GraphvizPrinter:
    def __init__(self, ast):
        self.ast = ast

    def generate_pdf(self):
        dot = Digraph(comment='AST', node_attr={'shape': 'record', 'height': '.1'})

        for statement in self.ast:
            if type(statement) == VariableDeclaration:
                dot.node('VariableDeclaration', '<f0> Name|<f1> Variable Declaration|<f2> Value')
                self.__render_expression(dot, statement.initializer, 'VariableDeclaration:f2')
                dot.node('Identifier', '<f0> Name | <f1> Identifier |<f2> {}'.format(statement.name))
                dot.edge('VariableDeclaration:f0', 'Identifier:f0')
            if isinstance(statement, Expression):
                self.__render_expression(dot, statement)

        dot.render('test-output/round-table.gv', view=True)

    def __render_expression(self, graph, expression, previous_node=None):
        if type(expression) == Integer:
            graph.node('Integer', '<f0> Value | <f1> {}'.format(expression.value))

            if previous_node is not None:
                graph.edge(previous_node, 'Integer:f0')
