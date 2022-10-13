from src.lib.logutils import *
from src.lib.task import *

class Login(Task):

    @click.command()
    @click.option("--count", default=1, help="Number of greetings.")
    def execute(self):
        print_msg(LogStatus.WARN, "")

    def get_description(self):
        return "A new update is available"

    def get_status(self):
        return TaskStatus.OK