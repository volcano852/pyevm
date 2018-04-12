from evm import VirtualMachine, Instruction


class Lt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a < b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        print(f"{res} <= LT {a} {b}")


class Gt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a > b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        print(f"{res} <= GT {a} {b}")


class Slt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Sgt(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Eq(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if a == b:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        print(f"{res} <= EQ {a} {b}")


class IsZero(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        if a == 0:
            res = 1
        else:
            res = 0
        vm.stack.append(res)
        print(f"{res} <= ISZERO {a}")


class And(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a & b
        vm.stack.append(res)
        print(f"{res} <= AND {a} {b}")


class Or(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a | b
        vm.stack.append(res)
        print(f"{res} <= OR {a} {b}")


class Xor(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a ^ b
        vm.stack.append(res)
        print(f"{res} <= XOR {a} {b}")


class Not(Instruction):
    def __init__(self):
        super().__init__(1, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        res = (1 << 16) - 1 - a
        vm.stack.append(res)
        print(f"{res} <= NOT {a}")


class Byte(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()
