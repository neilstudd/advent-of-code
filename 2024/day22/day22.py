import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def mix(secret_number, new_number):
    return new_number ^ secret_number

def prune(secret_number):
    return secret_number % 16777216

def evolve(secret_number):
    new_number = secret_number * 64
    secret_number = mix(secret_number, new_number)
    secret_number = prune(secret_number)
    new_number = secret_number // 32
    secret_number = mix(secret_number, new_number)
    secret_number = prune(secret_number)
    new_number = secret_number * 2048
    secret_number = mix(secret_number, new_number)
    secret_number = prune(secret_number)
    return secret_number

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    sum = 0
    for secret_number in data_file:
        secret_number = int(secret_number)
        for i in range(2000):
            secret_number = evolve(secret_number)
        sum += secret_number
    print_and_verify_answer(mode, "one", sum, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    answer = None # <-- Change this to answer
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 37327623)
run_part_one("prod", 13022553808    )
run_part_two("test", 0)
run_part_two("prod")
# Now run it and watch the magic happen 🪄