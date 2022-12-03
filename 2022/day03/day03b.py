import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def findCommonCharacter(a, b, c):
    for item in a:
        if item in b and item in c:
            return item

file_length = sum(1 for line in open_file("input.txt"))
file_content = open_file("input.txt")
total_priorities = 0

# Build alphabet dictionary (a-z = 1-26, A-Z = 27-52)
alphabet = {}
for i in range(1, 27):
    alphabet[chr(96+i)] = i
    alphabet[chr(64+i)] = i+26

for i in range(0, file_length, 3):
    rucksack1 = file_content[i].strip()
    rucksack2 = file_content[i+1].strip()
    rucksack3 = file_content[i+2].strip()
    total_priorities += alphabet[findCommonCharacter(rucksack1, rucksack2, rucksack3)]

print(total_priorities) # 2515