import os


def find_filetypes(path, ext):
    """Returns a list of all files that end with `ext` in `path`"""
    return list(filter(lambda v: True if ext in v else False, os.listdir(path)))


def get_file_contents(path, linenum=0):
    if not os.path.isdir(path):
        return 0


def get_line_count(path):
    if not os.path.isfile(path):
        return -1
    return sum(1 for line in open(path, "r"))


def generate_comment_stub(comment):
    """Return comment with attached fileinfo {id: filename: [line num] : comment}"""
