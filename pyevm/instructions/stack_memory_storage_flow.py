import logging

from evm import VirtualMachine
from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Pop(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class MLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class MStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class MStore8(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class SLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack_pop()
        value = vm.storage[storage_address]
        vm.stack_push(value)
        logger.info(f"{value} <= SLOAD {storage_address}")

    def consume_gas(self, vm):
        return op_cost["sload"]


class SStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack_pop()
        storage_value = vm.stack_pop()
        vm.storage[storage_address] = storage_value
        logger.info(f"SSTORE {storage_address}->{storage_value}")

    def consume_gas(self, vm):
        return cost_store_storage(sigma, mu)


class Jump(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        res = vm.stack_pop()
        vm.pc = res - 1
        logger.info(f"JUMP {res}")

    def consume_gas(self, vm):
        return op_cost["mid"]


class JumpI(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if b != 0:
            vm.pc = a - 1

    def consume_gas(self, vm):
        return op_cost["high"]


class Pc(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        res = vm.pc - 1
        vm.stack_push(res)
        logger.info(f"{res} <= PC")

    def consume_gas(self, vm):
        return op_cost["base"]


class MSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class Gas(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["base"]


class JumpDest(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["jumpdest"]
