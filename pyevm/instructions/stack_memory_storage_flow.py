from evm import VirtualMachine
from instructions.instruction import Instruction
import logging

logger = logging.getLogger('pyevm')


class Pop(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


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


class MStore8(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class SLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack_pop()
        value = vm.storage[storage_address]
        vm.stack_push(value)
        logger.info(f"{value} <= SLOAD {storage_address}")


class SStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack_pop()
        storage_value = vm.stack_pop()
        vm.storage[storage_address] = storage_value
        logger.info(f"SSTORE {storage_address}->{storage_value}")


class Jump(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        res = vm.stack_pop()
        vm.pc = res - 1
        logger.info(f"JUMP {res}")


class JumpI(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if b != 0:
            vm.pc = a - 1


class Pc(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        res = vm.pc - 1
        vm.stack_push(res)
        logger.info(f"{res} <= PC")


class MSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Gas(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class JumpDest(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
