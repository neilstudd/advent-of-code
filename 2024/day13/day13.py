import sys, os,re
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def get_numbers_from_line(line):
    pattern = r"X[+=](\d+), Y[+=](\d+)"
    match = re.search(pattern, line)
    return [int(match.group(1)), int(match.group(2))]

def calculate_games(data_file, is_part_two = False):
    games = []
    for line in data_file:
        if "Button A" in line:
            this_game = []
            x,y = get_numbers_from_line(line)
            this_game.append([x, y])
        elif "Button B" in line:
            x,y = get_numbers_from_line(line)
            this_game.append([x, y])
        elif "Prize" in line:
            x,y = get_numbers_from_line(line)
            if is_part_two:
                this_game.append([x+10000000000000, y+10000000000000])
            else:
                this_game.append([x, y])
        elif line == "\n":
            games.append(this_game)
    games.append(this_game) # add the last game...
    return games

# Brute force solver courtesy of my own dumb brain
def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    games = calculate_games(data_file)
    total_tokens_used = 0
    for input in games:
        for x_multiplier in range(0,100):
            for y_multiplier in range(0,100):
                x = x_multiplier * input[0][0] + y_multiplier * input[1][0]
                y = x_multiplier * input[0][1] + y_multiplier * input[1][1]
                if x == input[2][0] and y == input[2][1]:
                    total_tokens_used += (3 * x_multiplier) + y_multiplier
                    break
    print_and_verify_answer(mode, "one", total_tokens_used, expected)

# Linear equation solver courtesy of GPT4o
def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    games = calculate_games(data_file, True)
    total_tokens_used = 0
    for input in games:
        x1, y1 = input[0]
        x2, y2 = input[1]
        x_target, y_target = input[2]

        # Solve the system of linear equations:
        # x = x_multiplier * x1 + y_multiplier * x2
        # y = x_multiplier * y1 + y_multiplier * y2
        # We need to find x_multiplier and y_multiplier such that x == x_target and y == y_target
        det = x1 * y2 - x2 * y1
        if det == 0:
            continue  # No solution if determinant is zero

        # Calculate the multipliers
        x_multiplier = (x_target * y2 - x2 * y_target) // det
        y_multiplier = (x1 * y_target - x_target * y1) // det
        if (x_multiplier * x1 + y_multiplier * x2 == x_target and
            x_multiplier * y1 + y_multiplier * y2 == y_target):
            total_tokens_used += (3 * x_multiplier) + y_multiplier

    print_and_verify_answer(mode, "two", total_tokens_used, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 480)
run_part_one("prod", 26810)
run_part_two("test", 875318608908) # Implied, they don't say.
run_part_two("prod", 108713182988244)
# Now run it and watch the magic happen 🪄