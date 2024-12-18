import click
import my_file
import my_image
import my_date

program_version = "0.2.0"
program_description = "ImageSorter by Evgeny Maltsev (yevmal@gmail.com)"

@click.version_option(program_version, prog_name=program_description)
@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')

def image_sort(source_directory, destination_directory, recursive, move):
    """ImageSorter is a program for sorting photos based on the date of creation of the photo obtained from EXIF."""

    images = my_file.image_search(source_directory, recursive)

    count_ok = 0
    count_fail = 0

    for file_in in images:
        datetime_original = my_image.get_datetime_original(file_in)

        if datetime_original != "n/a":
            path_second = my_date.get_date(datetime_original)
        else:
            path_second = "unsorted"

        file_to = destination_directory + "/" + str(path_second)

        if my_file.file_processing(str(file_in), str(file_to), move):
            count_ok += 1
            print(f"The file {my_file.get_file_name(file_in)} has been processed successfully")
        else:
            count_fail += 1
            print(f"The file {my_file.get_file_name(file_in)} was not processed")

    print(f"Out of {len(images)} photos, {count_ok} were processed and {count_fail} were skipped.")

if __name__ == '__main__':
    image_sort()
