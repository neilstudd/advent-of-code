import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file

class Valve:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        self.amassed_score = 0
        self.valve_open = False

    def open_valve(self):
        print(f"You open valve {self.name}.\n")
        self.valve_open = True

    def update_score(self):
        if self.valve_open:
            self.amassed_score += self.flow_rate

def score_open_valves():
    for valve in valves.values():
        valve.update_score()

def print_open_valves():
    any_valves_open = False
    for valve in valves.values():
        if valve.valve_open:
            any_valves_open = True
            print(f"Valve {valve.name} is open, releasing {valve.flow_rate} pressure")
    if not any_valves_open: print("No valves are open.")

def check_flow_opportunity():
    opportunity = 0
    for tunnel in valves[current_location].tunnels:
        if not valves[tunnel].valve_open: opportunity += valves[tunnel].flow_rate
        for tunnel2 in valves[tunnel].tunnels:
            if not valves[tunnel2].valve_open: opportunity += valves[tunnel2].flow_rate
            for tunnel3 in valves[tunnel2].tunnels:
                if not valves[tunnel3].valve_open: opportunity += valves[tunnel3].flow_rate
    return opportunity

def make_a_move():
    current_valve = valves[current_location]

    # Find which valve has the highest flow opportunity
    best_tunnel = None
    best_opportunity = 0
    for tunnel in current_valve.tunnels:
        opportunity = check_flow_opportunity()
        if opportunity > best_opportunity:
            best_opportunity = opportunity
            best_tunnel = tunnel
    if best_tunnel:
        print(f"Best choice: You move to valve {best_tunnel}.\n")
        return best_tunnel


    for tunnel in current_valve.tunnels:
        if not valves[tunnel].valve_open and valves[tunnel].flow_rate > 0:
            print(f"You move to valve {tunnel}.\n")
            return tunnel
    for tunnel in current_valve.tunnels:
        for tunnel2 in valves[tunnel].tunnels:
            if not valves[tunnel2].valve_open and valves[tunnel2].flow_rate > 0:
                print(f"You move to valve {tunnel} (to set up a move to {tunnel2}).\n")
                return tunnel                



    print(f"Arbitrary choice: You move to valve {tunnel}.\n")
    return tunnel # none are open, just go to the last

valves = {}

valves['AA'] = Valve('AA', 0, ['DD', 'II', 'BB'])
valves['BB'] = Valve('BB', 13, ['CC', 'AA'])
valves['CC'] = Valve('CC', 2, ['DD', 'BB'])
valves['DD'] = Valve('DD', 20, ['CC', 'AA', 'EE'])
valves['EE'] = Valve('EE', 3, ['FF', 'DD'])
valves['FF'] = Valve('FF', 0, ['EE', 'GG'])
valves['GG'] = Valve('GG', 0, ['FF', 'HH'])
valves['HH'] = Valve('HH', 22, ['GG'])
valves['II'] = Valve('II', 0, ['AA', 'JJ'])
valves['JJ'] = Valve('JJ', 21, ['II'])

print(valves)
current_location = "AA"

for round in range(1,21):
    print(f"=== Minute {round}: {current_location} ===")
    score_open_valves()
    print_open_valves()
    if not valves[current_location].valve_open and valves[current_location].flow_rate > 0:
        valves[current_location].open_valve()
    else:
        current_location = make_a_move()

print(f"=== Final Score ===")
total_score = [ val.amassed_score for val in valves.values() ]
print(f"Total score: {sum(total_score)}")