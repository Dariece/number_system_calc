from enum import IntEnum


class Hexadecimal(IntEnum):
    A = 10,
    B = 11,
    C = 12,
    D = 13,
    E = 14,
    F = 15,

    @staticmethod
    def to_hex(dec_num) -> str:
        """returns hex string of dec hex and empty str if not convertable"""
        ret_val = ''
        if isinstance(dec_num, int) and 16 > dec_num > -1:
            ret_val = Hexadecimal(dec_num).name if dec_num > 9 else f'{dec_num}'
        return ret_val

    @staticmethod
    def to_dec(hex_num) -> int:
        """returns dec string of hex and None if not convertable"""
        ret_val = None

        if isinstance(hex_num, str) and len(hex_num) is 1:
            parsed_hex = Hexadecimal.try_hex_to_int(hex_num)
            ret_val = Hexadecimal[parsed_hex].value if isinstance(parsed_hex, str) else parsed_hex

        return ret_val

    @staticmethod
    def try_hex_to_int(hex_num):
        try:
            return int(hex_num)
        except ValueError:
            return hex_num
