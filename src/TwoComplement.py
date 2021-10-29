from typing import List

from src.Add import Add
from src.Arithmetic import Arithmetic
from src.BinaryNumber import BinaryNumber
from src.OneComplement import OneComplement


class TwoComplement(Arithmetic):

    def get_output_numbers(self) -> List[BinaryNumber]:
        pass

    def __init__(self, input_number: BinaryNumber, one_complement_number: BinaryNumber, one_constant: BinaryNumber, carry_number: BinaryNumber, output_number: BinaryNumber):
        if input_number.n != one_complement_number.n:
            raise Warning(
                "Input number has {} bits and one complement number has {} bits".format(
                    input_number.n, one_complement_number.n))
        if input_number.n != output_number.n:
            raise Warning(
                "Input number has {} bits and output number has {} bits".format(input_number.n, output_number.n))
        self.one_constant = one_constant
        self.carry_number = carry_number
        super().__init__([input_number], [output_number], [one_complement_number])

    def _generate(self):
        n = self.input_numbers[0].n

        # Step 1: One complement
        one_complement = OneComplement(self.wire_numbers[0], self.input_numbers[0])
        self.body += one_complement.get_body()

        # Step 2: Addition of one complement and one
        # Write constant one as a variable
        for i in range(n):
            one_constant_variables = self.one_constant.get_variables()
            if i == 0:
                self.body += ' assign {} = 1\'b1;\n'.format(one_constant_variables[i])
            else:
                self.body += ' assign {} = 1\'b0;\n'.format(one_constant_variables[i])

        add = Add([self.wire_numbers[0], self.one_constant], self.output_numbers[0], self.carry_number)
        self.body += add.get_body()
