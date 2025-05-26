import click
import sh
from .. cli_tools import loudspeaker, wrap_module_with_decorator

loud_sh = wrap_module_with_decorator('sh', loudspeaker)

@click.group()
@click.version_option()
def cli():
    "{{ cookiecutter.description }}"


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
