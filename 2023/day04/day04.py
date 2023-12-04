import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    points = 0
    for card in data_file:
        parts = card.split(':')
        winning_numbers, your_numbers = calculate_numbers(parts[1])
        this_card_points = 0
        for num in winning_numbers:
            if num in your_numbers:
                if this_card_points == 0:
                    this_card_points = 1
                else:
                    this_card_points *= 2
        points += this_card_points
    print_and_verify_answer(mode, "one", points, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    card_list = []
    card_stats = []
    
    for line in data_file:
        card_list.append(line.strip())
    
    for card in card_list:
        parts = card.split(':')
        card_number = int(parts[0].split()[-1])
        winning_numbers, your_numbers = calculate_numbers(parts[1])
        matching_numbers = 0
        for num in winning_numbers:
            if num in your_numbers:
                matching_numbers += 1
        card_stats.append({"number": card_number, "matches": matching_numbers, "count": 1})

    for card in card_stats:
        for _ in range(card["count"]):
            for i in range(card["matches"]):
                card_stats[card["number"]+i]["count"] += 1

    total = sum(card["count"] for card in card_stats)
    print_and_verify_answer(mode, "two", total, expected)

def calculate_numbers(data):
    numbers = data.strip().split('|')
    winning_numbers = [int(num) for num in numbers[0].split()]
    your_numbers = [int(num) for num in numbers[1].split()]
    return winning_numbers, your_numbers

def is_copy(card):
    return card.startswith("Copy")

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 13)
run_part_one("prod", 20829)
run_part_two("test", 30)
run_part_two("prod", 12648035)
# Now run it and watch the magic happen 🪄