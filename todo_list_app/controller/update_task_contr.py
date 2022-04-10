import datetime

from todo_list_app.controller.task_app import TaskApp
from todo_list_app.db.db_task import DBTask


class UpdateTask(TaskApp):
    _db_task = DBTask()
    _data = None
    _response = None

    def _execute(self):
        self._response = {
            "response": "error",
            "data": {"message": "Campos requeridos: (id) en el campo data"}
        }
        if self._data.get("id"):
            try:
                task = self._db_task.get_one(id_task=self._data.get("id"))
            except KeyError:
                self._response = {
                    "response": "warning",
                    "data": {"message": "Id no existe"}
                }
            else:
                prepare_data_task = self._validate_data(task=task)

                self._db_task.insert_update(data=prepare_data_task)
                self._response = {
                    "response": "success",
                    "data": {"message": "Data actualizada", "id": task.id}
                }

    def _validate_data(self, task):
        new_task = task
        new_task.title = self._data.get("title") if self._data.get("title") is not None else task.title
        new_task.description = \
            self._data.get("description") if self._data.get("description") is not None else task.description
        new_task.status = self._data.get("status") if self._data.get("status") is not None else task.status
        new_task.modified = datetime.datetime.now()
        return new_task
