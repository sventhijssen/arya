from src.Add import Add
from src.BinaryNumber import BinaryNumber
from src.Constant import Constant
from src.InstructionSequence import InstructionSequence
from src.LeftShift import LeftShift
from src.Sign import Sign
from src.TwoComplement import TwoComplement

n = 8

one = BinaryNumber("ONE", n + 1)
one_constant = Constant(['1\'b1', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0', '1\'b0'], one)

x1_unsigned = BinaryNumber("x1", n)
x1_signed = BinaryNumber("x1_signed", n + 1)

x2_unsigned = BinaryNumber("x2", n)
x2_signed = BinaryNumber("x2_signed", n + 1)
x2_shifted = BinaryNumber("x2_shifted", n + 1)

x3_unsigned = BinaryNumber("x3", n)
x3_signed = BinaryNumber("x3_signed", n + 1)

x7_unsigned = BinaryNumber("x7", n)
x7_signed = BinaryNumber("x7_signed", n + 1)
x7_one_compl = BinaryNumber("x7_one_compl", n + 1)
x7_carry = BinaryNumber("x7_carry", n + 1)
x7_two_compl = BinaryNumber("x7_two_compl", n + 1)

x8_unsigned = BinaryNumber("x8", n)
x8_signed = BinaryNumber("x8_signed", n + 1)
x8_shifted = BinaryNumber("x8_shifted", n + 1)
x8_one_compl = BinaryNumber("x8_one_compl", n + 1)
x8_carry = BinaryNumber("x8_carry", n + 1)
x8_two_compl = BinaryNumber("x8_two_compl", n + 1)

x9_unsigned = BinaryNumber("x9", n)
x9_signed = BinaryNumber("x9_signed", n + 1)
x9_one_compl = BinaryNumber("x9_one_compl", n + 1)
x9_carry = BinaryNumber("x9_carry", n + 1)
x9_two_compl = BinaryNumber("x9two_compl", n + 1)

s = BinaryNumber("s", n + 1)
c = BinaryNumber("c", n + 1)

sign_instruction_x1 = Sign(x1_unsigned, x1_signed)
sign_instruction_x2 = Sign(x2_unsigned, x2_signed)
sign_instruction_x3 = Sign(x3_unsigned, x3_signed)
sign_instruction_x7 = Sign(x7_unsigned, x7_signed)
sign_instruction_x8 = Sign(x8_unsigned, x8_signed)
sign_instruction_x9 = Sign(x9_unsigned, x9_signed)

shift_instruction_x2 = LeftShift(x2_signed, x2_shifted)
shift_instruction_x8 = LeftShift(x8_signed, x8_shifted)

two_complement_x7 = TwoComplement(x7_signed, x7_one_compl, one, x7_carry, x7_two_compl)
two_complement_x8 = TwoComplement(x8_shifted, x8_one_compl, one, x8_carry, x8_two_compl)
two_complement_x9 = TwoComplement(x7_signed, x9_one_compl, one, x9_carry, x9_two_compl)

add_instruction = Add([x1_signed, x2_shifted, x3_signed, x7_two_compl, x8_two_compl, x9_two_compl], s, c)

inputs = [x1_unsigned, x2_unsigned, x3_unsigned, x7_unsigned, x8_unsigned, x9_unsigned]
outputs = [s, c]
wires = [one,
         x1_signed, x2_signed, x3_signed, x7_signed, x8_signed, x9_signed,
         x2_shifted, x8_shifted,
         x7_one_compl, x7_carry,
         x8_one_compl, x8_carry,
         x9_one_compl, x9_carry,
         x7_two_compl, x8_two_compl, x9_two_compl]
instructions = [one_constant,
                sign_instruction_x1, sign_instruction_x2, sign_instruction_x3,
                sign_instruction_x7, sign_instruction_x8, sign_instruction_x9,
                shift_instruction_x2, shift_instruction_x8,
                two_complement_x7, two_complement_x8, two_complement_x9,
                add_instruction]

instruction_sequence = InstructionSequence(inputs, outputs, instructions, wires)
instruction_sequence.execute()
code = instruction_sequence.get_content()
print(code)
