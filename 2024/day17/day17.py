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
        self.expected_output = []

    # If we've given an expected_output, this method allows us to check if we've gone off track
    # eg: If we encounter a number in output which isn't in expected_output, or if we've got too many numbers
    def has_invalid_expected_output(self):
        if self.expected_output == []:
            return False
        elif len(self.expected_output) < len(self.output):
            return True
        else:
            for i in range(len(self.output)):
                if self.expected_output[i] != self.output[i]:
                    return True
        return False

    def get_next_instructions(self):
        if self.has_more_instructions():
            return self.instructions[self.instruction_pointer:self.instruction_pointer + 2]
        else:
            return None

    def has_more_instructions(self):
        return self.instruction_pointer < len(self.instructions)
    
    def compute_combo_operand(self, combo_operand):
        match combo_operand:
            case 0:
                return self.RegisterA
            case 1:
                return self.RegisterB
            case 2:
                return self.RegisterC
            case 3:
                return self.RegisterA ^ self.RegisterB
            case 4:
                return self.RegisterA ^ self.RegisterC
            case 5:
                return self.RegisterB ^ self.RegisterC
            case 6:
                return self.RegisterA ^ self.RegisterB ^ self.RegisterC
            case _:
                print("ERROR: Invalid combo operand")

    def execute_instruction(self, instruction):
        match instruction[0]:
            case 0: # adv # DONE
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
            case _:
                print("ERROR: Invalid opcode")
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

def run_part_two(mode, expected = None):
    data_file = open_file( mode + ".txt")
    computer = initialise_computer_from_file(data_file)
    desired_output_value = computer.instructions

    # If I was going to brute-force it, this is how it would go.
    # But based on AI projection, it would take literally 25 YEARS to complete.
    # Reddit tells me this is a problem which can be solved quickly with maths...
    initial_regA_value = 0
    while True: 
        computer = initialise_computer_from_file(data_file)
        computer.RegisterA = initial_regA_value
        computer.expected_output = desired_output_value
        while computer.has_more_instructions() and not computer.has_invalid_expected_output():
            next_instructions = computer.get_next_instructions()
            computer.execute_instruction(next_instructions)
        if computer.output == desired_output_value:
            break

        # if regA is divisible by 1000000, print a status update
        if initial_regA_value % 1000000 == 0:
            print("RegA: " + str(initial_regA_value) + "\nDesired output: " + str(desired_output_value) + "\nActual output: " + str(computer.output) + "\n")

        initial_regA_value += 1

    answer = initial_regA_value
    print_and_verify_answer(mode, "two", answer, expected)

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

    # PART TWO HELPER: invalid_expected_output remains False if we keep within bounds
    computer = Computer(117440, 0, 0, [0, 3, 5, 4, 3, 0])
    computer.expected_output = [0, 3, 5, 4, 3, 0]
    while computer.has_more_instructions() and not computer.has_invalid_expected_output():
        computer.execute_instruction(computer.get_next_instructions())
    assert computer.has_invalid_expected_output() == False

    # PART TWO HELPER: invalid_expected_output is triggered if the output is different
    computer = Computer(2, 0, 0, [0, 3, 5, 4, 3, 0])
    computer.expected_output = [9, 3, 5, 4, 3, 0]
    while computer.has_more_instructions() and not computer.has_invalid_expected_output():
        computer.execute_instruction(computer.get_next_instructions())
    print(computer.output)
    assert computer.has_invalid_expected_output() == True

# ADD EXPECTED OUTPUTS TO TESTS HERE 👇
run_tests()
run_part_one("test", "4,6,3,5,6,3,5,2,1,0")
run_part_one("prod", "1,2,3,1,3,2,5,3,1")
run_part_two("test2", 117440)
#run_part_two("prod")
# Now run it and watch the magic happen 🪄