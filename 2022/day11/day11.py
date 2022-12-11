import sys, os, operator
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

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

    def operation(self):
        for index, item in enumerate(self.items):
            self.total_items_inspected += 1
            new_value = self.operator(item, self.operation_value)
            new_value //= 3 if RELIEF_ENABLED else 1
            self.items[index] = new_value

    def test(self):
        throws = []
        for item in self.items:
            if item % self.test_divisor == 0:
                throws.append([item, self.true_monkey])
            else:
                throws.append([item, self.false_monkey])

        self.items = []
        return throws

    def __str__(self):
        return f"Monkey {self.position} has inspected {self.total_items_inspected} items."


monkeys = []

# Test monkeys
# monkeys.append(Monkey(0, [79, 98], operator.mul, 19, 23, 2, 3))
# monkeys.append(Monkey(1, [54, 65, 75, 74], operator.add, 6, 19, 2, 0))
# monkeys.append(Monkey(2, [79, 60, 97], operator.pow, 2, 13, 1, 3))
# monkeys.append(Monkey(3, [74], operator.add, 3, 17, 0, 1))

# # Real monkeys
monkeys.append(Monkey(0, [73, 77], operator.mul, 5, 11, 6, 5))
monkeys.append(Monkey(1, [57, 88, 80], operator.add, 5, 19, 6, 0))
monkeys.append(Monkey(2, [61, 81, 84, 69, 77, 88], operator.mul, 19, 5, 3, 1))
monkeys.append(Monkey(3, [78, 89, 71, 60, 81, 84, 87, 75], operator.add, 7, 3, 1, 0))
monkeys.append(Monkey(4, [60, 76, 90, 63, 86, 87, 89], operator.add, 2, 13, 2, 7))
monkeys.append(Monkey(5, [88], operator.add, 1, 17, 4, 7))
monkeys.append(Monkey(6, [84, 98, 78, 85], operator.pow, 2, 7, 5, 4))
monkeys.append(Monkey(7, [98, 89, 78, 73, 71], operator.add, 4, 2, 3, 2))

NUM_ROUNDS = 10000
RELIEF_ENABLED = False

for round in range(1,NUM_ROUNDS+1):
    print(f"Round {round}")
    for monkey in monkeys:
        monkey.operation()
        for item in monkey.test():
            monkeys[item[1]].items.append(item[0])

for monkey in monkeys:
        print(monkey)

# Part 1 (20 rounds, RELIEF_ENABLED=True): 244 * 230 = 56120
# Part 2: number explosion pain