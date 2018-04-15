from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction
import logging


class BlockHash(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["blockhash"]


class CoinBase(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class TimeStamp(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Number(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Difficulty(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class GasLimit(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]
