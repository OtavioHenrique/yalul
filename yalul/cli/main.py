import click
from yalul.lexer import Lexer
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.utils.ast_printer import ASTPrinter


@click.command()
@click.option("--render-ast", help="Render code AST as pdf", is_flag=True)
@click.argument('filename', required=False)
def execute(filename, render_ast):
    if filename is None:
        click.echo(
            'Welcome to yalul, acronym for "Yet another language to understand languages"\n\n'
            'yalul is a simple tree-walk interpreter written in python for easy understanding and study of programming '
            'languages, compilers and interpreters. '
        )
    else:
        source_file = open(filename, 'r')
        tokens = Lexer(source_file).run()

        errors = list(filter(lambda x: x.type == TokenType.ERROR, tokens))

        if errors is None:
            for token in tokens:
                click.echo(token)
        else:
            for error in errors:
                click.echo(error.value)

        parser_response = Parser(tokens).parse()

        if render_ast:
            ASTPrinter(parser_response.asts).print()

        print(parser_response.errors.errors)
