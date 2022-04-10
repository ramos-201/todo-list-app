from abc import abstractmethod


class TaskApp:
    _response = None

    def __init__(self, data=None):
        self._data = data
        self._execute()

    @abstractmethod
    def _execute(self):
        pass

    def response(self):
        return self._response

