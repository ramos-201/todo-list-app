from todo_list_app.controller.task_app import TaskApp
from todo_list_app.db.db_task import DBTask


class FilterTask(TaskApp):
    _db_task = DBTask()
    _data = None
    _response = None

    def _execute(self):
        self._response = {
            "response": "error",
            "data": {"message": "Campos requeridos: (action) en el campo data"}
        }
        if self._data.get("action"):
            self._response = {
                "response": "error",
                "data": {"message": "Acciones disponibles: (all, filter) en el campo action"}
            }
            if self._data.get("action") == "all":
                self._response = {
                    "response": "success",
                    "data": {"message": "Data encotrada correctamente", "data_task": self._db_task.get_all()}
                }
            if self._data.get("action") == "filter":
                self._filter_tasks()

    def _filter_tasks(self):
        self._response = {
            "response": "error",
            "data": {"message": "Campos requeridos: (data_filter) tipo dict en el campo data"}
        }
        if self._data.get("data_filter") and type(self._data.get("data_filter")) == dict:
            response_filter = {}

            def exist_in_data(data_task):
                for key, value in self._data.get("data_filter").items():
                    if value not in data_task[key] or value == "":
                        return False
                return True

            for task in self._db_task.get_all():
                if exist_in_data(self._db_task.get_one(task).__dict__):
                    response_filter[task] = self._db_task.get_one(task)
            self._response = {
                "response": "success",
                "data": {"message": "Data encontrada correctamente", "data_task": response_filter}
            }
