import os
import re
import argparse
import datetime


def main():
    today = get_today()

    parser = argparse.ArgumentParser(description="Replace whitespace with dashes")
    parser.add_argument("-d", default=today, help="prefix the date as YYMMDD", type=int)
    parser.add_argument(
        "-s",
        default="-",
        help="choose symbol to replace whitespace, default is '-'",
        type=str,
    )
    parser.add_argument(
        "-p", default=".", help="specify filename, defaults to all files", type=str
    )
    args = parser.parse_args()

    directory = os.getcwd()
    pattern = args.p
    date = str(args.d)
    separator = args.s

    # Rename file(s) in the current directory, prefix a date and replace whitespace with a separator
    rename_files(directory, pattern, date, separator)


def rename_files(dir: str, pattern: str, date: str, separator: str) -> None:
    for filename in os.listdir(dir):
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


if __name__ == "__main__":
    main()
