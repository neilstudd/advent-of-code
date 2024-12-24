import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def process_operation(gates, gate1, operation, gate2):
    gate1_val = gates.get(gate1)
    gate2_val = gates.get(gate2)
    if operation == "AND":
        return gate1_val & gate2_val
    elif operation == "OR":
        return gate1_val | gate2_val
    elif operation == "XOR":
        return gate1_val ^ gate2_val

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    gates = {}
    new_gates = {}
    for line in data_file:
        line = line.strip()
        if not line:
            continue
        if '->' in line:
            operation, result = line.split('->')
            operation_parts = operation.strip().split()
            new_gates[result.strip()] = operation_parts
        else:
            key, value = line.split(':')
            gates[key.strip()] = int(value.strip())
    while len(new_gates) > 0:
        for gate, gate_val in new_gates.items():
            gate1, operation, gate2 = gate_val
            if gate1 in gates and gate2 in gates:
                gates[gate] = process_operation(gates, gate1, operation, gate2)
                del new_gates[gate]
                break
    answer = "".join([str(gates[key]) for key in sorted(gates.keys(), reverse=True) if key.startswith("z")])
    answer = int(answer, 2) 
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Part Two code goes here

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 2024)
run_part_one("prod", 49574189473968)
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄