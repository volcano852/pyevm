import logging
from typing import Tuple

from instructions.binary_maths import *
from instructions.gas_costs import op_cost
from instructions.instruction import Instruction, StopExecutionException

logger = logging.getLogger('pyevm')


class Stop(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise StopExecutionException("Program halted")

    def consume_gas(self, vm):
        return op_cost["zero"]


class Add(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] + args[1]
        logger.info(f"{res} <= ADD {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Mul(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] * args[1]
        logger.info(f"{res} <= MUL {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["low"]


class Sub(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] - args[1]
        logger.info(f"{res} <= SUB {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Div(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[1] == 0:
            res = 0
        else:
            res = args[0] / args[1]
        logger.info(f"{res} <= DIV {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["low"]


class SDiv(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["low"]


class Mod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[1] == 0:
            res = 0
        else:
            res = args[0] % args[1]
        logger.info(f"{res} <= MOD {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["low"]


class SMod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[1] == 0:
            res = 0
        else:
            sign_bit = get_ith_bit(args[0], 255)
            res = abs(twos_complement_binary_to_decimal(args[0], 256)) % abs(
                twos_complement_binary_to_decimal(args[1], 256))
            if sign_bit == 1:  # negative number
                res = res * -1
        res = decimal_to_twos_complement_binary(res, 256)
        logger.info("SMOD")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["low"]


class AddMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[2] == 0:
            res = 0
        else:
            res = (args[0] + args[1]) % args[2]

        logger.info(f"{res} <= ADDMOD {args[0]} {args[1]} {args[2]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["mid"]


class MulMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[2] == 0:
            res = 0
        else:
            res = (args[0] * args[1]) % args[2]
        logger.info(f"{res} <= MULMOD {args[0]} {args[1]} {args[2]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["mid"]


class Exp(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] ** args[1]
        logger.info(f"{res} <= EXP {a} {b}")
        return (res,)

    def consume_gas(self, vm):
        mu_s_1 = None
        if mu_s_1 == 0:
            return op_cost["exp"]
        elif mu_s_1 > 0:
            return op_cost["exp"] + (1 * op_cost["expbyte"] * (1 + math.log(mu_s_2, 256)))


class SignExtend(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        number_bits = args[0]
        binary = args[1]
        res = sign_extend(binary, number_bits, 256)
        logger.info(f"{bin(res)[:8]}... <= SIGNEXTEND {number_bits} {binary}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["low"]
