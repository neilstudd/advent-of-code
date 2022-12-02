import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

ROCK = 1, 
PAPER = 2
SCISSORS = 3

OUTCOMES = {"X": 0, "Y": 3, "Z": 6}

STRATEGY_GUIDE = {
    "A": {"X": SCISSORS, "Y": ROCK, "Z": PAPER},
    "B": {"X": ROCK, "Y": PAPER, "Z": SCISSORS},
    "C": {"X": PAPER, "Y": SCISSORS, "Z": ROCK}
}

score = 0

for line in file_content:
    thisRound = line.strip().split(" ")
    oppGuess = thisRound[0]
    yourGuess = thisRound[1]
    score += OUTCOMES[yourGuess] + STRATEGY_GUIDE[oppGuess][yourGuess]

print(score) # 14060