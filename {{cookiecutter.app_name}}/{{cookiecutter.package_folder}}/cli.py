import click


@click.command()
@click.version_option()
def cli() -> None:
    "{{ cookiecutter.description }}"
    click.echo("{{ cookiecutter.title}}")
