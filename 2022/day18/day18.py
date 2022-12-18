import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def create_grid(x, y, z):
    return [[[0 for k in range(z)] for j in range(y)] for i in range(x)]

def create_exposure_grid(x, y, z):
    return [[[None for k in range(z)] for j in range(y)] for i in range(x)]

def is_exposed(x, y, z):
    return exposed[x][y][z]

cubes = create_grid(30, 30, 30)
exposed = create_exposure_grid(30, 30, 30)

for line in open_file("input.txt"):
    x, y, z = line.strip().split(",")
    cubes[int(x)][int(y)][int(z)] = 1

# Traverse through all nodes in cubes, and calculate if that node has a route to the edge
# (i.e. it connects to a line of 0s)
for x in range(len(cubes)):
    for y in range(len(cubes[x])):
        for z in range(len(cubes[x][y])):
            if cubes[x][y][z] == 0:
                if x == 0 or cubes[x-1][y][z] == 0: exposed[x][y][z] = True
                elif y == 0 or cubes[x][y-1][z] == 0: exposed[x][y][z] = True
                elif z == 0 or cubes[x][y][z-1] == 0: exposed[x][y][z] = True
                elif x == len(cubes)-1 or cubes[x+1][y][z] == 0: exposed[x][y][z] = True
                elif y == len(cubes[x])-1 or cubes[x][y+1][z] == 0: exposed[x][y][z] = True
                elif z == len(cubes[x][y])-1 or cubes[x][y][z+1] == 0: exposed[x][y][z] = True
                else:
                    exposed[x][y][z] = False
            else:
                exposed[x][y][z] = False

# Count outside faces
num_faces = 0
for x in range(len(cubes)):
    for y in range(len(cubes[x])):
        for z in range(len(cubes[x][y])):
            if cubes[x][y][z] != 0:
                if x == 0 or cubes[x-1][y][z] == 0: num_faces += 1
                if x == len(cubes)-1 or cubes[x+1][y][z] == 0: num_faces += 1
                if y == 0 or cubes[x][y-1][z] == 0: num_faces += 1
                if y == len(cubes[x])-1 or cubes[x][y+1][z] == 0: num_faces += 1
                if z == 0 or cubes[x][y][z-1] == 0: num_faces += 1
                if z == len(cubes[x][y])-1 or cubes[x][y][z+1] == 0: num_faces += 1
print(f"Part 1: {num_faces}") # 3586

# Count just the exposed faces
num_exposed_faces = 0
for x in range(len(cubes)):
    for y in range(len(cubes[x])):
        for z in range(len(cubes[x][y])):
            if cubes[x][y][z] != 0:
                if is_exposed(x-1, y, z): num_exposed_faces += 1
                if is_exposed(x+1, y, z): num_exposed_faces += 1
                if is_exposed(x, y-1, z): num_exposed_faces += 1
                if is_exposed(x, y+1, z): num_exposed_faces += 1
                if is_exposed(x, y, z-1): num_exposed_faces += 1
                if is_exposed(x, y, z+1): num_exposed_faces += 1

print(f"Part 2: {num_exposed_faces}") # 1792 too low, 3023 too high