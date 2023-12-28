import os
import re
import datetime

PATTERN = re.compile(r"(\.jpg|\.jpeg)$")


def rename_files(dir: str, pattern: str, date: str, separator: str) -> None:
    # Change the current directory to the directory containing the files
    os.chdir(dir)
    # Iterate over all items in the current directory
    for filename in os.scandir(dir):
        # Generate a new name for the file
        new_name = get_new_name(date, separator, filename.name)
        # Check if the current item is a file and its name matches the defined patterns
        if (
            filename.is_file()
            and re.search(pattern, filename.name)
            and re.search(PATTERN, filename.name)
        ):
            # Rename the file with the generated new name
            os.rename(filename.name, replace_whitespace(new_name, separator))


def replace_whitespace(filename: str, repl: str) -> str:
    # Define a regular expression pattern to match whitespace characters or underscores
    pattern = r"[-\s_]"
    # Replace all occurrences of the matched pattern in the filename with the replacement string
    return re.sub(pattern, repl, filename)


def get_new_name(date: str, separator: str, filename: str) -> str:
    # If the date is "0", return the original filename
    if date == "0":
        return filename
    # Try to parse the first 6 characters of the filename as a date
    else:
        try:
            if (
                datetime.datetime.strptime(filename[:6], "%y%m%d")
                and filename[6] == separator
            ):
                return date + filename[6:]
        except ValueError:
            return date + separator + filename
        # If successful, return the date followed by the rest of the filename
