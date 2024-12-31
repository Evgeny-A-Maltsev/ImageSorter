import pathlib
import shutil

def file_processing(source_path, destination_path, files_moving):
    """The function for processing files"""

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

def image_search(source_directory, recursive, image_format):
    """The function for file search"""

    if recursive:
        images = list(pathlib.Path(source_directory).rglob(image_format, case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob(image_format, case_sensitive=False))

    return list(images)

def get_file_name(path):
    """The function for getting the file name"""

    return pathlib.PurePosixPath(path).name

def checking_path(path):
    """The function for checking the path"""

    if pathlib.Path(path).is_dir():
        status = True
    else:
        status = False

    return status