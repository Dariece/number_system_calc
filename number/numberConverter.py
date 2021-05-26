from number.hexadecimal import Hexadecimal
from number.integer import Integer
from number.numberSystem import NumberSystem


class NumberConverter:
    num = None
    system = NumberSystem.BINARY

    def __init__(self, num):
        self.num = num

    def to_dec(self, num=None, prnt=False) -> int:
        """Convert num to decimal number"""
        pass

    def to_bin(self, num=None, prnt=False) -> str:
        """Convert num to binary number"""
        pass

    def to_hex(self, num=None, prnt=False) -> str:
        """Convert num to hexadecimal number"""
        pass

    def to_oct(self, num=None, prnt=False) -> str:
        """Convert num to octal number"""
        pass


class BinaryConverter(NumberConverter):
    system = NumberSystem.BINARY

    def __init__(self, num):
        if isinstance(num, str) and all([x in ('0', '1') for x in num]):
            super().__init__(num)
        else:
            raise ValueError(f'Input no {self.system.name.lower()} number')

    def convert(self, num=None, prnt=False, system=NumberSystem.BINARY):
        if prnt:
            print(f'Convert {self.system.name.lower()} to {system.name.lower()} number')
        return self.num if num is None else num

    @staticmethod
    def get_exponent(i, num) -> int:
        return len(num) - i - 1

    def convert_dec(self, num, prnt=False) -> Integer:
        ret_val = Integer(0)

        [ret_val.add(int(x) * 2 ** self.get_exponent(i, num),
                     self.get_exponent(i, num), prnt=prnt)
         if int(x) is not 0 else 0
         for i, x in enumerate(num)]

        return ret_val

    def to_bin(self, num=None, prnt=False) -> str:
        return self.convert(num, prnt)

    def to_dec(self, num=None, prnt=False) -> int:
        num = self.convert(num, prnt, NumberSystem.DECIMAL)
        return self.convert_dec(num, prnt=prnt).value

    def to_hex(self, num=None, prnt=False) -> str:
        num = self.convert(num, prnt, NumberSystem.HEXADECIMAL)

        ret_val = ''
        quarter = ''
        quarter_length = 4

        if num is None:
            num = self.num

        for i, digit in enumerate(num):
            quarter += digit

            if len(quarter) is quarter_length or i is len(num) - 1:
                quarter = quarter.zfill(quarter_length)
                integer = self.convert_dec(quarter, prnt=prnt)
                ret_val = f'{ret_val}{integer.get_hex()}'
                quarter = ''

        return ret_val

    def to_oct(self, num=None, prnt=False) -> str:
        dec_num = self.to_dec(num, prnt=prnt)
        dec_converter = DecimalConverter(dec_num)
        return dec_converter.to_oct(prnt=prnt)


class OctalNumber(NumberConverter):
    system = NumberSystem.OCTAL

    def __init__(self, num):
        if isinstance(num, int):
            super().__init__(num)
        else:
            raise ValueError(f'Input {num} no {self.system.name.lower()} number')


class DecimalConverter(NumberConverter):
    system = NumberSystem.DECIMAL

    def __init__(self, num):
        if isinstance(num, int):
            super().__init__(num)
        else:
            raise ValueError(f'Input {num} no {self.system.name.lower()} number')

    def convert(self, num=None, prnt=False, system=NumberSystem.BINARY):
        divisor = system.value

        if prnt:
            print(f'Convert {self.system.name.lower()} to {system.name.lower()} number')

        ret_val = ''

        if num is None:
            num = self.num

        tmp_num = num

        if num != 0:
            while tmp_num is not 0:
                message = f'{tmp_num:5} / {divisor:2} ='
                rest = tmp_num % divisor
                if system is NumberSystem.HEXADECIMAL:
                    rest = Hexadecimal.to_hex(rest)
                tmp_num = tmp_num // divisor
                ret_val = f'{rest}{ret_val}'
                message = f'{message} {tmp_num:5} R {rest}'

                if prnt:
                    print(message)
        else:
            ret_val = '0'

        if system is NumberSystem.BINARY:
            assert ret_val == bin(num).split(sep='b')[1]
        elif system is NumberSystem.OCTAL:
            assert ret_val == oct(num).split(sep='o')[1]
        else:
            assert ret_val == hex(num).split(sep='x')[1].upper()

        return ret_val

    def to_bin(self, num=None, prnt=False) -> str:
        return self.convert(num, prnt)

    def to_oct(self, num=None, prnt=False) -> str:
        return self.convert(num, prnt, NumberSystem.OCTAL)

    def to_dec(self, num=None, prnt=False) -> int:
        return self.num if num is None else num

    def to_hex(self, num=None, prnt=False) -> str:
        return self.convert(num, prnt, NumberSystem.HEXADECIMAL)


class HexadecimalConverter(NumberConverter):
    system = NumberSystem.HEXADECIMAL

    def __init__(self, num):
        if isinstance(num, str):
            super().__init__(num)
        else:
            raise ValueError(f'Input no {self.system.name.lower()} number')

    def convert(self, num=None, prnt=False, system=NumberSystem.BINARY):
        if prnt:
            print(f'Convert {self.system.name.lower()} to {system.name.lower()} number')
        return self.num if num is None else num

    def to_hex(self, num=None, prnt=False) -> str:
        return self.convert(prnt=prnt, system=self.system)

    def to_bin(self, num=None, prnt=False) -> str:
        num = self.convert(num, prnt)
        if prnt:
            print('-Convert quarters:')
        ret_val = ''.join(DecimalConverter(Hexadecimal.to_dec(x)).to_bin(prnt=prnt).zfill(4) for x in num)
        return ret_val

    def to_dec(self, num=None, prnt=False) -> int:
        ret_val = Integer(0)
        num = self.convert(num, prnt, system=NumberSystem.DECIMAL)
        base = 16
        [ret_val.add_hex(Hexadecimal.to_dec(x) * base ** BinaryConverter.get_exponent(i, num),
                         exp=BinaryConverter.get_exponent(i, num),
                         base=base,
                         multiplicator=Hexadecimal.to_dec(x),
                         prnt=prnt)
         for i, x in enumerate(num)]
        return ret_val.value

    def to_oct(self, num=None, prnt=False) -> str:
        dec_num = self.to_dec(num, prnt=prnt)
        dec_converter = DecimalConverter(dec_num)
        return dec_converter.to_oct(prnt=prnt)
