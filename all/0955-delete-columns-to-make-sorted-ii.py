'''
2025/12/21 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/editorial/#solution

just check every time if strings were sorted or not after appending a column.
'''


import itertools


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        prev = [""] * len(strs)

        for cols in zip(*strs):
            curr = prev[:]
            for i, c in enumerate(cols):
                curr[i] = curr[i] + c
            
            if all(a <= b for a, b in itertools.pairwise(curr)):
                prev = curr
            else:
                # delete column
                ans += 1
        return ans

