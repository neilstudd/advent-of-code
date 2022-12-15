import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def print_grid():
    # Print the grid
    for y in range(-2, len(grid)):
        for x in range(-2, len(grid[y])):
            print(grid[y][x], end='')
        print()

# BUG: For real data, this is too big to generate...
#grid = [["." for x in range(4000000)] for y in range(4000000)]

# Even numpy explodes
# grid = np.full((4000000, 4000000), ".")

grid = [["." for x in range(100)] for y in range(100)]

for line in open_file("input.txt"):
    sensor_x = int(line.split(" ")[2].split(",")[0].split("=")[1])
    sensor_y = int(line.split(" ")[3].split(":")[0].split("=")[1])
    beacon_x = int(line.split(" ")[8].split(",")[0].split("=")[1])
    beacon_y = int(line.split(" ")[9].split(":")[0].split("=")[1])
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    for x in range(sensor_x - distance, sensor_x + distance + 1):
        for y in range(sensor_y - distance, sensor_y + distance + 1):
            if abs(sensor_x - x) + abs(sensor_y - y) <= distance:
                grid[y][x] = "#"
    
    grid[sensor_y][sensor_x] = "S"
    grid[beacon_y][beacon_x] = "B"

print(grid[10].count("#"))    