import math

from instructions.block_info import *
from instructions.comparison_bitwise import *
from instructions.environmental import *
from instructions.instruction import UnknownInstructionException
from instructions.push_dup_swap_log import *
from instructions.sha_op import Sha3
from instructions.stack_memory_storage_flow import *
from instructions.stop_arithmetic import *
from instructions.system_ops import *

op_cost = {"zero": 0,
           "base": 2,
           "verylow": 3,
           "low": 5,
           "mid": 8,
           "high": 10,
           "extcode": 700,
           "balance": 400,
           "sload": 200,
           "jumpdest": 1,
           "sset": 20000,
           "sreset": 5000,
           "refund_sclear": 15000,
           "refund_sdestruct": 24000,
           "create": 32000,
           "codedeposit": 200,
           "call": 700,
           "callvalue": 9000,
           "callstipend": 2300,
           "newaccount": 25000,
           "exp": 10,
           "expbyte": 50,
           "memory": 3,
           "txcreate": 32000,
           "txdatazero": 4,
           "txdatanonzero": 68,
           "transaction": 21000,
           "log": 375,
           "logdata": 8,
           "logtopic": 375,
           "sha3": 30,
           "sha3word": 6,
           "copy": 3,
           "blockhash": 20,
           "quaddivisor": 100}


def cost_store_storage(sigma, mu) -> int:
    pass


def cost_call(sigma, mu) -> int:
    pass


def cost_self_destruct(sigma, mu) -> int:
    pass


def gas_cost(op: Instruction) -> int:
    mu_s_1 = 10
    mu_s_2 = 20
    mu_s_3 = 30
    s_1 = 10
    sigma = None
    mu = None

    if isinstance(op, SStore):
        return cost_store_storage(sigma, mu)
    elif isinstance(op, Exp):
        if mu_s_1 == 0:
            return op_cost["exp"]
        elif mu_s_1 > 0:
            return op_cost["exp"] + (1 * op_cost["expbyte"] * (1 + math.log(mu_s_2, 256)))
    elif isinstance(op, (CallDataCopy, CodeCopy, ReturnDataCopy)):
        return op_cost["verylow"] + op_cost["copy"] * (mu_s_2 / 32)
    elif isinstance(op, ExtCodeCopy):
        op_cost["extcode"] + op_cost["copy"] * (mu_s_3 / 32)
    elif isinstance(op, Log):
        cost = op_cost["log"]
        for i in range(op.count):
            cost += op_cost["logtopic"]
    elif isinstance(op, (Call, CallCode, DelegateCall)):
        return cost_call(sigma, mu)
    elif isinstance(op, SelfDestruct):
        return cost_self_destruct(sigma, mu)
    elif isinstance(op, Create):
        return op_cost["create"]
    elif isinstance(op, Sha3):
        return op_cost["sha3"] + op_cost["sha3word"] * (s_1 / 32)
    elif isinstance(op, JumpDest):
        return op_cost["jumpdest"]
    elif isinstance(op, SLoad):
        return op_cost["sload"]
    elif isinstance(op, (Stop, Return, Revert)):
        return op_cost["zero"]
    elif isinstance(op, (Address, Origin, Caller, CallValue, CallDataSize, CodeSize, GasPrice,
                         CoinBase, TimeStamp, Number, Difficulty, GasLimit, ReturnDataSize, Pop, Pc,
                         MSize, Gas)):
        return op_cost["base"]
    elif isinstance(op, (Add, Sub, Not, Lt, Gt, Slt, Sgt, Eq, IsZero, And, Or, Xor, Byte, CallDataLoad, MLoad, MStore,
                         MStore8, Push, Dup, Swap)):
        return op_cost["verylow"]
    elif isinstance(op, (Mul, Div, SDiv, Mod, SMod, SignExtend)):
        return op_cost["low"]
    elif isinstance(op, (AddMod, MulMod, Jump)):
        return op_cost["mid"]
    elif isinstance(op, JumpI):
        return op_cost["high"]
    elif isinstance(op, ExtCodeSize):
        return op_cost["extcode"]
    elif isinstance(op, Balance):
        return op_cost["balance"]
    elif isinstance(op, BlockHash):
        return op_cost["blockhash"]
    else:
        raise UnknownInstructionException(f"{instruction} does not exist in the instruction set")
