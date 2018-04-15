import pytest

from evm import VirtualMachine, StackOverflowException
from instructions.binary_maths import decimal_to_twos_complement_binary, twos_complement_binary_to_decimal
from instructions.instruction_set import instruction_set, StopExecutionException


@pytest.fixture
def setup_vm(scope='function'):
    vm = VirtualMachine()
    vm.instruction_set = instruction_set
    return vm


def test_simple_sum(setup_vm):
    # 5 + 4 == 9
    operations = bytearray([0x60, 0x05, 0x60, 0x04, 0x01])
    setup_vm.execute(operations)
    assert setup_vm.stack_pop(1) == (9,)


def test_more_complex_arithmetic(setup_vm):
    # (5 * 10 - 1) % 2 == 1
    operations = bytearray([0x63, 0x02, 0x01, 0x0a, 0x05, 0x02, 0x03, 0x06])
    setup_vm.execute(operations)
    assert setup_vm.stack_pop(1) == (1,)


def test_dup(setup_vm):
    operations = bytearray([0x62, 0x03, 0x02, 0x01, 0x82])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0x03, 0x02, 0x01, 0x03]


def test_swap(setup_vm):
    operations = bytearray([0x62, 0x03, 0x02, 0x01, 0x91])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0x01, 0x02, 0x03]


def test_comparisons_bitwise(setup_vm):
    # (2 > 1) && (3 < 4) || (10 == 10) == 1
    operations = bytearray([0x61, 0x01, 0x02, 0x11, 0x61, 0x04, 0x03, 0x10, 0x61, 0x0a, 0x0a, 0x14, 0x17, 0x16])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0x01]


def test_not(setup_vm):
    # not 0b00001010 == 0b11110101
    operations = bytearray([0x60, 0b00001010, 0x19])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0xfff5]


def test_storage(setup_vm):
    # save(1 -> 10); load(1) == 10
    operations = bytearray([0x61, 0x0a, 0x01, 0x55, 0x60, 0x01, 0x54, 0x60, 0x0a, 0x14])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0x01]
    assert setup_vm.storage == {1: 0x0a}


def test_pc(setup_vm):
    operations = bytearray([0x62, 0x0a, 0x01, 0x02, 0x01, 0x01, 0x58])
    setup_vm.execute(operations)
    assert setup_vm.stack == [0x0d, 0x05]


def test_sign_extend(setup_vm):
    setup_vm.stack_push((decimal_to_twos_complement_binary(-42, 8),))
    setup_vm.stack_push((8,))
    setup_vm.execute(bytearray([0x0b]))
    assert twos_complement_binary_to_decimal(setup_vm.stack_pop(1)[0], 256) == twos_complement_binary_to_decimal(-42, 8)


def test_smod(setup_vm):
    setup_vm.stack_push((decimal_to_twos_complement_binary(3, 256),))
    setup_vm.stack_push((decimal_to_twos_complement_binary(-23, 256),))
    setup_vm.execute(bytearray([0x07]))
    assert twos_complement_binary_to_decimal(setup_vm.stack_pop(1)[0], 256) == -2


def test_byte(setup_vm):
    setup_vm.stack_push((0b111111110000000011111111,))
    setup_vm.stack_push((2,))
    setup_vm.execute(bytearray([0x1a]))
    assert setup_vm.stack_pop(1)[0] == 0b11111111


def test_vm_stack_size_and_exception_raised_when_full(setup_vm):
    for i in range(1024):
        setup_vm.stack_push((i,))
    assert setup_vm
    with pytest.raises(StackOverflowException):
        setup_vm.stack_push((0xdead,))  # one too much and you are 0xdead


def test_stop_instruction(setup_vm):
    with pytest.raises(StopExecutionException):
        setup_vm.execute(bytearray([0x060, 0x05, 0x00]))
