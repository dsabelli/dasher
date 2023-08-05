import os
import re
import argparse
import datetime
import sys


def main():
    directory = os.getcwd()

    args = get_args()
    pattern = args.p
    date = str(args.d)
    separator = args.s

    check_separator(separator)

    rename_files(directory, pattern, date, separator)


# Rename file(s) in the current directory, prefix a date and replace whitespace with a separator
def rename_files(dir: str, pattern: str, date: str, separator: str) -> None:
    for filename in os.scandir(dir):
        new_name = get_new_name(date, separator, filename.name)
        if filename.is_file() and re.match(pattern, filename.name):
            os.rename(filename.name, replace_whitespace(new_name, separator))


# replace all whitespace with dashes by default
def replace_whitespace(filename: str, repl: str) -> str:
    pattern = r"\s"
    return re.sub(pattern, repl, filename)


# Get todays date and format as an int formatted as YYMMDD
def get_today() -> int:
    return int(datetime.date.today().strftime("%y%m%d"))


# Add arg defaults and return args
def get_args():
    today = get_today()

    parser = argparse.ArgumentParser(description="Replace whitespace with dashes")
    parser.add_argument(
        "-d",
        default=today,
        help="prefixes the date as today's date in format YYMMDD, indicate '0' for no date prefix",
        type=int,
    )
    parser.add_argument(
        "-s",
        default="-",
        help="indicate '_' or '-' as separator, default is '-'",
        type=str,
    )
    parser.add_argument(
        "-p", default=".", help="define regex pattern, defaults to all files", type=str
    )
    return parser.parse_args()


# Returns the filename with a date prefix by default, or as is if date=str(args.d) == "0"
def get_new_name(date: str, separator: str, filename: str) -> str:
    if date == "0":
        return filename
    else:
        return date + separator + filename


# Checks if the separator is a dash or underscore, exits with message if it isn't
def check_separator(separator: str) -> None:
    if separator != "-" and separator != "_":
        sys.exit("Separator must be either '-' or '_'")


if __name__ == "__main__":
    main()
