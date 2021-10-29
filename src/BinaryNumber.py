from typing import List


class BinaryNumber:

    def __init__(self, variable_name: str, n: int, signed: bool = False):
        self.variable_name = variable_name
        self.n = n
        self.signed = signed

    def get_variables(self) -> List[str]:
        return ["{}[{}]".format(self.variable_name, i) for i in range(self.n)]

    def __str__(self):
        return ", ".join(self.get_variables())

    def to_signed(self, m: int = None):
        if m is None:
            if self.signed:
                return BinaryNumber(self.variable_name, self.n, True)
            else:
                raise Warning("Converting an unsigned integer of {} bits into a signed integer of {} bits can result "
                              "in loss of information.".format(self.n, self.n))
        else:
            if self.signed:
                if m >= self.n:
                    return BinaryNumber(self.variable_name, m, True)
                else:
                    raise Warning("Converting a signed integer of {} bits into an unsigned integer of {} bits can "
                                  "result in loss of information.".format(self.n, m))
            else:
                if m > self.n:
                    return BinaryNumber(self.variable_name, m, True)
                else:
                    raise Warning("Converting an unsigned integer of {} bits into an unsigned integer of {} bits can "
                                  "result in loss of information.".format(self.n, m))

    def to_unsigned(self, m: int = None):
        if m is None:
            return BinaryNumber(self.variable_name, self.n, False)
        else:
            if self.signed:
                if m >= self.n:
                    return BinaryNumber(self.variable_name, m, False)
                else:
                    raise Warning("Converting a signed integer of {} bits into an unsigned integer of {} bits can "
                                  "result in loss of information.".format(self.n, m))
            else:
                if m >= self.n:
                    return BinaryNumber(self.variable_name, m, False)
                else:
                    raise Warning("Converting an unsigned integer of {} bits into an unsigned integer of {} bits can "
                                  "result in loss of information.".format(self.n, m))
