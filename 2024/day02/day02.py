import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def calculate_level_difference(levels):
    differences = []
    last_level = None
    for level in levels:
        if not last_level:
            last_level = int(level)
        else:
            differences.append(int(level) - last_level)
            last_level = int(level)
    return differences

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    safe_reports = 0
    for line in data_file:
        levels = line.split()
        differences = calculate_level_difference(levels)
        if all((x > 0 and x <= 3) for x in differences) or all((x < 0 and x >= -3) for x in differences):
            safe_reports += 1        
    print_and_verify_answer(mode, "one", safe_reports, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    safe_reports = 0
    for line in data_file:        
        levels = list(map(int, line.split()))
        all_combos_of_levels_with_one_removed = [levels[:i] + levels[i+1:] for i in range(len(levels))]
        for combo in all_combos_of_levels_with_one_removed:
            differences = calculate_level_difference(combo)
            if all((x > 0 and x <= 3) for x in differences) or all((x < 0 and x >= -3) for x in differences):
                safe_reports += 1
                break
    print_and_verify_answer(mode, "two", safe_reports, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2)
run_part_one("prod", 591)
run_part_two("test", 4)
run_part_two("prod", 621)
# Now run it and watch the magic happen 🪄