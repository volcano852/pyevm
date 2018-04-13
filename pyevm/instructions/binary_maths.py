def twos_complement_binary_to_decimal(binary: int, number_bits: int) -> int:
    if binary < 2 ** (number_bits - 1):
        return binary
    else:
        return binary - 2 ** number_bits


def decimal_to_twos_complement_binary(decimal: int, number_bits: int) -> int:
    if 0 <= decimal < 2 ** (number_bits - 1):
        return decimal
    elif -2 ** number_bits <= decimal:
        return decimal + 2 ** number_bits
    else:
        raise RuntimeError(f"value encoding {decimal} overflows in {number_bits} bits encoding")


def get_ith_bit(value, i):
    return (2 ** i & value) // 2 ** i


def sign_extend(binary, number_bits, number_bits_extension):
    res = 0
    sign_bit = get_ith_bit(binary, number_bits - 1)
    for i in range(number_bits_extension):
        if i < number_bits:
            res += get_ith_bit(binary, i) * 2 ** i
        else:
            res += sign_bit * 2 ** i
    return res
