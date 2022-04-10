from todo_list_app.db.storage import Storage
from todo_list_app.model.task import Task


class DBTask:
    _storage = Storage()

    def insert_update(self, data: Task) -> None:
        self._storage.task[data.id] = data

    def delete(self, id_task: str) -> None:
        self._storage.task.pop(id_task)

    def get_all(self) -> dict:
        return self._storage.task

    def get_one(self, id_task: str) -> Task:
        return self._storage.task[id_task]
