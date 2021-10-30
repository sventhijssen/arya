from src.Instruction import Instruction
from src.BinaryNumber import BinaryNumber


class LeftShift(Instruction):

    def __init__(self, input_number: BinaryNumber, output_number: BinaryNumber):
        if input_number.n != output_number.n:
            raise Warning(
                "Input number has {} bits and output number has {} bits".format(input_number.n, output_number.n))
        super().__init__([input_number], [output_number])

    def execute(self):
        n = self.inputs[0].n
        input_variables = self.get_input_variables()
        output_variables = self.get_output_variables()

        self.body += ' assign {} = 1\'b0;\n'.format(output_variables[0])
        for i in range(1, n):
            self.body += ' assign {} = {};\n'.format(output_variables[i], input_variables[i - 1])
