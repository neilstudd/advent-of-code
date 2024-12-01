import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer



# def run_part_one(mode, expected = None):
    # data_file = open_file( mode + ".txt")
    # for line in data_file:
        # x
    # print_and_verify_answer(mode, "one", total, expected)



# def run_part_two(mode, expected = None):
    # data_file = open_file( mode + ".txt")
    # for line in data_file:
        # x
    # print_and_verify_answer(mode, "two", total, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 11)
run_part_one("prod")
# run_part_two("test", 31)
# run_part_two("prod")
# Now run it and watch the magic happen 🪄