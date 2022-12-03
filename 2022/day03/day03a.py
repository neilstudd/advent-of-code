import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")
total_priorities = 0
commonItems = []

# Build alphabet dictionary (a-z = 1-26, A-Z = 27-52)
alphabet = {}
for i in range(1, 27):
    alphabet[chr(96+i)] = i
    alphabet[chr(64+i)] = i+26

for line in file_content:
    thisRucksack = line.strip()
    compartment1, compartment2 = thisRucksack[:len(line)//2], thisRucksack[len(line)//2:]
    for item in compartment1:
        if item in compartment2:
            commonItems.append(item)
            break

for item in commonItems:
    total_priorities += alphabet[item]

print(total_priorities) # 8085