import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def build_lobby(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def build_robots(data_file):
    robots = []
    for line in data_file:
        position, velocity = line.strip().split(" v=")
        x, y = map(int, position.replace("p=", "").split(","))
        vx, vy = map(int, velocity.split(","))
        robots.append({
            "pos_x": x,
            "pos_y": y,
            "vel_x": vx,
            "vel_y": vy
        })
    return robots

def update_positions(robots, lobby):
    for robot in robots:
        x = robot["pos_x"]
        y = robot["pos_y"]
        lobby[y][x] += 1
    return lobby

def calculate_quadrants(lobby):
    quadrant_width = len(lobby[0]) // 2
    quadrant_height = len(lobby) // 2
    q1 = []
    for y in range(quadrant_height):
        row = []
        for x in range(quadrant_width):
            row.append(lobby[y][x])
        q1.append(row)
    q2 = []
    for y in range(quadrant_height):
        row = []
        for x in range(quadrant_width+1, len(lobby[0])):
            row.append(lobby[y][x])
        q2.append(row)
    q3 = []
    for y in range(quadrant_height+1, len(lobby)):
        row = []
        for x in range(quadrant_width):
            row.append(lobby[y][x])
        q3.append(row)
    q4 = []
    for y in range(quadrant_height+1, len(lobby)):
        row = []
        for x in range(quadrant_width+1, len(lobby[0])):
            row.append(lobby[y][x])
        q4.append(row)
    q1_sum = sum([sum(row) for row in q1])
    q2_sum = sum([sum(row) for row in q2])
    q3_sum = sum([sum(row) for row in q3])
    q4_sum = sum([sum(row) for row in q4])
    return q1_sum * q2_sum * q3_sum * q4_sum

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    robots = build_robots(data_file)
    width, height = (11, 7) if mode == "test" else (101, 103)
    lobby = build_lobby(width, height)
    for _ in range(1,101):
        for robot in robots:
            robot["pos_x"] += robot["vel_x"]
            robot["pos_y"] += robot["vel_y"]
            if robot["pos_x"] < 0:
                robot["pos_x"] += width
            elif robot["pos_x"] >= width:
                robot["pos_x"] -= width
            if robot["pos_y"] < 0:
                robot["pos_y"] += height
            elif robot["pos_y"] >= height:
                robot["pos_y"] -= height
        lobby = build_lobby(width, height)
        update_positions(robots, lobby)
    answer = calculate_quadrants(lobby)
    print_and_verify_answer(mode, "one", answer, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    robots = build_robots(data_file)
    width, height = (11, 7) if mode == "test" else (101, 103)
    lobby = build_lobby(width, height)
    for seconds in range(1,10000):
        for robot in robots:
            robot["pos_x"] += robot["vel_x"]
            robot["pos_y"] += robot["vel_y"]
            if robot["pos_x"] < 0:
                robot["pos_x"] += width
            elif robot["pos_x"] >= width:
                robot["pos_x"] -= width
            if robot["pos_y"] < 0:
                robot["pos_y"] += height
            elif robot["pos_y"] >= height:
                robot["pos_y"] -= height
        lobby = build_lobby(width, height)
        new_positions = update_positions(robots, lobby)
        output = "\n".join("".join("#" if char > 0 else " " for char in line) for line in new_positions)
        # (NB: Actually solved this by printing all the outputs to file, then checking the file)
        # Check if output contains "#################"
        # If so, the current number of seconds is the answer
        if "#################" in output:
            break
    print_and_verify_answer(mode, "two", seconds, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 12)
run_part_one("prod", 214400550)
run_part_two("prod", 8149)
# Now run it and watch the magic happen 🪄