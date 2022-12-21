import sys, os, operator, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

def shout(monkey_name):
    for monkey in monkeys:
        if monkey["name"] == monkey_name:
            if "number" in monkey: return monkey["number"]
            else: return monkey["operator"](shout(monkey["a"]),shout(monkey["b"]))

def find_monkey(monkey_name):
    for monkey in monkeys:
        if monkey["name"] == monkey_name: return monkey

def change_my_shout(new_number):
    for monkey in monkeys:
        if monkey["name"] == "humn":
            monkey["number"] = new_number
            break

def binary_chop(low, high):
    mid = (low + high) // 2
    my_monkey["number"] = mid
    first_number = shout(root_monkey["a"])
    second_number = shout(root_monkey["b"])
    diff = first_number - second_number
    if diff < 0: return binary_chop(low, mid - 1)
    elif diff > 0: return binary_chop(mid + 1, high)
    else: return mid

monkeys = []

for line in open_file("input.txt"):
    monkey_name = line.strip().split(": ")[0]
    monkey_data = line.strip().split(": ")[1]
    if monkey_data.isnumeric():
        number = int(monkey_data)
        monkeys.append({"name": monkey_name, "number": number})
    else:
        a, operation, b = monkey_data.split(" ")
        monkeys.append({"name": monkey_name, "a": a, "operator": ops[operation], "b": b})

print(f"Part 1: Root shouts {int(shout('root'))}") # 56490240862410

# Hone in on the correct answer with a binary chop
my_monkey = find_monkey("humn")
root_monkey = find_monkey("root")
print(f"Part 2: Human should shout {binary_chop(1, 40000000000000)}")
# When I shout 3403989691757, both monkeys shout 17522552903925.