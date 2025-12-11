import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

def parse_input(input):
    server_rack = {}
    for line in input:
        line = line.strip()
        if not line:
            continue
        parts = line.split(':')
        server = parts[0].strip()
        connections = parts[1].strip().split() if len(parts) > 1 else []
        server_rack[server] = connections
    return server_rack

def get_server(server_rack, server_name):
    for server in server_rack:
        if server.lower() == server_name.lower():
            return server
    return None

def calculate_all_paths_to_destination(server_rack, starting_server):
    exit_paths = set()
    stack = [(starting_server, [starting_server])]
    while stack:
        current_server, path = stack.pop()
        connections = server_rack.get(current_server, [])
        for conn in connections:
            if conn == "out":
                exit_paths.add(tuple(path + [conn]))
            elif conn in server_rack:
                stack.append((conn, path + [conn]))
    return exit_paths

def run_part_one(mode, expected = None):
    input = open_file( mode + ".txt")
    server_rack = parse_input(input)
    starting_server = get_server(server_rack, "you")
    unique_exits = len(calculate_all_paths_to_destination(server_rack, starting_server))
    print_and_verify_answer(mode, "one", unique_exits, expected)

def run_part_two(mode, expected = None):
    pass


# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_part_one("test", 5)
run_part_one("prod", 749)
run_part_two("test", 0)
run_part_two("prod", 0)
# Now run it and watch the magic happen 🪄