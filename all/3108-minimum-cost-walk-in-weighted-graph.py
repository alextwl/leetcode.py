'''
2025/03/20 daily challenge

union find approach

since a vertex could be visited multiple times,
to obtain the minimum bitwise-AND cost
we travel all edges in the same group of s & t.
'''


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = [v for v in range(n)]
        rank = [0] * n
        ands = [131071] * n  # an all 1's bits number: (2**17 - 1) > 10**5

        def find(v):
            if uf[v] != v:
                uf[v] = find(uf[v])
            return uf[v]

        def union(a, b, w):
            a, b = find(a), find(b)
            if a == b:
                ands[a] &= w
                return
            
            if rank[a] >= rank[b]:
                uf[b] = uf[a]
                rank[a] += 1
                ands[a] &= ands[b] & w
            else:
                uf[a] = uf[b]
                rank[b] += 1
                ands[b] &= ands[a] & w

        for u, v, w in edges:
            union(u, v, w)

        ans = []
        for s, t in query:
            s, t = find(s), find(t)
            if s != t:
                ans.append(-1)
            else:
                ans.append(ands[s])
        return ans

