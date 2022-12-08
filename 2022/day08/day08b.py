import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file
  
def get_view(r, c, direction):
    if direction == "N":
        tree_column = [row[c] for row in tree_data][0:r+1]
        tree_column.reverse()
        return tree_column
    elif direction == "S":
        tree_column = [row[c] for row in tree_data]
        return tree_column[r:]
    elif direction == "W":
        tree_row = tree_data[r][:c+1]
        tree_row.reverse()
        return tree_row
    elif direction == "E":    
        return tree_data[r][c:]

def get_score(list):
    if len(list) == 1:
        return 1
    first_element = list.pop(0)
    for i, item in enumerate(list):
        if item >= first_element:
            break
    return i+1

tree_data = [list(line.strip()) for line in open_file("input.txt")]

best_scenic_score = 0
for row_index, row in enumerate(tree_data):
    for col_index, col in enumerate(row):
        scenic_score = get_score(get_view(row_index, col_index, "W")) * \
            get_score(get_view(row_index, col_index, "E")) * \
            get_score(get_view(row_index, col_index, "S")) * \
            get_score(get_view(row_index, col_index, "N"))
        best_scenic_score = max (scenic_score, best_scenic_score)

print(best_scenic_score) # 535680