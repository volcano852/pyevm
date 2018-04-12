from abc import ABC, abstractmethod
from typing import Dict, List


class VirtualMachine:
    def __init__(self, instruction_set):
        self.instruction_set: Dict[int, Instruction] = instruction_set
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
            self.instruction_set[operation].execute(self)
            self.pc += 1


class Instruction(ABC):
    def __init__(self, stack_removed: int, stack_added: int):
        self.stack_removed = stack_removed
        self.stack_added = stack_added

    @abstractmethod
    def execute(self, vm: VirtualMachine):
        pass
