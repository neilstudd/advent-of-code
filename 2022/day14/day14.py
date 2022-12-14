import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def fill_lines(this_x, this_y, next_x, next_y):
    print(f"fill from {this_x}, {this_y} to {next_x}, {next_y}")
    if this_x > next_x:
        print(f"1: x is decreasing")
        for x in range(int(this_x), int(next_x)-1, -1):
                grid[this_y][x] = '#'
    elif this_x < next_x:
        print(f"2: x is increasing")
        for x in range(int(this_x), int(next_x)+1):
                grid[this_y][x] = '#'
    elif this_y > next_y:
        print(f"3: y is decreasing")
        for y in range(int(this_y), int(next_y)-1, -1):
                grid[y][this_x] = '#'
    elif this_y < next_y:
        print(f"4: y is increasing")
        for y in range(int(this_y), int(next_y)+1):
                grid[y][this_x] = '#'
    else:
        print("I shouldn't be here")

def print_grid():
    # Print the grid for x > 493 and y < 11
    for y in range(200):
        for x in range(400, 520):
            print(grid[y][x], end='')
        print()

def determine_abyss_row():
    # Get index of last row that has a '#' in it
    for y in range(len(grid)-1, 0, -1):
        if '#' in grid[y]:
            return y

def drop_sand():
    sand_location = (500, 0)
    while sand_location[1] < abyss_row:
        if can_move_down_to(sand_location[0], sand_location[1]+1):
            sand_location = (sand_location[0], sand_location[1]+1)
        elif can_move_down_to(sand_location[0]-1, sand_location[1]+1):
            sand_location = (sand_location[0]-1, sand_location[1]+1)
        elif can_move_down_to(sand_location[0]+1, sand_location[1]+1):
            sand_location = (sand_location[0]+1, sand_location[1]+1)
        else:
            grid[sand_location[1]][sand_location[0]] = 'o'
            return True
    # if entrance_blocked:
    #     print("ENTRANCE BLOCKED")
    #     return False
    if sand_location[1] >= abyss_row:
        print("IN THE ABYSS")
        return False
    return True

def flush_sand():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'o':
                grid[y][x] = '.'

can_move_down_to = lambda x, y: grid[y][x] == '.'
entrance_blocked = lambda: grid[0][500] == 'o'

# Create a grid of dots that's 1000 wide, 1000 high
grid = [['.' for x in range(1000)] for y in range(1000)]

# Populate the grid with the input
for line in open_file("input.txt"):

    # Line will be in the following format:
    # 498,4 -> 498,6 -> 496,6
    # Extract these coordinates and draw lines between them in the grid
    coords = line.strip().split(' -> ')
    for index, coord in enumerate(coords):
        if index < len(coords)-1:
            this_x, this_y = coord.split(',')
            next_x, next_y = coords[index+1].split(',')
            fill_lines(int(this_x), int(this_y), int(next_x), int(next_y))

abyss_row = determine_abyss_row() # Game over when we hit this row

# Drop one piece of sand
for i in range(1000):
    if not drop_sand():
        print(f"Part 1: Successfully dropped {i} pieces of sand") # 578
        #print_grid()
        break

# PART 2: Re-initialise grid (remove sand, and draw floor)
flush_sand()
abyss_row += 2
grid[abyss_row] = ['#' for x in range(1000)]
for i in range(1000000):
    drop_sand()
    if grid[0][500] == "o":
        print(f"Part 2: Successfully dropped {i+1} pieces of sand") # 24377
        print_grid()
        break