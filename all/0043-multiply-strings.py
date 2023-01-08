'''
leetcode 75 lv2 day 2

does not use any builtin conversion.
'''

ZERO = ord('0')


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        ans = 0

        # calculate the answer
        for j, op2 in enumerate(reversed(num2)):
            base2 = 10**j
            int2 = ord(op2) - ZERO
            for i, op1 in enumerate(reversed(num1)):
                base1 = 10**i
                int1 = ord(op1) - ZERO
                ans += int1 * base1 * int2 * base2

        # convert ans to str
        ansstr = ""
        while(ans):
            ans, rem = divmod(ans, 10)
            ansstr += chr(rem + ZERO)

        return ansstr[::-1]

