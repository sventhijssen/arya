from src.BinaryNumber import BinaryNumber
from src.OneComplement import OneComplement
from src.Shift import Shift
from src.TwoComplement import TwoComplement

n = 8

one_constant = BinaryNumber("ONE", n + 1)

x1_unsigned = BinaryNumber("x1", n)
x1_signed = x1_unsigned.to_signed(n + 1)

x2_unsigned = BinaryNumber("x2", n)
x2_signed = x2_unsigned.to_signed(n + 1)
x2_shifted = BinaryNumber("x2_shift", n + 1)

x3_unsigned = BinaryNumber("x3", n)
x3_signed = x3_unsigned.to_signed(n + 1)

x7_unsigned = BinaryNumber("x7", n)
x7_signed = x7_unsigned.to_signed(n + 1)
x7_one_complement = BinaryNumber("x7_one_compl", n + 1)
x7_two_complement = BinaryNumber("x7_two_compl", n + 1)
x7_carry = BinaryNumber("x7_carry", n + 1)

x8_unsigned = BinaryNumber("x8", n)
x8_signed = x8_unsigned.to_signed(n + 1)
x8_shifted = BinaryNumber("x8_shift", n + 1)

x9_unsigned = BinaryNumber("x9", n)
x9_signed = x9_unsigned.to_signed(n + 1)

shift = Shift(x2_signed, x2_shifted)
content = shift.get_content()
print(content)

shift = Shift(x8_signed, x8_shifted)
content = shift.get_content()
print(content)

one_complement = OneComplement(x7_signed, x7_one_complement)
content = one_complement.get_content()
print(content)

print("---")

two_complement = TwoComplement(x7_signed, x7_one_complement, one_constant, x7_carry, x7_two_complement)
content = two_complement.get_content()
print(content)
