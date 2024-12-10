import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def get_all_coords_with_this_character(grid, reference_char):
    return [(line_index, char_index) for line_index, line in enumerate(grid) for char_index, char in enumerate(line) if char == reference_char]

def add_all_antinodes(grid, antinodes, line_index, char_index, line_diff, row_diff):
    antinode_target_location = (line_index + line_diff, char_index + row_diff)
    while antinode_target_location[0] < len(grid) and antinode_target_location[1] < len(grid[0]) and antinode_target_location[0] >= 0 and antinode_target_location[1] >= 0:
        antinodes.add((antinode_target_location[0], antinode_target_location[1]))
        antinode_target_location = (antinode_target_location[0] + line_diff, antinode_target_location[1] + row_diff)
    return antinodes

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    grid = initialise_grid(data_file)
    antinodes = set()
    for line_index, line in enumerate(grid):
        for char_index, char in enumerate(line):
            if char != ".":
                for target_line, target_row in get_all_coords_with_this_character(grid, char):
                    if target_line != line_index and target_row != char_index: # don't check yourself lest you wreck yourself
                        line_diff = target_line - line_index
                        row_diff = target_row - char_index
                        antinode_target_location = (target_line + line_diff, target_row + row_diff)
                        if antinode_target_location[0] < len(grid) and antinode_target_location[1] < len(grid[0]) and antinode_target_location[0] >= 0 and antinode_target_location[1] >= 0:
                            antinodes.add((antinode_target_location[0], antinode_target_location[1]))
    print_and_verify_answer(mode, "one", len(antinodes), expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    grid = initialise_grid(data_file)
    antinodes = set()
    for line_index, line in enumerate(grid):
        for char_index, char in enumerate(line):
            if char != ".":
                for target_line, target_row in get_all_coords_with_this_character(grid, char):
                    if target_line != line_index and target_row != char_index: # don't check yourself lest you wreck yourself
                        line_diff = target_line - line_index
                        row_diff = target_row - char_index
                        antinodes = add_all_antinodes(grid, antinodes, target_line, target_row, line_diff, row_diff) # Add downwards
                        antinodes = add_all_antinodes(grid, antinodes, target_line, target_row, -line_diff, -row_diff) # Add upwards
    
    print_and_verify_answer(mode, "two", len(antinodes), expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 14)
run_part_one("prod", 301)
run_part_two("test", 34)
run_part_two("prod", 1019)
# Now run it and watch the magic happen 🪄