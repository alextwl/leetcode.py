'''
2025/11/16 daily challenge

summation formula approach
'''


class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        repeat = 0
        for c in s:
            if c == '1':
                repeat += 1
            else:
                ans = (ans + repeat * (repeat + 1) // 2) % 1_000_000_007
                repeat = 0
        if repeat:
            ans = (ans + repeat * (repeat + 1) // 2) % 1_000_000_007
        return ans

