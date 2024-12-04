import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def construct_grid_from_file(file):
    return [list(line.strip()) for line in file]

def is_start_of_word(char):
    return char == "X"

def is_start_of_x(char):
    return char == "M" or char == "S"

def chunk_contains_mas(word_search, row_index, col_index):
    chunk = extract_chunk(word_search, row_index, col_index)
    chunk[0][1], chunk[1][0], chunk[1][2], chunk[2][1] = ".", ".", ".", "."
    valid_chunks = [
        [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
        [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
        [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
        [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
        [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]]
    ]
    return chunk in valid_chunks

def is_word_in_direction(grid, row_index, column_index, direction):
    directions = {
        "north": (-1, 0),
        "north_east": (-1, 1),
        "east": (0, 1),
        "south_east": (1, 1),
        "south": (1, 0),
        "south_west": (1, -1),
        "west": (0, -1),
        "north_west": (-1, -1)
    }

    row_delta, col_delta = directions[direction]
    cells = []
    for i in range(1, 4):
        new_row = row_index + i * row_delta
        new_col = column_index + i * col_delta
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        cells.append(grid[new_row][new_col])
    return is_mas(cells)

def is_mas(cells):
    return "".join(cells) == "MAS"

def section_in_range(grid, row_index, column_index):
    return True if row_index + 2 < len(grid) and column_index + 2 < len(grid[row_index]) else False

def extract_chunk(grid, row_index, column_index):
    if row_index + 2 < len(grid) and column_index + 2 < len(grid[row_index]):
        return [grid[row_index][column_index:column_index+3], 
            grid[row_index + 1][column_index:column_index+3], 
            grid[row_index + 2][column_index:column_index+3]]
    return False

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    word_search = construct_grid_from_file(data_file)
    words_found = 0
    for row_index, row in enumerate(word_search):
        for col_index, col in enumerate(row):
            if is_start_of_word(col):
                directions = ["east", "north", "south", "west", "north_east", "south_east", "south_west", "north_west"]
                for direction in directions:
                    if is_word_in_direction(word_search, row_index, col_index, direction):
                        words_found += 1
    print_and_verify_answer(mode, "one", words_found, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    word_search = construct_grid_from_file(data_file)
    x_found = 0
    for row_index, row in enumerate(word_search):
        for col_index, col in enumerate(row):
            if is_start_of_x(col):
                enough_cells_to_check = section_in_range(word_search, row_index, col_index)
                x_found += 1 if enough_cells_to_check and chunk_contains_mas(word_search, row_index, col_index) else 0
    print_and_verify_answer(mode, "two", x_found, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 18)
run_part_one("prod", 2644)
run_part_two("test", 9)
run_part_two("prod", 1952)
# Now run it and watch the magic happen 🪄