import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    data_grid = []

    for line in data_file:
        this_line = []
        for char in line.strip():
            this_line.append(char)
        data_grid.append(this_line)

    number_tally = 0
    row_index = 0
    col_index = 0
    this_number = ""
    this_number_touching = False

    for line in data_grid:

        # Special case: check to see if the previous line ended with a number
        if col_index > 0 and this_number != "" and this_number_touching:
            number_tally += int(this_number)
            
        this_number = ""
        this_number_touching = False
        col_index = 0
        for char in line:
            if char.isnumeric():
                if check_for_touching_symbols(data_grid, row_index, col_index):
                    this_number_touching = True
                this_number += char
            elif this_number != "":
                # Anything touching this number?
                if this_number_touching:
                    number_tally += int(this_number)
                    this_number_touching = False
                this_number = ""
            col_index += 1
        row_index += 1

    print_and_verify_answer(mode, "one", number_tally, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    data_grid = []

    for line in data_file:
        this_line = []
        for char in line.strip():
            this_line.append(char)
        data_grid.append(this_line)

    gear_ratios = 0

    # Change values in grid so that each cell has the full number that it's part of
    row_index = 0
    for line in data_grid:
        this_number = ""
        col_index = 0
        for char in line:
            if char.isnumeric():
                this_number += char
            elif this_number != "":
                for i in range(0, len(this_number)):
                    data_grid[row_index][col_index - i - 1] = this_number
                this_number = ""
            col_index += 1
        
        # Now we've finished the line, deal with there being a number in progress
        if this_number != "":
            for i in range(0, len(this_number)):
                data_grid[row_index][col_index - i - 1] = this_number
            this_number = ""
        row_index += 1

    # To ease parsing, add @ symbols on all four sides of grid
    data_grid.insert(0, ["@"] * len(data_grid[0]))
    data_grid.append(["@"] * len(data_grid[0]))
    for line in data_grid:
        line.insert(0, "@")
        line.append("@")
    
    row_index = 0
    col_index = 0

    for line in data_grid:
        col_index = 0
        for char in line:
            if is_gear(char):
                gear_ratios += count_matching_parts(data_grid, row_index, col_index) 
            col_index += 1
        row_index += 1

    print_and_verify_answer(mode, "two", gear_ratios, expected)

def check_for_touching_symbols(data_grid, row_index, col_index):
    if row_index > 0 and is_symbol(data_grid[row_index - 1][col_index]): # Above
        return True
    if row_index > 0 and col_index > 0 and is_symbol(data_grid[row_index - 1][col_index - 1]): # Above Left
        return True
    if row_index > 0 and col_index < len(data_grid[row_index]) - 1 and is_symbol(data_grid[row_index - 1][col_index + 1]): # Above Right
        return True
    if row_index < len(data_grid) - 1 and col_index > 0 and is_symbol(data_grid[row_index + 1][col_index - 1]): # Below Left
        return True
    if row_index < len(data_grid) - 1 and col_index < len(data_grid[row_index]) - 1 and is_symbol(data_grid[row_index + 1][col_index + 1]): # Below Right
        return True
    if row_index < len(data_grid) - 1 and is_symbol(data_grid[row_index + 1][col_index]): # Below
        return True
    if col_index > 0 and is_symbol(data_grid[row_index][col_index - 1]): # Left
        return True
    if col_index < len(data_grid[row_index]) - 1 and is_symbol(data_grid[row_index][col_index + 1]): # Right
        return True
    return False

def is_symbol(char):
    return not (char.isnumeric() or char == ".")

def is_gear(char):
    return char == "*"

def count_matching_parts(data_grid, row_index, col_index):
    touching_numbers_found = []
    nw = data_grid[row_index - 1][col_index - 1]
    n = data_grid[row_index - 1][col_index]
    ne = data_grid[row_index - 1][col_index + 1]
    w = data_grid[row_index][col_index - 1]
    e = data_grid[row_index][col_index + 1]
    sw = data_grid[row_index + 1][col_index - 1]
    s = data_grid[row_index + 1][col_index]
    se = data_grid[row_index + 1][col_index + 1]

    if nw.isnumeric():
        touching_numbers_found.append(nw)
        if not n.isnumeric() and ne.isnumeric(): # i.e. there's a dot to the north
            touching_numbers_found.append(ne)
    elif n.isnumeric():
        touching_numbers_found.append(n)
    elif ne.isnumeric():
        touching_numbers_found.append(ne)
    touching_numbers_found.append(w) if w.isnumeric() else None
    touching_numbers_found.append(e) if e.isnumeric() else None
    if sw.isnumeric():
        touching_numbers_found.append(sw)
        if not s.isnumeric() and se.isnumeric(): # i.e. there's a dot to the south
            touching_numbers_found.append(se)
    elif s.isnumeric():
        touching_numbers_found.append(s)
    elif se.isnumeric():
        touching_numbers_found.append(se)
    print(touching_numbers_found)
    if len(touching_numbers_found) == 2:
        return int(touching_numbers_found[0]) * int(touching_numbers_found[1])
    return 0

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 4361)
run_part_one("prod", 533775)
run_part_two("test", 467835)
run_part_two("prod", 78236071)
# Now run it and watch the magic happen 🪄