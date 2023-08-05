import os
import re
import argparse
import datetime
import sys


def main():
    args = get_args()

    directory = os.getcwd()
    pattern = args.p
    date = str(args.d)
    separator = args.s
    print(separator)

    if separator != "-" and separator != "_":
        sys.exit("Separator must be either '-' or '_'")
    # Rename file(s) in the current directory, prefix a date and replace whitespace with a separator
    rename_files(directory, pattern, date, separator)


def rename_files(dir: str, pattern: str, date: str, separator: str) -> None:
    for filename in os.listdir(dir):
        newName = ""
        if date == "0":
            newName = filename
        else:
            newName = date + separator + filename
        if re.match(pattern, filename):
            os.rename(filename, replace_whitespace(newName, separator))


# replace all whitespace with dashes by default
def replace_whitespace(filename: str, repl: str) -> str:
    pattern = r"\s"
    return re.sub(pattern, repl, filename)


# Get todays date and format as an int formatted as YYMMDD
def get_today() -> int:
    return int(datetime.date.today().strftime("%y%m%d"))


# Add arg default and return args
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


if __name__ == "__main__":
    main()

# look into using *args and **kwargs
# look into -d "0" for a no date option, add to helper
# validate adding a pattern for targeting specific files
# restrict separator to - and _

# write unit tests
