import pathlib
import shutil

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

def image_search(source_directory, recursive):
    if recursive:
        images = list(pathlib.Path(source_directory).rglob("*.jpg", case_sensitive=False))
    else:
        images = list(pathlib.Path(source_directory).glob("*.jpg", case_sensitive=False))

    return list(images)

def get_file_name(path):
    return pathlib.PurePosixPath(path).name