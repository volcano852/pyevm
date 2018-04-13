from evm import VirtualMachine
from instructions.instruction_set import instruction_set
from instructions.binary_maths import decimal_to_twos_complement_binary, twos_complement_binary_to_decimal


def test_simple_sum():
    # 5 + 4 == 9
    operations = bytearray([0x60, 0x05, 0x60, 0x04, 0x01])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack.pop() == 9


def test_more_complex_arithmetic():
    # (5 * 10 - 1) % 2 == 1
    operations = bytearray([0x63, 0x02, 0x01, 0x0a, 0x05, 0x02, 0x03, 0x06])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack.pop() == 1


def test_dup():
    operations = bytearray([0x62, 0x03, 0x02, 0x01, 0x82])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0x03, 0x02, 0x01, 0x03]


def test_swap():
    operations = bytearray([0x62, 0x03, 0x02, 0x01, 0x92])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0x01, 0x02, 0x03]


def test_comparisons_bitwise():
    # (2 > 1) && (3 < 4) || (10 == 10) == 1
    operations = bytearray([0x61, 0x01, 0x02, 0x11, 0x61, 0x04, 0x03, 0x10, 0x61, 0x0a, 0x0a, 0x14, 0x17, 0x16])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0x01]


def test_not():
    # not 0b00001010 == 0b11110101
    operations = bytearray([0x60, 0b00001010, 0x19])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0xfff5]


def test_storage():
    # save(1 -> 10); load(1) == 10
    operations = bytearray([0x61, 0x0a, 0x01, 0x55, 0x60, 0x01, 0x54, 0x60, 0x0a, 0x14])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0x01]
    assert vm.storage == {1: 0x0a}


def test_pc():
    operations = bytearray([0x62, 0x0a, 0x01, 0x02, 0x01, 0x01, 0x58])
    vm = VirtualMachine(instruction_set)
    vm.execute(operations)
    assert vm.stack == [0x0d, 0x05]


def test_sign_extend():
    vm = VirtualMachine(instruction_set)
    vm.stack.append(decimal_to_twos_complement_binary(-42, 8))
    vm.stack.append(8)
    vm.execute(bytearray([0x0b]))
    assert twos_complement_binary_to_decimal(vm.stack.pop(), 256) == twos_complement_binary_to_decimal(-42, 8)


def test_smod():
    vm = VirtualMachine(instruction_set)
    vm.stack.append(decimal_to_twos_complement_binary(3, 256))
    vm.stack.append(decimal_to_twos_complement_binary(-23, 256))
    vm.execute(bytearray([0x07]))
    assert twos_complement_binary_to_decimal(vm.stack.pop(), 256) == -2
