"""
CONTROLLER:

- accepts user input
- delegates:
        - data representation to VIEW
        - data handling       to MODEL
"""
from view import View
from model import UserInterface


class Controller:

    def __init__(self, view: View, ui: UserInterface):
        self.view = view
        self.ui = ui

    def play_game(self):

        # print welcome message:
        self.view.message_welcome()


def main():
    c = Controller(View(), UserInterface())
    c.play_game()


if __name__ == '__main__':
    main()
