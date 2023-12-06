import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from functools import reduce

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    times = []
    distances = []
    winning_combinations = []

    for line in data_file:
        parts = line.split()
        if parts[0] == "Time:":
            times = [int(x) for x in parts[1:]]
        else:
            distances = [int(x) for x in parts[1:]]
    stats = [{"time": t, "record": d} for t, d in zip(times, distances)]

    for race in stats:
        winners = 0
        for i in range(1,race["time"]):
            speed_and_delay = i
            boat_travels = speed_and_delay * (race["time"]-speed_and_delay)
            if boat_travels > race["record"]:
                winners += 1
        winning_combinations.append(winners)
    
    magic_number = reduce(lambda x, y: x*y, winning_combinations)
    print_and_verify_answer(mode, "one", magic_number, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    time = None
    distance = None

    for line in data_file:
        parts = line.split()
        if parts[0] == "Time:":
            time = int(''.join(parts[1:]))
        else:
            distance = int(''.join(parts[1:]))

    winners = 0
    for i in range(1,time):
        speed_and_delay = i
        boat_travels = speed_and_delay * (time-speed_and_delay)
        if boat_travels > distance:
            winners += 1

    print_and_verify_answer(mode, "two", winners, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 288)
run_part_one("prod", 1159152)
run_part_two("test", 71503)
run_part_two("prod", 41513103)
# Now run it and watch the magic happen 🪄