import sys, os, re
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def parse_file(data_file):
    towels = data_file[0].strip().split(", ")
    patterns = [line.strip() for line in data_file[2:]]
    return towels, patterns

def count_ways_to_form_pattern(pattern, towels, result=None):
    if result is None:
        result = {}
    if pattern in result:
        return result[pattern]
    if pattern == "":
        return 1
    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            count += count_ways_to_form_pattern(pattern[len(towel):], towels, result)
    result[pattern] = count
    return count

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    towels, patterns = parse_file(data_file)
    patterns_achievable = sum(1 for pattern in patterns if count_ways_to_form_pattern(pattern, towels))
    print_and_verify_answer(mode, "one", patterns_achievable, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    towels, patterns = parse_file(data_file)
    ways_to_form_patterns = sum(count_ways_to_form_pattern(pattern, towels) for pattern in patterns)
    print_and_verify_answer(mode, "two", ways_to_form_patterns, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 6)
run_part_one("test2", 0)
run_part_one("prod", 300)
run_part_two("test", 16)
run_part_two("prod", 624802218898092)
# Now run it and watch the magic happen 🪄