'''
2025/09/07 daily challenge

eliminate positive values by its negative equivalents
'''


class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n // 2
        ans = [i for i in range(-half, half + 1)]
        if n & 1 == 0:
            # no need for a central zero
            ans.pop(half)
        return ans

