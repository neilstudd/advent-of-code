import sys, os, collections
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

RANK_HIGH_CARD = 0
RANK_ONE_PAIR = 1
RANK_TWO_PAIR = 2
RANK_THREE_OF_A_KIND = 3
RANK_FULL_HOUSE = 4
RANK_FOUR_OF_A_KIND = 5
RANK_FIVE_OF_A_KIND = 6

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    hand_data = []

    CARD_TO_ALPHA = {
            '2': 'a', '3': 'b', '4': 'c', '5': 'd', '6': 'e',
            '7': 'f', '8': 'g', '9': 'h', 'T': 'i', 'J': 'j',
            'Q': 'k', 'K': 'l', 'A': 'm'
        }

    for line in data_file:
        this_hand = line.strip().split(" ")[0]
        converted_hand = ''.join(CARD_TO_ALPHA.get(card, card) for card in this_hand)
        bid = int(line.strip().split(" ")[1])
        hand_data.append({"hand": this_hand, "converted_hand": converted_hand, "strength": calculate_hand_strength(this_hand), "bid": bid})

    hand_data.sort(key=lambda x: (x["strength"], x["converted_hand"]), reverse=False)
    hand_rank = rank_hands(hand_data)
    print_and_verify_answer(mode, "one", hand_rank, expected)

def run_part_two(mode, expected = None):

    data_file = open_file( mode + ".txt")
    hand_data = []

    CARD_TO_ALPHA = {
        'J': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', 'T': 'j',
        'Q': 'k', 'K': 'l', 'A': 'm'
    }

    for line in data_file:
        this_hand = line.strip().split(" ")[0]
        converted_hand = ''.join(CARD_TO_ALPHA.get(card, card) for card in this_hand)
        bid = int(line.strip().split(" ")[1])
        hand_data.append({"hand": this_hand, "converted_hand": converted_hand, "strength": calculate_hand_strength_pt2(this_hand), "bid": bid})

    hand_data.sort(key=lambda x: (x["strength"], x["converted_hand"]), reverse=False)
    hand_rank = rank_hands(hand_data)
    print_and_verify_answer(mode, "two", hand_rank, expected)

def calculate_hand_strength_pt2(hand):
    count_of_most_common_card = collections.Counter(hand).most_common(1)[0][1]
    count_of_jokers = hand.count("J")

    if len(set(hand)) == 1:
        return RANK_FIVE_OF_A_KIND
    elif len(set(hand)) == 2:
        if count_of_jokers > 0:
            return RANK_FIVE_OF_A_KIND # the jokers convert to the other card
        else:
            return RANK_FOUR_OF_A_KIND if count_of_most_common_card == 4 else RANK_FULL_HOUSE
    elif len(set(hand)) == 3:
        if count_of_jokers == 1:
            return RANK_FOUR_OF_A_KIND if count_of_most_common_card == 3 else RANK_FULL_HOUSE
        elif count_of_jokers >= 2:
            return RANK_FOUR_OF_A_KIND # it must be 2J + 2 + 1, or 3J + 1 + 1
        else:
            return RANK_THREE_OF_A_KIND if count_of_most_common_card == 3 else RANK_TWO_PAIR
    elif len(set(hand)) == 4:
        return RANK_THREE_OF_A_KIND if count_of_jokers > 0 else RANK_ONE_PAIR
    elif count_of_jokers > 0:
        return RANK_ONE_PAIR
    else:
        return RANK_HIGH_CARD

def calculate_hand_strength(hand):
    count_of_most_common_card = collections.Counter(hand).most_common(1)[0][1]
    if len(set(hand)) == 1:
        return RANK_FIVE_OF_A_KIND
    elif len(set(hand)) == 2:
        return RANK_FOUR_OF_A_KIND if count_of_most_common_card == 4 else RANK_FULL_HOUSE
    elif len(set(hand)) == 3:
        return RANK_THREE_OF_A_KIND if count_of_most_common_card == 3 else RANK_TWO_PAIR
    elif len(set(hand)) == 4:
        return RANK_ONE_PAIR
    else:
        return RANK_HIGH_CARD
    
def rank_hands(hand_data):
    rank_total = 0
    current_rank = 1
    for hand in hand_data:
        rank_total += hand["bid"] * current_rank
        current_rank += 1
    return rank_total

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 6440)
run_part_one("prod", 250370104)
run_part_two("test", 5905)
run_part_two("prod", 251735672)
# Now run it and watch the magic happen 🪄