import click
import pathlib
from re import search
from PIL import Image
from datetime import datetime

@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')
def image_sort(source_directory, destination_directory, recursive, move):
    images = image_search(source_directory, recursive)
    for file in images:
        file_name = pathlib.PurePosixPath(file).name
        datetime_original = get_datetime_original(file)

        if datetime_original != "n/a":
            date_str = get_date(datetime_original)
            print(f'The file {file_name} new path in {date_str}')
        else:
            print(f'The file {file_name} new path in n/a')


def image_search(source_directory, recursive):
    if recursive:
        images = list(pathlib.Path(source_directory).rglob("*.jpg", case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob("*.jpg", case_sensitive=False))
    return list(images)


def get_datetime_original(file):
    datetime_original = 'n/a'
    exif = Image.open(file)._getexif()
    if exif:
        if 36867 in exif:
            datetime_original = exif[36867]
    return datetime_original


def get_date(datetime_original):
    return datetime.strptime(search("\\d{4}:\\d{2}:\\d{2}", datetime_original).group(), '%Y:%m:%d').date()


if __name__ == '__main__':
    image_sort()
