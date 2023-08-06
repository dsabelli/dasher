# test dasher replaces spaces in specific file
# test dasher replaces blank spaces in specified directory


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
    assert get_today() == "230806"


def test_replace_whitespace():
    assert (
        replace_whitespace("This sentence has whitespace", "-")
        == "This-sentence-has-whitespace"
    )
    assert (
        replace_whitespace("This-sentence_has a mix", "-") == "This-sentence-has-a-mix"
    )


def test_validate_date_valid():
    assert validate_date("230806") == None
    assert validate_date("991231") == None
    assert validate_date("0") == None


def test_validate_date_invalid():
    with pytest.raises(SystemExit):
        validate_date("wrongFormat")
    with pytest.raises(SystemExit):
        validate_date("231301")
    with pytest.raises(SystemExit):
        validate_date("230133")


def test_validate_separator_valid():
    assert validate_separator("-") == None
    assert validate_separator("_") == None


def test_validate_separator_invalid():
    with pytest.raises(SystemExit):
        validate_separator(" ")
    with pytest.raises(SystemExit):
        validate_separator("@")
    with pytest.raises(SystemExit):
        validate_separator("/")


def test_get_new_name():
    assert get_new_name("0", "-", "filename") == "filename"
    assert get_new_name(get_today(), "-", "filename") == get_today() + "-filename"


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
