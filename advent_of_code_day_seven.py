import itertools
class Parameter:
    def __init__(self, value, mode):
        self.value = value
        self.mode = mode

    def read_parameter(self, dataset):
        if self.mode == 0:
            return dataset[self.value]
        elif self.mode == 1:
            return self.value
    
    def write_parameter(self, dataset, result):
        if self.mode == 0:
            dataset[self.value] = result
        elif self.mode == 1:
            print(f"Illegal write method")
            exit()

class ModeOp:
 
    def __init__(self, value):
        self.value = value
        self.modeoperator = self.standardise_modeoperator(self.value)
        self.opcode = int(self.modeoperator[3:5])
        self.firstmode = int(self.modeoperator[2])
        self.secondmode = int(self.modeoperator[1])
        self.thirdmode = int(self.modeoperator[0])

    def standardise_modeoperator(self, value: int):
        this_string = str(value)
        needed_zeros = 5 - len(this_string)
        return ('0' * needed_zeros) + this_string


    def advance(self):
        if self.opcode in [1, 2, 7, 8]:
            return 4
        if self.opcode in [3, 4]:
            return 2
        if self.opcode in [5, 6]:
            return 3
        if self.opcode == 99:
            return 0
        else:
            print(f"Whoops! ModeOp {self.opcode} shouldn't exist!")
            exit()

class Instruction:
    def __init__(self, modeop: ModeOp, parameters: [Parameter]):
        self.modeop = modeop
        self.parameters = parameters

    def execute(self, dataset, inputs, outputs):
        if self.modeop.opcode == 1:
            a = self.parameters[0].read_parameter(dataset)
            b = self.parameters[1].read_parameter(dataset)
            c = a + b
            self.parameters[2].write_parameter(dataset, c)
        elif self.modeop.opcode == 2:
            a = self.parameters[0].read_parameter(dataset)
            b = self.parameters[1].read_parameter(dataset)
            c = a * b
            self.parameters[2].write_parameter(dataset, c)
        elif self.modeop.opcode == 3:
            this_input = inputs.pop()
            self.parameters[0].write_parameter(dataset, this_input)
        elif self.modeop.opcode == 4:
            outputs.append(self.parameters[0].read_parameter(dataset))
        elif self.modeop.opcode == 5:
            if self.parameters[0].read_parameter(dataset) != 0:
                pc = self.parameters[1].read_parameter(dataset)
                return pc
        elif self.modeop.opcode == 6:
            if self.parameters[0].read_parameter(dataset) == 0:
                pc = self.parameters[1].read_parameter(dataset)
                return pc
        elif self.modeop.opcode == 7:
            if self.parameters[0].read_parameter(dataset) < self.parameters[1].read_parameter(dataset):
                self.parameters[2].write_parameter(dataset, 1)
            else:
                self.parameters[2].write_parameter(dataset, 0)
        elif self.modeop.opcode == 8:
            if self.parameters[0].read_parameter(dataset) == self.parameters[1].read_parameter(dataset):
                self.parameters[2].write_parameter(dataset, 1)
            else:
                self.parameters[2].write_parameter(dataset, 0)            
          
    
def decode(pc, data):
    this_modeop = ModeOp(data[pc])
    parameters = []
    if this_modeop.opcode in [1, 2, 7, 8]:
        parameters.append(Parameter(data[pc+1], this_modeop.firstmode))
        parameters.append(Parameter(data[pc+2], this_modeop.secondmode))
        parameters.append(Parameter(data[pc+3], this_modeop.thirdmode))
    elif this_modeop.opcode in [3, 4]:
        parameters.append(Parameter(data[pc+1], this_modeop.firstmode))
    elif this_modeop.opcode in [5, 6]:
        parameters.append(Parameter(data[pc+1], this_modeop.firstmode))
        parameters.append(Parameter(data[pc+2], this_modeop.secondmode))        
    elif this_modeop.opcode == 99:
        pass
    else:
        print(f"Whoops! ModeOp {this_modeop.opcode} shouldn't exist!")
    return Instruction(this_modeop, parameters)


with open("AdventofCode/advent_of_code_puzzle_file_day_seven.txt") as number_sequence:    
    number_string = number_sequence.read()
    split_string = number_string.split(',')
    memory = [int(i) for i in split_string]

def run_cpu(memory, inputs):
    outputs = []
    pc = 0
    while True:
        this_instruction = decode(pc, memory)
        jump = this_instruction.execute(memory, inputs, outputs)
        if this_instruction.modeop.opcode == 99:
            return outputs
        if jump is not None:
            pc = jump
        else:
            pc += this_instruction.modeop.advance()

def run_amplifier_series(memory, input_items):
    a_result = run_cpu(memory[:], [0, input_items[0]])
    b_result = run_cpu(memory[:], [a_result[0], input_items[1]])
    c_result = run_cpu(memory[:], [b_result[0], input_items[2]])
    d_result = run_cpu(memory[:], [c_result[0], input_items[3]])
    e_result = run_cpu(memory[:], [d_result[0], input_items[4]])
    return e_result[0]


ten = [5, 6, 7, 8, 9]
possibilities = list(itertools.permutations(ten, 5))
maximum_result = 0
for combo in possibilities:
    result = run_amplifier_series(memory, combo)
    if result > maximum_result:
        maximum_result = result
print(maximum_result)
    

