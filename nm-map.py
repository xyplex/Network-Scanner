import click
from scapy.all import *


@click.group()
@click.version_option(version='0.1', prog_name='Network Scanner')
def main():
    """ Network Scanner"""
    pass


@main.command()
@click.argument('')
def sL():
    """List Scan - simply list target to scan"""
    click.echo("This is a list of targets to scan")


@main.command()
@click.argument('')
def sn():
    """Ping Scan - disable port port scan"""
    click.secho('This is Ping scan', fg='green')


if __name__ == '__main__':
    main()
