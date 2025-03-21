import os, sys

# Returns the lines of the file, ready to iterate over.
# Returns error if the file is empty.
# Usage:
# my_lines = open_file("input.txt")
def open_file(filename):
    file_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),filename)
    if os.stat(file_path).st_size == 0:
        print("\n❌ File " + filename + " is empty!")
        sys.exit()
    file = open(file_path, 'r')
    return file.readlines()

# Take multiple lines (e.g. from input file), and split into grid,
# assuming each line is a row, and each character is a cell.
# Usage:
# my_grid = initialise_grid(my_lines)
def initialise_grid(lines):
    return [list(line.strip()) for line in lines]

# Prints the answer, and (if there's an expected value to check) verifies the answer.
def print_and_verify_answer(mode, part, answer, expected):
    print("\nPart " + part + " " + mode + " answer: " + str(answer))
    if expected != None:
        if answer != expected:
            print("❌ FAILED! Expected", expected, "got", answer)
        else:
            print("✅ Output matches expected value")