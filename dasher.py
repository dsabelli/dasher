import os
import re


def main():
    list_files(".")


def list_files(dir):
    for filename in os.listdir(dir):
        if re.match(r"^.+\s.+$", filename):
            os.rename(filename, replace_whitespace(filename))


def replace_whitespace(filename):
    pattern = r"\s"
    repl = "-"
    return re.sub(pattern, repl, filename)


if __name__ == "__main__":
    main()
