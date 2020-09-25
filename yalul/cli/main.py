import click
from yalul.lexer import Lexer
from yalul.parser import Parser

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

        for token in tokens:
            click.echo(token)