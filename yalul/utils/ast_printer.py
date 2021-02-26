from yalul.utils.ast.graphviz_printer import GraphvizPrinter


class ASTPrinter:
    """
    AST Printer will print AST on a pretty way based on supported outputs types
    """

    def __init__(self, ast, format='pdf'):
        """
        Construct a new ASTPrinter object.

        :param ast: An array of statements
        :output: Output format of the print
        :return: returns nothing
        """
        self.ast = ast
        self.format = format

    def print(self):
        """
        Print AST in the given file output
        """
        if self.format == 'pdf':
            GraphvizPrinter(self.ast).generate_pdf()
