import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def create_grid(x, y, z):
    return [[[0 for k in range(z)] for j in range(y)] for i in range(x)]

def is_exposed(x, y, z):
    # TODO: Implement this
    return True

cubes = create_grid(20, 20, 20)

for line in  open_file("input.txt"):
    x, y, z = line.strip().split(",")
    cubes[int(x)][int(y)][int(z)] = 1

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
                if x == 0: num_exposed_faces += 1
                elif cubes[x-1][y][z] == 0:
                    if is_exposed(x-1, y, z): num_exposed_faces += 1
                if x == len(cubes)-1: num_exposed_faces += 1
                elif cubes[x+1][y][z] == 0:
                    if is_exposed(x+1, y, z): num_exposed_faces += 1
                if y == 0: num_exposed_faces += 1
                elif cubes[x][y-1][z] == 0:
                    if is_exposed(x, y-1, z): num_exposed_faces += 1 
                if y == len(cubes[x])-1: num_exposed_faces += 1
                elif cubes[x][y+1][z] == 0:
                    if is_exposed(x, y+1, z): num_exposed_faces += 1
                if z == 0: num_exposed_faces += 1
                elif cubes[x][y][z-1] == 0:
                    if is_exposed(x, y, z-1): num_exposed_faces += 1
                # Check if the back face is not touching another cube
                if z == len(cubes[x][y])-1: num_exposed_faces += 1
                elif cubes[x][y][z+1] == 0:
                    if is_exposed(x, y, z+1): num_exposed_faces += 1

print(f"Part 2: {num_exposed_faces}")