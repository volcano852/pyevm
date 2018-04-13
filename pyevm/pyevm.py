import sys

from evm import VirtualMachine
from instructions.instruction_set import instruction_set
import logging


def main(args):
    virtual_machine = VirtualMachine(instruction_set)
    virtual_machine.execute(bytearray.fromhex(args[0]))
    print(virtual_machine)


if __name__ == "__main__":
    logger = logging.getLogger("pyevm")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    if len(sys.argv) < 1:
        print("** pyevm: missing opcodes in hexa")
        exit(1)
    try:
        main(sys.argv[1:])
    except Exception as err:
        logger.fatal("Error!")
        # print(err.with_traceback())
        exit(1)
