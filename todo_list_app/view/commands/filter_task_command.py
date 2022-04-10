from todo_list_app.controller.filter_task_contr import FilterTask
from todo_list_app.view.commands.command import Command
from todo_list_app.view.commands.utils import show_task


class FilterTaskCommand(Command):
    _description = 'Read task'

    def run(self):
        option = input('Filter all task?: (yes) | continue: (enter): ')
        data = {}
        if option == 'yes':
            get_tasks = FilterTask(data={"action": "all"}).response()
        else:
            id_task = input('Filter id: ')
            status = input('Filter status: ')
            title = input('Filter title: ')

            prepare_data = {
                'id': id_task,
                'status': status,
                'title': title
            }

            for key, value in prepare_data.items():
                if value != '':
                    data[key] = value

            get_tasks = FilterTask(data={
                "action": "filter",
                "data_filter": data
            }).response()
        if get_tasks.get("response") == "success":
            show_task(text='Tasks', tasks=get_tasks.get("data")["data_task"])
        else:
            print("no se encontro las tareas")
