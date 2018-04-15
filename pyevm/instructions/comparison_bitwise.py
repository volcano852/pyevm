import logging

from evm import VirtualMachine
from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Lt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if a < b:
            res = 1
        else:
            res = 0
        vm.stack_push(res)
        logger.info(f"{res} <= LT {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Gt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if a > b:
            res = 1
        else:
            res = 0
        vm.stack_push(res)
        logger.info(f"{res} <= GT {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Slt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Sgt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Eq(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if a == b:
            res = 1
        else:
            res = 0
        vm.stack_push(res)
        logger.info(f"{res} <= EQ {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class IsZero(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        if a == 0:
            res = 1
        else:
            res = 0
        vm.stack_push(res)
        logger.info(f"{res} <= ISZERO {a}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class And(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a & b
        vm.stack_push(res)
        logger.info(f"{res} <= AND {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Or(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a | b
        vm.stack_push(res)
        logger.info(f"{res} <= OR {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Xor(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a ^ b
        vm.stack_push(res)
        logger.info(f"{res} <= XOR {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Not(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack_pop()
        res = (1 << 16) - 1 - a
        vm.stack_push(res)
        logger.info(f"{res} <= NOT {a}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Byte(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        n = vm.stack_pop()  # 0 <= n < 32
        b = vm.stack_pop()
        bit_mask = (2 ** 8 - 1) << n * 8
        res = b & bit_mask
        res = res >> n * 8
        vm.stack_push(res)
        logger.info("BYTE")

    def consume_gas(self, vm):
        return op_cost["verylow"]
