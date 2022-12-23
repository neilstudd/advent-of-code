import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def has_board_won(board):
    for row in board:
        if all(column["called"] == True for column in row): return True
    for column_number in range(len(board[0])):
        if all(row[column_number]["called"] == True for row in board): return True
    return False

def get_winning_board():
    for game_board in game_boards:
        if has_board_won(game_board): return game_board
    return []

def count_winning_boards():
    winning_boards = 0
    for game_board in game_boards:
        if has_board_won(game_board): winning_boards += 1
    return winning_boards

numbers_to_call = []
game_boards = []
making_board = False

for line in open_file("input.txt"): 
    if numbers_to_call == []: numbers_to_call = line.strip().split(",")
    elif line.strip() == "":
        if making_board == False:
            making_board = True
            this_board = []
        else:
            game_boards.append(this_board)
            this_board = []
    else:
        this_row = []
        for number in line.strip().split():
            this_row.append({"number": number, "called": False})
        this_board.append(this_row)
game_boards.append(this_board)

for number in numbers_to_call:
    for game_board in game_boards:
        for row in game_board:
            for column in row:
                if column["number"] == number:
                    column["called"] = True
    winning_board = get_winning_board()
    if len(winning_board) > 0:
        break

# A game has won!
# Sum all numbers on winning board which have not been called
uncalled_numbers = sum(int(column["number"]) for row in winning_board for column in row if column["called"] == False)
print(f"Part 1: {uncalled_numbers * int(number)}") # 22680

# Reset all game boards to called=False
for game_board in game_boards:
    for row in game_board:
        for column in row:
            column["called"] = False

# This time, play til all boards have won
winning_boards = []
for number in numbers_to_call:
    for game_board in game_boards:
        for row in game_board:
            for column in row:
                if column["number"] == number:
                    column["called"] = True
        if game_board not in winning_boards and has_board_won(game_board):
            winning_boards.append(game_board)

    if count_winning_boards() == len(game_boards):
        break

# Get the last board which won
winning_board = winning_boards[-1]
uncalled_numbers = sum(int(column["number"]) for row in winning_board for column in row if column["called"] == False)
print(f"Part 2: {uncalled_numbers * int(number)}") # 16168