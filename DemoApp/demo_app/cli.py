import click


@click.command()
@click.version_option()
def cli():
    ""
    click.echo("Demo App")
