import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

tree_data = []

for line in file_content:
    tree_data.append(list(line.strip()))

def tree_on_edge(row, col, tree_data):
    if row == 0 or row == len(tree_data)-1:
        return True
    if col == 0 or col == len(tree_data[0])-1:
        return True
    return False

def visible_from_north(row, col, tree_data):
    this_tree_size = int(tree_data[row][col])
    for i in range(0, row):
        if int(tree_data[i][col]) >= this_tree_size:
            return False
    return True

def visible_from_south(row, col, tree_data):
    this_tree_size = int(tree_data[row][col])
    for i in range(row+1, len(tree_data)):
        if int(tree_data[i][col]) >= this_tree_size:
            return False
    return True

def visible_from_west(row, col, tree_data):
    this_tree_size = int(tree_data[row][col])
    for i in range(0, col):
        if int(tree_data[row][i]) >= this_tree_size:
            return False
    return True

def visible_from_east(row, col, tree_data):
    this_tree_size = int(tree_data[row][col])
    for i in range(col+1, len(tree_data[0])):
        if int(tree_data[row][i]) >= this_tree_size:
            print(f"{row},{col}: found bigger tree to east at {row},{i}")
            return False
    return True

counter = 0
for row_index, row in enumerate(tree_data):
    for col_index, col in enumerate(row):
        if tree_on_edge(row_index, col_index, tree_data):
            counter += 1
        elif visible_from_north(row_index, col_index, tree_data) or visible_from_south(row_index, col_index, tree_data) or visible_from_west(row_index, col_index, tree_data) or visible_from_east(row_index, col_index, tree_data):
                counter += 1

print(counter)