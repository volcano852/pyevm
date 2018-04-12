from evm import VirtualMachine, Instruction


class Sha3(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
