import click
import own_file_functions as own_file
import own_image_functions as own_image
import own_date_functions as own_date

program_description_full = "ImageSorter by Evgeny A. Maltsev (yevmal@gmail.com)"
program_version = "0.3.0"

@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively photo search')
@click.option('-m', '--move', is_flag=True, default=False, help='Move sorted photos')

def image_sort(source_directory, destination_directory, recursive, move):
    """Image sorting function"""

    if (own_file.checking_path(source_directory) and own_file.checking_path(destination_directory)):
        images = own_file.image_search(source_directory, recursive, "*.jpg")

        count_ok = 0
        count_fail = 0

        for file_in in images:
            datetime_original = own_image.get_datetime_original(file_in)

            if datetime_original != "n/a":
                path_second = own_date.get_date(datetime_original)
            else:
                path_second = "unsorted"

            file_to = destination_directory + "/" + str(path_second)

            if own_file.file_processing(str(file_in), str(file_to), move):
                count_ok += 1
                print(f"The file {own_file.get_file_name(file_in)} has been processed successfully")
            else:
                count_fail += 1
                print(f"The file {own_file.get_file_name(file_in)} was not processed")

        print(f"Out of {len(images)} photos, {count_ok} were processed and {count_fail} were skipped.")
    else:
        print("Error: SOURCE_DIRECTORY or DESTINATION_DIRECTORY does not exist")

if __name__ == '__main__':
    print(f'{program_description_full}\nversion {program_version}\n')
    image_sort()
