from typing import Dict, List, Tuple

from instructions.instruction import Instruction, UnknownInstructionException


class StackEmptyException(Exception):
    pass


class StackOverflowException(Exception):
    pass


class VirtualMachine:
    def __init__(self):
        self.instruction_set: Dict[int, Instruction] = {}
        self.gas_available: int = 0
        self.pc: int = 0
        self.memory: Dict[int, int] = {}
        self.stack: List[int] = []
        self.gas_used: int = 0
        self.operations = []
        self.storage = {}

    def execute(self, operations: bytearray):
        self.operations = operations
        while self.pc < len(self.operations):
            op_code = operations[self.pc]
            try:
                instruction = self.instruction_set[op_code]
            except KeyError as err:
                raise UnknownInstructionException(f"{instruction} does not exist in the instruction set", err)

            args = self.stack_pop(instruction.number_input)
            self.gas_used += instruction.consume_gas(args)
            ret_values = instruction.execute(args, self)
            self.stack_push(ret_values)
            self.pc += 1

    def stack_pop(self, number: int) -> Tuple[int]:
        res = []
        i = 0
        while i < number and len(self.stack) > 0:
            res.append(self.stack.pop())
            i += 1
        if i < number:
            raise StackEmptyException(f"Stack is empty. Cannot pop {number - i} remaining values")
        return tuple(res)

    def stack_push(self, values: Tuple[int]):
        vals = list(values)
        for _ in values:
            val = vals.pop()
            self.stack.append(val)
            if len(self.stack) > 1024:
                raise StackOverflowException(f"Maximum stack size reached {len(self.stack)}. Cannot push {val}")

