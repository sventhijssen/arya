from BinaryNumber import BinaryNumber
from Constant import Constant
from InstructionSequence import InstructionSequence
from TwoComplement import TwoComplement

n = 8

one = BinaryNumber("ONE", n + 1)
one_constant = Constant(['1\'b1', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0'], one)

x1_signed = BinaryNumber("x1_signed", n + 1)
x1_one_complement = BinaryNumber("x1_one_compl", n + 1)
x1_two_complement = BinaryNumber("x1_two_compl", n + 1)
x1_carry = BinaryNumber("x1_carry", n + 1)

two_complement_x1 = TwoComplement(x1_signed, x1_one_complement, one, x1_carry, x1_two_complement)

inputs = [x1_signed]
outputs = [x1_two_complement]
wires = [x1_one_complement, one, x1_carry]
instructions = [two_complement_x1]

instruction_sequence = InstructionSequence(inputs, outputs, instructions, wires)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
