import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def calculate_movement(line):
    line = line.strip()
    if line[0] == 'R':
        return int(line[1:])
    else:
        return -int(line[1:])

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    current_safe_value = 50
    times_at_zero = 0
    for rotation in data_file:
        current_safe_value = (current_safe_value + calculate_movement(rotation)) % 100        
        times_at_zero += 1 if current_safe_value == 0 else 0
    print_and_verify_answer(mode, "one", times_at_zero, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    current_safe_value = 50
    times_at_zero = 0
    for rotation in data_file:
        movement = calculate_movement(rotation)
        # Manually "step through" every rotation. How many times do we pass through 0?
        number_of_steps = abs(movement)
        step_direction = 1 if movement > 0 else -1
        for step in range(number_of_steps):
            current_safe_value = (current_safe_value + step_direction) % 100
            times_at_zero += 1 if current_safe_value == 0 else 0
    print_and_verify_answer(mode, "two", times_at_zero, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 3)
run_part_one("prod", 992)
run_part_two("test", 6)
run_part_two("prod", 6133)
# Now run it and watch the magic happen 🪄