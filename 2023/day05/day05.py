import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    maps = []
    current_map = None
    for line in data_file:
        if line.startswith("seeds:"): # first line
            parts = line.split()
            seeds = [int(x) for x in parts[1:]]
        elif line[0].isalpha(): # start of new map
            if current_map:
                maps.append(current_map)
            current_map = []
        elif line[0].isdigit(): # map line
            parts = line.split()
            parts_split = [int(x) for x in parts]
            current_map.append(parts_split)
    maps.append(current_map) # add last map

    converted_seeds = []
    for seed in seeds:
        for map in maps:
            seed = map_value(map, seed)
        converted_seeds.append(seed)

    print_and_verify_answer(mode, "one", min(converted_seeds), expected)

# NB: Part 2 currently won't complete due to complexity
def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")
    maps = []
    current_map = None
    for line in data_file:
        if line.startswith("seeds:"): # first line
            parts = line.split()
            seeds = generate_seeds(line)
        elif line[0].isalpha(): # start of new map
            if current_map:
                maps.append(current_map)
            current_map = []
        elif line[0].isdigit(): # map line
            parts = line.split()
            parts_split = [int(x) for x in parts]
            current_map.append(parts_split)
    maps.append(current_map) # add last map

    lowest_value = None
    for seed in seeds:
        for map in maps:
            seed = map_value(map, seed)
        lowest_value = seed if lowest_value == None or seed < lowest_value else lowest_value

    print_and_verify_answer(mode, "two", lowest_value, expected)

def map_value(map, value):
    for line in map:
        start, source_start, length = line
        end = source_start + length
        if value < source_start:
            continue 
        elif source_start <= value <= end:
            return start + (value - source_start)
    return value  # Value not found in any range, so leave it unmapped

def generate_seeds(input_str): # ChatGPT assist
    parts = input_str.split()
    numbers = [int(x) for x in parts[1:]]
    for i in range(0, len(numbers), 2):
        start = numbers[i]
        length = numbers[i + 1]
        for num in range(start, start + length):
            yield num

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 35)
run_part_one("prod", 265018614)
run_part_two("test", 46)
run_part_two("prod")
# Now run it and watch the magic happen 🪄