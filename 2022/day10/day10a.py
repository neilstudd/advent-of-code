import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def update_key_cycles():
    global last_cycle_summed, summed_strengths
    if cycle in key_cycles:
        if last_cycle_summed != cycle:
            summed_strengths += x * cycle
            last_cycle_summed = cycle 

is_addx = lambda line: line.startswith("addx")
key_cycles = [20, 60, 100, 140, 180, 220]
cycle = 0
x = 1
last_cycle_summed = 0
summed_strengths = 0

for line in open_file("input.txt"):
    cycle += 1
    update_key_cycles()
    cycle += 1 if is_addx(line) else 0
    update_key_cycles()
    x += int(line.split(" ")[1]) if is_addx(line) else 0

print(summed_strengths) # 16880