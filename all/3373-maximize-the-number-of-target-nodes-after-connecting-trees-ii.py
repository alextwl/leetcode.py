'''
2025/05/29 daily challenge

level order traversal approach

split nodes into 2 groups of 0 & 1 by alternating current group during traversal.
since we can connect tree1 to any node of tree2,
no need to find an exact incoming node in tree 2 (we can make any node odd/non-target in tree 2),
we can just append tree2's larger group to tree1's answer.
'''


import collections


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_counts(edges):
            n = len(edges) + 1
            g = [list() for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            count = [0, 0]  # count[parity] = total number of nodes with specific parity
            node_group = [0] * n

            # BFS
            q = collections.deque([(0, None)])  # (node, parent)
            lv = 0  # == parity/group
            while q:
                width = len(q)
                count[lv] += width
                for _ in range(width):
                    node, parent = q.popleft()
                    node_group[node] = lv
                    for adj in g[node]:
                        if adj != parent:
                            q.append((adj, node))
                lv ^= 1
            return (count, node_group)
        
        count1, group1 = get_counts(edges1)
        count2, _ = get_counts(edges2)
        max_count2 = max(count2)
        ans = [count1[grp] + max_count2 for grp in group1]
        return ans

