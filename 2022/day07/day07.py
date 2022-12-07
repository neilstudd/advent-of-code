import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

def is_command(line):
    return line.startswith("$")

def is_change_dir(line):
    return line.startswith("$ cd ")

def is_list_dir(line):
    return line.startswith("$ ls")

def is_dir_name(line):
    return line.startswith("dir ")

def is_root_dir(dir):
    return dir == "/"

def is_navigate_up(dir):
    return dir == ".."

def get_file_size(line):
    return int(line.split(" ")[0])

dir_tree = {}
cwd = ""
currently_listing_directory = False
current_directory_size = 0

for line in file_content:
    if currently_listing_directory:
        if is_command(line):
            currently_listing_directory = False
            for folder in dir_tree:
                if cwd.startswith(folder):
                    dir_tree[folder] += current_directory_size
            current_directory_size = 0
        elif not is_dir_name(line):
            current_directory_size += get_file_size(line)
    if is_command(line):
        if is_change_dir(line):
            dir_to_select = line.strip().split("$ cd ")[1]
            if is_root_dir(dir_to_select):
                cwd = "/"
            elif is_navigate_up(dir_to_select):
                cwd = cwd.split("/")[:-1]
                cwd = "/".join(cwd)
            else:
                if cwd == "/":
                    cwd = cwd + dir_to_select
                else:
                    cwd = cwd + "/" + dir_to_select
            if not cwd in dir_tree:
                dir_tree[cwd] = 0
        if is_list_dir(line):
            currently_listing_directory = True
    
# Now we are out of the loop, we need to finalise the final directory
for folder in dir_tree:
    if cwd.startswith(folder):
        dir_tree[folder] += current_directory_size

# Calculate sum of all directories of at most 100000
total = 0
for folder in dir_tree:
    if dir_tree[folder] <= 100000:
        total += dir_tree[folder]

print(f"PART ONE: Total of all small directories: {total}") # 1449447

## PART TWO

TOTAL_DISK_SPACE = 70000000
REQUIRED_DISK_SPACE = 30000000
AVAILABLE_DISK_SPACE = TOTAL_DISK_SPACE - dir_tree["/"]
SPACE_TO_CREATE = REQUIRED_DISK_SPACE - AVAILABLE_DISK_SPACE

sorted_directories = sorted(dir_tree.items(), key=lambda x: x[1])
for dir in sorted_directories:
    # hack for weird bonus directory
    if dir[0] != "":
        if dir[1] >= SPACE_TO_CREATE:
            print(f"PART TWO: Delete {dir[0]} with size {dir[1]}")
            break