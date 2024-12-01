import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def construct_and_sort_lists(data_file):
    list_one = []
    list_two = []
    for line in data_file:
        numbers = line.split()
        list_one.append(int(numbers[0]))
        list_two.append(int(numbers[1]))
    return list_one, list_two

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    list_one, list_two = construct_and_sort_lists(data_file)
    total_difference = 0
    list_one.sort()
    list_two.sort()
    for i in range(len(list_one)):
        total_difference += abs(list_one[i] - list_two[i])
    print_and_verify_answer(mode, "one", total_difference, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    list_one, list_two = construct_and_sort_lists(data_file)
    running_total = 0
    for i in range(len(list_one)):
        running_total += list_two.count(list_one[i]) * list_one[i]
    print_and_verify_answer(mode, "two", running_total, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 11)
run_part_one("prod", 2066446)
run_part_two("test", 31)
run_part_two("prod", 24931009)
# Now run it and watch the magic happen 🪄