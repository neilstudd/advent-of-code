import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    total = 0
    for line in data_file:
        line_stripped = ''.join(filter(str.isdigit, line))
        value_to_add = line_stripped[0] + line_stripped[-1]
        total += int(value_to_add)
    print_and_verify_answer(mode, "one", total, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    total = 0
    for line in data_file:
        num_list = ["🙈","one","two","three","four","five","six","seven","eight","nine"]
        number_starting_characters = "soften"
        i = 0
        first_number = ""
        last_number = ""
        while i < len(line):
            if line[i].isnumeric():
                first_number = line[i] if first_number == "" else first_number
                last_number = line[i]
            if line[i] in number_starting_characters:
                for each in num_list:
                    if line[i:i+len(each)] == each:
                        first_number = str(num_list.index(each)) if first_number == "" else first_number
                        last_number = str(num_list.index(each))
                        break
            i += 1
        total += int(first_number + last_number)
    print_and_verify_answer(mode, "two", total, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 142)
run_part_one("prod", 54390)
run_part_two("test2", 281)
run_part_two("prod", 54277)
# Now run it and watch the magic happen 🪄