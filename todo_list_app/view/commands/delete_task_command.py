from todo_list_app.controller.delete_task_cotr import DeleteTask
from todo_list_app.view.commands.command import Command
from todo_list_app.view.commands.utils import show_task


class DeleteTaskCommand(Command):
    _description = 'Delete task'

    def run(self):
        id_task = input('Id task delete : ')

        data_delete = DeleteTask(data={"id": id_task}).response()

        if data_delete.get("response") == "success":
            print("Se elimino la tarea: ")
        else:
            print("No se elimino la tarea: ", data_delete.get("data")["message"])
