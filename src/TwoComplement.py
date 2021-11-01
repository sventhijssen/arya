from Add import Add
from Instruction import Instruction
from BinaryNumber import BinaryNumber
from OneComplement import OneComplement


class TwoComplement(Instruction):

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

    def execute(self):
        n = self.inputs[0].n

        # Step 1: One complement
        one_complement = OneComplement(self.inputs[0], self.wires[0])
        one_complement.execute()
        self.body += one_complement.get_body()

        # Step 2: Addition of one complement and one
        add = Add([self.wires[0], self.one_constant], self.outputs[0], self.carry_number)
        add.execute()
        self.body += add.get_body()
