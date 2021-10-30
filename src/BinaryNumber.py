from typing import List


class BinaryNumber:

    def __init__(self, variable_name: str, n: int, signed: bool = False):
        """
        Binary number representation of n bits.
        Bit n-1 is the MSB and bit 0 is the LSB.
        :param variable_name:
        :param n:
        :param signed:
        """
        self.variable_name = variable_name
        self.n = n
        self.signed = signed

    def get_variables(self) -> List[str]:
        return ["{}[{}]".format(self.variable_name, i) for i in range(self.n)]

    def __str__(self):
        return ", ".join(self.get_variables())
