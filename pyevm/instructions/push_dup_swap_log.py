import logging
from typing import Tuple, List

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Push(Instruction):
    def __init__(self, count):
        super().__init__(0, 1)
        self.count = count

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        values: List[int] = []
        for i in range(self.count):
            vm.pc += 1
            value = vm.operations[vm.pc]
            values.append(value)

        logger.info(f"PUSH{self.count} {values}")
        return tuple(reversed(values))

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Dup(Instruction):
    def __init__(self, count):
        super().__init__(count, count + 1)
        self.count = count

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        dup_value = args[-1]
        logger.info(f"{dup_value} <= DUP{self.count}")
        values = [dup_value]
        values.extend(args)
        return tuple(values)

    def consume_gas(self, vm):
        return op_cost["verylow"]


# TODO: Refactoring and make sure this works now that we pop out the values before going into execute
class Swap(Instruction):
    def __init__(self, count):
        super().__init__(count + 1, count + 1)
        self.count = count

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        vals = list(args)
        swap_value = vals[0]
        vals[0] = vals[-1]
        vals[-1] = swap_value
        logger.info(f"{vals[0],vals[-1]} <= SWAP{self.count}")
        return tuple(vals)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Log(Instruction):
    def __init__(self, count):
        super().__init__(count + 2, 0)
        self.count = count

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        cost = op_cost["log"]
        for i in range(self.count):
            cost += op_cost["logtopic"]
