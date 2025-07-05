'''
rank-based union find approach

runtime=319ms, beats 5.07%
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = dict()
        rank = dict()

        def find(v):
            if uf.setdefault(v, v) != v:
                uf[v] = find(uf[v])
            return uf[v]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if rank.setdefault(a, 1) > rank.setdefault(b, 1):
                rank[a] += rank[b]
                uf[b] = a
            else:
                rank[b] += rank[a]
                uf[a] = b

        for x1 in nums:
            x0, x2 = x1 - 1, x1 + 1
            find(x1)
            rank.setdefault(x1, 1)
            if x0 >= -1_000_000_000 and x0 in uf:
                union(x0, x1)
            if x2 <= 1_000_000_000 and x2 in uf:
                union(x1, x2)

        return max(rank.values())

