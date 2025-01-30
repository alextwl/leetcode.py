'''
2025/01/30 daily challenge

Union find + level order traversal approach

learnt from official editorial 2:
https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/editorial/#approach-2-bfs--union-find
'''


import collections


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [list() for _ in range(n)]
        uf = list(range(n))
        rank = [1] * n

        def find(v):
            if uf[v] != v:
                uf[v] = find(uf[v])
            return uf[v]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if rank[a] > rank[b]:
                a, b = b, a
            uf[a] = b
            rank[b] += rank[a]

        def get_group_size(src):
            q = collections.deque()
            layer_seen = [-1] * n
            q.append(src)
            layer_seen[src] = 0

            lv = 0
            # level order BFS
            while q:
                width = len(q)
                for _ in range(width):
                    node = q.popleft()
                    for adj in g[node]:
                        if layer_seen[adj] == -1:
                            layer_seen[adj] = lv + 1
                            q.append(adj)
                        elif layer_seen[adj] == lv:
                            # invalid partition
                            return -1
                lv += 1
            return lv

        for a, b in edges:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
            union(a, b)

        component_group_size = collections.defaultdict(int)
        for src in range(n):
            size = get_group_size(src)
            if size == -1:
                return -1
            root = find(src)
            component_group_size[root] = max(component_group_size[root], size)

        return sum(component_group_size.values())

