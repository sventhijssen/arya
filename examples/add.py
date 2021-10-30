from Add import Add
from BinaryNumber import BinaryNumber
from InstructionSequence import InstructionSequence

n = 4

x1 = BinaryNumber("x1", n)
x2 = BinaryNumber("x2", n)
x3 = BinaryNumber("x3", n)
sum = BinaryNumber("sum", n)
carry = BinaryNumber("carry", n)
add_instruction = Add([x1, x2, x3], sum, carry)

inputs = [x1, x2, x3]
outputs = [sum, carry]
instructions = [add_instruction]

instruction_sequence = InstructionSequence(inputs, outputs, instructions)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
