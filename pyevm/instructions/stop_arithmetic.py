import logging

from instructions.binary_maths import *
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Stop(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm):
        raise RuntimeError("Programmed stopped")


class Add(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a + b
        vm.stack.append(res)
        logger.info(f"{res} <= ADD {a} {b}")


class Mul(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a * b
        res = vm.stack.append(res)
        logger.info(f"{res} <= MUL {a} {b}")


class Sub(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a - b
        vm.stack.append(res)
        logger.info(f"{res} <= SUB {a} {b}")


class Div(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b == 0:
            res = 0
        else:
            res = a / b
        vm.stack.append(res)
        logger.info(f"{res} <= DIV {a} {b}")


class SDiv(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        raise NotImplementedError()


class Mod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b == 0:
            res = 0
        else:
            res = a % b
        vm.stack.append(res)
        logger.info(f"{res} <= MOD {a} {b}")


class SMod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b == 0:
            res = 0
        else:
            sign_bit = get_ith_bit(a, 255)
            res = abs(twos_complement_binary_to_decimal(a, 256)) % abs(twos_complement_binary_to_decimal(b, 256))
            if sign_bit == 1:  # negative number
                res = res * -1
        res = decimal_to_twos_complement_binary(res, 256)
        vm.stack.append(res)
        logger.info("SMOD")


class AddMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        c = vm.stack.pop()
        if c == 0:
            res = 0
        else:
            res = (a + b) % c
        vm.stack.append(res)
        logger.info(f"{res} <= ADDMOD {a} {b} {c}")


class MulMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        c = vm.stack.pop()
        if c == 0:
            res = 0
        else:
            res = (a * b) % c
        vm.stack.append(res)
        logger.info(f"{res} <= MULMOD {a} {b} {c}")


class Exp(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a ** b
        vm.stack.append(res)
        logger.info(f"{res} <= EXP {a} {b}")


class SignExtend(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        number_bits = vm.stack.pop()
        binary = vm.stack.pop()
        res = sign_extend(binary, number_bits, 256)
        vm.stack.append(res)
        logger.info(f"{bin(res)[:8]}... <= SIGNEXTEND {number_bits} {binary}")
