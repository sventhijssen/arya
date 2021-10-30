import itertools
from abc import ABC, abstractmethod
from typing import List

from src.BinaryNumber import BinaryNumber


class Instruction(ABC):

    def __init__(self, inputs: List[BinaryNumber], outputs: List[BinaryNumber], wires: List[BinaryNumber] = None):
        self.inputs = inputs
        self.outputs = outputs
        if wires is None:
            self.wires = []
        else:
            self.wires = wires
        self.body = ""

    def get_input_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.inputs]))

    def get_output_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.outputs]))

    def get_wire_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.wires]))

    def get_header(self) -> str:
        content = "module kernel ("
        if len(self.inputs) != 0:
            content += "\n "
            content += ", ".join(self.get_input_variables())
            content += ", "
        content += "\n "
        content += ", ".join(self.get_output_variables())
        content += " );\n"
        content += "\n "
        if len(self.inputs) != 0:
            content += "input "
            content += ", ".join(self.get_input_variables())
            content += ";\n "
        content += "output "
        content += ", ".join(self.get_output_variables())
        content += ";\n "

        if len(self.wires) != 0:
            content += "wire "
            content += ", ".join(self.get_wire_variables())
            content += ";\n "

        content += "\n"
        return content

    def get_body(self) -> str:
        return self.body

    def get_footer(self) -> str:
        return "endmodule\n"

    def get_content(self) -> str:
        return self.get_header() + self.get_body() + self.get_footer()

    def write_instruction(self, file_name: str):
        with open(file_name, 'w') as f:
            f.write(self.get_content())

    @abstractmethod
    def execute(self):
        pass
