from number.hexadecimal import Hexadecimal
from number.numberSystem import NumberSystem


class Integer:
    value = 0

    def __init__(self, num):
        self.value = num

    def add(self, num, exp=0, base=2, prnt=False):
        if prnt:
            print(f"(1 * {base})^{exp} + ({num})")

        self.value += num

    def get_hex(self) -> str:
        return Hexadecimal.to_hex(self.value)

    def sub(self, num):
        self.value -= num

    def __str__(self):
        return f'{self.value}'
