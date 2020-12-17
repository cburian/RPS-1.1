"""
MODEL

- business logic
- manages data
- defines rules and behaviours
- data can be stored in:
            - MODEL
            - database
- only MODEL has access to database

Has to do:
    - return available games
    - extract rules
"""
import rps_exceptions as re


class UserInterface:

    @staticmethod
    def ask_user(message: str) -> str:
        return input('\n' + message + '\n>')

    # @staticmethod
    # def inform_user(message: str) -> None:
    #     print(message)

    @staticmethod
    def make_menu(menu_data: list) -> dict:
        """

        Args:
            =============================================================
            menu_data (list(tuple)) - VERSION 1:
                                    [(character1, string1, func1),
                                     (character2, string2, func2)]

                ex: ('N', 'New game', play_game)
                        for menu entry:
                     (N) New game
                play_game - function to be executed when player chooses N
            -------------------------------------------------------------
            menu_data (list(tuple)) - VERSION 2:
                                     [(char1, char2,),
                                      (string1, string2,)
                                      (func1, func2,)]

                ex: [('N', 'Q'),
                     ('New Game', 'Quit to main menu'),
                     (new_game_func, quit_to_main_func)]
            =============================================================

        Returns:
            menu_dict (dict): {'char':
                                    {'label': ''},
                                    {'func': FUNC}
                               }

        """
        menu_dict = {}

        # if menu_data has VERSION 1:

        if len(menu_data[0][1]) > 1:

            for i in menu_data:
                menu_dict[i[0]] = {'label': i[1], 'func': i[2]}
            return menu_dict

        else:
            for i in range(len(menu_data[0])):
                menu_dict[menu_data[0][i]] = {'label': menu_data[1][i],
                                              'func': menu_data[2][i]}
            return menu_dict

    @staticmethod
    def show_menu(menu_dict: dict) -> None:
        for k in menu_dict.keys():
            print(f"({k}) {menu_dict[k]['label']}")

    @staticmethod
    def validate_input(choice_options):
        while True:
            try:
                choice = input('\n---> Your choice: ').lower()
                if choice not in choice_options:
                    raise re.ChoiceError
            except re.ChoiceError:
                print('\nInvalid choice!')
            else:
                return choice


class Player:
    pass


class HumanPlayer(Player):
    pass


class Game:
    pass
