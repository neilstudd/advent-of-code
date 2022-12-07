import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

file_content = open_file("input.txt")

is_command = lambda line: (line.startswith("$"))
is_change_dir = lambda line: (line.startswith("$ cd "))
is_list_dir = lambda line: (line.startswith("$ ls"))
is_dir_name = lambda line: (line.startswith("dir "))
is_root_dir = lambda dir: (dir == "/")
is_navigate_up = lambda dir: (dir == "..")
get_file_size = lambda line: (int(line.split(" ")[0]))

def add_size_to_relevant_directories(dir_tree, cwd, size):
    for dir in dir_tree:
        if cwd.startswith(dir):
            dir_tree[dir] += size

dir_tree = {}
cwd = ""
currently_listing_directory = False
current_directory_size = 0

for line in file_content:
    # Begin by checking if we are currently processing a list of directory files
    if currently_listing_directory:
        if is_command(line):
            # We've finished listing files, so print the collated filesize to this directory and parents
            add_size_to_relevant_directories(dir_tree, cwd, current_directory_size)
            currently_listing_directory = False
            current_directory_size = 0
        elif not is_dir_name(line):
            # We are still gathering files, so increment total filesize
            current_directory_size += get_file_size(line)
    # If we have received terminal input (cd or ls), do something with it
    if is_change_dir(line):
        dir_to_select = line.strip().split("$ cd ")[1]
        if is_root_dir(dir_to_select):
            cwd = "/"
        elif is_navigate_up(dir_to_select):
            cwd = cwd.split("/")[:-1]
            cwd = "/".join(cwd) if cwd != "" else "/"
        else:
            cwd += dir_to_select if is_root_dir(cwd) else f"/{dir_to_select}"
        # Initialise directory if it's not already in the tree
        dir_tree[cwd] = 0 if not cwd in dir_tree else dir_tree[cwd]
    elif is_list_dir(line):
        currently_listing_directory = True
    
# Now we are out of the loop, we need to finalise the final directory
add_size_to_relevant_directories(dir_tree, cwd, current_directory_size)

# Calculate sum of all directories of at most 100000
total = sum([dir_tree[dir] for dir in dir_tree if dir_tree[dir] <= 100000])
print(f"PART ONE: Total of all small directories: {total}") # 1449447

## PART TWO
TOTAL_DISK_SPACE = 70000000
REQUIRED_DISK_SPACE = 30000000
AVAILABLE_DISK_SPACE = TOTAL_DISK_SPACE - dir_tree["/"]
SPACE_TO_CREATE = REQUIRED_DISK_SPACE - AVAILABLE_DISK_SPACE
sorted_directories = sorted(dir_tree.items(), key=lambda x: x[1])
for dir in sorted_directories:
    if dir[1] >= SPACE_TO_CREATE:
        print(f"PART TWO: Delete {dir[0]} with size {dir[1]}") # 8679207
        break