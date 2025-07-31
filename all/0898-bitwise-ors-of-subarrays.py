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


'''
brute-force two pointers + set approach

save all bitwise-ORs in a list and then convert it to a set in the end.
'''


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        left = 1
        ORs = []
        for v in arr:
            right = len(ORs)
            ORs.append(v)
            for i in range(left, right):
                w = ORs[i] | v
                if ORs[-1] != w:
                    ORs.append(w)
            left = right
        return len(set(ORs))

