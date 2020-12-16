from userinterface import UserInterface


class App:
    """The main class of the app."""

    def __init__(self):
        self.ui = UserInterface()

    @staticmethod
    def method1():
        print("Method 1: Success!")

    @staticmethod
    def method2():
        print("Method 2: Success!")

    @staticmethod
    def method3():
        print("Method 3: Success!")

    def app_menu(self):
        """The main menu of the app."""

        # The nested dict to be sent as an argument
        main_menu = {
            1: {
                "label": "Method 1",
                "func": self.method1
            },
            2: {
                "label": "Method 2",
                "func": self.method2
            },
            3: {
                "label": "Method 3",
                "func": self.method3
            }
        }

        # Menu heading and nested dict are sent as arguments
        self.ui.choose_menu("MAIN MENU", main_menu)


# Instantiate class and call the menu function
a = App()
a.app_menu()
