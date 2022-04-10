from todo_list_app.controller.create_task_contr import CreateTask
from todo_list_app.controller.filter_task_contr import FilterTask
from todo_list_app.view.commands.command import Command
from todo_list_app.view.commands.utils import show_task, get_deadline


class CreateTaskCommand(Command):
    _description = 'Create task'

    def run(self):
        title = input('Title task : ')
        description = input('Description task : ')
        deadline = get_deadline().strftime('%Y-%m-%d')
        data_create = CreateTask(data={
            "title": title,
            "deadline": deadline,
            "description": description
        }).response()

        if data_create.get('response') == "success":
            data_filter_task = FilterTask(data={
                "action": "filter",
                "data_filter": {"id": data_create.get("data")["id"]}
            }).response()
            if data_filter_task.get("response") == "success":
                show_task(text=f'New created task', tasks=data_filter_task.get("data")["data_task"])
        else:
            print("Error, no se creo la tarea")
