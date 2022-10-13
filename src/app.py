import sys

from src.tasks.internal.initializer import Initialize
from src.tasks.ping import *
from src.tasks.kafka.produce import *
import click

@click.group()
def kafka():
    """List of kafka commands."""
    pass

@click.group()
def cli():
    pass

class App:

    def awake(self):
        cli.add_command(demo)

        # Kafka
        kafka.add_command(send)
        cli.add_command(kafka)

    def start(self):
        pass

    def execute(self):
        if len(sys.argv) > 1:
            print_logo()
            initializer = Initialize()
            initializer.execute()
        cli()

    def dispose(self):
        pass