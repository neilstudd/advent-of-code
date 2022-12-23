import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

previousNumber = 0
timesIncreased = 0
depthArray = []
for line in open_file("input.txt"):
    thisNumber = int(line.strip())
    depthArray.append(thisNumber)
    if previousNumber != 0 and thisNumber > previousNumber: timesIncreased += 1
    previousNumber = thisNumber
print(f"Part 1: {timesIncreased}") # 1655

previousWindow = 0
sumsIncreased = 0
for i in range(0, len(depthArray)-2):
    sum_of_this_window = depthArray[i] + depthArray[i+1] + depthArray[i+2]
    if previousWindow != 0 and sum_of_this_window > previousWindow: sumsIncreased += 1
    previousWindow = sum_of_this_window
print(f"Part 2: {sumsIncreased}") # 1683