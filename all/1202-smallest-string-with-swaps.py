'''
union-find + counter approach

similar to problem 1722.
'''


import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        cnt = collections.defaultdict(lambda: collections.defaultdict(int))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a, b = find(a), find(b)
            if a > b:
                parent[a] = b
            elif b > a:
                parent[b] = a

        # group nodes by swappable pairs
        for a, b in pairs:
            union(a, b)

        for i, c in enumerate(s):
            i = find(i)
            cnt[i][c] += 1

        ans = []
        for i in range(n):
            # append the lexicographical smallest character
            # from the component of parent i.
            i = find(i)
            c = min(cnt[i].keys())
            ans.append(c)
            cnt[i][c] -= 1
            if cnt[i][c] == 0:
                del cnt[i][c]

        return ''.join(ans)

