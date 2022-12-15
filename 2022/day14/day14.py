import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

can_drop_to = lambda x, y: grid[y][x] == '.'

def fill_lines(this_x, this_y, next_x, next_y):
    if this_x > next_x:
        for x in range(int(this_x), int(next_x)-1, -1): grid[this_y][x] = '#'
    elif this_x < next_x:
        for x in range(int(this_x), int(next_x)+1): grid[this_y][x] = '#'
    elif this_y > next_y:
        for y in range(int(this_y), int(next_y)-1, -1): grid[y][this_x] = '#'
    else:
        for y in range(int(this_y), int(next_y)+1): grid[y][this_x] = '#'

def print_grid():
    for y in range(200):
        for x in range(400, 720): print(grid[y][x], end='')
        print()

def determine_abyss_row():
    for y in range(len(grid)-1, 0, -1):
        if '#' in grid[y]: return y

def drop_sand():
    sand_location = (500, 0)
    while sand_location[1] < abyss_row:
        if can_drop_to(sand_location[0], sand_location[1]+1):
            sand_location = (sand_location[0], sand_location[1]+1)
        elif can_drop_to(sand_location[0]-1, sand_location[1]+1):
            sand_location = (sand_location[0]-1, sand_location[1]+1)
        elif can_drop_to(sand_location[0]+1, sand_location[1]+1):
            sand_location = (sand_location[0]+1, sand_location[1]+1)
        else:
            grid[sand_location[1]][sand_location[0]] = 'o'
            return True
    if sand_location[1] >= abyss_row:
        print("IN THE ABYSS")
        return False
    return True

def flush_sand():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'o': grid[y][x] = '.'

grid = [['.' for x in range(1000)] for y in range(1000)]
for line in open_file("input.txt"):
    coords = line.strip().split(' -> ')
    for index, coord in enumerate(coords):
        if index < len(coords)-1:
            this_x, this_y = coord.split(',')
            next_x, next_y = coords[index+1].split(',')
            fill_lines(int(this_x), int(this_y), int(next_x), int(next_y))

abyss_row = determine_abyss_row()
sand_dropped = 0
while True:
    if not drop_sand():
        print(f"Part 1: Successfully dropped {sand_dropped} pieces of sand") # 578
        break
    sand_dropped += 1

# PART 2: Re-initialise grid (remove sand, and draw floor)
flush_sand()
abyss_row += 2
grid[abyss_row] = ['#' for x in range(1000)]
sand_dropped = 0
while grid[0][500] != "o":
    sand_dropped += 1
    drop_sand()
print(f"Part 2: Successfully dropped {sand_dropped} pieces of sand") # 24377