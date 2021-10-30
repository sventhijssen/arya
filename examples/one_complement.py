from src.BinaryNumber import BinaryNumber
from src.InstructionSequence import InstructionSequence
from src.OneComplement import OneComplement

n = 8

x1_signed = BinaryNumber("x1_signed", n + 1)
x1_one_complement = BinaryNumber("x1_one_compl", n + 1)

one_complement_x1 = OneComplement(x1_signed, x1_one_complement)

inputs = [x1_signed]
outputs = [x1_one_complement]
instructions = [one_complement_x1]

instruction_sequence = InstructionSequence(inputs, outputs, instructions)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
