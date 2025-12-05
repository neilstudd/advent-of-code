import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def parse_input(input):
    fresh_food_ranges = []
    ingredients = []
    for line in input:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            parts = line.split('-')
            fresh_food_ranges.append([int(parts[0]), int(parts[1])])
        else:
            ingredients.append(int(line))
    return fresh_food_ranges, ingredients

# AI ASSIST
# Sorting/merging ranges to get from O(M) to O(N) complexity
def calculate_total_fresh_ingredients(input):
    ranges = []
    for line in input:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    ranges.sort(key=lambda x: x[0])
    merged = []
    curr_start, curr_end = ranges[0]
    for next_start, next_end in ranges[1:]:
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged.append((curr_start, curr_end))
    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
    return total_count

def run_part_one(mode, expected = None):
    input = open_file( mode + ".txt")
    fresh_food_ranges, ingredients = parse_input(input)
    fresh_ingredients_count = 0
    for ingredient in ingredients:
        is_fresh = False
        for r in fresh_food_ranges:
            if r[0] <= ingredient <= r[1]:
                is_fresh = True
                break
        if is_fresh:
            fresh_ingredients_count += 1
    print_and_verify_answer(mode, "one", fresh_ingredients_count, expected)

def run_part_two(mode, expected = None):
    input = open_file( mode + ".txt")
    total_fresh_ingredients = calculate_total_fresh_ingredients(input)
    print_and_verify_answer(mode, "two", total_fresh_ingredients, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 3)
run_part_one("prod", 821)
run_part_two("test", 14)
run_part_two("prod", 344771884978261)
# Now run it and watch the magic happen 🪄