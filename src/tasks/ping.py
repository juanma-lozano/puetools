from src.lib.logutils import *
import click

@click.command()
@click.option("-host", default="carrefour-dev", help="Development environment")
def demo(host):
    """This command exists for showcase."""
    print_msg(LogStatus.OK, "Loading config file: ./hosts.yaml")
    print_msg(LogStatus.OK, "Verifiying VPN connection.")
    print_msg(LogStatus.OK, "Stablishing SSH conection with remote host.")
    print_msg(LogStatus.OK, "Ping successful.")
