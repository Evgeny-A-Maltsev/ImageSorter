import click
import pathlib
import exif


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')
def image_sort(source_directory, destination_directory, recursive, move):
    images = image_search(source_directory, recursive)
    for file in images:
        print(f'The file {pathlib.PurePosixPath(file).name} was created in {get_datetime_original(file)}')


def image_search(source_directory, recursive):
    if recursive:
        images = list(pathlib.Path(source_directory).rglob("*.jpg", case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob("*.jpg", case_sensitive=False))
    return list(images)


def get_datetime_original(file):
    datetime_original = 'n/a'
    try:
        with open(file, 'rb') as image_file:
            my_image = exif.Image(image_file)
            datetime_original = my_image.datetime_original
    except KeyError:
        pass
    finally:
        return datetime_original


if __name__ == '__main__':
    image_sort()
