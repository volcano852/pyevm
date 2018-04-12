from evm import VirtualMachine, Instruction


class Address(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Balance(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Origin(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Caller(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CallValue(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CallDataLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CallDataSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CallDataCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CodeSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class CodeCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class GasPrice(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class ExtCodeSize(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class ExtCodeCopy(Instruction):
    def __init__(self):
        super().__init__(4, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class ReturnDataSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class ReturnDataCopy(Instruction):
    def __init__(self):
        super().__init__(3, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
