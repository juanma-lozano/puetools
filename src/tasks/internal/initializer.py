import vars
from src.lib.logutils import *
from src.lib.task import Task, TaskStatus

class Initialize(Task):

    def execute(self):
        print_msg(LogStatus.OK, "Initializing PueTools-CLI " + vars.VERSION)

    def get_description(self):
        return ""

    def get_status(self):
        return TaskStatus.OK
