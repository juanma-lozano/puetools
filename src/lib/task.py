from abc import abstractmethod
from enum import Enum

class TaskStatus(Enum):
    OK = 0
    WARN = 1
    FAIL = 2

# All actions executed by PueTools are called Task.
class Task:

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    # Three outputs: OK, WARN or ERROR.
    @abstractmethod
    def get_status(self):
        pass