import rps_exceptions as re


class UserInterface:

    @staticmethod
    def ask_user(message: str) -> str:
        return input('\n' + message + '\n>')

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
                                    {'label': '',
                                     'func': FUNC}
                               }

        """
        menu_dict = {}

        # if menu_data has VERSION 1:
        if len(str(menu_data[0][1])) > 1:

            for i in menu_data:
                menu_dict[i[0]] = {'label': i[1], 'func': i[2]}
            return menu_dict

        # if menu_data has VERSION 2:
        else:
            for i in range(len(menu_data[0])):
                menu_dict[menu_data[0][i]] = {'label': menu_data[1][i],
                                              'func': menu_data[2][i]}
            return menu_dict

    @staticmethod
    def ask_usr_and_validate_str(choice_options):
        while True:
            try:
                choice = input('---> Your choice: ').upper()
                if choice not in choice_options:
                    raise re.ChoiceError
            except re.ChoiceError:
                print('\nInvalid choice!')
            else:
                return choice

    @staticmethod
    def ask_usr_and_validate_int(choice_options):
        """choose a game from the list where we need to
        pick by using integers.

        Args:
            choice_options (list(str)): list of strings
                        ex: name of files in the 'Rules' directory
                        ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

        Returns:
            chosen_game (str): string
                        ex: the name of the file
                        ex: 'RPS-3.txt'

        """
        while True:
            try:
                choice = int(input('---> Your choice: '))
                if choice not in list(range(1, len(choice_options) + 1)):
                    raise re.ChoiceError
            except (re.ChoiceError, ValueError):
                print('\nInvalid choice!')
            else:
                final_choice = choice_options[choice - 1]
                return final_choice

    def chose_menu(self, choice_options, menu: dict):
        choice = self.ask_usr_and_validate_str(choice_options)
        menu[choice]['func']()
