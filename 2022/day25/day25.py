import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def convert_from_snafu_to_decimal(number):
    running_total = 0
    for index, digit in enumerate(reversed(number)):
        if digit == "=": digit = -2
        elif digit == "-": digit = -1
        else: digit = int(digit)
        multiplier = 1 if index == 0 else 5 ** index
        running_total += (digit * multiplier)
    return running_total

def convert_from_decimal_to_snafu(number):
    conversion = []
    while number > 0:
        conversion.append("012=-"[number % 5])
        number = (number + 2) // 5
    return "".join(reversed(conversion))

sum = 0
for line in open_file("input.txt"): sum += convert_from_snafu_to_decimal(line.strip())
print(f"Part 1: Convert {sum} to snafu = {convert_from_decimal_to_snafu(sum)}") # 29541007400367 converts to = 2=--=0000-1-0-=1=0=2