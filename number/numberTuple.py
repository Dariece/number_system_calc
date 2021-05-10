from number.numberConverter import NumberConverter, DecimalConverter, BinaryConverter, HexadecimalConverter, OctalNumber
from number.numberSystem import NumberSystem


class NumberTuple:
    decimal_number = 0
    binary_number = ''
    hexadecimal_number = ''
    octal_number = ''

    def __init__(self, num, system=NumberSystem.DECIMAL):
        converter = NumberConverter(num)

        if system == NumberSystem.DECIMAL:
            converter = DecimalConverter(num)
        if system == NumberSystem.BINARY:
            converter = BinaryConverter(num)
        if system == NumberSystem.HEXADECIMAL:
            converter = HexadecimalConverter(num)
        # if system == NumberSystem.OCTAL:
        #     converter = OctalNumber(num)

        self.decimal_number = converter.to_dec(prnt=True)
        self.binary_number = converter.to_bin(prnt=True)
        self.hexadecimal_number = converter.to_hex(prnt=True)
        # self.octal_number = converter.to_oct(prnt=True)

    def __str__(self):
        return f"""dec: {self.decimal_number}
bin: {self.binary_number}
hex: {self.hexadecimal_number}
oct: {self.octal_number}"""
