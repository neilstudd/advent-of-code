import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def are_any_squares_left(squares):
    return len(squares) > 0

def find_connected_cells(grid, start_row, start_col):
    # Get the target letter
    target_letter = grid[start_row][start_col]
    
    # Define the possible movements (up, down, left, right)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Initialize a set to store the visited cells
    visited = set()
    
    # Initialize a list to store the connected cells
    connected_cells = []
    
    # Perform DFS
    def dfs(row, col):
        # Mark the current cell as visited
        visited.add((row, col))
        
        # Add the current cell to the connected cells list
        connected_cells.append((row, col))
        
        # Explore the neighboring cells
        for movement in movements:
            new_row, new_col = row + movement[0], col + movement[1]
            
            # Check if the new position is within the grid boundaries and has the target letter
            if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and grid[new_row][new_col] == target_letter and (new_row, new_col) not in visited:
                dfs(new_row, new_col)
    
    # Start the DFS from the given starting cell
    if (0 <= start_row < len(grid)) and (0 <= start_col < len(grid[0])):
        dfs(start_row, start_col)
    
    return connected_cells

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    allotment = initialise_grid(data_file)
    cells_visited = set()
    total_fencing = 0
    # Use for loop to move through grid from top-left to bottom-right
    for row_index, row in enumerate(allotment):
        for cell_index, cell in enumerate(row):
            if (row_index, cell_index) in cells_visited:
                #print("Already visited cell at", row_index, cell_index)
                continue
            print("Finding all cells connected to the cell at", row_index, cell_index, "with value", cell)
            this_set = find_connected_cells(allotment, row_index, cell_index)
            area = len(this_set)
            perimeter = 0

            # Calculate perimeter of cells in this_set
            for cell in this_set:
                x, y = cell
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) not in this_set:
                        perimeter += 1
            print("Area:", area, "Perimeter:", perimeter)
            total_fencing += (area * perimeter)

            # Add all cells from set to cells_visited
            for cell in this_set:
                cells_visited.add(cell)

    print_and_verify_answer(mode, "one", total_fencing, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")
    allotment = initialise_grid(data_file)
    cells_visited = set()
    total_price = 0
    # Use for loop to move through grid from top-left to bottom-right
    for row_index, row in enumerate(allotment):
        for cell_index, cell in enumerate(row):
            if (row_index, cell_index) in cells_visited:
                #print("Already visited cell at", row_index, cell_index)
                continue
            print("Finding all cells connected to the cell at", row_index, cell_index, "with value", cell)
            this_set = find_connected_cells(allotment, row_index, cell_index)
            area = len(this_set)

            # Find the perimeter, but this time we need to calculate the number of sides, so only count each edge once
            # Calculate perimeter of cells in this_set
            perimeter = 0
            top_cells_checked = set()
            bottom_cells_checked = set()
            left_cells_checked = set()
            right_cells_checked = set()
            for cell in this_set:
                x, y = cell
                print("Checking cell at", x, y)
                cell_to_left_in_this_set = (x, y - 1) in this_set
                cell_to_right_in_this_set = (x, y + 1) in this_set
                cell_above_in_this_set = (x - 1, y) in this_set
                cell_below_in_this_set = (x + 1, y) in this_set


                above_cell_in_left_set = (x - 1, y) in left_cells_checked
                below_cell_in_left_set = (x + 1, y) in left_cells_checked
                above_cell_in_right_set = (x - 1, y) in right_cells_checked
                below_cell_in_right_set = (x + 1, y) in right_cells_checked
                cell_to_left_in_top_set = (x, y - 1) in top_cells_checked
                cell_to_right_in_top_set = (x, y + 1) in top_cells_checked
                cell_to_left_in_bottom_set = (x, y - 1) in bottom_cells_checked
                cell_to_right_in_bottom_set = (x, y + 1) in bottom_cells_checked
                
                if not cell_to_left_in_this_set:
                    print("We're at a left side,")
                    if not above_cell_in_left_set and not below_cell_in_left_set:
                        print("...and we haven't counted this side yet, so add 1")
                        perimeter += 1
                        # mark all other contiguous left cells as checked too
                        checked_up = False
                        x, y = cell
                        while not checked_up:
                            if (x - 1, y) in this_set and x > 0 and (x-1, y-1) not in this_set:
                                left_cells_checked.add((x - 1, y))
                                x -= 1
                            else:
                                checked_up = True
                        checked_down = False
                        x, y = cell
                        while not checked_down:
                            if (x + 1, y) in this_set and x < len(allotment) - 1 and (x+1, y-1) not in this_set:
                                left_cells_checked.add((x + 1, y))
                                x += 1
                            else:
                                checked_down = True
                    left_cells_checked.add(cell)
                    
                if not cell_to_right_in_this_set:
                    print("We're at a right side,")
                    print("Right cells checked: ", right_cells_checked)
                    if not above_cell_in_right_set and not below_cell_in_right_set:
                        print("...and we haven't counted this side yet, so add 1")
                        perimeter += 1
                        # mark all other contiguous right cells as checked too
                        checked_up = False
                        x, y = cell
                        while not checked_up:
                            if (x - 1, y) in this_set and x > 0 and (x-1, y+1) not in this_set: # i.e. not a corner
                                print("adding right cell at", x - 1, y)
                                right_cells_checked.add((x - 1, y))
                                x -= 1
                            else:
                                checked_up = True
                        checked_down = False
                        x, y = cell
                        while not checked_down:
                            if (x + 1, y) in this_set and x < len(allotment) - 1 and (x+1, y+1) not in this_set:
                                print("adding right cell at", x + 1, y)
                                right_cells_checked.add((x + 1, y))
                                x += 1
                            else:
                                checked_down = True
                    right_cells_checked.add(cell)
                if not cell_above_in_this_set:
                    print("We're at a top side,")
                    #print("Top cells checked: ", top_cells_checked)
                    if not cell_to_left_in_top_set and not cell_to_right_in_top_set:
                        print("...and we haven't counted this side yet, so add 1")
                        perimeter += 1
                        # mark all other contiguous top cells as checked too
                        checked_left = False
                        x, y = cell
                        while not checked_left:
                            if (x, y - 1) in this_set and y > 0 and (x-1, y-1) not in this_set:
                                print("adding top cell at", x, y - 1)
                                top_cells_checked.add((x, y - 1))
                                y -= 1
                            else:
                                checked_left = True
                        checked_right = False
                        x, y = cell
                        while not checked_right:
                            if (x, y + 1) in this_set and y < len(allotment[0]) - 1 and (x-1, y+1) not in this_set:
                                print("adding top cell at", x, y + 1)
                                top_cells_checked.add((x, y + 1))
                                y += 1
                            else:
                                checked_right = True
                    top_cells_checked.add(cell)
                if not cell_below_in_this_set:
                    print("We're at a bottom side,")
                    if not cell_to_left_in_bottom_set and not cell_to_right_in_bottom_set:
                        print("...and we haven't counted this side yet, so add 1")
                        perimeter += 1
                        # mark all other contiguous bottom cells as checked too
                        checked_left = False
                        x, y = cell
                        while not checked_left:
                            if (x, y - 1) in this_set and y > 0 and (x+1, y-1) not in this_set:
                                bottom_cells_checked.add((x, y - 1))
                                y -= 1
                            else:
                                checked_left = True
                        checked_right = False
                        x, y = cell
                        while not checked_right:
                            if (x, y + 1) in this_set and y < len(allotment[0]) - 1 and (x+1, y+1) not in this_set:
                                bottom_cells_checked.add((x, y + 1))
                                y += 1
                            else:
                                checked_right = True
                    bottom_cells_checked.add(cell)
                
            sides = perimeter
            print("DEBUG -- Area:", area, "* Number of sides:", sides, "=", area * sides)
            print()
            total_price += (area * sides)

            # Add all cells from set to cells_visited
            for cell in this_set:
                cells_visited.add(cell)

    print_and_verify_answer(mode, "two", total_price, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
#run_part_one("test", 1930)
#run_part_one("prod")
run_part_two("test", 1206)
run_part_two("test2", 368)
run_part_two("test3", 236)
run_part_two("prod", 893790)
# Now run it and watch the magic happen 🪄