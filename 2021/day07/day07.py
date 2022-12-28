import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def triangle_number(n: int) -> int:
  return sum(range(1, n+1))

def find_minimum_fuel(part_two = False):
    best_position = 0
    smallest_sum = 9999999999
    for position in range(max(crabs)):
        sum_of_crabs = 0
        for crab in crabs: 
            if part_two: sum_of_crabs += triangle_number(abs(position - crab))
            else: sum_of_crabs += abs(position - crab)
        if sum_of_crabs < smallest_sum:
            smallest_sum = sum_of_crabs
            best_position = position
    return best_position, smallest_sum

crabs = []
for line in open_file("input.txt"): 
    crab_list = line.strip().split(",")
    for crab in crab_list: crabs.append(int(crab))

best_position, smallest_sum = find_minimum_fuel()
print(f"Part 1: Best position: {best_position} with a sum of {smallest_sum}") # 349 with a sum of 355592
best_position, smallest_sum = find_minimum_fuel(True)
print(f"Part 2: Best position: {best_position} with a sum of {smallest_sum}") # 488 with a sum of 101618069