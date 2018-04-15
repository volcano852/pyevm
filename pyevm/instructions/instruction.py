from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__(self, stack_removed: int, stack_added: int):
        self.stack_removed = stack_removed
        self.stack_added = stack_added

    @abstractmethod
    def execute(self, vm):
        pass

    @abstractmethod
    def consume_gas(self, vm):
        pass
