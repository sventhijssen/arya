from src.BinaryNumber import BinaryNumber
from src.Instruction import Instruction


class Sign(Instruction):

    def __init__(self, old_binary_number: BinaryNumber, new_binary_number: BinaryNumber):
        super().__init__([old_binary_number], [new_binary_number])

    def execute(self):
        old_binary_number = self.inputs[0]
        new_binary_number = self.outputs[0]

        if new_binary_number.n < old_binary_number.n:
            raise Warning("Converting an integer of {} bits into an integer of {} bits can result in loss of "
                          "information.".format(old_binary_number.n, new_binary_number.n))

        new_binary_variables = new_binary_number.get_variables()
        old_binary_variables = old_binary_number.get_variables()

        if new_binary_number.signed and old_binary_number.signed:
            for i in range(new_binary_number.n):
                if i >= old_binary_number.n:
                    self.body += " assign {} = {};\n".format(new_binary_variables[i],
                                                             old_binary_variables[old_binary_number.n - i - 1])
                else:
                    self.body += " assign {} = {};\n".format(new_binary_variables[i],
                                                             old_binary_variables[i])
        else:
            for i in range(new_binary_number.n):
                if i >= old_binary_number.n:
                    self.body += " assign {} = {};\n".format(new_binary_variables[i],
                                                             '1\'b0')
                else:
                    self.body += " assign {} = {};\n".format(new_binary_variables[i],
                                                             old_binary_variables[i])
