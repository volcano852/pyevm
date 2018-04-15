import logging
from typing import Tuple

from instructions.gas_costs import op_cost
from instructions.instruction import Instruction

logger = logging.getLogger('pyevm')


class Lt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[0] < args[1]:
            res = 1
        else:
            res = 0
        logger.info(f"{res} <= LT {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Gt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[0] > args[1]:
            res = 1
        else:
            res = 0
        logger.info(f"{res} <= GT {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Slt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Sgt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        raise NotImplementedError()

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Eq(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[0] == args[1]:
            res = 1
        else:
            res = 0
        logger.info(f"{res} <= EQ {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class IsZero(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        if args[0] == 0:
            res = 1
        else:
            res = 0
        logger.info(f"{res} <= ISZERO {args[0]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class And(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] & args[1]
        logger.info(f"{res} <= AND {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Or(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] | args[1]
        logger.info(f"{res} <= OR {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Xor(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = args[0] ^ args[1]
        logger.info(f"{res} <= XOR {args[0]} {args[1]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Not(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        res = (1 << 16) - 1 - args[0]
        logger.info(f"{res} <= NOT {args[0]}")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]


class Byte(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        n = args[0]  # 0 <= n < 32
        b = args[1]
        bit_mask = (2 ** 8 - 1) << n * 8
        res = b & bit_mask
        res = res >> n * 8
        logger.info("BYTE")
        return (res,)

    def consume_gas(self, vm):
        return op_cost["verylow"]
