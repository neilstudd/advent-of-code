import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from math import gcd

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    sequence, tunnels = build_tunnels(data_file)
    found_exit = False
    sequence_index = -1
    moves = 0
    tunnel_name = "AAA"
    while not found_exit:
        tunnel_data = next((tunnel for tunnel in tunnels if tunnel['name'] == tunnel_name), None)
        if is_exit(tunnel_data):
            found_exit = True
            break
        if sequence_index == len(sequence)-1:
            sequence_index = 0
        else:
            sequence_index += 1
        this_sequence = sequence[sequence_index]
        tunnel_name = tunnel_data["options"][0] if this_sequence == "L" else tunnel_data["options"][1]
        moves += 1
    print_and_verify_answer(mode, "one", moves, expected)

# GPT assist: Brute forcing won't work for 21 trillion... 
# Calculate the length of the route through each tunnel, then find the "lowest
# common multiple" to establish when they align.
def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    sequence, tunnels = build_tunnels(data_file)

    # construct a list of all the is_entrance tunnels
    entrances = [tunnel for tunnel in tunnels if tunnel["is_entrance"]]

    exit_cycle_lengths = []
    for entrance in entrances:
        at_exit = False
        sequence_index = -1
        moves = 0
        while not at_exit:
            if sequence_index == len(sequence)-1:
                sequence_index = 0
            else:
                sequence_index += 1
            tunnel_data = next((tunnel for tunnel in tunnels if tunnel['name'] == entrance["name"]), None)
            this_sequence = sequence[sequence_index]
            new_entrance_name = tunnel_data["options"][0] if this_sequence == "L" else tunnel_data["options"][1]
            new_entrance = next((tunnel for tunnel in tunnels if tunnel['name'] == new_entrance_name), None)
            entrance["name"] = new_entrance["name"]
            entrance["options"] = new_entrance["options"]
            entrance["is_entrance"] = new_entrance["is_entrance"]
            entrance["is_exit"] = new_entrance["is_exit"]
            moves += 1
            at_exit = entrance["is_exit"]
        exit_cycle_lengths.append(moves)            
    
    lcm = 1
    for i in exit_cycle_lengths:
        lcm = lcm*i//gcd(lcm, i)

    print_and_verify_answer(mode, "two", lcm, expected)

def is_exit(tunnel):
    return tunnel["name"] == "ZZZ"

def build_tunnels(data_file):
    sequence = []
    tunnels = []
    for line in data_file:
        if sequence == []:
            sequence = list(line.strip())
        elif line.strip() != "":
            parts = line.strip().split('=')
            name = parts[0].strip()
            options_str = parts[1].strip().strip('()')
            options = [option.strip() for option in options_str.split(',')]
            result = {"name": name, "options": options, "is_entrance": name.endswith("A"), "is_exit": name.endswith("Z") }
            tunnels.append(result)
    return sequence, tunnels

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2)
run_part_one("test2", 6)
run_part_one("prod")
run_part_two("test3", 6)
run_part_two("prod", 21083806112641)
# Now run it and watch the magic happen 🪄