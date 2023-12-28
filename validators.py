import sys
import datetime


def validate_date(date: str) -> bool:
    # If the date is "0", return True because "0" is considered a valid date
    if date == "0":
        return True
    # Try to parse the date as a date in the format "%y%m%d"
    try:
        datetime.datetime.strptime(date, "%y%m%d")
        # If parsing is successful, return True
        return True
    # If parsing fails, exit the program with an error message
    except ValueError:
        sys.exit("Date must be either YYMMDD or 0")


def validate_separator(separator: str) -> bool:
    # Check if the separator is not equal to '-' or '_'
    if separator != "-" and separator != "_":
        # If the separator does not meet the condition, exit the program with an error message
        sys.exit("Separator must be either '-' or '_'")
    # If the separator meets the condition, return True
    return True
