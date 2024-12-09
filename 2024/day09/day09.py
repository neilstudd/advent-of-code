import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    input = "".join(line.strip() for line in data_file)
    disk_array = []
    current_block_index = 0
    for i in range(0, len(input)):
        if i % 2 == 1:
            disk_array.extend(['.'] * int(input[i]))
        else: 
            block_size = int(input[i])
            disk_array.extend([(current_block_index, block_size)] * block_size)
            current_block_index += 1

    last_non_dot_index = len(disk_array) - 1
    for char_index in range(len(disk_array)):
        if disk_array[char_index] == '.':
            while disk_array[last_non_dot_index] == '.' and last_non_dot_index > char_index:
                last_non_dot_index -= 1
            if last_non_dot_index > char_index:
                disk_array[char_index], disk_array[last_non_dot_index] = disk_array[last_non_dot_index], '.'
                last_non_dot_index -= 1

    disk_array = [char for char in disk_array if char != '.'] # strip dots
    calculated_checksum = sum(index * block_id for index, (block_id, _) in enumerate(disk_array))
    print_and_verify_answer(mode, "one", calculated_checksum, expected)

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    input = "".join(line.strip() for line in data_file)
    disk_array = []
    current_block_index = 0
    i = 0
    while i < len(input):
        if i % 2 == 1:
            disk_array.append('.' * int(input[i]))
        else:
            block_size = int(input[i])
            disk_array.append((current_block_index, 'X' * block_size))
            current_block_index += 1
        i += 1

    max_block_id = current_block_index - 1
    for block_id in range(max_block_id, 0, -1):
        block_index = next((index for index, char in enumerate(disk_array) if isinstance(char, tuple) and char[0] == block_id), None)
        if block_index is None:
            continue
        block_size = len(disk_array[block_index][1])

        for char_index, char in enumerate(disk_array):
            if isinstance(char, str) and len(char) >= block_size and char_index < block_index:
                disk_array[char_index] = disk_array[block_index]
                disk_array[block_index] = '.' * block_size
                remaining_dots = len(char) - block_size
                if remaining_dots > 0:
                    disk_array.insert(char_index + 1, '.' * remaining_dots)
                break

    calculated_checksum = 0
    file_index = 0
    for item in disk_array:
        if type(item) == str:
            file_index += len(item)
        else:
            for _ in range(0, len(item[1])):
                calculated_checksum += file_index*item[0]
                file_index += 1

    print_and_verify_answer(mode, "two", calculated_checksum, expected)

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 1928)
run_part_one("prod", 6283170117911)
run_part_two("test", 2858)
run_part_two("prod", 6307653242596)
# Now run it and watch the magic happen 🪄