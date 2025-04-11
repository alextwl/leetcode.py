'''
2025/04/11 daily challenge

exhaustive method approach
'''


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for curr in range(low, high+1):
            s = str(curr)
            if len(s) & 1:
                continue
            half = len(s)>>1
            if sum(map(int, s[:half])) == sum(map(int, s[half:])):
                count += 1
        return count

