import sys, os, operator, itertools
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def generate_equations(mode):
    data_file = open_file( mode + ".txt")
    equations = []
    for line in data_file:
        parts = line.strip().split(":")
        equation = [int(parts[0]), list(map(int, parts[1].split()))]
        equations.append(equation)
    return equations

def generate_expressions(nums, target_number, is_part_two = False):
    operators = {
        '+': operator.add,
        '*': operator.mul
    }    

    if is_part_two:
        operators['||'] = concatenate

    expressions = set()
    
    # Generate all possible operator combinations
    op_combinations = list(itertools.product(operators.keys(), repeat=len(nums)-1))
    
    for ops in op_combinations:
        result = nums[0]
        for i, op in enumerate(ops):
            result = operators[op](result, nums[i+1])
        expressions.add(result)
        if result == target_number:
            return target_number

    return 0

def concatenate(x, y):
    return int(str(x) + str(y))

def run_part_one(mode, expected = None):
    equations = generate_equations(mode)
    valid_equation_sums = 0
    for equation in equations:
        valid_equation_sums += generate_expressions(equation[1], equation[0])
    print_and_verify_answer(mode, "one", valid_equation_sums, expected)

def run_part_two(mode, expected = None):
    equations = generate_equations(mode)
    valid_equation_sums = 0
    for equation in equations:
        valid_equation_sums += generate_expressions(equation[1], equation[0], True)
    print_and_verify_answer(mode, "two", valid_equation_sums, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 3749)
run_part_one("prod", 20665830408335)
run_part_two("test", 11387)
run_part_two("prod", 354060705047464)
# Now run it and watch the magic happen 🪄