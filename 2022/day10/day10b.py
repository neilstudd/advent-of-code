import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def render_crt():
    for i in range(len(crt)//40):
        print(crt[i*40:(i+1)*40-1])

def update_crt():
    global crt
    pixel_range = range(x-1, x+2)
    if cycle-1 in pixel_range or cycle-41 in pixel_range or \
        cycle-81 in pixel_range or cycle-121 in pixel_range or \
        cycle-161 in pixel_range or cycle-201 in pixel_range or \
        cycle-241 in pixel_range:
            crt = crt[:cycle-1] + "#" + crt[cycle:]
    
is_addx = lambda line: line.startswith("addx")

crt = "." * 240
cycle = 0
x = 1

for line in open_file("input.txt"):
    cycle += 1
    update_crt()
    cycle += 1 if is_addx(line) else 0
    update_crt()
    x += int(line.split(" ")[1]) if is_addx(line) else 0

print(render_crt()) # RKAZAJBR