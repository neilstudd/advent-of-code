import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

tree_on_edge = lambda: (row == 0 or row == len(tree_data)-1) or (col == 0 or col == len(tree_data[0])-1)
visible_from_north = lambda row, col: not any(int(tree_data[i][col]) >= this_tree_size for i in range(0, row))
visible_from_south = lambda row, col: not any(int(tree_data[i][col]) >= this_tree_size for i in range(row+1, len(tree_data)))
visible_from_west = lambda row, col: not any(int(tree_data[row][i]) >= this_tree_size for i in range(0, col))
visible_from_east = lambda row, col: not any(int(tree_data[row][i]) >= this_tree_size for i in range(col+1, len(tree_data[0])))
is_visible = lambda row, col: visible_from_north(row, col) or visible_from_south(row, col) or visible_from_west(row, col) or visible_from_east(row, col)
tree_data = [line.strip() for line in open_file("input.txt")]

counter = 0
for r, row in enumerate(tree_data):
    for c, col in enumerate(row):
        this_tree_size = int(col)
        counter += 1 if tree_on_edge() or is_visible(r, c) else 0

print(counter) # 1690