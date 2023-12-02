import sys, os, re
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    id_tally = 0
    for line in data_file:
        id = int(re.search(r'Game (\d+):', line).group(1))
        rounds = get_round_data(line)
        valid_bag = True
        for round in rounds:
            if round['blue'] > 14 or round['red'] > 12 or round['green'] > 13:
                valid_bag = False
        id_tally += id if valid_bag else 0
    print_and_verify_answer(mode, "one", id_tally, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    power = 0
    for line in data_file:
        id = int(re.search(r'Game (\d+):', line).group(1))
        rounds = get_round_data(line)
        max_red = 0
        max_green = 0
        max_blue = 0
        for round in rounds:
            if round['blue'] > max_blue:
                max_blue = round['blue']
            if round['red'] > max_red:
                max_red = round['red']
            if round['green'] > max_green:
                max_green = round['green']
        power += (max_red * max_green * max_blue)
    print_and_verify_answer(mode, "two", power, expected)

def get_round_data(line):
    rounds = []
    round_sections = line.split(';')   
    for section in round_sections:
        round_data = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }       
        blue_match = re.search(r'(\d+) blue', section)
        red_match = re.search(r'(\d+) red', section)
        green_match = re.search(r'(\d+) green', section)        
        if blue_match:
            round_data['blue'] = int(blue_match.group(1))
        if red_match:
            round_data['red'] = int(red_match.group(1))
        if green_match:
            round_data['green'] = int(green_match.group(1))        
        rounds.append(round_data)    
    return rounds

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 8)
run_part_one("prod", 2085)
run_part_two("test", 2286)
run_part_two("prod", 79315)
# Now run it and watch the magic happen 🪄