# flake8: noqa: C901

from datetime import datetime
from graphviz import Digraph


class GraphvizPrinter:
    """
    GraphvizPrinter will render and export all given ast as graphviz graphs
    """

    def __init__(self, tokens):
        """
        Construct a new GraphvizPrinter object.

        :ast: A Yalul's lex tokens
        :return: returns nothing
        """
        self.tokens = tokens

    def generate_pdf(self):
        graph = Digraph(comment='Lex tokens', node_attr={'shape': 'record', 'height': '.1'})

        for index, token in enumerate(self.tokens):
            self.__render_lex_token(graph, token, index)

        graph.render('yalul-renders/lex-tokens-{}.gv'.format(datetime.now().strftime('%Y-%m-%d-%H:%M:%S')), view=True)

    def __render_lex_token(self, graph, token, number):
        token_name = 'Lex_token{}'.format(number)

        graph.node(token_name, '<f0> Token|<f1> {}'.format(token))

        if number != 0:
            previous_token = 'Lex_token{}'.format(number - 1)
            graph.edge('{}:f0'.format(previous_token), '{}:f0'.format(token_name))
