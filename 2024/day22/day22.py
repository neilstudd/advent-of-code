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

def sum_values_across_keys(secrets):
    summed_values = {} 
    for sub_dict in secrets.values():
        for key, value in sub_dict.items():
            if key in summed_values:
                summed_values[key] += value
            else:
                summed_values[key] = value
    return summed_values

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
    secrets = {}
    for secret_number in data_file:
        these_prices = []
        starting_number = int(secret_number)
        these_prices.append(starting_number % 10)
        for i in range(2000):
            secret_number = evolve(int(secret_number))
            these_prices.append(int(secret_number) % 10)
        these_differences = [these_prices[i + 1] - these_prices[i] for i in range(len(these_prices) - 1)]
        if starting_number not in secrets:
            secrets[starting_number] = {}
        for index, difference in enumerate(these_differences):
            diff_string = ",".join([str(difference)] + [str(d) for d in these_differences[index + 1: index + 4]])
            if diff_string not in secrets[starting_number] and index + 4 < len(these_prices):
                secrets[starting_number][diff_string] = these_prices[index + 4]      
    result = sum_values_across_keys(secrets)
    highest_value = max(result.values())
    print_and_verify_answer(mode, "two", highest_value, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 37327623)
run_part_one("prod", 13022553808)
run_part_two("test2", 23)
run_part_two("prod", 1555)
# Now run it and watch the magic happen 🪄