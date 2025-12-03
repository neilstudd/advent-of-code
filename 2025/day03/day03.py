import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from itertools import combinations

def highest_joltage(bank, digits):
    max_joltage = 0
    for combo in combinations(bank, digits):
        candidate = int(''.join(combo))
        if candidate > max_joltage:
            max_joltage = candidate
    return max_joltage    

def run_part_one(mode, expected = None):
    banks = open_file( mode + ".txt")
    total_joltage = sum(highest_joltage(bank, 2) for bank in banks)
    print_and_verify_answer(mode, "one", total_joltage, expected)

def run_part_two(mode, expected = None):
    banks = open_file( mode + ".txt")
    total_joltage = sum(highest_joltage(bank, 12) for bank in banks)
    print_and_verify_answer(mode, "two", total_joltage, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 357)
run_part_one("prod", 17452)
run_part_two("test", 3121910778619)
# run_part_two("prod", 0) # This will never complete - too many combinations
# Now run it and watch the magic happen 🪄