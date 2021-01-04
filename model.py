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
from user_interface import UserInterface


class Player:
    """Robot player"""

    def __init__(self, username: str = 'Computer'):
        self._username = username
        self.__score = 0
        self._choice = ''  # game choice: 'rock'

    @property
    def username(self):
        return self._username

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def choice(self):
        return self._choice

    # @choice.setter
    # def choice(self, choice):
    #     self._choice = choice

    def make_game_choice(self, options: list):
        """Randomly chooses one component from the list

        Args:
             options (list): - list of game options
                        ex: ['rock', 'paper', etc.]

        Returns:
            npc_choice (str): - npc choice
                        ex: 'rock'

        """
        import random
        self._choice = random.choice(options)
        # return self._choice


class HumanPlayer(Player):
    """Human player"""
    def __init__(self):
        super().__init__()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    def make_game_choice(self, options: list):
        """

        Args:
             options (list): - list of game options
                        ex: ['rock', 'paper', etc.]

        Returns:
            npc_choice (str): - npc choice
                        ex: 'rock'

        """

        ui = UserInterface()

        self._choice = ui.ask_usr_and_validate_int(options)
        # return self._choice


class GameSession:

    available_games: list
    chosen_game: str
    rules: str
    components: list
    win_dict: dict

    def __init__(self):
        self.available_games = []
        self.chosen_game = ''
        self.rules = ''
        self.components = []
        self.win_dict = {}

    @staticmethod
    def get_available_games(directory: str = 'Rules') -> list:
        """Returns a list of files (game rules) in 'Rules' directory

            Returns:
                game_files (list(str)): list of strings with name of
                            files in the 'Rules' directory
                            ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

        """
        import os
        game_files = os.listdir(directory)
        return sorted(game_files)

    @staticmethod
    def extract_rules(game_file_name: str) -> str:
        """Function to extract game rules from txt file.

        Args:
            game_file_name (str): string with the name of the file
                        ex: 'RPS-3.txt'

        Returns:
            rules (str): - string with game rules
                        Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                        \npaper covers rock'

        """
        game_file_name = 'Rules/' + game_file_name
        with open(game_file_name) as f:
            data = f.readlines()
        rules = ''.join(data)

        return rules

    @staticmethod
    def get_components_dict(rules: str) -> tuple:
        """Creates a dictionary from the game rules string

        Takes in rules (str) and extracts a dictionary with
            keys   = tuple(winner(str), looser(str))
            values = rule ex: "Rock breaks scissors"
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        Args:
            rules (str): - rules of the game
                    ex: 'Rock breaks scissors, \n
                        scissors cuts paper, \n
                        paper covers rock'

        Return:
            components (list): - all the components of the game
                    ex: ['rock', 'paper', 'scissors')]

            win_dic (dict): - wining dictionary - with the following form:
                    {(winner, looser) : rule}
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        """
        components = set()
        win_dic = {}

        rules_list = rules.split(', \n')
        for rule in rules_list:
            strong_component = rule.split(' ')[0].lower()
            weak_component = rule.split(' ')[-1].lower()

            if strong_component not in components:
                components.add(strong_component)

            if (strong_component, weak_component) not in win_dic.keys():
                win_dic[(strong_component, weak_component)] = rule

        return list(components), win_dic

    @staticmethod
    def determine_result(player_1_choice, player_2_choice,
                         win_dic: dict) -> tuple:
        """Determines the winner of a RPS round

        Args:
            player_1_choice (str): - human_1 answer
                    ex: 'rock'

            player_2_choice (str): - npc / human_2 answer
                    ex: 'scissors'

            win_dic (dict): - winning dictionary - with the following form:
                    {(winner, looser) : rule}
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        Returns:
            winner (str / None): - the winning choice
                                 - can be: - str: 'rock' - rock won
                                           - None:       - draw

            winning_rule (str / None): - the rule explaining the win
                                       - can be: - str: 'Rock breaks scissors'
                                                 - None: draw

        """
        # for improved readability:
        p1_c = player_1_choice
        p2_c = player_2_choice

        if p1_c != p2_c:

            if (p1_c, p2_c) in win_dic.keys():
                winner = p1_c
                winning_rule = win_dic[(p1_c, p2_c)]
            else:
                winner = p2_c
                winning_rule = win_dic[(p2_c, p1_c)]
            return winner, winning_rule

        return None, None,
