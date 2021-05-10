#!/usr/bin/env python

from number import testNumberTuple
from number.hexadecimal import Hexadecimal
from number.numberSystem import NumberSystem


def main():
    try:
        while True:
            exit = 'exit'
            print("||Number Calculator||")
            args = input(
                '   Zahlensysteme: [decimal, hexadecimal, binary]\n'  
                '   Beispiel 123 decimal\n'
                '   Exit zum beenden\n'
                'Bitte Zahl und Zahlensystem eingeben: (zahl zahlensystem)') \
                .split(' ')
            if any(x.lower() == exit for x in args):
                return 0

            num = args[0]
            system = NumberSystem[args[1].upper()]
            if system is NumberSystem.DECIMAL:
                num = Hexadecimal.try_hex_to_int(num)
            testNumberTuple.print_number_calculation(num, system)
    except IndexError:
        print('--> Zu wenig Argumente, bitte versuchen Sie es noch einmal.\n')
        main()

    except Exception as e:
        print('Error occurred:', e)
        return 1


if __name__ == '__main__':
    main()
