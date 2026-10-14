'''
2026/10/14 daily challenge

greedy method approach

always make larger digit first.
'''


class Solution:
    def maxSumOfSquares(self, num: int, target_sum: int) -> str:
        if target_sum > num * 9:
            # exceeded the maximum possible sum
            return ""
        quo, rem = divmod(target_sum, 9)
        digits = "9" * quo  # fill floor(sum/9) nines first
        if rem:
            digits += str(rem)
        return digits + "0" * (num - len(digits))

