'''
2025/09/16 daily challenge

stack approach
'''


import math


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        it = iter(nums)
        stack = [next(it)]

        for v in it:
            while v > 1 and stack and stack[-1] > 1 and math.gcd(stack[-1], v) > 1:
                v = math.lcm(stack[-1], v)
                stack.pop()
            stack.append(v)

        return stack

