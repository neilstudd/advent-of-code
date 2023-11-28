import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Part One code goes here

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Part Two code goes here

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 0)
run_part_one("prod")
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄