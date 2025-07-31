'''
2025/07/31 daily challenge

frontier set (optimized brute-force) approach

learnt from official editorial:
https://leetcode.com/problems/bitwise-ors-of-subarrays/editorial/#solution
'''


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ORs = set()
        curr = {0}
        for v in arr:
            curr = {v | w for w in curr} | {v}
            ORs |= curr
        return len(ORs)

