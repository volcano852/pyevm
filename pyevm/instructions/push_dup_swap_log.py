import logging

from evm import VirtualMachine
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Push(Instruction):
    def __init__(self, count):
        super().__init__(0, 1)
        self.count = count

    def execute(self, vm: VirtualMachine):
        values = []
        for i in range(self.count):
            vm.pc += 1
            value = vm.operations[vm.pc]
            vm.stack_push(value)
            values.append(value)

        logger.info(f"PUSH{self.count} {values}")


class Dup(Instruction):
    def __init__(self, count):
        super().__init__(count, count + 1)
        self.count = count

    def execute(self, vm: VirtualMachine):
        values = []
        for i in range(self.count):
            values.append(vm.stack_pop())

        dup_value = values[-1]

        while values:
            vm.stack_push(values.pop())
        vm.stack_push(dup_value)
        logger.info(f"{dup_value} <= DUP{self.count}")


class Swap(Instruction):
    def __init__(self, count):
        super().__init__(count + 1, count + 1)
        self.count = count

    def execute(self, vm: VirtualMachine):
        swap_value1 = vm.stack_pop()
        values = []
        for i in range(self.count - 1):
            values.append(vm.stack_pop())

        swap_value2 = values.pop()
        vm.stack_push(swap_value1)

        while values:
            vm.stack_push(values.pop())
        vm.stack_push(swap_value2)
        logger.info(f"{swap_value1,swap_value2} <= SWAP{self.count}")


class Log(Instruction):
    def __init__(self, count):
        super().__init__(count + 2, 0)
        self.count = count

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
