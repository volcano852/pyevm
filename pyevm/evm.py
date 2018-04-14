from typing import Dict, List

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
            operation = operations[self.pc]
            try:
                instruction = self.instruction_set[operation]
                instruction.execute(self)
            except KeyError as err:
                raise UnknownInstructionException(f"{instruction} does not exist in the instruction set", err)
            self.pc += 1

    def stack_pop(self) -> int:
        if len(self.stack) <= 0:
            raise StackEmptyException("Stack is empty. Cannot pop any value")

        return self.stack.pop()

    def stack_push(self, value: int):
        if len(self.stack) >= 1024:
            raise StackOverflowException(f"Maximum stack size reached {len(self.stack)}. Cannot push {value}")

        self.stack.append(value)
