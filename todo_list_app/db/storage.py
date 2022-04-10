class Storage:
    _instance = None
    _task = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Storage, cls).__new__(cls)
        return cls._instance

    @property
    def task(self):
        return self._task
