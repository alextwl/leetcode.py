'''
2026/10/29 daily challenge

binary indexed tree (segment tree) + lowest common ancestor (LCA) approach

learnt from official editorial:
https://leetcode.com/problems/palindromic-path-queries-in-a-tree/editorial/#approach-binary-indexed-tree--lowest-common-ancestor
'''


ASCII_A = ord('a')


class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, x, v):
        while x <= self.n:
            self.tree[x] ^= v
            x += x & -x

    def query(self, x):
        ret = 0
        while x:
            ret ^= self.tree[x]
            x -= x & -x
        return ret

    def update_range(self, l, r, v):
        self.update(l, v)
        self.update(r + 1, v)


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # build graph with bidirectional edges
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        blen = n.bit_length()
        f = [[0] * blen for _ in range(n)]

        depth = [0] * n
        left = [0] * n
        right = [0] * n
        timer = 0

        def dfs(u, parent):
            nonlocal timer
            timer += 1
            left[u] = timer
            f[u][0] = parent
            for v in g[u]:
                if v == parent:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
            right[u] = timer

        dfs(0, 0)

        for j in range(1, blen):
            for i in range(n):
                f[i][j] = f[f[i][j - 1]][j - 1]

        def lca(u, v):
            # get lowest common ancestor of u & v
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for i in range(blen):
                if (diff >> i) & 1:
                    u = f[u][i]
            if u == v:
                return u
            for i in range(blen - 1, -1, -1):
                if f[u][i] != f[v][i]:
                    u = f[u][i]
                    v = f[v][i]
            return f[u][0]

        seg = SegTree(n + 1)
        s = list(s)
        for i, c in enumerate(s):
            seg.update_range(left[i], right[i], 1 << (ord(c) - ASCII_A))

        ans = []
        for q in queries:
            op, arg0, arg1 = q.split()
            if op == "update":
                u, c = int(arg0), arg1
                seg.update_range(left[u], right[u], (1 << (ord(s[u]) - ASCII_A)) ^ (1 << (ord(c) - ASCII_A)))
                s[u] = c
            else:
                # op == "query"
                u, v = int(arg0), int(arg1)
                w = lca(u, v)
                mask = seg.query(left[u]) ^ seg.query(left[v]) ^ (1 << (ord(s[w]) - ASCII_A))
                ans.append(mask.bit_count() <= 1)

        return ans

