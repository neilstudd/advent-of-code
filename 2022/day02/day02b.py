import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

ROCK = 1
PAPER = 2
SCISSORS = 3
WIN = "X"
DRAW = "Y"
LOSS = "Z"

OUTCOMES = {WIN: 0, DRAW: 3, LOSS: 6}

STRATEGY_GUIDE = {
    "A": {WIN: SCISSORS, DRAW: ROCK, LOSS: PAPER},
    "B": {WIN: ROCK, DRAW: PAPER, LOSS: SCISSORS},
    "C": {WIN: PAPER, DRAW: SCISSORS, LOSS: ROCK}
}

score = 0

for line in file_content:
    thisRound = line.strip().split(" ")
    oppGuess = thisRound[0]
    yourGuess = thisRound[1]
    score += OUTCOMES[yourGuess] + STRATEGY_GUIDE[oppGuess][yourGuess]

print(score) # 14060