import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

def all_characters_unique(snippet):
    return len(set(snippet)) == len(snippet) # Thanks, StackOverflow

def find_start_of_packet(datastream, sequence_length):
    for i in range(0, len(datastream) - sequence_length):
        this_range = datastream[i:i+sequence_length]
        if all_characters_unique(this_range):
            return i+sequence_length 

file_content = open_file("input.txt")

for datastream in file_content:
    print("Part 1: " + str(find_start_of_packet(datastream, 4))) # 1282
    print("Part 2: " + str(find_start_of_packet(datastream, 14))) # 3513