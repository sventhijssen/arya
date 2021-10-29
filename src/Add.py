import itertools
from typing import List

from src.Arithmetic import Arithmetic
from src.BinaryNumber import BinaryNumber


class Add(Arithmetic):

    def get_output_numbers(self) -> List[BinaryNumber]:
        pass

    def __init__(self, input_numbers: List[BinaryNumber], sum_number: BinaryNumber, carry_number: BinaryNumber):
        n = input_numbers[0].n
        for i in range(1, len(input_numbers)):
            if input_numbers[i].n != n:
                raise Warning("Input numbers must all have {} bits.".format(n))
        if sum_number.n != n:
            raise Warning("Input numbers have {} bits and sum number has {} bits.".format(n, sum_number.n))
        if carry_number.n != n:
            raise Warning("Input numbers have {} bits and carry number has {} bits.".format(n, carry_number.n))

        self.sum_number = sum_number
        self.carry_number = carry_number
        output_numbers = [sum_number, carry_number]
        super().__init__(input_numbers, output_numbers)

    def _generate(self):
        n = self.input_numbers[0].n

        for i in range(n):
            # For the last bit, we do not have a carry-in.
            input_variables = self.get_input_variables()
            xor_operands = input_variables.copy()
            if i != 0:
                xor_operands.append(self.carry_number.get_variables()[i])
            xor_operation = " ^ ".join(xor_operands)

            self.body += ' assign {} = {};\n'.format(self.sum_number.get_variables()[i], xor_operation)

            and_operands = self.get_input_variables().copy()
            if i != 0:
                and_operands.append(self.carry_number.get_variables()[i])
            and_combinations = list(itertools.combinations(and_operands, 2))
            and_operations = [" & ".join(and_combination) for and_combination in and_combinations]
            or_operation = " | ".join(and_operations)

            self.body += ' assign {} = {};\n'.format(self.carry_number.get_variables()[i], or_operation)
