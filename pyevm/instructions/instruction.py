from abc import ABC, abstractmethod
from typing import Tuple


class Instruction(ABC):
    def __init__(self, number_input: int, number_output: int):
        self.number_input = number_input
        self.number_output = number_output

    @abstractmethod
    def execute(self, args: Tuple[int], vm) -> Tuple[int]:
        pass

    @abstractmethod
    def consume_gas(self, instructions_args) -> int:
        pass


class StopExecutionException(Exception):
    pass


class UnknownInstructionException(Exception):
    pass
