import logging
from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Address(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Balance(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["balance"]


class Origin(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Caller(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class CallValue(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class CallDataLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class CallDataSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class CallDataCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"] + op_cost["copy"] * (mu_s_2 / 32)


class CodeSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class CodeCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"] + op_cost["copy"] * (mu_s_2 / 32)


class GasPrice(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class ExtCodeSize(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["extcode"]


class ExtCodeCopy(Instruction):
    def __init__(self):
        super().__init__(4, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        op_cost["extcode"] + op_cost["copy"] * (mu_s_3 / 32)


class ReturnDataSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class ReturnDataCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"] + op_cost["copy"] * (mu_s_2 / 32)
