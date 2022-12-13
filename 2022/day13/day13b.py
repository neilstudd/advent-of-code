import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file
from ast import literal_eval # Thanks, StackOverflow

zero_pad = lambda number: "0" + str(number) if number < 10 else str(number)

def get_first_item_from_list(this_list):
    if len(this_list) == 0:
        return 0
    elif isinstance(this_list[0], int):
        return this_list[0]
    return get_first_item_from_list(this_list[0])

def sort_data(data):
    new_data = []
    for i in range(0, len(data)):
        if isinstance(data[i], int):
            new_data.append(f"{zero_pad(data[i])}: {data[i]}")
        if len(data[i]) == 0:
            new_data.append(f"00: {data[i]}")
        elif isinstance(data[i][0], list):
            new_data.append(f"{zero_pad(get_first_item_from_list(data[i][0]))}: {data[i]}")
        else:
            new_data.append(f"{zero_pad(data[i][0])}: {data[i]}")
    new_data.sort()
    return new_data

raw_data = []
for line in open_file("input.txt"):
    if line.strip() != "":
        raw_data.append(literal_eval(line.strip()))

# add divider packets
raw_data.append([[2]])
raw_data.append([[6]])

# https://pbs.twimg.com/media/EvUc8krXAAUMYnb.jpg
# So, this works, because:
# I've done a very naive sort, to extract the first integer from each packet (or a 0 if it's empty)
# Example: 
#   01: [1, 0, 9, 5, 8]
#   02: [[2], [5]]
# We identify the first packet beginning with a 2 (and a 6)
# It's actually the *wrong* packet because of the naive sort, but because [[2]] is supposed to be
# the first packet in the list which begins with a 2, it gets the correct answer 
first_packet = -1
second_packet = -1
count = 1
for row in sort_data(raw_data):
    if first_packet == -1 and row[:2] == "02":
        first_packet = count
    elif second_packet == -1 and row[:2] == "06":
        second_packet = count
    count += 1
print(f"Part two: {first_packet} * {second_packet} = {first_packet * second_packet}") # 118 * 200 = 23600