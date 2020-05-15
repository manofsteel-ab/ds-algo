import math
from typing import List


class Solution:

    def applyOperands(self, val_1, val_2, operand):
        if operand == '+':
            return val_1 + val_2
        if operand == '-':
            return val_1 - val_2
        if operand == '*':
            return val_1 * val_2
        if operand == '/':
            res = val_1 / (val_2)
            if res < 0:
                return math.ceil(res)
            return math.floor(res)

    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['*', '+', '-', '/']

        ans = 0

        stack = []

        tokens_sz = len(tokens)

        index = 0

        while index < tokens_sz:
            if tokens[index] not in operands:
                stack.append(int(tokens[index]))
            else:
                element2 = stack.pop()
                element1 = stack.pop()
                res = self.applyOperands(element1, element2, tokens[index])
                stack.append(res)
            index += 1
        return stack.pop()

