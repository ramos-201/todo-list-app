from abc import ABC, abstractmethod


class Command(ABC):
    _description = ''

    @abstractmethod
    def run(self):
        pass

    @property
    def description(self):
        return self._description
