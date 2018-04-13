from pyevm.evm import VirtualMachine, Instruction
from instructions.binary_maths import sign_extend


class Stop(Instruction):
    def __init__(self):
        super().__init__(0, 0)

    def execute(self, vm: VirtualMachine):
        raise RuntimeError("Programmed stopped")


class Add(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a + b
        vm.stack.append(res)
        print(f"{res} <= ADD {a} {b}")


class Mul(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a * b
        res = vm.stack.append(res)
        print(f"{res} <= MUL {a} {b}")


class Sub(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a - b
        vm.stack.append(res)
        print(f"{res} <= SUB {a} {b}")


class Div(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b == 0:
            res = 0
        else:
            res = a / b
        vm.stack.append(res)
        print(f"{res} <= DIV {a} {b}")


class SDiv(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class Mod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        if b == 0:
            res = 0
        else:
            res = a % b
        vm.stack.append(res)
        print(f"{res} <= MOD {a} {b}")


class SMod(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        raise NotImplementedError()


class AddMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        c = vm.stack.pop()
        if c == 0:
            res = 0
        else:
            res = (a + b) % c
        vm.stack.append(res)
        print(f"{res} <= ADDMOD {a} {b} {c}")


class MulMod(Instruction):
    def __init__(self):
        super().__init__(3, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        c = vm.stack.pop()
        if c == 0:
            res = 0
        else:
            res = (a * b) % c
        vm.stack.append(res)
        print(f"{res} <= MULMOD {a} {b} {c}")


class Exp(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        a = vm.stack.pop()
        b = vm.stack.pop()
        res = a ** b
        vm.stack.append(res)
        print(f"{res} <= EXP {a} {b}")


class SignExtend(Instruction):
    def __init__(self):
        super().__init__(2, 1)

    def execute(self, vm: VirtualMachine):
        number_bits = vm.stack.pop()
        binary = vm.stack.pop()
        res = sign_extend(binary, number_bits, 256)
        vm.stack.append(res)
        print(f"{bin(res)[:8]}... <= SIGNEXTEND {number_bits} {binary}")
