'''
2026/07/25 daily challenge

the product of top-1 & top-2 digits approach
'''


class Solution:
    def maxProduct(self, n: int) -> int:
        top1 = top2 = 0
        while n:
            n, digit = divmod(n, 10)
            if digit > top1:
                top1, top2 = digit, top1
            elif digit > top2:
                top2 = digit
        return top1 * top2

