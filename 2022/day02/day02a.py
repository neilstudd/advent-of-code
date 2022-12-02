import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

YOUR_THROW = {"X": 1, "Y": 2, "Z": 3}
TRANSLATE_YOUR_THROW_TO_THEIRS = {"X": "A", "Y": "B", "Z": "C"}
score = 0

for line in file_content:
    thisRound = line.strip().split(" ")
    oppGuess = thisRound[0]
    yourGuess = thisRound[1]

    score += YOUR_THROW[yourGuess]
    score += 3 if oppGuess == TRANSLATE_YOUR_THROW_TO_THEIRS[yourGuess] else 0
    score += 6 if (oppGuess == "A" and yourGuess == "Y") or (oppGuess == "B" and yourGuess == "Z") or (oppGuess == "C" and yourGuess == "X") else 0  

print(score) # 10624