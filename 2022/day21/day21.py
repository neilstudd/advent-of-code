import sys, os, operator, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }

def shout(monkey_name):
    for monkey in monkeys:
        if monkey["name"] == monkey_name:
            if "number" in monkey:
                #print(f"Monkey {monkey_name} shouts {monkey['number']}")
                return monkey["number"]
            else:
                #print(f"...checking {monkey['a']} {monkey['operator']} {monkey['b']}")
                return monkey["operator"](shout(monkey["a"]),shout(monkey["b"]))

def find_monkey(monkey_name):
    for monkey in monkeys:
        if monkey["name"] == monkey_name:
            return monkey

def change_my_shout(new_number):
    for monkey in monkeys:
        if monkey["name"] == "humn":
            monkey["number"] = new_number
            break

monkeys = []

for line in open_file("input.txt"):
    monkey_name = line.strip().split(": ")[0]
    monkey_data = line.strip().split(": ")[1]
    # check if monkey_data can convert to integer
    if monkey_data.isnumeric():
        number = int(monkey_data)
        monkeys.append({"name": monkey_name, "number": number})
    else:
        # monkey_data is in format abcd + efgh
        # split it into three parts: abcd, +, efgh 
        a, operation, b = monkey_data.split(" ")
        monkeys.append({"name": monkey_name, "a": a, "operator": ops[operation], "b": b})

print(f"Part 1: Root shouts {shout('root')}.")

# Part 2: In a rush today, and this is hella slow (shouting about 100 numbers per minute)
# So I did a bit of binary chopping, modifying my_number one digit at a time until I got in the ballpark
my_number = 3403989691740
first_number = -1
my_monkey = find_monkey("humn")
root_monkey = find_monkey("root")
second_number = shout(root_monkey["b"]) # This doesn't change in my data; it might be an incorrect assumption with other data
while first_number != second_number:
    my_number += 1
    my_monkey["number"] = my_number
    first_number = shout(root_monkey["a"])
    if my_number % 10 == 0: print(f"...When I shout {my_number}, left={first_number}, right={second_number}. diff {first_number - second_number}.")
print(f"Part 2: When I shout {my_number}, left monkey shouts {first_number}, right monkey shouts {second_number}")
