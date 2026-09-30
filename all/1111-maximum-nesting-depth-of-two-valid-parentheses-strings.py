'''
2026/09/30 daily challenge

depth tracking (single variable stack) approach

parentheses with odd depth go to the group of A.
'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []
        for c in seq:
            if c == '(':
                depth += 1
            ans.append(depth & 1)
            if c == ')':
                depth -= 1
        return ans

