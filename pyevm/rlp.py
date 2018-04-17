def rlp_encoding(data: bytearray) -> bytearray:
    if len(data) == 1 and data[0] < 0x80:
        return data
    elif len(data) < 56:
        res = bytearray()
        res.append(len(data) + 0x80)
        res.extend(data)
        return res
    else:
        raise NotImplementedError("Cannot encode the input data")


def int_to_big_endian(data: int) -> bytearray:
    res = bytearray()
    while data > 0:
        res.append(data & 0xff)
        data = data >> 8
    res.reverse()
    return res


def big_endian_to_int(data: bytearray) -> int:
    res = 0
    for i, number in enumerate(reversed(data)):
        res += number * (2 ** (i * 8))
    return res
