from src.BinaryNumber import BinaryNumber
from src.InstructionSequence import InstructionSequence
from src.Sign import Sign

n = 8

x1_unsigned = BinaryNumber("x1", n)
x1_signed = BinaryNumber("x1_signed", n + 1)
sign_instruction_x1 = Sign(x1_unsigned, x1_signed)

inputs = [x1_unsigned]
outputs = [x1_signed]
instructions = [sign_instruction_x1]

instruction_sequence = InstructionSequence(inputs, outputs, instructions)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
