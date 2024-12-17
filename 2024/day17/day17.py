import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from common import open_file, print_and_verify_answer

class Computer:
    def __init__ (self, regA = 0, regB = 0, regC = 0, instructions = []):
        self.RegisterA = regA
        self.RegisterB = regB
        self.RegisterC = regC
        self.instructions = instructions
        self.instruction_pointer = 0
        self.output = []

    def get_next_instructions(self):
        if self.has_more_instructions():
            return self.instructions[self.instruction_pointer:self.instruction_pointer + 2]
        else:
            return None

    def has_more_instructions(self):
        return self.instruction_pointer < len(self.instructions)

    def execute_instruction(self, instruction):
        match instruction[0]:
            case 0: # adv
                numerator = self.RegisterA
                denominator = self.compute_combo_operand(instruction[1])
                self.RegisterA = numerator // (2 ** denominator)
            case 1: # bxl
                self.RegisterB = self.RegisterB ^ instruction[1]
            case 2: # bst
                input = self.compute_combo_operand(instruction[1])
                self.RegisterB = input % 8
            case 3: # jnz
                if self.RegisterA != 0:
                    self.instruction_pointer = instruction[1] - 2
            case 4: # bxc
                self.RegisterB = self.RegisterB ^ self.RegisterC
            case 5: # out
                combo_operand = self.compute_combo_operand(instruction[1])
                self.output.append(combo_operand % 8)
            case 6: # bdv
                numerator = self.RegisterA
                denominator = self.compute_combo_operand(instruction[1])
                self.RegisterB = numerator // (2 ** denominator)
            case 7: # cdv
                numerator = self.RegisterA
                denominator = self.compute_combo_operand(instruction[1])
                self.RegisterC = numerator // (2 ** denominator)
        self.instruction_pointer += 2

    def compute_combo_operand(self, combo_operand):
        match combo_operand:
            case 4:
                return self.RegisterA
            case 5:
                return self.RegisterB
            case 6:
                return self.RegisterC
            case _:
                return combo_operand

def initialise_computer_from_file(data_file):
    regA = 0
    regB = 0
    regC = 0
    program_string = []
    for line in data_file:
        if line.startswith("Register A: "):
            regA = int(line.strip().split(": ")[1])
        elif line.startswith("Register B: "):
            regB = int(line.strip().split(": ")[1])
        elif line.startswith("Register C: "):
            regC = int(line.strip().split(": ")[1])
        elif line.startswith("Program: "):
            program_string.extend([int(x) for x in line.strip().split(": ")[1].split(",")])
    return Computer(regA, regB, regC, program_string)

def run_part_one(mode, expected = None):
    data_file = open_file( mode + ".txt")
    computer = initialise_computer_from_file(data_file)
    while computer.has_more_instructions():
        next_instructions = computer.get_next_instructions()
        computer.execute_instruction(next_instructions)
    answer = ",".join([str(x) for x in computer.output])
    print_and_verify_answer(mode, "one", answer, expected)

# Maths logic assist from Reddit, but the code is all my own!
def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    computer = initialise_computer_from_file(data_file)
    desired_output_value = computer.instructions
    matching_digits_from_right = 0
    initial_regA_value = 0
    while matching_digits_from_right < len(desired_output_value): 
        computer = initialise_computer_from_file(data_file)
        computer.RegisterA = initial_regA_value
        computer.expected_output = desired_output_value
        while computer.has_more_instructions():
            next_instructions = computer.get_next_instructions()
            computer.execute_instruction(next_instructions)
        while len(computer.output) < len(desired_output_value):
            computer.output.insert(0, 0) # Front-pad to avoid length violation
        if matching_digits_from_right <= len(computer.output):
            if computer.output[-1 - matching_digits_from_right] == desired_output_value[-1 - matching_digits_from_right]:
                matching_digits_from_right += 1
                initial_regA_value *= 8
            else:
                initial_regA_value += 1
    initial_regA_value = initial_regA_value // 8 # lowest multiple
    print_and_verify_answer(mode, "two", initial_regA_value, expected)

# Shortcut to taking a proper TDD approach, which I'll do in 2025!
def run_tests():
    # Write a test which checks that a new Computer has all registers set to None
    computer = Computer()
    assert computer.RegisterA == 0
    assert computer.RegisterB == 0
    assert computer.RegisterC == 0
    assert computer.instructions == []

    # NEIL TEST 1: adv specification (use literal combo)
    # Divides the value from Register A
    computer  = Computer(12, 0, 0, [0, 2])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterA == 3

    # NEIL TEST 2: adv specification (use register value)
    # Divides the value from Register A
    computer  = Computer(12, 2, 0, [0, 5])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterA == 3

    # RULE 1: If register C contains 9, the program 2,6 would set register B to 1.
    computer = Computer(0, 0, 9, [2, 6])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterB == 1

    # RULE 2: If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
    computer = Computer(10, 0, 0, [5, 0, 5, 1, 5, 4])
    computer.execute_instruction(computer.get_next_instructions())
    computer.execute_instruction(computer.get_next_instructions())
    computer.execute_instruction(computer.get_next_instructions()) 
    assert computer.output == [0, 1, 2]

    # RULE 3: If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
    computer = Computer(2024, 0, 0, [0, 1, 5, 4, 3, 0])
    while computer.has_more_instructions():
        computer.execute_instruction(computer.get_next_instructions())
    assert computer.output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert computer.RegisterA == 0

    # RULE 4: If register B contains 29, the program 1,7 would set register B to 26.
    computer = Computer(0, 29, 0, [1, 7])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterB == 26

    # RULE 5: If register B contains 29, the program 1,7 would set register B to 26.
    computer = Computer(0, 29, 0, [1, 7])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterB == 26

    # RULE 6: If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354
    computer = Computer(0, 2024, 43690, [4, 0])
    computer.execute_instruction(computer.get_next_instructions())
    assert computer.RegisterB == 44354

    # PART TWO TEST CASE: 117440 should output itself
    computer = Computer(117440, 0, 0, [0, 3, 5, 4, 3, 0])
    while computer.has_more_instructions():
        computer.execute_instruction(computer.get_next_instructions())
    assert computer.output == [0, 3, 5, 4, 3, 0]

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_tests()
run_part_one("test", "4,6,3,5,6,3,5,2,1,0")
run_part_one("prod", "1,2,3,1,3,2,5,3,1")
run_part_two("test2", 117440)
run_part_two("prod", 105706277661082) 
# Now run it and watch the magic happen 🪄