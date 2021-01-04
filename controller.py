"""
CONTROLLER:

- accepts user input
- delegates:
        - data representation to VIEW
        - data handling       to MODEL
"""
import rps_exceptions as re
from view import View
from model import GameSession, Player, HumanPlayer
from menus import Menu
from user_interface import UserInterface


class Controller:

    def __init__(self, view: View, ui: UserInterface,
                 gs: GameSession, menu: Menu,
                 player1: HumanPlayer, player2: Player):
        self.view = view
        self.ui = ui
        self.gs = gs
        self.m = menu
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        self.view.prt_options(self.gs.components)
        self.player1.make_game_choice(self.gs.components)
        self.player2.make_game_choice(self.gs.components)

        winner, winning_rule = self.gs.determine_result(
            self.player1.choice,
            self.player2.choice,
            self.gs.win_dict
        )

        self.view.print_outcome(winner, winning_rule,
                                self.player1.choice,
                                self.player2.choice)

    def play_game_session(self):

        # 2. available games:
        # 2.1. get:
        self.gs.available_games = self.gs.get_available_games()
        # 2.2. print:
        self.view.prt_games_menu(self.gs.available_games)
        # 2.3. choose the game to play
        self.gs.chosen_game = self.ui.ask_usr_and_validate_int(
            self.gs.available_games)

        # 3. print rules for the chosen game
        # 3.1. extract the rules:
        self.gs.rules = self.gs.extract_rules(self.gs.chosen_game)
        # 3.2. print the rules:
        self.view.prt_rules(self.gs.rules)

        # 4. get components and win_dictionary:
        self.gs.components, self.gs.win_dict = self.gs.get_components_dict(
            self.gs.rules)

        self.play_round()

    def play_continuous(self):
        while True:
            try:
                another_round = input('\nPlay another round? Y/N: ').lower()

                if another_round not in ['y', 'n']:
                    raise re.ChoiceError
                if another_round == 'n':
                    break

            except re.ChoiceError:
                print('Please chose YES or NO (Y/N)!')

            else:
                self.play_round()

    def play_game(self):
        # 1. print welcome message:
        self.view.message_welcome()

        # main menu:
        self.view.prt_menu(self.m.main_menu_dict)
        self.ui.chose_menu(self.m.main_menu_dict.keys(),
                           self.m.main_menu_dict)





        # play game session
        self.play_game_session()
        self.play_continuous()


def main():
    c = Controller(View(), UserInterface(), GameSession(), Menu(),
                   HumanPlayer(), Player())
    c.play_game()


if __name__ == '__main__':
    main()
