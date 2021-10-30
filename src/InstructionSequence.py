from typing import List

from src.BinaryNumber import BinaryNumber
from src.Instruction import Instruction


class InstructionSequence(Instruction):

    def __init__(self, inputs: List[BinaryNumber], outputs: List[BinaryNumber], instructions: List[Instruction],
                 wires: List[BinaryNumber] = None):
        super().__init__(inputs, outputs, wires)
        self.inputs = inputs
        self.outputs = outputs
        self.instructions = instructions

    def execute(self):
        for instruction in self.instructions:
            instruction.execute()
            self.body += instruction.get_body()
