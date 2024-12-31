import exifread

def get_datetime_original(file_name):
    """Function for getting the DateTimeOriginal value from EXIF"""

    with open(file_name, 'rb') as file:
        tags = exifread.process_file(file)

        if 'EXIF DateTimeOriginal' in tags:
            datetime_original = str(tags['EXIF DateTimeOriginal'])
        else:
            datetime_original = "n/a"

    return datetime_original