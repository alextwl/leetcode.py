'''
2023/12/05 daily challenge

simulation approach
'''

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0

        while (n > 1):
            ans += (n&1) + (n>>1)
            n >>= 1

        return ans

