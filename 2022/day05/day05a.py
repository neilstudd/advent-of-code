import sys, os, re
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

def how_many_stacks():
    line_count = 1
    for line in file_content:
        if line[1] == "1":
            return int(line.strip()[-1]), line_count
        line_count += 1

def determine_the_move(text):
    numbers = re.findall(r'\d+', text)
    return int(numbers[0]), int(numbers[1]), int(numbers[2])

stacks, starting_depth = how_many_stacks()
stack_array = [ [] for i in range(stacks) ]

line_count = 0
for line in file_content:
    line_count += 1
    if line_count <= starting_depth:
        line.strip()
        current_index = 0
        for i in range(1, stacks*4, 4):
            thisItem = line[i:i+1]
            stack_array[current_index].insert(0, thisItem) if thisItem != " " else None
            current_index += 1
    else:
        if line[0:4] == "move":
            number_to_move, move_from, move_to = determine_the_move(line)
            for x in range(number_to_move):
                stack_array[move_to-1].append(stack_array[move_from-1].pop())

print("".join([thisStack[-1] for thisStack in stack_array])) # VJSFHWGFT