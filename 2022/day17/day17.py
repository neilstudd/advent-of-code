import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

# TODO: WORK IN PROGRESS
# This still doesn't work, but I've put in too much effort to give up forever.
# It takes approximately 11 minutes to come to the wrong answer, but it's 100% accurate
# on the test data set.
# The issue is likely caused by trying to keep the processing time down by randomly
# trimming the play grid when it exceeds 200 rows, and trying to track the "rows banked"
# along the way.

FLOOR_ROW = ["+","-", "-", "-", "-", "-", "-", "-", "+"]
NEW_ROW = ["|", ".", ".", ".", ".", ".", ".", ".", "|"]
ROCK_HORIZ = [["@", "@", "@", "@"]]
ROCK_PLUS = [[".", "@", "."],["@", "@", "@"],[".", "@", "."]]
ROCK_L = [["@", "@", "@"],[".", ".", "@"],[".", ".", "@"]]
ROCK_VERT = [["@"], ["@"], ["@"], ["@"]]
ROCK_SQUARE = [["@", "@"], ["@", "@"]]
ROCK_QUEUE = [ROCK_HORIZ, ROCK_PLUS, ROCK_L, ROCK_VERT, ROCK_SQUARE]

def print_grid():
    for row in reversed(chamber):
        print("".join(row))

def find_highest_block():
    row_idx = 1
    for index, row in enumerate(chamber):
        if "#" in row:
            row_idx = index
    return row_idx

def find_tetris_row():
    highest_row = -1
    for y, row in enumerate(chamber):
        if y > 0: # don't destroy the bottom
            if "#" in row and "." not in row:
                highest_row = y
    return highest_row

def add_shape_to_grid(shape):
    global is_first_shape
    row_idx = 1
    col_idx = 3
    # Find the latest row of chamber which contains a #
    for index, row in enumerate(chamber):
        if "#" in row:
            row_idx = index
    if is_first_shape:
        row_idx += 3
        is_first_shape = False
    else:
        row_idx += 4
    
    for row in shape:
        for index, char in enumerate(row):
            chamber[row_idx][col_idx + index] = char
        row_idx += 1

def can_move_right():
    for y, row in enumerate(chamber):
        for x, char in enumerate(row):
            if char == "@":
                if chamber[y][x+1] in ["#", "|"]:
                    return False
    return True

def can_move_left():
    for y, row in enumerate(chamber):
        for x, char in enumerate(row):
            if char == "@":
                if chamber[y][x-1] in ["#", "|"]:
                    return False
    return True

def can_move_down():
    for y, row in enumerate(chamber):
        for x, char in enumerate(row):
            if char == "@":
                if chamber[y-1][x] in ["#", "-"]:
                    return False
    return True

def move_right():
    if can_move_right():
        for y, row in enumerate(chamber):
            if y > 0: # don't destroy the bottom
                temp_row = ["|", "v", "v", "v", "v", "v", "v", "v", "|"]
                for x, char in enumerate(row):
                    if chamber[y][x] == "@":
                        temp_row[x+1] = "@"
                    elif chamber[y][x] == "#":
                        temp_row[x] = "#"
                chamber[y] = temp_row
            for y, row in enumerate(chamber):
                for x, char in enumerate(row):
                    if char == "v":
                        chamber[y][x] = "."

def move_left():
    if can_move_left():
        for y, row in enumerate(chamber):
            if y > 0: # don't destroy the bottom
                temp_row = ["|", "v", "v", "v", "v", "v", "v", "v", "|"]
                for x, char in enumerate(row):
                    if chamber[y][x] == "@":
                        temp_row[x-1] = "@"
                    elif chamber[y][x] == "#":
                        temp_row[x] = "#"
                chamber[y] = temp_row
            for y, row in enumerate(chamber):
                for x, char in enumerate(row):
                    if char == "v":
                        chamber[y][x] = "."

def move_down():
    if can_move_down():
        for y, row in enumerate(chamber):
            for x, char in enumerate(row):
                if char == "@":
                    chamber[y][x] = "."
                    chamber[y-1][x] = "@"
        return True
    else:
        # Lock the shape in place
        for y, row in enumerate(chamber):
            for x, char in enumerate(row):
                if char == "@":
                    chamber[y][x] = "#"
        return False

def get_next_shape():
    global current_shape
    if current_shape is None:
        current_shape = ROCK_QUEUE.pop(0)
    else:
        current_shape = ROCK_QUEUE.pop(0)
        ROCK_QUEUE.append(current_shape)
    return current_shape

def get_next_char():
    global current_char
    if current_char is None:
        current_char = CHAR_QUEUE.pop(0)
    else:
        current_char = CHAR_QUEUE.pop(0)
        CHAR_QUEUE.append(current_char)
    return current_char

# --------------- Good stuff starts here ------------------
# Initialise chamber
chamber = []
chamber.append(FLOOR_ROW.copy())
for i in range(220): chamber.append(NEW_ROW.copy())
current_shape = None
current_char = None
rows_banked = 0

for line in open_file("input.txt"):
    CHAR_QUEUE = list(line.strip())

# Add first shape to grid
is_first_shape = True
add_shape_to_grid(get_next_shape())
rocks_which_have_stopped_falling = 0
start_time = time.time()

while True:
    if rocks_which_have_stopped_falling == 2022:
        break

    # Freak out if no piece is on the board
    if not any("@" in row for row in chamber):
        print("ERROR: No piece on the board.")
        break

    char = get_next_char()
    move_right() if char == ">" else move_left()

    # Find the highest completed row, and scoop out everything below that
    highest_block = find_highest_block()
    highest_tetris = find_tetris_row()
    if highest_tetris > 0 and highest_tetris < highest_block-10:
            print(f"... Found a tetris at row {highest_tetris}! Highest block at {highest_block}. Banked {highest_tetris-1} rows")
            chamber.pop(0) # remove the floor
            rows_banked += highest_tetris-1
            for i in range(highest_tetris): chamber.pop(0)
            chamber.insert(0, FLOOR_ROW.copy())
            for i in range(highest_tetris): chamber.append(NEW_ROW.copy())
    elif highest_block > 210:
        chamber.pop(0) # remove the floor
        rows_banked += 10
        for i in range(10): chamber.pop(0)
        chamber.insert(0, FLOOR_ROW.copy())
        for i in range(10): chamber.append(NEW_ROW.copy())
    
    if not move_down():
        rocks_which_have_stopped_falling += 1
        elapsed_time = time.time() - start_time
        if rocks_which_have_stopped_falling % 50 == 0: print(f"Piece {rocks_which_have_stopped_falling} dropped after {elapsed_time:.2f} seconds. Grid height: {find_highest_block()}. Rows banked: {rows_banked}.")
        add_shape_to_grid(get_next_shape())
        
# Find the latest row of chamber which contains a #
highest_row = 0
for index, row in enumerate(chamber):
    if "#" in row: highest_row = index
answer = highest_row + rows_banked
print("Answer is {}".format(answer)) # 3121 is too low. Other wrong answers: 3132, 3152