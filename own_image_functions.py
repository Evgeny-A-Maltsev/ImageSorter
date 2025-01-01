from typing import Any
import exifread


def get_datetime_original(file_name):
    """The function for getting the DateTimeOriginal value from EXIF"""

    with open(file_name, 'rb') as file:
        tags: dict[str, Any] = exifread.process_file(file)

        if 'EXIF DateTimeOriginal' in tags:
            datetime_original: str = str(tags['EXIF DateTimeOriginal'])
        else:
            datetime_original: str = "n/a"

    return datetime_original
