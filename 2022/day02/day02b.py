import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = "X"
DRAW = "Y"
WIN = "Z"

OUTCOMES = {LOSS: 0, DRAW: 3, WIN: 6}

STRATEGY_GUIDE = {
    "A": {LOSS: SCISSORS, DRAW: ROCK, WIN: PAPER},
    "B": {LOSS: ROCK, DRAW: PAPER, WIN: SCISSORS},
    "C": {LOSS: PAPER, DRAW: SCISSORS, WIN: ROCK}
}

score = 0

for line in file_content:
    thisRound = line.strip().split(" ")
    oppGuess = thisRound[0]
    yourGuess = thisRound[1]
    score += OUTCOMES[yourGuess] + STRATEGY_GUIDE[oppGuess][yourGuess]

print(score) # 14060