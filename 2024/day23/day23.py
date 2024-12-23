import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from itertools import combinations



def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    networked_computers = []
    for line in data_file:
        c1, c2 = line.strip().split("-")
        networked_computers.append([c1, c2])
        
    links = {frozenset(pair) for pair in networked_computers}
    trios_of_machines = set()

    # Check all combinations of three nodes
    for a, b, c in combinations(set().union(*networked_computers), 3):
        if frozenset([a, b]) in links and frozenset([b, c]) in links and frozenset([a, c]) in links:
            trios_of_machines.add(frozenset([a, b, c]))

    result = [list(trio) for trio in trios_of_machines]
    answer = sum(1 for trio in result if any(computer.startswith("t") for computer in trio))
    print_and_verify_answer(mode, "one", answer, expected)

# Needed an AI assist to get this to be performant 🤖
def run_part_two(mode, expected=None):
    data_file = open_file(mode + ".txt")
    networked_computers = []
    for line in data_file:
        c1, c2 = line.strip().split("-")
        networked_computers.append([c1, c2])

    links = {frozenset(pair) for pair in networked_computers}

    def find_largest_group(nodes, potential_group, candidates, already_found):
        nonlocal largest_group

        if not candidates and not already_found:
            if len(potential_group) > len(largest_group):
                largest_group = potential_group[:]
            return

        for node in list(candidates):
            new_candidates = candidates.intersection(neighbours[node])
            new_already_found = already_found.intersection(neighbours[node])
            find_largest_group(nodes, potential_group + [node], new_candidates, new_already_found)
            candidates.remove(node)
            already_found.add(node)

    neighbours = {node: set() for node in set().union(*networked_computers)}
    for a, b in links:
        neighbours[a].add(b)
        neighbours[b].add(a)

    largest_group = []
    all_nodes = set(neighbours.keys())
    find_largest_group(all_nodes, [], all_nodes, set())
    answer = ",".join(sorted(largest_group))
    print_and_verify_answer(mode, "two", answer, expected)


# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 7)
run_part_one("prod", 1119)
run_part_two("test","co,de,ka,ta")
run_part_two("prod","av,fr,gj,hk,ii,je,jo,lq,ny,qd,uq,wq,xc")
# Now run it and watch the magic happen 🪄