#!/opt/homebrew/bin/python3
import os
import argparse
import datetime
import validators
from rename import rename_files
from img_compress import resize_images


# todo:
# error handling
# testing for file compression
# folder watching
# folder cleanup
def main():
    QUALITY = 95
    args = get_args()
    size = args.c
    directory = args.d
    output_directory = args.o
    pattern = args.p
    date = args.t
    separator = args.s

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    validators.validate_date(date)
    validators.validate_separator(separator)

    rename_files(directory, pattern, date, separator)
    resize_images(directory, output_directory, size, QUALITY)


# Add arg defaults and return args
def get_args(args=None):
    today = datetime.date.today().strftime("%y%m%d")
    default_dir = os.getcwd()

    parser = argparse.ArgumentParser(description="Replace whitespace with dashes")
    parser.add_argument(
        "-d",
        default=default_dir,
        help="specify directory, default is current directory",
        type=str,
    )
    parser.add_argument(
        "-o",
        default=default_dir + "/dasher_output",
        help="specify ooutput directory, default is current directory/dasher_output",
        type=str,
    )
    parser.add_argument(
        "-t",
        default=today,
        help="prefixes the date as today's date in format YYMMDD, indicate '0' for no date prefix",
        type=str,
    )
    parser.add_argument(
        "-s",
        default="-",
        help="indicate '_' or '-' as separator, default is '-'",
        type=str,
    )
    parser.add_argument(
        "-p", default=".", help="define regex pattern, defaults to all files", type=str
    ),
    parser.add_argument(
        "-c",
        default=200000,
        help="define image compression size as an integer, defaults to 200000",
        type=int,
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
