import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def spawn_fish():
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for line in open_file("input.txt"): 
        for fish in line.strip().split(","): fish_dict[int(fish)] += 1
    return fish_dict

def wait_for_days(shoal, days):
    for _ in range(days):
        new_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        new_fish = 0
        for days, count in shoal.items():
            if days == 0:
                new_fish += count
                new_dict[8] = count
            else: new_dict[days-1] = count
        new_dict[6] += new_fish
        shoal = new_dict
    return sum(shoal.values())

print(f"Part 1: {wait_for_days(spawn_fish(), 80)}") # 380612
print(f"Part 2: {wait_for_days(spawn_fish(), 256)}") # 1710166656900