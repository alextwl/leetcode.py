'''
2024/07/21 daily challenge

Kahn's algorithm + topology sort approach

learnt from official solution 2:
https://leetcode.com/problems/build-a-matrix-with-conditions/solution/
'''


import collections


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topology_sort(edges, n):
            adj = [[] for _ in range(n+1)]
            indegree = [0] * (n+1)
            order = []
            
            for a, b in edges:
                adj[a].append(b)
                indegree[b] += 1

            # init with leaves
            q = collections.deque([i for i, deg in enumerate(indegree) if deg == 0])
            q.popleft()  # remove dummy zero, keep 1..k only
            while q:
                a = q.popleft()
                order.append(a)
                n -= 1
                
                for b in adj[a]:
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        q.append(b)
            if n != 0:
                return []
            return order
        
        order_rows = topology_sort(rowConditions, k)
        order_cols = topology_sort(colConditions, k)
        
        if not order_rows or not order_cols:
            return []
        
        # treat the matrix as two different topologies,
        # and we are going to find the position of 1..k numbers.
        #
        # for rowConditions & colConditions we can treat it
        # as the precedences between two vertices in the topology,
        # so that we can use topology sort to find an order that satisfies the conditions.
        #
        # since there're two different groups of conditions to be met,
        # we can find each vertex's position in these two conditions' topology sort order,
        # and convert it to the matrix's coordinate.
        ans = [[0] * k for _ in range(k)]
        for i, v in enumerate(order_rows):
            j = order_cols.index(v)
            ans[i][j] = v

        return ans

