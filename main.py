import pathlib
import click


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')
def image_sort(source_directory, destination_directory, recursive, move):
    images = image_search(source_directory, recursive)
    for files in images:
        print(files, pathlib.PurePosixPath(files).parent, pathlib.PurePosixPath(files).name)


def image_search(source_directory, recursive):
    if recursive:
        images = list(pathlib.Path(source_directory).rglob("*.jpg", case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob("*.jpg", case_sensitive=False))
    return list(images)


if __name__ == '__main__':
    image_sort()
