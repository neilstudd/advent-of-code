import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def string_to_range(elf):
    low, high = elf.split("-")
    return list(range(int(low),int(high)+1))

def all_within(elf1,elf2):
    return all(floor in elf2 for floor in elf1) or all(floor in elf1 for floor in elf2)

def any_within(elf1,elf2):
    return any(num in elf2 for num in elf1)

file_content = open_file("input.txt")
part1_count = 0
part2_count = 0

for line in file_content:
    elf1, elf2 = line.strip().split(",")
    elf1_range = string_to_range(elf1)
    elf2_range = string_to_range(elf2)
    part1_count +=1 if all_within(elf1_range, elf2_range) else 0
    part2_count +=1 if any_within(elf1_range, elf2_range) else 0

print(part1_count) # 582
print(part2_count)  # 893