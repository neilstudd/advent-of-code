import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

# AI ASSIST
# Check whether digit is larger than what came before, and - if so - 
# check whether we have enough "spare" characters left to justify promoting it.
def highest_joltage(bank, digits):
    bank = bank.strip()
    drop_count = len(bank) - digits        
    stack = []
    for digit in bank.strip():
        while drop_count > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop_count -= 1        
        stack.append(digit)
    return int("".join(stack[:digits]))

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
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄