import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import *

file_content = open_file("input.txt")

elfArray = []
thisElf = 0

for line in file_content:
    if line.strip() != "":
        thisElf += int(line.strip())
    else:
        elfArray.append(thisElf)
        thisElf = 0

# Reverse list
elfArray.sort(reverse=True)
print(sum(elfArray[0:3])) #213089