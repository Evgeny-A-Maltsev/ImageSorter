import click
import pathlib
import shutil
import exifread
from re import search
from datetime import datetime


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')


def image_sort(source_directory, destination_directory, recursive, move):
    """ImageSorter is a program for sorting photos based on the date of creation of the photo obtained from EXIF."""
    images = image_search(source_directory, recursive)

    count_ok = 0
    count_fail = 0

    for file_in in images:
        datetime_original = get_datetime_original(file_in)

        if datetime_original != "n/a":
            path_second = get_date(datetime_original)
        else:
            path_second = "unsorted"

        file_to = destination_directory + "/" + str(path_second)

        if file_processing(str(file_in), str(file_to), move):
            count_ok += 1
            print(f"The file {pathlib.PurePosixPath(file_in).name} has been processed successfully")
        else:
            count_fail += 1
            print(f"The file {pathlib.PurePosixPath(file_in).name} was not processed")

    print(f"Out of {len(images)} photos, {count_ok} were processed and {count_fail} were skipped.")


def image_search(source_directory, recursive):
    if recursive:
        images = list(pathlib.Path(source_directory).rglob("*.jpg", case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob("*.jpg", case_sensitive=False))

    return list(images)

def get_datetime_original(file_name):
    with open(file_name, 'rb') as file:
        tags = exifread.process_file(file)

        if 'EXIF DateTimeOriginal' in tags:
            datetime_original = str(tags['EXIF DateTimeOriginal'])
        else:
            datetime_original = "n/a"

    return datetime_original

def get_date(datetime_original):
    return datetime.strptime(search("\\d{4}:\\d{2}:\\d{2}", datetime_original).group(), "%Y:%m:%d").date()


def file_processing(source_path, destination_path, files_moving):
    status = True

    try:
        if not pathlib.Path(destination_path).is_dir():
            pathlib.Path.mkdir(destination_path)

        path_in = pathlib.PurePosixPath(source_path)
        path_to = pathlib.PurePosixPath(destination_path)

        if files_moving:
            shutil.move(path_in, path_to)
        else:
            shutil.copy(path_in, path_to)
    except KeyError:
        status = False

    return status


if __name__ == '__main__':
    image_sort()
