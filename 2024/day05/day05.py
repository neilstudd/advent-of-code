import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

page_ordering_rules = []
updates = []

def process_file(data_file):
    global page_ordering_rules, updates
    page_ordering_rules = []
    updates = []
    for line in data_file:
        if "|" in line:
            this_rule = line.strip().split("|")
            page_ordering_rules.append(this_rule)
        elif "," in line:
            this_update = line.strip().split(",")
            updates.append(this_update)
    return page_ordering_rules, updates

def is_update_valid(update):
    global page_ordering_rules
    for page_index, page in enumerate(update):
        pages_which_come_before = get_all_updates_before_index(page_index, update)
        for prev_page in pages_which_come_before:
            if prev_page in pages_which_must_come_after(page):
                return False
    return True

def pages_which_must_come_after(page):
    global page_ordering_rules
    pages = []
    for rule in page_ordering_rules:
        if rule[0] == page:
            pages.append(rule[1])
    return pages

def pages_which_must_come_before(page):
    global page_ordering_rules
    pages = []
    for rule in page_ordering_rules:
        if rule[1] == page:
            pages.append(rule[0])
    return pages

def get_all_pages_after_index(page_index):
    global updates
    if page_index == len(updates) - 1:
        return []
    return updates[page_index+1:]

def get_all_updates_before_index(page_index, update):
    if page_index == 0:
        return []
    return update[:page_index]

def partition_updates_by_validity():
    global updates, page_ordering_rules
    valid_updates = [update for update in updates if is_update_valid(update)]
    invalid_updates = [update for update in updates if not is_update_valid(update)]
    return valid_updates, invalid_updates
            
def are_there_any_invalid_updates_left():
    global updates
    return any(not is_update_valid(update) for update in updates)

def sum_the_middles(updates):
    return sum(int(update[len(update) // 2]) for update in updates)

def run_part_one(mode, expected = None):
    global page_ordering_rules, updates
    data_file = open_file( mode + ".txt")
    page_ordering_rules, updates = process_file(data_file)
    valid_updates, _ = partition_updates_by_validity()
    sum_of_middle_numbers = sum_the_middles(valid_updates)
    print_and_verify_answer(mode, "one", sum_of_middle_numbers, expected)

def run_part_two(mode, expected = None):
    global page_ordering_rules, updates
    data_file = open_file( mode + ".txt")
    page_ordering_rules, updates = process_file(data_file)
    _, invalid_updates = partition_updates_by_validity()
    while are_there_any_invalid_updates_left():
        for invalid_update in invalid_updates:
            for page in invalid_update:
                must_come_after_these = pages_which_must_come_before(page)
                furthest_to_the_right = max((invalid_update.index(must_come_after) for must_come_after in must_come_after_these if must_come_after in invalid_update), default=-1)
                invalid_update.remove(page)
                invalid_update.insert(furthest_to_the_right + 1, page)
    sum_of_middle_numbers = sum_the_middles(invalid_updates)
    print_and_verify_answer(mode, "two", sum_of_middle_numbers, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 143)
run_part_one("prod", 6505)
run_part_two("test", 123)
run_part_two("prod", 6897)
# Now run it and watch the magic happen 🪄