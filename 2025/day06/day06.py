import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def get_sums(input):
    integers_horizontal = []
    for line in input:
        line = line.strip()
        if not line[0].isdigit():
            operations = [x for x in line.split()]
            break
        this_line = []
        this_line.append([int(x) for x in line.split()])
        integers_horizontal.extend(this_line)
    integers_vertical = []
    for col in range(len(integers_horizontal[0])):
        this_col = []
        for row in range(len(integers_horizontal)):
            this_col.append(integers_horizontal[row][col])
        integers_vertical.append(this_col)  
    return integers_vertical, operations

# AI ASSIST
# Work vertically from right to left to build number grid, like a backwards blackboard
def calculate_cephlapod_numbers(input):
    operations = [x for x in input[-1].split()]
    input = input[:-1] # exclude from the operations processing
    max_width = max(len(line) for line in input)
    grid = [line.ljust(max_width) for line in input]    
    results = []
    current_group = []
    for col_idx in range(max_width - 1, -1, -1):
        col_chars = [row[col_idx] for row in grid]
        num_str = "".join(col_chars).strip()        
        if num_str:
            current_group.append(int(num_str))
        elif current_group:
            results.append(current_group)
            current_group = []
    if current_group:
        results.append(current_group)        
    return results, operations

def do_calculations(calculations, operations, flip_operation = False):
    total = 0
    for calculation_idx, calculation in enumerate(calculations):      
        if flip_operation: # pt2 reads operations from right to left
            operation = operations[len(operations) - 1 - calculation_idx]
        else:
            operation = operations[calculation_idx]
        total += eval('*'.join(map(str, calculation))) if operation == "*" else sum(calculation)
    return total

def run_part_one(mode, expected = None):
    input = open_file( mode + ".txt")
    calculations, operations = get_sums(input)
    total = do_calculations(calculations, operations)
    print_and_verify_answer(mode, "one", total, expected)

def run_part_two(mode, expected = None):
    input = open_file( mode + ".txt")
    calculations, operations = calculate_cephlapod_numbers(input)
    total = do_calculations(calculations, operations, True)
    print_and_verify_answer(mode, "two", total, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 4277556)
run_part_one("prod", 6172481852142)
run_part_two("test", 3263827)
run_part_two("prod", 10188206723429)
# Now run it and watch the magic happen 🪄