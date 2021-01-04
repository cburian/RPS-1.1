from model import GameSession
from user_interface import UserInterface
import controller_utils as cu
from view import View


class Menu:

    ui: UserInterface
    gs: GameSession
    view: View
    game_files: str
    users_data: dict

    def __init__(self):
        self.ui = UserInterface()
        self.gs = GameSession()
        self.view = View()
        self.game_file = ''

        self.users_data = {}  # initialize users data
        self.get_users_data()  # actualise users data

        # main menu components:
        self.main_menu_lst = [
            ('L', 'Login', self.login),
            ('R', 'Register', self.register),
            ('Q', 'Quit Game', self.quit)]
        self.main_menu_dict = self.ui.make_menu(self.main_menu_lst)

    def get_users_data(self):
        self.users_data = cu.get_users_data()

    def print_and_chose_main_menu(self):
        self.view.prt_menu_all('Main Menu:', self.main_menu_dict)
        self.ui.chose_menu(self.main_menu_dict.keys(),
                           self.main_menu_dict)
        return

    def login(self):
        # verify if username - in database
        while True:
            username = cu.ask_for_username_password(password=False)
            if username in ['q', 'Q']:
                self.print_and_chose_main_menu()
                return
            elif username in self.users_data.keys():
                break  # continue to next while
            else:  # if username - not in database => unknown user message
                self.view.unknown_user_message()

        # verify password:
        while True:
            password = cu.ask_for_username_password()
            print('password ', password, type(password))
            print('passwords: ', self.users_data[username],
                  type(self.users_data[username]))
            if password in ['q', 'Q']:
                # back to main menu:
                self.print_and_chose_main_menu()
                return
            # password does not correspond to user
            elif password != self.users_data[username]:
                self.view.invalid_password_message()
            else:
                break  # continue to print welcome back message

        self.view.print_old_user_message(username)
        return

    def register(self):
        pass

    @staticmethod
    def quit():
        exit()



