from BinaryNumber import BinaryNumber
from Constant import Constant
from InstructionSequence import InstructionSequence

n = 8

one = BinaryNumber("ONE", n + 1)
one_constant = Constant(['1\'b1', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0'], one)

inputs = []
outputs = [one]
instructions = [one_constant]

instruction_sequence = InstructionSequence(inputs, outputs, instructions)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
