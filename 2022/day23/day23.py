import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def print_grove():
    for row in grove:
        for cell in row:
            if cell["has_elf"]: print("#", end="")
            else: print(".", end="")
        print()

def extend_grove_if_needed():
    # Check if first row contains any elf
    for cell in grove[0]:
        if cell["has_elf"]: 
            grove.insert(0, [{ "has_elf": False } for _ in range(len(grove[0]))])
            break
    # Check if last row contains any elf
    for cell in grove[-1]:
        if cell["has_elf"]: 
            grove.append([{ "has_elf": False } for _ in range(len(grove[0]))])
            break
    # Check if first column contains any elf
    for row in grove:
        if row[0]["has_elf"]:
            for row in grove: row.insert(0, { "has_elf": False })
            break
    # Check if last column contains any elf
    for row in grove:
        if row[-1]["has_elf"]:
            for row in grove: row.append({ "has_elf": False })
            break

def shrink_grid_if_needed():
    if not any([cell["has_elf"] for cell in grove[0]]):
        grove.pop(0)
    if not any([cell["has_elf"] for cell in grove[-1]]):
        grove.pop(-1)
    if not any([row[0]["has_elf"] for row in grove]):
        for row in grove: row.pop(0)
    if not any([row[-1]["has_elf"] for row in grove]):
        for row in grove: row.pop(-1)

def check_destination_is_unique(elf_x, elf_y, destination):
    for check_row_index, check_row in enumerate(grove):
        for check_cell_index, check_cell in enumerate(check_row):
            if check_cell["has_elf"] and check_cell["moved_this_round"] == False and check_cell["proposed_target"] == destination:
                if elf_x == check_row_index and elf_y == check_cell_index:
                    continue
                return False
    return True

def any_elf_in_directions(elf_x, elf_y, directions):
    for direction in directions:
        if direction == "N":
            if elf_x > 0 and grove[elf_x - 1][elf_y]["has_elf"]:
                return True
        elif direction == "S":
            if elf_x < len(grove) - 1 and grove[elf_x + 1][elf_y]["has_elf"]:
                return True
        elif direction == "W":
            if elf_y > 0 and grove[elf_x][elf_y - 1]["has_elf"]:
                return True
        elif direction == "E":
            if elf_y < len(grove[elf_x]) - 1 and grove[elf_x][elf_y + 1]["has_elf"]:
                return True
        elif direction == "NW":
            if elf_x > 0 and elf_y > 0 and grove[elf_x - 1][elf_y - 1]["has_elf"]:
                return True
        elif direction == "NE":
            if elf_x > 0 and elf_y < len(grove[elf_x]) - 1 and grove[elf_x - 1][elf_y + 1]["has_elf"]:
                return True
        elif direction == "SW":
            if elf_x < len(grove) - 1 and elf_y > 0 and grove[elf_x + 1][elf_y - 1]["has_elf"]:
                return True
        elif direction == "SE":
            if elf_x < len(grove) - 1 and elf_y < len(grove[elf_x]) - 1 and grove[elf_x + 1][elf_y + 1]["has_elf"]:
                return True
    return False

def play_rounds(rounds, part_two=False):
    global round_count
    start_time = time.time()

    for round_number in range(rounds):
        round_count += 1
        has_any_elf_moved = False
        extend_grove_if_needed()

        # First half of round: iterate over every cell which has an elf
        for row_index, row in enumerate(grove):
            for cell_index, cell in enumerate(row):
                if cell["has_elf"]:
                    # If no elves in any direction, they don't move
                    if not any_elf_in_directions(row_index, cell_index, ["NW","N","NE","W","E","SW","S","SE"]):
                        continue
                    else:
                        for direction in considered_directions:
                            if direction == "N":
                                if not any_elf_in_directions(row_index, cell_index, ["NW","N","NE"]):
                                    cell["proposed_target"] = {"row": row_index - 1, "col": cell_index}
                                    break
                            elif direction == "S":
                                if not any_elf_in_directions(row_index, cell_index, ["SW","S","SE"]):
                                    cell["proposed_target"] = {"row": row_index + 1, "col": cell_index}
                                    break
                            elif direction == "W":
                                if not any_elf_in_directions(row_index, cell_index, ["NW","W","SW"]):
                                    cell["proposed_target"] = {"row": row_index, "col": cell_index - 1}
                                    break
                            elif direction == "E":
                                if not any_elf_in_directions(row_index, cell_index, ["NE","E","SE"]):
                                    cell["proposed_target"] = {"row": row_index, "col": cell_index + 1}
                                    break

        # Second half of round: make proposed moves if they're unique
        for row_index, row in enumerate(grove):
            for cell_index, cell in enumerate(row):
                if cell["has_elf"]:
                    if cell["proposed_target"]:
                        if check_destination_is_unique(row_index, cell_index, cell["proposed_target"]):
                            grove[row_index][cell_index]["has_elf"] = False
                            grove[cell["proposed_target"]["row"]][cell["proposed_target"]["col"]] = {"has_elf": True, "moved_this_round": True, "proposed_target": None}
                            has_any_elf_moved = True

        # If this is Part 2, exit if all the elves stood still
        if part_two and not has_any_elf_moved:
            return

        # Finish the round: Set all elves back to clean state
        for row in grove:
            for cell in row:
                if cell["has_elf"]:
                    cell["moved_this_round"] = False
                    cell["proposed_target"] = None

        # Move the first proposed direction to the end of the list
        considered_directions.append(considered_directions.pop(0))

        if round_number % 50 == 0: print(f"Round {round_number+1} completed after {round(time.time() - start_time, 2)} seconds")

same_elf = lambda elf_x, elf_y: lambda x, y: x == elf_x and y == elf_y

grove = []
considered_directions = ["N","S","W","E"]

for line in open_file("input.txt"):
    this_row = []
    for char in line.strip():
        if char == ".": this_row.append({ "has_elf": False })
        else: this_row.append({ "has_elf": True, "moved_this_round": False, "proposed_target": None })
    grove.append(this_row)

# Part 1: Play 10 rounds, count how many squares do NOT have elves
round_count = 0
play_rounds(10)
shrink_grid_if_needed()
squares_without_elves = 0
for row in grove:
    for cell in row:
        if not cell["has_elf"]: squares_without_elves += 1
print(f"Part 1: {squares_without_elves} gaps") # 3800

# Part 2: Play until the elves stop moving
play_rounds(10000, True)
print(f"Part 2: Game stopped after {round_count} rounds") # 916 rounds (took 35 minutes to run!)