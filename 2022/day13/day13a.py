import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file
from ast import literal_eval # Thanks, StackOverflow

def evaluate_data(left, right):
    for i in range(len(left)):
        if i > len(right)-1:
            return False # Right list ran out of items first
        if isinstance(left[i], list) and not isinstance(right[i], list):
            right[i] = [right[i]] # convert right[i] to a list
        elif not isinstance(left[i], list) and isinstance(right[i], list):
            left[i] = [left[i]] # convert left[i] to a list
        if isinstance(left[i], list) and isinstance(right[i], list):
            outcome = evaluate_data(left[i], right[i])
            if not outcome:
                return False
        if left[i] < right[i]:
            return True # Left number is smaller; pass
        elif left[i] > right[i]:
            return False # Left number is larger; fail
    return True

raw_data = []
for line in open_file("input.txt"):
    if line.strip() != "":
        raw_data.append(line.strip())

pair_number = 1
sum_of_true_pairs = 0
for i in range(0, len(raw_data)-1, 2):
    left = raw_data[i]
    right = raw_data[i+1]
    outcome = evaluate_data(literal_eval(left), literal_eval(right))
    sum_of_true_pairs += pair_number if outcome else 0
    pair_number += 1

print(f"Part one: {sum_of_true_pairs}") # 5806