import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

encrypted_file = []
index = 0
for line in open_file("input.txt"):
    encrypted_file.append({"value": int(line.strip()), "start_pos": index})
    index += 1

current_positions = encrypted_file.copy()

index = 0
for move in encrypted_file:
    # Find item in encrypted_file where start_pos = index
    cur_pos = next((i for i, item in enumerate(current_positions) if item["start_pos"] == index), None)
    new_pos = cur_pos + move["value"]
    if new_pos > 0:    
        while new_pos > len(current_positions) - 1: new_pos -= len(current_positions)-1
    elif new_pos < 0:
        while abs(new_pos) > len(current_positions) - 1: new_pos += len(current_positions)-1
    current_positions.insert(new_pos, current_positions.pop(cur_pos))
    index += 1
    
start_of_coords = next((i for i, item in enumerate(current_positions) if item["value"] == 0), None)
thousandth_coord = current_positions[(start_of_coords+1000) % len(current_positions)]["value"]
two_thousandth_coord = current_positions[(start_of_coords+2000) % len(current_positions)]["value"]
three_thousandth_coord = current_positions[(start_of_coords+3000) % len(current_positions)]["value"]
print(f"Part 1: 1000th coord is {thousandth_coord}, 2000th coord is {two_thousandth_coord}, 3000th coord is {three_thousandth_coord}, sum is {thousandth_coord + two_thousandth_coord + three_thousandth_coord}") # 8712; -4413; 9668; answer is 13967