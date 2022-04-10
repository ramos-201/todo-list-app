from todo_list_app.view.commands.command import Command


class ExitAppCommand(Command):
    _description = 'Exit app'
    is_exit_app = False

    def run(self):
        self.is_exit_app = True

    @property
    def exit(self):
        return self.is_exit_app
