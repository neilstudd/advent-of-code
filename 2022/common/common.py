import os, sys

# Returns the lines of the file, ready to iterate over.
# Usage:
# my_lines = open_file("input.txt")
def open_file(filename):
    file_path = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\" + filename
    file = open(file_path, 'r')
    return file.readlines()