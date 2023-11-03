import os
import pytest
from dasher import (
    validate_date,
    validate_separator,
    get_new_name,
    get_args,
    get_today,
    replace_whitespace,
    rename_files,
)


def test_get_today():
    assert get_today() == "231103"


def test_replace_whitespace():
    assert (
        replace_whitespace("This sentence has whitespace", "-")
        == "This-sentence-has-whitespace"
    )
    assert (
        replace_whitespace("This-sentence_has a mix", "-") == "This-sentence-has-a-mix"
    )


def test_validate_date_valid():
    assert validate_date("230806") == True
    assert validate_date("991231") == True
    assert validate_date("0") == True


def test_validate_date_invalid():
    with pytest.raises(SystemExit):
        validate_date("wrongFormat")
    with pytest.raises(SystemExit):
        validate_date("231301")
    with pytest.raises(SystemExit):
        validate_date("230133")


def test_validate_separator_valid():
    assert validate_separator("-") == True
    assert validate_separator("_") == True


def test_validate_separator_invalid():
    with pytest.raises(SystemExit):
        validate_separator(" ")
    with pytest.raises(SystemExit):
        validate_separator("@")
    with pytest.raises(SystemExit):
        validate_separator("/")


def test_get_new_name():
    assert get_new_name("0", "-", "filename") == "filename"
    assert get_new_name(get_today(), "-", "filename") == get_today() + "--filename"
    assert (
        get_new_name(get_today(), "-", "230807-filename") == "231103--230807-filename"
    )


def test_get_args_inputs():
    args = ["-d", "specified_dir", "-t", "0", "-s", "_", "-p", "test"]
    parsed_args = get_args(args)
    assert parsed_args.d == "specified_dir"
    assert parsed_args.t == "0"
    assert parsed_args.s == "_"
    assert parsed_args.p == "test"


def test_get_args_defaults():
    parsed_args = get_args([])
    assert parsed_args.d == os.getcwd()
    assert parsed_args.t == get_today()
    assert parsed_args.s == "-"
    assert parsed_args.p == "."


def test_rename_files_valid():
    directory = os.getcwd() + "/test_files"
    file_name = "test file.txt"
    file_path = os.path.join(directory, file_name)
    file = open(file_path, "w").close()
    rename_files(directory, ".", get_today(), "-")
    assert os.listdir(directory)[0] == get_today() + "--test-file.txt"
    os.remove(directory + "/" + get_today() + "--test-file.txt")


def test_rename_files_specify_file():
    directory = os.getcwd()
    file_name1 = "test file one.txt"
    file_path1 = os.path.join(directory, file_name1)
    file = open(file_path1, "w").close()
    file_name2 = "test file two.txt"
    file_path2 = os.path.join(directory, file_name2)
    file = open(file_path2, "w").close()
    rename_files(directory, "one", get_today(), "-")
    assert os.listdir(directory)[1] == get_today() + "--test-file-one.txt"
    os.remove(directory + "/" + get_today() + "--test-file-one.txt")
    assert os.listdir(directory)[0] == "test file two.txt"
    os.remove(directory + "/" + "test file two.txt")
