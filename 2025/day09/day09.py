import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def calculate_tiles(mode):
    tile_coords = set()
    tiles = open_file( mode + ".txt")
    for tile in tiles:
        x, y = map(int, tile.split(","))
        tile_coords.add((x, y))
    return tile_coords

def calculate_all_rectangles(tile_coords):
    rectangles = []
    for tile in tile_coords:
        for other_tile in tile_coords:
            if tile != other_tile:
                x1, y1 = tile
                x2, y2 = other_tile
                area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
                rectangles.append(((tile, other_tile), area))
    rectangles.sort(key=lambda x: x[1], reverse=True) # descending order of area
    return rectangles

def run_part_one(mode, expected = None):
    tile_coords = calculate_tiles(mode)
    rectangles = calculate_all_rectangles(tile_coords)
    print_and_verify_answer(mode, "one", rectangles[0][1], expected)
    
def run_part_two(mode, expected = None):
    pass

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 50)
run_part_one("prod", 4746238001)
run_part_two("test", 0)
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄