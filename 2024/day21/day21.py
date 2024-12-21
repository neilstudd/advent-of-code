import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from collections import deque
from itertools import product


numpad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }

arrows = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def get_routes_between_buttons(grid, start, end):

    moves = {
        (0, 1): '>',  # Right
        (0, -1): '<', # Left
        (1, 0): 'v',  # Down
        (-1, 0): '^'  # Up
    }
    
    # Initialize the queue for BFS
    queue = deque([(grid[start], "")])
    visited = set()
    shortest_paths = []
    min_length = float('inf')
    
    while queue:
        (current_pos, path) = queue.popleft()
        
        if current_pos == grid[end]:
            if len(path) < min_length:
                min_length = len(path)
                shortest_paths = [path]
            elif len(path) == min_length:
                shortest_paths.append(path)
            continue
        
        for move, symbol in moves.items():
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            if new_pos in grid.values():
                if new_pos not in visited or len(path) + 1 <= min_length:
                    queue.append((new_pos, path + symbol))
        
        # Mark the current position as visited after exploring all moves
        visited.add(current_pos)
    
    return shortest_paths

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    running_total = 0
    for code in data_file:
        current_shortest_sequence = 1000000
        last_char = "A" # Always starts here
        combos = []
        for char in code.strip():
            combos.append(get_routes_between_buttons(numpad, last_char, char))
            combos.append(["A"]) # Press the button
            last_char = char
        all_combinations = [''.join(combo) for combo in product(*combos)]

        # First robot
        last_char = "A" # Always starts here
        all_first_robot_combos = []
        for combination in all_combinations:
            this_combo_combos = []
            for char in combination:
                this_combo_combos.append(get_routes_between_buttons(arrows, last_char, char))
                this_combo_combos.append(["A"]) # Press the button
                last_char = char
            all_first_robot_combos.append([''.join(combo) for combo in product(*this_combo_combos)])

        # Second robot
        last_char = "A" # Always starts here
        for combo_of_combos in all_first_robot_combos:
            for combo in combo_of_combos:
                this_combo_combos = []
                for char in combo:
                    this_combo_combos.append(get_routes_between_buttons(arrows, last_char, char))
                    this_combo_combos.append(["A"]) # Press the button
                    last_char = char

                all_second_robot_combinations = [''.join(combo) for combo in product(*this_combo_combos)]
                shortest_combination = min([len(comb) for comb in all_second_robot_combinations])
                current_shortest_sequence = min(current_shortest_sequence, shortest_combination)

        numeric_code = int(''.join([char for char in code if char.isdigit()]))
        running_total += (current_shortest_sequence * numeric_code)

    print_and_verify_answer(mode, "one", running_total, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")

    # -------------------------------
    # Part Two code goes here

    answer = None # <-- Change this to answer
    # -------------------------------
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 126384)
run_part_one("prod", 94426)
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄