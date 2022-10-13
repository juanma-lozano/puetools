import click
from src.lib.task import Task, TaskStatus

class Updates(Task):

    @click.command()
    @click.option("--count", default=1, help="Number of greetings.")
    def execute(self):
        pass

    def get_description(self):
        return "A new update is available"

    def get_status(self):
        return TaskStatus.OK