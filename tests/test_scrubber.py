import pytest
from ..src.main import find_filetypes, get_file_contents, get_line_count


def test_pytest_sanity_check():
    sanity_string = "Hello world!"

    assert 1 + 1 == 2
    assert True is True
    assert False is False
    assert "String" is "String"
    assert sanity_string is "Hello world!"


# TODO: Move tests to separate files

########################### find_filetypes() #############################
def test_return_filenames_in_directory():
    found = find_filetypes("tests/dummy_dir", ".py")
    not_found = find_filetypes("tests/dummy_dir", ".asm")

    assert found == ["dummy_file.py"]
    assert not_found == []


##########################################################################

########################### get_file_contents() ##########################
def test_open_file_from_empty_directory():
    assert get_file_contents("") == 0


def test_open_file_with_broken_name():
    assert get_file_contents("not a dir.wav") == 0


def test_open_file_and_return_contents():
    first_line = get_file_contents("tests/dummy_dir/dummy_file.py", 1)


#########################################################################

####################### get_line_count() ###############################
def test_check_line_numbers_with_broken_file():
    n = get_line_count("not a dir.blend")
    assert n == -1


def test_check_line_numbers():
    n = get_line_count("tests/dummy_dir/dummy_file.py")
    assert n == 15


#######################################################################


def test_generate_comment_stub():
    pass


def test_generate_comment_stub_from_open_file():
    pass


def test_read_file_info_to_buffer():
    pass


# Read all files in a directory of a certain file type

# Open the file

# Find the comments
