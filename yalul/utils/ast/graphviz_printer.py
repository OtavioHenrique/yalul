# flake8: noqa: C901

import uuid
from datetime import datetime

from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.func_call import FuncCall
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable
from yalul.parsers.ast.nodes.statements.func import Func
from yalul.parsers.ast.nodes.statements.if_statement import If
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration
from yalul.parsers.ast.nodes.statements.expression import Expression
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.expressions.values.float import Float
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean
from yalul.parsers.ast.nodes.statements.while_statement import While
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

        graph.node('AST', '<f0> Abstract Syntax Tree|<f1> Statements')

        for statement in self.ast.statements:
            self.__render_statement(graph, statement, 'AST:f1')

        graph.render('yalul-renders/ast-print-{}.gv'.format(datetime.now().strftime('%Y-%m-%d-%H:%M:%S')), view=True)

    def __render_statement(self, graph, statement, previous_node=None, identifier=None):
        if type(statement) == VariableDeclaration:
            self.__render_var_declaration_statement(graph, statement, previous_node, identifier)
        if type(statement) == Block:
            self.__render_block_statement(graph, statement, previous_node, identifier)
        if type(statement) == If:
            self.__render_if_statement(graph, statement, previous_node, identifier)
        if isinstance(statement, Expression):
            self.__render_expression(graph, statement, previous_node, identifier)
        if type(statement) == Func:
            self.__render_func(graph, statement, previous_node, identifier)
        if type(statement) == While:
            self.__render_while(graph, statement, previous_node, identifier)

    def __render_while(self, graph, statement, previous_node, identifier):
        while_name = 'while{}'.format(identifier)

        graph.node(while_name, '<f0> Condition|<f1> While Statement|<f2> Block')

        self.__render_expression(graph, statement.condition, '{}:f0'.format(while_name))
        self.__render_block_statement(graph, statement.block, '{}:f2'.format(while_name), str(uuid.uuid4()))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(while_name))

    def __render_func(self, graph, statement, previous_node, identifier):
        func_graph_name = '{}{}'.format('FuncStatement', identifier)

        graph.node(func_graph_name, '<f0> Identifier|<f1> Func Statement|<f2> Parameters|<f3> Block')
        graph.node(statement.identifier, '<f0> Func Identifier|<f1> {}'.format(statement.identifier))
        graph.edge('{}:f0'.format(func_graph_name), '{}:f0'.format(statement.identifier))

        for parameter in statement.parameters:
            parameter_name = 'Parameter{}{}'.format(parameter.value, identifier)
            graph.node(parameter_name, '<f0> {}'.format(parameter.value))
            graph.edge('{}:f2'.format(func_graph_name), '{}:f0'.format(parameter_name))

        self.__render_block_statement(graph, statement.block, '{}:f3'.format(func_graph_name), str(uuid.uuid4()))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(func_graph_name))

    def __render_if_statement(self, graph, statement, previous_node, identifier):
        if_name = '{}{}'.format('IfStatement', identifier)

        graph.node(if_name, '<f0> Condition|<f1> If Statement|<f2> Then Block|<f3> Else Block')

        self.__render_expression(graph, statement.condition, '{}:f0'.format(if_name))

        self.__render_block_statement(graph, statement.then_block, '{}:f2'.format(if_name), str(uuid.uuid4()))
        self.__render_block_statement(graph, statement.else_block, '{}:f3'.format(if_name), str(uuid.uuid4()))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(if_name))

    def __render_var_declaration_statement(self, graph, statement, previous_node=None, identifier=None):
        var_declaration_name = '{}{}'.format('VarDeclaration', identifier)

        graph.node(var_declaration_name, '<f0> Name|<f1> Variable Declaration|<f2> Value')

        self.__render_expression(graph, statement.initializer, '{}:f2'.format(var_declaration_name))

        identifier_name = 'Identifier{}'.format(identifier)

        graph.node(identifier_name, '<f0> Identifier |<f2> {}'.format(statement.name))
        graph.edge('{}:f0'.format(var_declaration_name), '{}:f0'.format(identifier_name))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(var_declaration_name))

    def __render_block_statement(self, graph, statement, previous_node, identifier):
        block_name = '{}{}'.format('Block', identifier)

        graph.node(block_name, '<f0> Block | <f1> Statements')

        for block_statement in statement.statements:
            self.__render_statement(graph, block_statement, '{}:f1'.format(block_name), str(uuid.uuid4()))

        if previous_node is not None:
            graph.edge(previous_node, '{}:f1'.format(block_name))

    def __render_expression(self, graph, expression, previous_node=None, identifier=None):
        expression_name = '{}{}'.format(type(expression).__name__, identifier)

        if type(expression) in VALUES_TYPES:
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
            graph.node(expression_name, '<f0> Left | <f1> Binary Operation |<f2> Right')
            graph.node('Operator{}'.format(identifier), '<f0> {}'.format(expression.operator))
            graph.edge('{}:f1'.format(expression_name), 'Operator{}:f0'.format(identifier))
            self.__render_expression(graph, expression.left, '{}:f0'.format(expression_name), str(uuid.uuid4()))
            self.__render_expression(graph, expression.right, '{}:f2'.format(expression_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f1'.format(expression_name))
        elif type(expression) == Grouping:
            graph.node(expression_name, '<f0> Grouping | <f1> Expression')

            self.__render_expression(graph, expression.value, '{}:f1'.format(expression_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f0'.format(expression_name))
        elif type(expression) == Return:
            graph.node(expression_name, '<f0> Return | <f1> Expression')

            self.__render_expression(graph, expression.value, '{}:f1'.format(expression_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f0'.format(expression_name))
        elif type(expression) == VarAssignment:
            graph.node(expression_name, '<f0> Identifier | <f1> Variable Assignment |<f2> Value')
            graph.node('VarName{}'.format(identifier), '<f0> {}'.format(expression.identifier))
            graph.edge('{}:f0'.format(expression_name), 'VarName{}:f0'.format(identifier))
            self.__render_expression(graph, expression.value, '{}:f2'.format(expression_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f1'.format(expression_name))
        elif type(expression) == FuncCall:
            graph.node(expression_name, '<f0> Callee | <f1> Func Call |<f2> Arguments')
            self.__render_expression(graph, expression.callee, '{}:f0'.format(expression_name), str(uuid.uuid4()))

            for argument in expression.arguments:
                self.__render_expression(graph, argument, '{}:f2'.format(expression_name), str(uuid.uuid4()))

            if previous_node is not None:
                graph.edge(previous_node, '{}:f1'.format(expression_name))
