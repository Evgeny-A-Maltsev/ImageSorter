import click


@click.command("cli", context_settings={'show_default': True})
@click.argument('source', required=True)
@click.argument('targetr', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')
def image_sort(source, target, recursive, move):
    click.echo(f"Photo source directory = {source}")
    click.echo(f"Photo destination directory = {target}")
    click.echo(f"Recursively photo search = {recursive}")
    click.echo(f"Move sorted photos = {move}")


if __name__ == '__main__':
    image_sort()
