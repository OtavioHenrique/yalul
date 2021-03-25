import tempfile
import uuid

from yalul.interpreter import Interpreter
from yalul.interpreters.environment import Environment
from yalul.lex.token_type import TokenType
from yalul.lexer import Lexer
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class Repl:
    @staticmethod
    def start():
        print('\n\nWelcome to Yalul REPL, to quit just type quit\n\n')

        user_input = None

        repl_environment = Environment({}, {})

        with tempfile.TemporaryDirectory() as tmp_dirname:
            while user_input != 'quit':
                user_input = input("Yalul v0.0.1 > ")

                tmp_file_name = '{}/run{}.yalul'.format(tmp_dirname, str(uuid.uuid4()))

                tmp_file = open(tmp_file_name, 'w')
                tmp_file.write(user_input)
                tmp_file.close()

                with open(tmp_file_name, 'r') as temp_file:
                    tokens = Lexer(temp_file).run()

                    errors = list(filter(lambda x: x.type == TokenType.ERROR, tokens))

                    if errors is None:
                        for token in tokens:
                            print(token)
                    else:
                        for error in errors:
                            print(error.value)

                    parser_response = Parser(tokens).parse()

                    if parser_response.errors():
                        print(parser_response.errors())

                    response = Interpreter(parser_response.ast, repl_environment).run()

                    print('=> ', end='')

                    if isinstance(response, str):
                        print('"{}"'.format(response))
                    elif response is None:
                        print('null')
                    else:
                        print(response)
