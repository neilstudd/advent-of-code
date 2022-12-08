import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def get_west_view(row, col, tree_data):
    trees = []
    for i in range(0, col+1):
        trees.append(int(tree_data[row][i]))
    trees.reverse()
    return trees

def get_east_view(row, col, tree_data):
    trees = []
    for i in range(col, len(tree_data[0])):
        trees.append(int(tree_data[row][i]))
    return trees

def get_north_view(row, col, tree_data):
    trees = []
    for i in range(0, row+1):
        trees.append(int(tree_data[i][col]))
    trees.reverse()
    return trees

def get_south_view(row, col, tree_data):
    trees = []
    for i in range(row, len(tree_data)):
        trees.append(int(tree_data[i][col]))
    return trees

def get_score(list):
    if len(list) == 1:
        return 1
    first_element = list.pop(0)
    for i, item in enumerate(list):
        if item >= first_element:
            break
    return i+1

file_content = open_file("input.txt")

tree_data = []
for line in file_content:
    tree_data.append(list(line.strip()))

best_scenic_score = 0
for row_index, row in enumerate(tree_data):
    for col_index, col in enumerate(row):
        scenic_score = get_score(get_west_view(row_index, col_index, tree_data)) * \
            get_score(get_east_view(row_index, col_index, tree_data)) * \
            get_score(get_south_view(row_index, col_index, tree_data)) * \
            get_score(get_north_view(row_index, col_index, tree_data))
        best_scenic_score = max (scenic_score, best_scenic_score)

print(best_scenic_score) # 535680