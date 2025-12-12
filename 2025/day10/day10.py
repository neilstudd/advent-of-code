import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from collections import deque

def parse_input(input):
    machines = []
    for line in input:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        machine = {
            "target_lights": list(parts[0][1:-1]),
            "buttons": [list(map(int, button.strip("()").split(","))) for button in parts[1:-1]],
            "joltages": list(map(int, parts[-1].strip("{}").split(",")))
        }
        machines.append(machine)
    return machines

# AI ASSIST
# My annual reminder on how deque works
def calculate_steps_to_light_sequence(machine):
    initial_state = ''.join(['.' for _ in machine["target_lights"]])
    target_state =  ''.join(machine["target_lights"])
    button_effects = machine["buttons"]
    queue = deque([(initial_state, 0)])
    visited = set([initial_state])
    while queue:
        current_state, keypress_count = queue.popleft()
        if current_state == target_state:
            return keypress_count
        for button in button_effects:
            new_state_list = list(current_state)
            for index in button:
                if 0 <= index < len(new_state_list):
                    new_state_list[index] = '#' if new_state_list[index] == '.' else '.'
            new_state = ''.join(new_state_list)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, keypress_count + 1))
    print("ERROR - No solution found!")

def run_part_one(mode, expected = None):
    input = open_file( mode + ".txt")
    machines = parse_input(input)
    total_keypresses = sum(calculate_steps_to_light_sequence(machine) for machine in machines)
    print_and_verify_answer(mode, "one", total_keypresses, expected)

def run_part_two(mode, expected = None):
    pass

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 7)
run_part_one("prod", 479)
run_part_two("test", 33)
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄