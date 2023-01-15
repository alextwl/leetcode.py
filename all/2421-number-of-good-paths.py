'''
2023/01/15 daily challenge

union-find approach
learnt from official solution

note solving it by DFS/BFS will exceed the time limit.
'''

import collections


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        # Union-Find functions
        uf = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}  # priority of union parents

        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return

            if rank[px] < rank[py]:
                uf[px] = py
            elif rank[px] > rank[py]:
                uf[py] = px
            else:
                uf[py] = px
                '''
                let px be the common parent and increase its priority when px & py have the same priority.
                '''
                rank[px] += 1

        # build the tree
        vertices = [set() for _ in range(n)]  # node <-> node
        for v1, v2 in edges:
            vertices[v1].add(v2)
            vertices[v2].add(v1)

        val2nodes = collections.defaultdict(set)  # val -> node
        for i, val in enumerate(vals):
            val2nodes[val].add(i)

        '''
        while the definition of good path requires
        all node values in a path are not greater than start/end nodes,
        we iterate from the smallest value of nodes as a path's start/end nodes.
        '''
        ans = 0
        for val in sorted(val2nodes.keys()):
            nodes = val2nodes[val]
            for v in nodes:
                '''
                find if adjacent nodes could be added into a path or not.

                use Union-Find structure to group these nodes.
                '''
                for adj in vertices[v]:
                    if val >= vals[adj]:
                        union(v, adj)

            '''
            if there're different groups, that means
            although the specific value was assigned to multiple nodes as start/end nodes,
            these nodes cannot travel to each other in all pairs because of the good path requirement
            and they are grouped by disjoint subtrees.
            '''
            group = collections.defaultdict(int)
            for v in nodes:
                # calculate the group size
                group[find(v)] += 1

            '''
            in a group of nodes as start/end nodes,
            the number of pathes is:

            (n * (n+1))
            -----------
                 2

            and btw for all intermediate nodes in the group,
            because its values are smaller than the start/end nodes,
            all pathes consisted of one of them were counted
            in the previous round of group (with smaller start/end node values).
            '''
            for subtree_size in group.values():
                ans += (subtree_size * (subtree_size+1)) // 2

        return ans

