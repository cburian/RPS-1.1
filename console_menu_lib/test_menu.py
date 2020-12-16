from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem

menu = ConsoleMenu(title='Menu Title', subtitle='Subtitle')

command_item = CommandItem('Run a console command!', 'touch.txt')
function_item = FunctionItem('call a function', input, ['enter input'])

submenu = ConsoleMenu('a submenu')
submenu_item = SubmenuItem('show a submenu', submenu, menu=menu)

menu.append_item(command_item)
menu.append_item(function_item)
menu.append_item(submenu_item)

# menu.start()

# menu.join()

menu.show()

