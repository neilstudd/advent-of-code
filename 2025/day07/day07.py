import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer, initialise_grid

def run_part_one(mode, expected = None):
    grid_data = open_file( mode + ".txt")
    grid = initialise_grid(grid_data)
    for line in grid:
        if "S" in line:
            beam_indices = [line.index("S")]
        else:
            new_beam_indices = []
            for index in beam_indices:
                if line[index] == ".":
                    new_beam_indices.append(index)
                elif line[index] == "^":
                    line[index] = "X" # we hit this splitter
                    new_beam_indices.append(index - 1)
                    new_beam_indices.append(index + 1)
            beam_indices = new_beam_indices
    beam_hit_count = sum(line.count("X") for line in grid)
    print_and_verify_answer(mode, "One", beam_hit_count, expected)

def run_part_two(mode, expected = None):
    grid_data = open_file( mode + ".txt")
    grid = initialise_grid(grid_data)
    beam_indices = {}
    for line in grid:
        if "S" in line:
            beam_indices = {line.index("S"): 1}
        else:
            for index, count in list(beam_indices.items()):
                if line[index] == "^":
                    beam_indices[index] = 0 # no longer a beam in this column
                    beam_indices[index - 1] = beam_indices.get(index - 1, 0) + count
                    beam_indices[index + 1] = beam_indices.get(index + 1, 0) + count
    total_ways = sum(beam_indices.values())
    print_and_verify_answer(mode, "Two", total_ways, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 21)
run_part_one("prod", 1585)
run_part_two("test", 40)
run_part_two("prod", 16716444407407) # FIRST SUBMIT: "435 too low" (lol)
# Now run it and watch the magic happen 🪄