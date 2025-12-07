import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def run_part_one(mode, expected = None):
    grid_data = open_file( mode + ".txt")
    grid = initialise_grid(grid_data)
    for line in grid:
        # check if S in line
        if "S" in line:
            beam_indices = [line.index("S")]
        else:
            new_beam_indices = []
            for index in beam_indices:
                if line[index] == ".":
                    line[index] = "|"
                    new_beam_indices.append(index)
                elif line[index] == "^":
                    line[index] = "X" # we hit this splitter
                    if index - 1 >= 0:
                        new_beam_indices.append(index - 1)
                        line[index-1] = "|"
                    if index + 1 < len(line):
                        new_beam_indices.append(index + 1)
                        line[index+1] = "|"
            beam_indices = new_beam_indices

    # count the number of X's (the number of splitters we hit)
    beam_hit_count = sum(line.count("X") for line in grid)
    print_and_verify_answer(mode, "One", beam_hit_count, expected)

def run_part_two(mode, expected = None):
    pass

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 21)
run_part_one("prod", 1585)
run_part_two("test", 0)
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄