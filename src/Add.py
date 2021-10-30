import itertools
from typing import List

from BinaryNumber import BinaryNumber
from Instruction import Instruction


class Add(Instruction):

    def __init__(self, inputs: List[BinaryNumber], sum_number: BinaryNumber, carry_number: BinaryNumber):
        n = inputs[0].n
        for i in range(1, len(inputs)):
            if inputs[i].n != n:
                raise Warning("Input numbers must all have {} bits.".format(n))
        if sum_number.n != n:
            raise Warning("Input numbers have {} bits and sum number has {} bits.".format(n, sum_number.n))
        if carry_number.n != n:
            raise Warning("Input numbers have {} bits and carry number has {} bits.".format(n, carry_number.n))

        self.sum_number = sum_number
        self.carry_number = carry_number
        output_numbers = [sum_number, carry_number]
        super().__init__(inputs, output_numbers)

    def execute(self):
        n = self.inputs[0].n

        for i in range(n):
            # For the last bit, we do not have a carry-in.
            xor_operands = []
            for j in range(len(self.inputs)):
                input_variables = self.inputs[j].get_variables()
                xor_operands.append(input_variables[i])
            if i != 0:
                xor_operands.append(self.carry_number.get_variables()[i - 1])
            xor_operation = " ^ ".join(xor_operands)

            self.body += ' assign {} = {};\n'.format(self.sum_number.get_variables()[i], xor_operation)

            and_operands = []
            for j in range(len(self.inputs)):
                input_variables = self.inputs[j].get_variables()
                and_operands.append(input_variables[i])
            if i != 0:
                and_operands.append(self.carry_number.get_variables()[i - 1])
            and_combinations = list(itertools.combinations(and_operands, 2))
            and_operations = [" & ".join(and_combination) for and_combination in and_combinations]
            or_operation = " | ".join(and_operations)

            self.body += ' assign {} = {};\n'.format(self.carry_number.get_variables()[i], or_operation)
