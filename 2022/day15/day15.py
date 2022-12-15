import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

scanned_spots = set()
beacons_found = set()
ROW_TO_CHECK = 2000000

start_time = time.time()
for line in open_file("input.txt"):
    sensor_x = int(line.split(" ")[2].split(",")[0].split("=")[1])
    sensor_y = int(line.split(" ")[3].split(":")[0].split("=")[1])
    beacon_x = int(line.split(" ")[8].split(",")[0].split("=")[1])
    beacon_y = int(line.split(" ")[9].split(":")[0].split("=")[1])
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    min_x = min(0, sensor_x - distance)
    max_x = max(0, sensor_x + distance)
    min_y = min(0, sensor_y - distance)
    max_y = max(0, sensor_y + distance)
    if min_y <= ROW_TO_CHECK <= max_y:
        numbers_to_check = [i for i in range(min_x, max_x + 1) if i not in scanned_spots]
        for x in numbers_to_check:
            if abs(sensor_x - x) + abs(sensor_y - ROW_TO_CHECK) <= distance: scanned_spots.add(x)
    if beacon_y == ROW_TO_CHECK and beacon_x not in beacons_found: beacons_found.add(beacon_x)    
    print(f"Done {sensor_x}, {sensor_y} after {round(time.time() - start_time, 1)} seconds")

print(f"Part 1: Scanned {len(set(scanned_spots))} spots in target row; but also {len(beacons_found)} beacons.")
print(f"Answer is therefore {len(set(scanned_spots)) - len(beacons_found)}")
# 5181557 spaces without beacons; minus 1 beacon = 5181556