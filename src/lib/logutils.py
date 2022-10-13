from enum import Enum
import click

class LogStatus(Enum):
    OK = 0
    WARN = 1
    FAIL = 2

def print_logo():
    print("______         _____           _              __  ")
    print("| ___ \       |_   _|         | |            /  | ")
    print("| |_/ /   _  ___| | ___   ___ | |___  __   __`| | ")
    print("|  __/ | | |/ _ \ |/ _ \ / _ \| / __| \ \ / / | | ")
    print("| |  | |_| |  __/ | (_) | (_) | \__ \  \ V / _| |_")
    print("\_|   \__,_|\___\_/\___/ \___/|_|___/   \_/  \___/")
    print("")

def print_msg(status, message):
    click.secho("[", nl=False)
    if status == LogStatus.OK:
        click.secho(" OK ", fg="green", nl=False)
    if status == LogStatus.WARN:
        click.secho("WARN", fg="yellow", nl=False)
    if status == LogStatus.FAIL:
        click.secho("FAIL", fg="red", nl=False)
    click.echo("] " + message, nl=True)