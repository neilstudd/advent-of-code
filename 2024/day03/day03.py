import sys, os, re
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def do_multiplication(text):
    matches = re.findall(r'mul\((\d+),(\d+)\)', text)
    number_pairs = [(int(x), int(y)) for x, y in matches]
    return sum([x * y for x, y in number_pairs])

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    answer = 0
    for line in data_file:
        answer += do_multiplication(line)
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    big_string = "".join(line.strip() for line in data_file)
    scrubbed = re.sub(r"don't\(\).*?(?=do\(\))", "", big_string)
    answer = do_multiplication(scrubbed)
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 161)
run_part_one("prod", 166630675)
run_part_two("test2", 48)
run_part_two("prod", 93465710)
# Now run it and watch the magic happen 🪄