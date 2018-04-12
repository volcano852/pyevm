from evm import VirtualMachine, Instruction


class Pop(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class MLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class MStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class MStore8(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class SLoad(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack.pop()
        value = vm.storage[storage_address]
        vm.stack.append(value)
        print(f"{value} <= SLOAD {storage_address}")


class SStore(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        storage_address = vm.stack.pop()
        storage_value = vm.stack.pop()
        vm.storage[storage_address] = storage_value
        print(f"SSTORE {storage_address}->{storage_value}")


class Jump(Instruction):
    def __init__(self):
        super().__init__(1, 0)

    def execute(self, vm: VirtualMachine):
        res = vm.stack.pop()
        vm.pc = res - 1
        print(f"JUMP {res}")


class JumpI(Instruction):
    def __init__(self):
        super().__init__(2, 0)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b != 0:
            vm.pc = a - 1


class Pc(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        res = vm.pc - 1
        vm.stack.append(res)
        print(f"{res} <= PC")


class MSize(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Gas(Instruction):
    def __init__(self):
        super().__init__(0, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class JumpDest(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
