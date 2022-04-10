from todo_list_app.view.commands.create_task_command import CreateTaskCommand
from todo_list_app.view.commands.delete_task_command import DeleteTaskCommand
from todo_list_app.view.commands.exit_app_command import ExitAppCommand
from todo_list_app.view.commands.filter_task_command import FilterTaskCommand
from todo_list_app.view.commands.update_task_command import UpdateTaskCommand
from todo_list_app.view.menu.option_menu import OptionMenu


class MainMenu(OptionMenu):
    _description = 'Main menu'
    _exit_app_command = None

    def _get_commands(self):
        self._exit_app_command = ExitAppCommand()
        return {
            '1': CreateTaskCommand(),
            '2': UpdateTaskCommand(),
            '3': FilterTaskCommand(),
            '4': DeleteTaskCommand(),
            '5': self._exit_app_command
        }

    def run(self):
        while not self._exit_app_command.is_exit_app:
            super(MainMenu, self).run()
            if not self._exit_app_command.is_exit_app:
                input('> continue (enter): ')

