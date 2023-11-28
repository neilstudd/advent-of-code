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

# Prints the answer, and (if there's test output / expected value) verifies the answer.
def print_and_verify_answer(mode, part, answer, expected):
    print("\nPart " + part + " " + mode + " answer: " + str(answer))
    if mode == "test":
        if answer != expected:
            print("❌ Test FAILED, expected", expected, "got", answer)
        else:
            print("✅ Output matches expected value ")