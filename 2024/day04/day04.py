import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def construct_grid_from_file(file):
    grid = []
    for line in file:
        this_line = []
        for char in line.strip():
            this_line.append(char)
        grid.append(this_line)
    return grid

def is_start_of_word(char):
    return char == "X"

def is_start_of_x(char):
    return char == "M" or char == "S"

def is_valid_mas(chunk):
    chunk[0][1] = "."
    chunk[1][0] = "."
    chunk[1][2] = "."
    chunk[2][1] = "."
    return chunk == [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]] or chunk == [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]] or chunk == [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]] or chunk == [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]] or chunk == [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]] 

def is_word_to_north(grid, row_index, column_index):
    if row_index - 3 >= 0:
        return grid[row_index - 1][column_index] == "M" and grid[row_index - 2][column_index] == "A" and grid[row_index - 3][column_index] == "S"
    return False

def is_word_to_north_east(grid, row_index, column_index):
    if row_index - 3 >= 0 and column_index + 3 < len(grid[row_index]):
        return grid[row_index - 1][column_index + 1] == "M" and grid[row_index - 2][column_index + 2] == "A" and grid[row_index - 3][column_index + 3] == "S"
    return False

def is_word_to_east(grid, row_index, column_index):
    if column_index + 3 < len(grid[row_index]):
        return grid[row_index][column_index + 1] == "M" and grid[row_index][column_index + 2] == "A" and grid[row_index][column_index + 3] == "S"
    return False

def is_word_to_south_east(grid, row_index, column_index):
    if row_index + 3 < len(grid) and column_index + 3 < len(grid[row_index]):
        return grid[row_index + 1][column_index + 1] == "M" and grid[row_index + 2][column_index + 2] == "A" and grid[row_index + 3][column_index + 3] == "S"
    return False

def is_word_to_south(grid, row_index, column_index):
    if row_index + 3 < len(grid):
        return grid[row_index + 1][column_index] == "M" and grid[row_index + 2][column_index] == "A" and grid[row_index + 3][column_index] == "S"
    return False

def is_word_to_south_west(grid, row_index, column_index):
    if row_index + 3 < len(grid) and column_index - 3 >= 0:
        return grid[row_index + 1][column_index - 1] == "M" and grid[row_index + 2][column_index - 2] == "A" and grid[row_index + 3][column_index - 3] == "S"
    return False

def is_word_to_west(grid, row_index, column_index):
    if column_index - 3 >= 0:
        return grid[row_index][column_index - 1] == "M" and grid[row_index][column_index - 2] == "A" and grid[row_index][column_index - 3] == "S"
    return False

def is_word_to_north_west(grid, row_index, column_index):
    if row_index - 3 >= 0 and column_index - 3 >= 0:
        return grid[row_index - 1][column_index - 1] == "M" and grid[row_index - 2][column_index - 2] == "A" and grid[row_index - 3][column_index - 3] == "S"
    return False

def extract_potential_x(grid, row_index, column_index):
    if row_index + 2 < len(grid) and column_index + 2 < len(grid[row_index]):
        return [grid[row_index][column_index:column_index+3], grid[row_index + 1][column_index:column_index+3], grid[row_index + 2][column_index:column_index+3]]
    return False

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    word_search = construct_grid_from_file(data_file)
    words_found = 0
    for row_index, row in enumerate(word_search):
        for col_index, col in enumerate(row):
            if is_start_of_word(col):
                if is_word_to_east(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_north(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_south(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_west(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_north_east(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_south_east(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_south_west(word_search, row_index, col_index):
                    words_found += 1
                if is_word_to_north_west(word_search, row_index, col_index):
                    words_found += 1

    print_and_verify_answer(mode, "one", words_found, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    word_search = construct_grid_from_file(data_file)
    x_found = 0

    for row_index, row in enumerate(word_search):
        for col_index, col in enumerate(row):
            if is_start_of_x(col):
                this_mas = extract_potential_x(word_search, row_index, col_index)
                if this_mas:
                    if is_valid_mas(this_mas):
                        x_found += 1

    print_and_verify_answer(mode, "two", x_found, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 18)
run_part_one("prod", 2644)
run_part_two("test", 9)
run_part_two("prod", 1952)
# Now run it and watch the magic happen 🪄