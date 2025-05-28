'''
2025/05/28 daily challenge

level order traversal (BFS) + brute-force method approach
'''


import collections


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def bfs(g, root, max_depth):
            q = collections.deque([(root, None)])  # (node, parent)
            target_count = 0
            lv = 0
            while q:
                if lv > max_depth:
                    break
                width = len(q)
                for _ in range(width):
                    node, parent = q.popleft()
                    target_count += 1
                    for adj in g[node]:
                        if adj != parent:
                            q.append((adj, node))
                lv += 1
            return target_count
        
        def build_target_counts(edges, max_depth):
            n = len(edges) + 1
            # build graph
            g = [set() for _ in range(n)]
            for u, v in edges:
                g[u].add(v)
                g[v].add(u)
            ret = [0] * n
            # brute-force counting from all nodes as a root of a tree.
            for i in range(n):
                ret[i] = bfs(g, i, max_depth)
            return ret
        
        target1 = build_target_counts(edges1, k)
        # it costs an edge connecting from any node of tree 1.
        target2 = build_target_counts(edges2, k - 1)
        max_target2 = max(target2)
        ans = [v + max_target2 for v in target1]
        return ans

