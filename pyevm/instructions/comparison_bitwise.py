from evm import VirtualMachine, Instruction
import logging

logger = logging.getLogger('pyevm')


class Lt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a < b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        logger.info(f"{res} <= LT {a} {b}")


class Gt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a > b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        logger.info(f"{res} <= GT {a} {b}")


class Slt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Sgt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Eq(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a == b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        logger.info(f"{res} <= EQ {a} {b}")


class IsZero(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        if a == 0:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        logger.info(f"{res} <= ISZERO {a}")


class And(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a & b
        vm.stack.append(res)
        logger.info(f"{res} <= AND {a} {b}")


class Or(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a | b
        vm.stack.append(res)
        logger.info(f"{res} <= OR {a} {b}")


class Xor(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a ^ b
        vm.stack.append(res)
        logger.info(f"{res} <= XOR {a} {b}")


class Not(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        res = (1 << 16) - 1 - a
        vm.stack.append(res)
        logger.info(f"{res} <= NOT {a}")


class Byte(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        n = vm.stack.pop()  # 0 <= n < 32
        b = vm.stack.pop()
        bit_mask = (2 ** 8 - 1) << n * 8
        res = b & bit_mask
        res = res >> n * 8
        vm.stack.append(res)
        logger.info("BYTE")
