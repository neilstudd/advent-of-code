import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def extract_ranges_from_file(mode):
    string = open_file( mode + ".txt")[0]
    ranges = string.split(',')
    extracted_values = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        extracted_values.extend(range(start, end + 1))
    return extracted_values

# AI ASSIST
# Given a number, split it into all possible sequences of equal-length parts
def split_id_into_sequences(id):
    value_to_str = str(id)
    str_length = len(value_to_str)
    results = []
    for k in range(1, (str_length // 2) + 1):
        if str_length % k == 0:
            parts = []            
            for i in range(0, str_length, k):
                chunk = int(value_to_str[i : i + k])
                parts.append(chunk)
            results.append(parts)            
    return results

def run_part_one(mode, expected = None):
    answer = 0
    extracted_values = extract_ranges_from_file(mode)
    for value in extracted_values:
        value_to_str = str(value)
        if len(value_to_str) % 2 == 0:
            half = len(value_to_str) // 2
            first_half = value_to_str[:half]
            second_half = value_to_str[half:]
            if first_half == second_half:
                answer += value
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):
    answer = 0
    extracted_values = extract_ranges_from_file(mode)
    for value in extracted_values:
        sequences = split_id_into_sequences(value)
        for sequence in sequences:
            if all(part == sequence[0] for part in sequence):
                answer += value
                break
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 1227775554)
run_part_one("prod", 28844599675)
run_part_two("test", 4174379265)
run_part_two("prod", 48778605167)
# Now run it and watch the magic happen 🪄