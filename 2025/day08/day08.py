import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def already_in_same_circuit(junction1, junction2, connected_junctions):
    for conn_set in connected_junctions:
        if junction1 in conn_set and junction2 in conn_set:
            return True
    return False

# AI ASSIST
# Find the closest pair of junctions which we've not opted to exclude
def find_closest_junctions(all_junctions, excluded_junctions):
    min_distance = None
    closest_junctions = None
    for i in range(len(all_junctions)):
        for j in range(i + 1, len(all_junctions)):
            x1, y1, z1 = all_junctions[i]
            x2, y2, z2 = all_junctions[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            if (min_distance is None or distance < min_distance) and (all_junctions[i], all_junctions[j]) not in excluded_junctions and (all_junctions[j], all_junctions[i]) not in excluded_junctions:
                min_distance = distance
                closest_junctions = (all_junctions[i], all_junctions[j])
    return closest_junctions

def run_part_one(mode, expected = None):
    junction_box_data = open_file( mode + ".txt")
    loop_target = 10 if mode == "test" else 1000
    all_junctions = []
    connected_junctions = []
    excluded_junctions = []
    for line in junction_box_data:
        line = line.strip()
        coords = tuple(int(x) for x in line.split(","))
        all_junctions.append(coords)
    loops_completed = 0
    while loops_completed < loop_target:
        closest1, closest2 = find_closest_junctions(all_junctions, excluded_junctions)
        if not already_in_same_circuit(closest1, closest2, connected_junctions):
            sets_to_merge = []
            for idx, conn_set in enumerate(connected_junctions):
                if closest1 in conn_set or closest2 in conn_set:
                    sets_to_merge.append(idx)
            if sets_to_merge:
                new_set = set()
                for idx in reversed(sets_to_merge):
                    new_set.update(connected_junctions[idx])
                    del connected_junctions[idx]
                new_set.update([closest1, closest2])
                connected_junctions.append(new_set)
            else:
                connected_junctions.append(set([closest1, closest2]))        
        excluded_junctions.append((closest1, closest2)) # Don't try this pair again
        loops_completed += 1
    # Find the three longest chains, and multiply their lengths
    connected_junctions.sort(key=lambda x: len(x), reverse=True)
    total_top_three = 1
    for i in range(3):
        total_top_three *= len(connected_junctions[i])
    print_and_verify_answer(mode, "one", total_top_three, expected)

def run_part_two(mode, expected = None):
    junction_box_data = open_file(mode + ".txt")
    all_junctions = []
    connected_junctions = []
    excluded_junctions = set()
    for line in junction_box_data:
        line = line.strip()
        coords = tuple(int(x) for x in line.split(","))
        all_junctions.append(coords)
    unconnected_junctions = set(all_junctions)
    while unconnected_junctions:
        closest1, closest2 = find_closest_junctions(all_junctions, excluded_junctions)
        if already_in_same_circuit(closest1, closest2, connected_junctions):
            excluded_junctions.add((closest1, closest2))
            continue
        unconnected_junctions.discard(closest1)
        unconnected_junctions.discard(closest2)
        sets_to_merge = []
        for idx, conn_set in enumerate(connected_junctions):
            if closest1 in conn_set or closest2 in conn_set:
                sets_to_merge.append(idx)
        if sets_to_merge:
            new_set = set()
            for idx in reversed(sets_to_merge):
                new_set.update(connected_junctions[idx])
                del connected_junctions[idx]
            new_set.update([closest1, closest2])
            connected_junctions.append(new_set)
        else:
            connected_junctions.append(set([closest1, closest2]))
        excluded_junctions.add((closest1, closest2))
        print("Unconnected junctions remaining:", len(unconnected_junctions))    
    # When we bust out of the loop, closest1 and closest2 are the last pair we connected
    # Multiply their x coordinates
    multiplied_x = closest1[0] * closest2[0]
    print_and_verify_answer(mode, "two", multiplied_x, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 40)
run_part_one("prod", 50568) # FIRST SUBMIT: 6210 too low (wasn't merging sets)
run_part_two("test", 25272)
run_part_two("prod", 36045012) # Takes about 20 minutes to run...
# Now run it and (very slowly today) watch the magic happen 🪄