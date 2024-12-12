import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

# Trusty old DFS saves our butts again (AI assist)
def find_connected_cells(grid, start_row, start_col):
    target_letter = grid[start_row][start_col]
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    connected_cells = []
    
    def dfs(row, col):
        visited.add((row, col))
        connected_cells.append((row, col))
        for movement in movements:
            new_row, new_col = row + movement[0], col + movement[1]
            if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and grid[new_row][new_col] == target_letter and (new_row, new_col) not in visited:
                dfs(new_row, new_col)
    
    if (0 <= start_row < len(grid)) and (0 <= start_col < len(grid[0])):
        dfs(start_row, start_col)
    
    return connected_cells

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    allotment = initialise_grid(data_file)
    cells_visited = set()
    total_fencing = 0
    for row_index, row in enumerate(allotment):
        for cell_index, cell in enumerate(row):
            if (row_index, cell_index) in cells_visited:
                continue
            this_set = find_connected_cells(allotment, row_index, cell_index)
            area = len(this_set)
            perimeter = 0
            for cell in this_set:
                x, y = cell
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) not in this_set:
                        perimeter += 1
            total_fencing += (area * perimeter)
            for cell in this_set:
                cells_visited.add(cell)
    print_and_verify_answer(mode, "one", total_fencing, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    allotment = initialise_grid(data_file)
    cells_visited = set()
    total_price = 0
    for row_index, row in enumerate(allotment):
        for cell_index, cell in enumerate(row):
            if (row_index, cell_index) in cells_visited:
                continue
            this_set = find_connected_cells(allotment, row_index, cell_index)
            area = len(this_set)
            sides = 0
            top_cells_checked = set()
            bottom_cells_checked = set()
            left_cells_checked = set()
            right_cells_checked = set()
            for cell in this_set:
                x, y = cell
                cell_to_left_part_of_set = (x, y - 1) in this_set
                cell_to_right_part_of_set = (x, y + 1) in this_set
                above_cell_part_of_set = (x - 1, y) in this_set
                below_cell_part_of_set = (x + 1, y) in this_set
                above_cell_already_checked_on_left = (x - 1, y) in left_cells_checked
                below_cell_already_checked_on_left = (x + 1, y) in left_cells_checked
                above_cell_already_checked_on_right = (x - 1, y) in right_cells_checked
                below_cell_already_checked_on_right = (x + 1, y) in right_cells_checked
                cell_to_left_already_checked_above = (x, y - 1) in top_cells_checked
                cell_to_right_already_checked_above = (x, y + 1) in top_cells_checked
                cell_to_left_already_checked_below = (x, y - 1) in bottom_cells_checked
                cell_to_right_already_checked_below = (x, y + 1) in bottom_cells_checked               
                if not cell_to_left_part_of_set and not above_cell_already_checked_on_left and not below_cell_already_checked_on_left:
                    sides += 1
                    x, y = cell
                    while (x - 1, y) in this_set and x > 0 and (x-1, y-1) not in this_set:
                        left_cells_checked.add((x - 1, y))
                        x -= 1
                    x, y = cell
                    while (x + 1, y) in this_set and x < len(allotment) - 1 and (x+1, y-1) not in this_set:
                        left_cells_checked.add((x + 1, y))
                        x += 1
                    left_cells_checked.add(cell)                  
                if not cell_to_right_part_of_set and not above_cell_already_checked_on_right and not below_cell_already_checked_on_right:
                    sides += 1
                    x, y = cell
                    while (x - 1, y) in this_set and x > 0 and (x-1, y+1) not in this_set:
                        right_cells_checked.add((x - 1, y))
                        x -= 1
                    x, y = cell
                    while (x + 1, y) in this_set and x < len(allotment) - 1 and (x+1, y+1) not in this_set:
                        right_cells_checked.add((x + 1, y))
                        x += 1
                    right_cells_checked.add(cell)                  
                if not above_cell_part_of_set and not cell_to_left_already_checked_above and not cell_to_right_already_checked_above:
                    sides += 1
                    x, y = cell
                    while (x, y - 1) in this_set and y > 0 and (x-1, y-1) not in this_set:
                        top_cells_checked.add((x, y - 1))
                        y -= 1
                    x, y = cell
                    while (x, y + 1) in this_set and y < len(allotment[0]) - 1 and (x-1, y+1) not in this_set:
                        top_cells_checked.add((x, y + 1))
                        y += 1
                    top_cells_checked.add(cell)
                if not below_cell_part_of_set and not cell_to_left_already_checked_below and not cell_to_right_already_checked_below:
                    sides += 1
                    x, y = cell
                    while (x, y - 1) in this_set and y > 0 and (x+1, y-1) not in this_set:
                        bottom_cells_checked.add((x, y - 1))
                        y -= 1
                    x, y = cell
                    while (x, y + 1) in this_set and y < len(allotment[0]) - 1 and (x+1, y+1) not in this_set:
                        bottom_cells_checked.add((x, y + 1))
                        y += 1
                    bottom_cells_checked.add(cell)
            total_price += (area * sides)
            for cell in this_set:
                cells_visited.add(cell)
    print_and_verify_answer(mode, "two", total_price, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 1930)
run_part_one("prod", 1465112)
run_part_two("test", 1206)
run_part_two("test2", 368)
run_part_two("test3", 236)
run_part_two("prod", 893790)
# Now run it and watch the magic happen 🪄