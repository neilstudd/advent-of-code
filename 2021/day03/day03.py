import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def segment_list(input_list):
    zero_list = []
    one_list = []
    for line in input_list:
        if line[i] == "0": zero_list.append(line)
        else: one_list.append(line)
    return zero_list, one_list

input = []
for line in open_file("input.txt"): input.append(line.strip())
oxygen_generator = input.copy()
co2_scrubber = input.copy()

gamma_rate = ""
epsilon_rate = ""
for i in range(len(input[0])):
    zero_count = 0
    one_count = 0
    for line in input:
        if line[i] == "0": zero_count += 1
        else: one_count += 1
    if zero_count > one_count: 
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(f"Part 1: Gamma {gamma_rate}, Epsilon {epsilon_rate}, Power consumption = {gamma_rate * epsilon_rate}") # 1540244

i = 0
while len(oxygen_generator) > 1:
    zero_list, one_list = segment_list(oxygen_generator)
    oxygen_generator = zero_list.copy() if len(zero_list) > len(one_list) else one_list.copy()
    i += 1
oxygen_rate = int(oxygen_generator[0], 2)
i = 0
while len(co2_scrubber) > 1:
    zero_list, one_list = segment_list(co2_scrubber)
    co2_scrubber = one_list.copy() if len(zero_list) > len(one_list) else zero_list.copy()
    i += 1
co2_rate = int(co2_scrubber[0], 2)
print(f"Part 2: Oxygen {oxygen_generator[0]}, CO2 {co2_scrubber[0]}, Life support = {oxygen_rate * co2_rate}") # 4203981