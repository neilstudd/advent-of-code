import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import *

file_content = open_file("input.txt")

biggestElf = 0
thisElf = 0

for line in file_content:
    if line.strip() != "":
        thisElf += int(line.strip())
    else:
        if thisElf > biggestElf:
            biggestElf = thisElf
        thisElf = 0

print(biggestElf)
# 72718