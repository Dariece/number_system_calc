from number.numberSystem import NumberSystem
from number.numberTuple import NumberTuple


def print_number_calculation(num, system=NumberSystem.DECIMAL):
    print(f'---Calculate {system.name.lower()}---')
    print(NumberTuple(num, system))


def testTuple():
    print_number_calculation(236)
    print_number_calculation('11101001', NumberSystem.BINARY)
    print_number_calculation('E6A1', NumberSystem.HEXADECIMAL)
