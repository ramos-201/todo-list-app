from todo_list_app.controller.filter_task_contr import FilterTask
from todo_list_app.controller.update_task_contr import UpdateTask
from todo_list_app.view.commands.command import Command
from todo_list_app.view.commands.utils import show_task


class UpdateTaskCommand(Command):
    _description = 'Update task'

    def run(self):
        id_task = input('Id update task : ')
        data_filter_task = FilterTask(data={
            "action": "filter",
            'data_filter': {'id': id_task}
        }).response()
        if data_filter_task.get("response") == "success" and \
                data_filter_task.get("data")["data_task"]:

            print(f"::: Id updated task : {data_filter_task.get('data')['data_task'][id_task].id}")
            status = input(f"Status actual = ({data_filter_task.get('data')['data_task'][id_task].status}), "
                           f"(enter) do not update : ")
            title = input(f"Title actual = ({data_filter_task.get('data')['data_task'][id_task].title}), "
                          f"(enter) do not update : ")
            description = input(f"Description actual = ({data_filter_task.get('data')['data_task'][id_task].description}), "
                                f"(enter) do not update : ")
            data = {
                "id": data_filter_task.get('data')['data_task'][id_task].id,
                "status": status if status != "" else None,
                "title": title if title != "" else None,
                "description": description if description != "" else None
            }

            data_task_update = UpdateTask(data=data).response()
            data_task_filter = FilterTask(data={
                "action": "filter",
                'data_filter': {'id': data_task_update.get('data')['id']}
            }).response()
            show_task(text=f'New created task', tasks=data_task_filter.get("data")["data_task"])

        else:
            print(f' ::: Id not exist')
