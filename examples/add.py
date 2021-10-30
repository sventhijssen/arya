from src.Add import Add
from src.BinaryNumber import BinaryNumber
from src.InstructionSequence import InstructionSequence

n = 8

left = BinaryNumber("x1", n + 1)
right = BinaryNumber("x2", n + 1)
sum = BinaryNumber("sum", n + 1)
carry = BinaryNumber("carry", n + 1)
add_instruction = Add([left, right], sum, carry)

inputs = [left, right]
outputs = [sum, carry]
instructions = [add_instruction]

instruction_sequence = InstructionSequence(inputs, outputs, instructions)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
