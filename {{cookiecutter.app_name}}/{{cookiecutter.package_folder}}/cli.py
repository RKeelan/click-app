import click


@click.command()
@click.version_option()
def cli():
    "{{ cookiecutter.description }}"
    click.echo("{{ cookiecutter.title}}")
