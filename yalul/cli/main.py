import click
from yalul.source import Source

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
        source = Source(source_file)
        click.echo(source.read())
