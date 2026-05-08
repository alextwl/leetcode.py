'''
2026/05/08 daily challenge

breadth first search approach (reversed)

learnt from official editorial 1:
https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/editorial/#approach-1-reversed-breadth-first-search

prebuild factor lookup table, and reverse possible jumps.

similar to a converted level order problem.
'''


import collections


MAX_VAL = 1_000_001
# build factors lookup table
FACTORS = [[] for _ in range(MAX_VAL)]
for i in range(2, MAX_VAL):
    if not FACTORS[i]:
        for j in range(i, MAX_VAL, i):
            FACTORS[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = collections.defaultdict(list)
        for i, v in enumerate(nums):
            if len(FACTORS[v]) == 1:
                # it's a prime
                edges[v].append(i)

        # BFS
        seen = [False] * n
        seen[-1] = True
        ans = 0
        q0 = [n - 1]  # search from terminal
        while True:
            q1 = []
            for i in q0:
                if i == 0:
                    # reached the starting point
                    return ans
                # reversed adjacent movement
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q1.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q1.append(i + 1)
                # reversed jumps
                for p in FACTORS[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q1.append(j)
                    edges[p] = []
            q0 = q1
            ans += 1

        return -1  # undefined behavior

