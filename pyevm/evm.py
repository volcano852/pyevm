from typing import Dict, List

from instructions.instruction import Instruction


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
            self.instruction_set[operation].execute(self)
            self.pc += 1


