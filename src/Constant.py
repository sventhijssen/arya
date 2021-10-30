from typing import List

from Instruction import Instruction
from BinaryNumber import BinaryNumber


class Constant(Instruction):

    def __init__(self, input: List[str], output: BinaryNumber):
        super().__init__([], [output])
        self.input = input

    def execute(self):
        n = self.outputs[0].n
        output_variables = self.get_output_variables()

        for i in range(n):
            self.body += ' assign {} = {};\n'.format(output_variables[i], self.input[i])
