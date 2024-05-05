import click


@click.command()
@click.option('-s', '--source', help='Photo source directory')
@click.option('-d', '--destination', help='Photo destination directory')
@click.option('-r', '--recursive', is_flag=True, default=True, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=True, help='Move sorted photos')
def image_sort(source, destination, recursive, move):
    click.echo(f"Photo source directory = {source}")
    click.echo(f"Photo destination directory = {destination}")
    click.echo(f"Recursively photo search = {recursive}")
    click.echo(f"Move sorted photos = {move}")


if __name__ == '__main__':
    image_sort()
