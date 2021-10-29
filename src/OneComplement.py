from typing import List

from src.Arithmetic import Arithmetic
from src.BinaryNumber import BinaryNumber


class OneComplement(Arithmetic):

    def get_output_numbers(self) -> List[BinaryNumber]:
        pass

    def __init__(self, input_number: BinaryNumber, output_number: BinaryNumber):
        if input_number.n != output_number.n:
            raise Warning(
                "Input number has {} bits and output number has {} bits".format(input_number.n, output_number.n))
        super().__init__([input_number], [output_number])

    def _generate(self):
        n = self.input_numbers[0].n
        input_variables = self.get_input_variables()
        output_variables = self.get_output_variables()
        for i in range(n):
            self.body += ' assign {} = ~{};\n'.format(input_variables[i], output_variables[i])
