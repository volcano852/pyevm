import logging

from instructions.gas_costs import op_cost
from instructions.binary_maths import *
from instructions.instruction import Instruction, StopExecutionException

logger = logging.getLogger('pyevm')


class Stop(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm):
        raise StopExecutionException("Program halted")

    def consume_gas(self, vm):
        return op_cost["zero"]


class Add(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a + b
        vm.stack_push(res)
        logger.info(f"{res} <= ADD {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Mul(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a * b
        res = vm.stack_push(res)
        logger.info(f"{res} <= MUL {a} {b}")

    def consume_gas(self, vm):
        return op_cost["low"]


class Sub(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a - b
        vm.stack_push(res)
        logger.info(f"{res} <= SUB {a} {b}")

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Div(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if b == 0:
            res = 0
        else:
            res = a / b
        vm.stack_push(res)
        logger.info(f"{res} <= DIV {a} {b}")

    def consume_gas(self, vm):
        return op_cost["low"]


class SDiv(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["low"]


class Mod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if b == 0:
            res = 0
        else:
            res = a % b
        vm.stack_push(res)
        logger.info(f"{res} <= MOD {a} {b}")

    def consume_gas(self, vm):
        return op_cost["low"]


class SMod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        if b == 0:
            res = 0
        else:
            sign_bit = get_ith_bit(a, 255)
            res = abs(twos_complement_binary_to_decimal(a, 256)) % abs(twos_complement_binary_to_decimal(b, 256))
            if sign_bit == 1:  # negative number
                res = res * -1
        res = decimal_to_twos_complement_binary(res, 256)
        vm.stack_push(res)
        logger.info("SMOD")

    def consume_gas(self, vm):
        return op_cost["low"]


class AddMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        c = vm.stack_pop()
        if c == 0:
            res = 0
        else:
            res = (a + b) % c
        vm.stack_push(res)
        logger.info(f"{res} <= ADDMOD {a} {b} {c}")

    def consume_gas(self, vm):
        return op_cost["mid"]


class MulMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        c = vm.stack_pop()
        if c == 0:
            res = 0
        else:
            res = (a * b) % c
        vm.stack_push(res)
        logger.info(f"{res} <= MULMOD {a} {b} {c}")

    def consume_gas(self, vm):
        return op_cost["mid"]


class Exp(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        a = vm.stack_pop()
        b = vm.stack_pop()
        res = a ** b
        vm.stack_push(res)
        logger.info(f"{res} <= EXP {a} {b}")

    def consume_gas(self, vm):
        mu_s_1 = None
        if mu_s_1 == 0:
            return op_cost["exp"]
        elif mu_s_1 > 0:
            return op_cost["exp"] + (1 * op_cost["expbyte"] * (1 + math.log(mu_s_2, 256)))


class SignExtend(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm):
        number_bits = vm.stack_pop()
        binary = vm.stack_pop()
        res = sign_extend(binary, number_bits, 256)
        vm.stack_push(res)
        logger.info(f"{bin(res)[:8]}... <= SIGNEXTEND {number_bits} {binary}")

    def consume_gas(self, vm):
        return op_cost["low"]
