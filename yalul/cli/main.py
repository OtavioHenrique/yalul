import click
from yalul.source import Source


@click.command()
def execute():
    click.echo(
        'Welcome to yalul, acronym for "Yet another language to understand languages"\n\n'
        'yalul is a simple tree-walk interpreter written in python for easy understanding and study of programming '
        'languages, compilers and interpreters. '
    )
