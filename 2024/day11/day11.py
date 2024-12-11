import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer
from collections import Counter

def count_stones_after_blinking(stones, number_of_blinks):
    stone_counts = Counter(stones)
    for _ in range(number_of_blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                new_stone_counts[int(str(stone)[:half])] += count
                new_stone_counts[int(str(stone)[half:])] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts
    return sum(stone_counts.values())

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    stones = list(map(int, data_file[0].split()))
    answer = count_stones_after_blinking(stones, 25)
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    stones = list(map(int, data_file[0].split()))
    answer = count_stones_after_blinking(stones, 75)
    print_and_verify_answer(mode, "two", answer, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 55312)
run_part_one("prod", 186424)
run_part_two("test", 65601038650482) # implied; puzzle doesn't provide it
run_part_two("prod", 219838428124832)
# Now run it and watch the magic happen 🪄