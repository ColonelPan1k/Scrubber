import os


def find_filetypes(path, ext):
    """Returns a list of all files in `path` that end with `ext`"""
    return list(filter(lambda v: True if ext in v else False, os.listdir(path)))


def get_file_contents(path, linenum=0):
    if not os.path.isdir(path):
        return 0


def get_line_count(path):
    if not os.path.isfile(path):
        return -1
    return sum(1 for line in open(path, "r"))


def generate_comment_stub(buf):
    stubs = {}
    for line in buf:
        formatted = "{line} : {dict[line]}"
        stubs.append({False: line})


# REFACTOR: Allow support for any comment type
#    - preferrably multiline comments and
#      languages that typically have comments at the
#      line, like scheme or asm.
def is_comment(comment):
    if comment[0:2] == "# ":
        return True
    return False


# TODO: need to store filename
def read_to_buffer(path):
    d = {}
    with open(path, "r") as f:
        for idx, line in enumerate(f):
            if is_comment(line):
                d.update({idx: line})
    return d
