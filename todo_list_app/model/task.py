import datetime
import uuid


class Task:
    _date = datetime.datetime.now()

    def __init__(self, data):
        self.id = str(uuid.uuid4())
        self.title = data['title']
        self.description = data['description']
        self.deadline = data['deadline']
        self.status = 'pending'
        self.created = self._date
        self.modified = self._date
