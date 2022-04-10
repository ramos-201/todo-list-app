from todo_list_app.controller.task_app import TaskApp
from todo_list_app.db.db_task import DBTask


class DeleteTask(TaskApp):
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
                self._db_task.delete(id_task=self._data.get("id"))
                self._response = {
                    "response": "success",
                    "data": {"message": "Data eliminada correctamente", "data_task": task}
                }

