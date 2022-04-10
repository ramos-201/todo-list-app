from todo_list_app.controller.task_app import TaskApp
from todo_list_app.db.db_task import DBTask
from todo_list_app.model.task import Task


class CreateTask(TaskApp):
    _db_task = DBTask()
    _data = None
    _response = None

    def _execute(self):
        self._response = {
            "response": "error",
            "data": {"message": "Campos requeridos: (title, description, deadline) en el campo data"}
        }
        if self._data.get("title") and self._data.get("description") and self._data.get("deadline"):
            new_task = Task(data={
                'title': self._data.get("title"),
                'description': self._data.get("description"),
                'deadline': self._data.get("deadline")
            })
            self._db_task.insert_update(data=new_task)
            self._response = {
                "response": "success",
                "data": {"message": "Nueva tarea creada", "id": new_task.id}
            }
