from abc import abstractmethod


class OptionMenu:
    _description = 'Option Menu'

    def __init__(self):
        self._commands = self._get_commands()

    @abstractmethod
    def _get_commands(self):
        pass

    def run(self):
        self._show_menu()
        option = self._get_option()
        option.run()

    def _show_menu(self):
        print(f'::: {self._description}')
        for key, value in self._commands.items():
            print(f'({key}) :  {value.description}')

    def _get_option(self):
        while True:
            response = input('> Write option (number): ')
            if response not in self._commands.keys():
                print(f'::: Invalid option')
            else:
                break
        return self._commands[response]
