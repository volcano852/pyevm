from evm import VirtualMachine, Instruction
import logging

logger = logging.getLogger('pyevm')


class Create(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Call(Instruction):
    def __init__(self):
        super().__init__(7, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CallCode(Instruction):
    def __init__(self):
        super().__init__(7, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Return(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class DelegateCall(Instruction):
    def __init__(self):
        super().__init__(6, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class StaticCall(Instruction):
    def __init__(self):
        super().__init__(6, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Revert(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Invalid(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class SelfDestruct(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
