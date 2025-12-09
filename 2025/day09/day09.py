import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    tile_coords = set()
    tiles = open_file( mode + ".txt")
    for tile in tiles:
        x, y = map(int, tile.split(","))
        tile_coords.add((x, y))
    largest_rectangle = 0
    for tile in tile_coords:
        for other_tile in tile_coords:
            if tile != other_tile:
                x1, y1 = tile
                x2, y2 = other_tile
                area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
                if area > largest_rectangle:
                    largest_rectangle = area

    print_and_verify_answer(mode, "one", largest_rectangle, expected)
    

def run_part_two(mode, expected = None):
    pass

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 50)
run_part_one("prod", 4746238001)
run_part_two("test", 0)
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄