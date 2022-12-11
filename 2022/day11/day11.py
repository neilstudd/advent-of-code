import sys, os, operator
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

class Monkey:
    def __init__(self, position, items, operator, operation_value, test_divisor, true_monkey, false_monkey):
        self.position = position
        self.items = items
        self.operator = operator
        self.operation_value = operation_value
        self.test_divisor = test_divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.total_items_inspected = 0

    def process_worry(self, anxiety):
        for index, worry_level in enumerate(self.items):
            self.total_items_inspected += 1
            self.items[index] = self.operator(worry_level, self.operation_value) // 3 if anxiety else self.operator(worry_level, self.operation_value) % modulo

    def throw_items(self):
        item_targets = []
        for item in self.items:
            if item % self.test_divisor == 0:
                item_targets.append([item, self.true_monkey])
            else:
                item_targets.append([item, self.false_monkey])
        self.items = []
        return item_targets

    def __str__(self):
        return f"Monkey {self.position} has inspected {self.total_items_inspected} items."

def get_monkeys(mode):
    monkeys = []
    if mode == TEST_MONKEYS:
        monkeys.append(Monkey(0, [79, 98], operator.mul, 19, 23, 2, 3))
        monkeys.append(Monkey(1, [54, 65, 75, 74], operator.add, 6, 19, 2, 0))
        monkeys.append(Monkey(2, [79, 60, 97], operator.pow, 2, 13, 1, 3))
        monkeys.append(Monkey(3, [74], operator.add, 3, 17, 0, 1))
    else:
        # Couldn't be bothered to additionally parse the file
        monkeys.append(Monkey(0, [73, 77], operator.mul, 5, 11, 6, 5))
        monkeys.append(Monkey(1, [57, 88, 80], operator.add, 5, 19, 6, 0))
        monkeys.append(Monkey(2, [61, 81, 84, 69, 77, 88], operator.mul, 19, 5, 3, 1))
        monkeys.append(Monkey(3, [78, 89, 71, 60, 81, 84, 87, 75], operator.add, 7, 3, 1, 0))
        monkeys.append(Monkey(4, [60, 76, 90, 63, 86, 87, 89], operator.add, 2, 13, 2, 7))
        monkeys.append(Monkey(5, [88], operator.add, 1, 17, 4, 7))
        monkeys.append(Monkey(6, [84, 98, 78, 85], operator.pow, 2, 7, 5, 4))
        monkeys.append(Monkey(7, [98, 89, 78, 73, 71], operator.add, 4, 2, 3, 2))
    return monkeys

def calculate_monkey_business():
    monkeys.sort(key=operator.attrgetter('total_items_inspected'), reverse=True)
    return (monkeys[0].total_items_inspected * monkeys[1].total_items_inspected)

# HINT_RECEIVED: The internet helped me to discover that this was a modulo problem
def calculate_modulo():
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.test_divisor
    return modulo

TEST_MONKEYS = "Test"
PROD_MONKEYS = "Production"
LOW_ANXIETY = True
HIGH_ANXIETY = False

# Part 1
monkeys = get_monkeys(PROD_MONKEYS)
modulo = calculate_modulo()
NUM_ROUNDS = 20
for round in range(1,NUM_ROUNDS+1):
    for monkey in monkeys:
        monkey.process_worry(LOW_ANXIETY)
        for item in monkey.throw_items():
            monkeys[item[1]].items.append(item[0])
print(f"Part 1: {calculate_monkey_business()}") # 56120

# Part 2
monkeys = get_monkeys(PROD_MONKEYS)
modulo = calculate_modulo()
NUM_ROUNDS = 10000
for round in range(1,NUM_ROUNDS+1):
    for monkey in monkeys:
        monkey.process_worry(HIGH_ANXIETY)
        for item in monkey.throw_items():
            monkeys[item[1]].items.append(item[0])
print(f"Part 2: {calculate_monkey_business()}")  # 24389045529