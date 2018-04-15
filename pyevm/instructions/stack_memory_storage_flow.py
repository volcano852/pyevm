import logging
from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Pop(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        return tuple()

    def consume_gas(self, vm):
        return op_cost["base"]


class MLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm)  -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, instructions_args):
        pass


class MStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class MStore8(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class SLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        storage_address = args[0]
        value = vm.storage[storage_address]
        logger.info(f"{value} <= SLOAD {storage_address}")
        return (value,)

    def consume_gas(self, vm):
        return op_cost["sload"]


class SStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        storage_address = args[0]
        storage_value = args[1]
        vm.storage[storage_address] = storage_value
        logger.info(f"SSTORE {storage_address}->{storage_value}")
        return tuple()

    def consume_gas(self, vm):
        return 99
        # return cost_store_storage(sigma, mu)


class Jump(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        vm.pc = args[0] - 1
        logger.info(f"JUMP {args[0]}")
        return tuple()

    def consume_gas(self, vm):
        return op_cost["mid"]


class JumpI(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[1] != 0:
            vm.pc = args[0] - 1
        return tuple()

    def consume_gas(self, vm):
        return op_cost["high"]


class Pc(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = vm.pc - 1
        logger.info(f"{res} <= PC")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["base"]


class MSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Gas(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class JumpDest(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["jumpdest"]
