import logging
from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Sha3(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["sha3"] + op_cost["sha3word"] * (s_1 / 32)
