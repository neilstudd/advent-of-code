import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def store_locks_and_keys(data_file):
    locks = []
    keys = []
    grid = []
    for line in data_file:
        if line.strip() == "":
            if grid:
                # Check the first and last line of the grid
                if all([c == "#" for c in grid[0]]):
                    locks.append(grid)
                elif all([c == "#" for c in grid[-1]]):
                    keys.append(grid)
                grid = []  # Reset grid for the next block
        else:
            grid.append(list(line.strip()))

    # Write out the final grid at end of file
    if grid:
        if all([c == "#" for c in grid[0]]):
            locks.append(grid)
        elif all([c == "#" for c in grid[-1]]):
            keys.append(grid)
    return locks, keys
            

def does_key_fit(lock, key):
    for y in range(len(lock)):
        for x in range(len(lock[0])):
            if lock[y][x] == "#" and key[y][x] == "#":
                return False
    return True

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    locks, keys = store_locks_and_keys(data_file)
    keys_which_fit = sum(1 for lock in locks for key in keys if does_key_fit(lock, key))
    print_and_verify_answer(mode, "one", keys_which_fit, expected)

# Can't be completed without finishing both parts of all puzzles :(
def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    answer = None # <-- Change this to answer
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 3)
run_part_one("prod", 3284)
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄