"""
VIEW:

- presents data to the user
- NEVER call its own methods
"""
from view_utils import prt_delimiter


class View:

    @staticmethod
    def message_welcome():
        welcome_msg = 'Welcome to'
        game_name = 'RPS'
        msg_2 = 'A game of Rock Paper Scissors and its variants!'
        print()
        prt_delimiter(len(msg_2), '=')
        print(f'{welcome_msg:^{len(msg_2)}}')
        print(f'{game_name:^{len(msg_2)}}')
        prt_delimiter(len(msg_2), '=')
        print(msg_2)
        prt_delimiter(len(msg_2), '=')

