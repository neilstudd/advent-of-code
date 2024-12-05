import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def process_file(data_file):
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

def pages_which_must_come_after(page, page_ordering_rules):
    pages = []
    for rule in page_ordering_rules:
        if rule[0] == page:
            pages.append(rule[1])
    return pages

def pages_which_must_come_before(page, page_ordering_rules):
    pages = []
    for rule in page_ordering_rules:
        if rule[1] == page:
            pages.append(rule[0])
    return pages

def get_all_pages_after_index(page_index, updates):
    if page_index == len(updates) - 1:
        return []
    return updates[page_index+1:]

def get_all_pages_before_index(page_index, update):
    if page_index == 0:
        return []
    return update[:page_index]

def sort_updates_by_page_ordering_rules(updates, page_ordering_rules):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        update_valid = True
        for page_index, page in enumerate(update):
            pages_which_come_before = get_all_pages_before_index(page_index, update)
            for prev_page in pages_which_come_before:
                if prev_page in pages_which_must_come_after(page, page_ordering_rules):
                    update_valid = False      
        if update_valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates
            
def are_there_any_invalid_updates_left(updates, page_ordering_rules):
    new_valid_updates, new_invalid_updates = sort_updates_by_page_ordering_rules(updates, page_ordering_rules)
    return len(new_invalid_updates) > 0

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    page_ordering_rules, updates = process_file(data_file)
    valid_updates, invalid_updates = sort_updates_by_page_ordering_rules(updates, page_ordering_rules)
    sum_of_middle_numbers = 0
    for valid_update in valid_updates:
        middle_index = len(valid_update) // 2
        sum_of_middle_numbers += int(valid_update[middle_index])
    print_and_verify_answer(mode, "one", sum_of_middle_numbers, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    page_ordering_rules, updates = process_file(data_file)
    valid_updates, invalid_updates = sort_updates_by_page_ordering_rules(updates, page_ordering_rules)
    while are_there_any_invalid_updates_left(invalid_updates, page_ordering_rules):
        for invalid_update in invalid_updates:
            for page in invalid_update:
                # find the index furthest to the right that it must come after
                must_come_after_these = pages_which_must_come_before(page, page_ordering_rules)
                furthest_to_the_right = -1
                for must_come_after in must_come_after_these:
                    if must_come_after in invalid_update:
                        furthest_to_the_right = max(furthest_to_the_right, invalid_update.index(must_come_after))
                # move page to the right of furthest_to_the_right
                invalid_update.remove(page)
                invalid_update.insert(furthest_to_the_right + 1, page)
    sum_of_middle_numbers = 0
    for invalid_update in invalid_updates:
        middle_index = len(invalid_update) // 2
        sum_of_middle_numbers += int(invalid_update[middle_index])
    print_and_verify_answer(mode, "two", sum_of_middle_numbers, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 143)
run_part_one("prod", 6505)
run_part_two("test", 123)
run_part_two("prod", 6897)
# Now run it and watch the magic happen 🪄