import sys
from readfiles import read_and_print_files


def test_arguments_ex1():
    if len(sys.argv) < 2:
        print("Usage python readfiles.py <file1> <file2> ...")
        sys.exit(1)

    filesnames = sys.argv[1:]
    read_and_print_files(filesnames)
