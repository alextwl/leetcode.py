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


'''
oneliner ver

each match eliminates a loser.

there are 1 winner and n-1 losers,
so the number of matches is n-1.
'''

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1

