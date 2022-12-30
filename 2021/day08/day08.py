import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def count_common_chars(str1, str2):
  set1 = set(str1)
  set2 = set(str2)
  common_chars = set1 & set2
  return len(common_chars)

def calculate_output():
    answer_string = ""
    for digit in output:
        if digit == zero_digit: answer_string += "0"
        elif digit == one_digit: answer_string += "1"
        elif digit == two_digit: answer_string += "2"
        elif digit == three_digit: answer_string += "3"
        elif digit == four_digit: answer_string += "4"
        elif digit == five_digit: answer_string += "5"
        elif digit == six_digit: answer_string += "6"
        elif digit == seven_digit: answer_string += "7"
        elif digit == eight_digit: answer_string += "8"
        elif digit == nine_digit: answer_string += "9"
    return int(answer_string)

part1_answer = 0
part2_answer = 0
for line in open_file("input.txt"): 
    digits = line.split("| ")[0].strip().split(" ")
    output = line.split("| ")[1].strip().split(" ")
    for i, digit in enumerate(digits): digits[i] = ''.join(sorted(digit))
    for i, digit in enumerate(output): output[i] = ''.join(sorted(digit))
    
    # Find 1, 4, 7 and 8 (they each have unique number of segments)
    for digit in digits:
        segments = len(digit)
        if segments == 2: one_digit = digit
        elif segments == 4: four_digit = digit
        elif segments == 3: seven_digit = digit
        elif segments == 7: eight_digit = digit

    # Six is the only six-segment digit which doesn't have all segments of 1
    for digit in digits:
        segments = len(digit)
        if segments == 6:
            for one_segment in one_digit:
                if one_segment not in digit: six_digit = digit

    # Zero is the only remaining six-segment digit which doesn't have all segments of 4
    for digit in digits:
        if digit != six_digit:
            segments = len(digit)
            if segments == 6:
                for four_segment in four_digit:
                    if four_segment not in digit: zero_digit = digit
                         
    # Nine is the only other remaining six-segment digit
    for digit in digits:
        if digit != six_digit and digit != zero_digit:
            segments = len(digit)
            if segments == 6:
                nine_digit = digit
    
    # Three is the only five-segment digit which contains both segments of 1
    for digit in digits:
        segments = len(digit)
        if segments == 5:
            if all(c in digit for c in one_digit): three_digit = digit
    
    # Five is the only remaining five-segment digit which has five segments in common with a 6
    for digit in digits:
        if digit != three_digit:
            segments = len(digit)
            if segments == 5:
                if count_common_chars(digit, six_digit) == 5: five_digit = digit

    # Two is the only other remaining five-segment digit
    for digit in digits:
        if digit != three_digit and digit != five_digit:
            segments = len(digit)
            if segments == 5:
                two_digit = digit

    # Count how many times 1, 4, 7 and 8 are in output
    for digit in output:
        if digit == one_digit: part1_answer += 1
        elif digit == four_digit: part1_answer += 1
        elif digit == seven_digit: part1_answer += 1
        elif digit == eight_digit: part1_answer += 1

    # Calculate the values for part 2
    part2_answer += calculate_output()

print(f"Part 1: {part1_answer}") # 440
print(f"Part 2: {part2_answer}") # 1046281