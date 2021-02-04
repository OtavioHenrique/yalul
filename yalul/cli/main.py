import click
from yalul.lexer import Lexer
from yalul.lex.token_type import TokenType


@click.command()
@click.argument('filename', required=False)
def execute(filename):
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
