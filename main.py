import click


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')
def image_sort(source_directory, destination_directory, recursive, move):
    click.echo(f"Photo source directory = {source_directory}")
    click.echo(f"Photo destination directory = {destination_directory}")
    click.echo(f"Recursively photo search = {recursive}")
    click.echo(f"Move sorted photos = {move}")


if __name__ == '__main__':
    image_sort()
