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
        description = 'A game of Rock Paper Scissors and its variants!'
        print()
        prt_delimiter(len(description), '=')
        print(f'{welcome_msg:^{len(description)}}')
        print(f'{game_name:^{len(description)}}')
        prt_delimiter(len(description), '=')
        print(description)
        prt_delimiter(len(description), '=')

    @staticmethod
    def prt_menu_title(title: str):
        print()
        print(title)

    @staticmethod
    def prt_menu(menu_dict: dict):
        for k in menu_dict.keys():
            print(f"({k}) {menu_dict[k]['label']}")

    def prt_menu_all(self, title: str, menu_dict: dict):
        self.prt_menu_title(title)
        self.prt_menu(menu_dict)

    @staticmethod
    def prt_games_menu(game_files: list):
        """Prints the lists of available games

            Args:
                 game_files (list(str)): list of strings with name of
                            files in the 'Rules' directory
                            ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

            """

        print()
        print('Available games:')
        for index, game in enumerate(game_files):
            print(f'({index + 1}) {game[:-4]}')

    @staticmethod
    def prt_rules(rules: str):
        """Prints the rules of the games

        Args:
             rules (str): - string with game rules
                        Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                        \npaper covers rock'

        """

        print()
        print('--- Game Rules: ---')
        print(rules)

    @staticmethod
    def prt_options(components: list):
        """ Prints the options to choose from.

        Args:
            components (list): - game options (components)
                        ex: ['rock', 'paper', etc.]

        """
        print()
        print('Available options: ')
        for index, k in enumerate(components):
            print(f'({index + 1}) {k}')

    @staticmethod
    def print_outcome(winner: str, winning_rule: str,
                      player_1: str, player_2: str):
        """Prints the outcome of the round

        Args:
            winner (str / None): - the winning choice
                                 - can be: - str: 'rock' - rock won
                                           - None:       - draw

            winning_rule (str / None): - the rule explaining the win
                                       - can be: - str: 'Rock breaks scissors'
                                                 - None: draw

            player_1 (str): - player choice
                        ex: 'rock'

            player_2 (str): - player choice
                        ex: 'rock'

        """

        if not winner:
            print('Draw!', '=')
        else:
            msg = 'AAAAAA'
            if player_1 == winner:
                msg = f'You win! {winning_rule}'
            elif player_2 == winner:
                msg = f'You lose! {winning_rule}'
            print(msg, '=')

    @staticmethod
    def unknown_user_message():

        msg = 'Unknown user!'

        print()
        prt_delimiter(len(msg), '!')
        print(msg)
        prt_delimiter(len(msg), '!')

    @staticmethod
    def invalid_password_message():

        msg = 'Invalid password. Please try again'

        print()
        prt_delimiter(len(msg), '!')
        print(msg)
        prt_delimiter(len(msg), '!')

    @staticmethod
    def print_old_user_message(username):
        print()
        print(f'Welcome back, {username}!')
