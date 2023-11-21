#!/opt/homebrew/bin/python3
import os
import re
import argparse
import datetime
import sys
from PIL import Image

#todo: 
# move renamed files to dasher-processed folder
# comments for file compression functions
# error handling
# testing for file compression
# folder watching
# folder cleanup
def main():
    QUALITY = 95
    args = get_args()
    size = args.c
    directory = args.d
    pattern = args.p
    date = args.t
    separator = args.s

    validate_date(date)
    validate_separator(separator)

    rename_files(directory, pattern, date, separator)
    resize_images(directory,separator,size,QUALITY)
    


# loop through files in directory. Scan for today's date with double separator


# Rename file(s) in the specified directory (defaulted to current dir),
# prefix a date and replace whitespace (or dash/underscore) with a separator
def rename_files(dir: str, pattern: str, date: str, separator: str) -> None:
    os.chdir(dir)
    for filename in os.scandir(dir):
        new_name = get_new_name(date, separator, filename.name)
        if filename.is_file() and re.search(pattern, filename.name):
            os.rename(filename.name, replace_whitespace(new_name, separator))


# replace all whitespace with dashes by default
def replace_whitespace(filename: str, repl: str) -> str:
    pattern = r"[-\s_]"
    return re.sub(pattern, repl, filename)


# Get todays date and returns formatted as YYMMDD
def get_today() -> str:
    return datetime.date.today().strftime("%y%m%d")


# Add arg defaults and return args
def get_args(args=None):
    today = get_today()
    default_dir = os.getcwd()

    parser = argparse.ArgumentParser(description="Replace whitespace with dashes")
    parser.add_argument(
        "-d",
        default=default_dir,
        help="specify directory, default is current directory",
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
        "-p", 
        default=".", 
        help="define regex pattern, defaults to all files", 
        type=str
    ),
    parser.add_argument(
        "-c", 
        default=200000, 
        help="define image compression size as an integer, defaults to 200000", 
        type=int
    )
    return parser.parse_args(args)


# Returns the filename with a date prefix by default, or as is if date=args.t == "0"
# Is called after validate_date and assumed the date format is YYMMDD or 0
# Does not prefix a date if a date as YYMMDD is already present
# Use double separator to differentiate files that have a date prefix not from Dasher
def get_new_name(date: str, separator: str, filename: str) -> str:
    try:
        if (
            datetime.datetime.strptime(filename[:6], "%y%m%d")
            and filename[6] == separator
        ):
            return filename
    except ValueError:
        ...
    if date == "0":
        return filename
    else:
        return date + separator + filename


# validates if the date is YYMMDD or 0, exits with message if it isn't
def validate_date(date: str) -> bool:
    if date == "0":
        return True
    try:
        datetime.datetime.strptime(date, "%y%m%d")
        return True
    except ValueError:
        sys.exit("Date must be either YYMMDD or 0")


# validates if the separator is a dash or underscore, exits with message if it isn't
def validate_separator(separator: str) -> bool:
    if separator != "-" and separator != "_":
        sys.exit("Separator must be either '-' or '_'")
    return True

def resize_images(dir: str, separator: str, size:int,quality:int) -> None:
    pattern = re.compile(r"(-|_).*(\.jpg|\.jpeg)$")
    os.chdir(dir)
    for filename in os.scandir(dir):
        if filename.is_file() and re.search(pattern, filename.name):
            check_image_size(filename.name,size,quality)

def check_image_size(file_path:str,size:int,quality:int)->None:
    current_size = os.stat(file_path).st_size
    while current_size > size or quality ==0:
        if quality == 0:
            os.remove(file_path)
            print("File cannot be compressed to defined size")
            break

        compress_image(file_path,quality)
        current_size = os.stat(file_path).st_size
        quality-=5

def compress_image(file_path:str,quality:int)->int:
    image = Image.open(file_path)
    image.save(file_path,"JPEG",optimize=True,quality=quality)
    compressed_size = os.stat(file_path).st_size
    return compressed_size

if __name__ == "__main__":
    main()
