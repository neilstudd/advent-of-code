import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def count_surrounding_paper(grid, this_row, this_col):
    count = 0
    for check_row in range(max(0, this_row-1), min(len(grid), this_row+2)):
        for check_col in range(max(0, this_col-1), min(len(grid[0]), this_col+2)):
            if (check_row != this_row or check_col != this_col) and grid[check_row][check_col] != ".":
                count += 1
    return count

def process_removal_cycle(grid):
    to_remove = []
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == "@":
                to_remove.append((row_idx, col_idx)) if count_surrounding_paper(grid, row_idx, col_idx) < 4 else None
    for row_idx, col_idx in to_remove:
        grid[row_idx][col_idx] = "."
    return len(to_remove)

def run_part_one(mode, expected = None):
    grid_data = open_file( mode + ".txt")
    grid = initialise_grid(grid_data)
    removable_count = process_removal_cycle(grid) # Just one pass for pt1
    print_and_verify_answer(mode, "One", removable_count, expected)

def run_part_two(mode, expected = None):
    grid_data = open_file( mode + ".txt")
    grid = initialise_grid(grid_data)
    total_rolls_removed = 0
    while True: # Keep checking paper until no more can be removed
        removed_this_cycle = process_removal_cycle(grid)
        if removed_this_cycle == 0:
            break
        total_rolls_removed += removed_this_cycle
    print_and_verify_answer(mode, "Two", total_rolls_removed, expected)
    
# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 13)
run_part_one("prod", 1367)
run_part_two("test", 43)
run_part_two("prod", 9144)
# Now run it and watch the magic happen 🪄