import itertools
from abc import ABC, abstractmethod
from typing import List

from src.BinaryNumber import BinaryNumber


class Arithmetic(ABC):

    def __init__(self, input_numbers: List[BinaryNumber], output_numbers: List[BinaryNumber], wire_numbers: List[BinaryNumber] = None):
        self.input_numbers = input_numbers
        self.output_numbers = output_numbers
        self.wire_numbers = wire_numbers
        self.body = ""
        self._generate()

    def get_input_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.input_numbers]))

    def get_output_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.output_numbers]))

    def get_wire_variables(self) -> List[str]:
        return list(itertools.chain(*[number.get_variables() for number in self.wire_numbers]))

    def get_header(self) -> str:
        content = "module adder ("
        content += "\n "
        content += ", ".join(self.get_input_variables())
        content += ", "
        content += "\n "
        content += ", ".join(self.get_output_variables())
        content += " );\n"
        content += "\n "
        content += "input "
        content += ", ".join(self.get_input_variables())
        content += ";\n "
        content += "output "
        content += ", ".join(self.get_output_variables())
        content += ";\n "

        if self.wire_numbers is not None:
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

    def write_verilog(self, file_name: str):
        with open(file_name, 'w') as f:
            f.write(self.get_content())

    @abstractmethod
    def _generate(self) -> str:
        pass

    @abstractmethod
    def get_output_numbers(self) -> List[BinaryNumber]:
        pass
