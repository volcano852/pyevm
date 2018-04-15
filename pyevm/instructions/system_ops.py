import logging
from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Create(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["create"]


class Call(Instruction):
    def __init__(self):
        super().__init__(7, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return cost_call(sigma, mu)


class CallCode(Instruction):
    def __init__(self):
        super().__init__(7, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return cost_call(sigma, mu)


class Return(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["zero"]


class DelegateCall(Instruction):
    def __init__(self):
        super().__init__(6, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return cost_call(sigma, mu)


class StaticCall(Instruction):
    def __init__(self):
        super().__init__(6, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()


class Revert(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["zero"]


class Invalid(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()


class SelfDestruct(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return cost_self_destruct(sigma, mu)
