'''
2024/09/03 daily challenge
'''


import functools


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ord('a') - 1  # replace 'a' with 1, **NOT ZERO**
        digits = []
        for c in s:
            d = ord(c) - a
            if d >= 10:
                digits.extend(divmod(d, 10))
            else:
                digits.append(d)

        for _ in range(k):
            digits = [int(c) for c in str(sum(digits))]

        return functools.reduce(lambda x, y: x * 10 + y, digits, 0)

